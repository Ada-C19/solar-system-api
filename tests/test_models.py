from app.models.planet import Planet

def test_to_dict_no_missing_data():
    #arrange
    test_data = Planet( 
                    id=1,
                    name="testopolis",
                    description="a testing place",
                    solar_day=300 
                    )
    #act
    result = test_data.to_dict()

    #assert
    assert len(result) == 4 
    assert result["id"] == 1
    assert result["name"] == "testopolis"
    assert result["solar_day"] == 300
    assert result["description"] == "a testing place"
