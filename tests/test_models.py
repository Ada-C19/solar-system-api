from app.models.planet import Planet


def test_to_dict_no_missing_data():
    # Arrange

    test_data = Planet(id = 1,
            name = "Venus",
            description = "hot enough to melt lead n ur heart </3",
            color = "she lil' rusty :(")
    
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Venus"
    assert result["description"] == "hot enough to melt lead n ur heart </3"
    
    

def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(
            name = "Venus",
            description = "hot enough to melt lead n ur heart </3",
            color = "she lil' rusty :(")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Venus"
    assert result["description"] == "hot enough to melt lead n ur heart </3"
    assert result["color"] == "she lil' rusty :("


def test_to_dict_missing_name():
    #Arrange
    test_data = Planet(id=1,
                description="hot enough to melt lead n ur heart </3",
                color="she lil' rusty :(")
    #Act
    result = test_data.to_dict()

    #Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "hot enough to melt lead n ur heart </3"
    assert result["color"] == "she lil' rusty :("


def test_to_dict_missing_description():
    #Arrange
    test_data = Planet(id=1,
                name="Venus",
                color="she lil' rusty :(")
    
    #Act
    result = test_data.to_dict()

    #Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Venus"
    assert result["description"] is None
    assert result["color"] == "she lil' rusty :("