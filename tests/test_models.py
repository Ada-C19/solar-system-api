from app.models.planet import Planet

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mercury",
                    description="Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun",
                    type="Rocky/Terrestrial")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] == "Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun."
    assert result["type"] == "Rocky/Terrestrial"

def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(name="Mercury",
                    description="Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun.",
                    type="Rocky/Terrestrial")
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Mercury"
    assert result["description"] == "Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun."
    assert result["type"] == "Rocky/Terrestrial"

def test_to_dict_missing_title():
    # Arrange
    test_data = Planet(id=1,
                    description="Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun.",
                    type="Rocky/Terrestrial")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun."
    assert result["type"] == "Rocky/Terrestrial"

def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mercury")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] is None
    assert result["type"] == "Rocky/Terrestrial"

def test_to_dict_missing_type():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mercury",
                    description="Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun.")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] == "Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun."
    assert result["type"] is None