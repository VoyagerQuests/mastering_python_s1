def update_attribute(character, attribute_name, delta):
    """
    Update a character's attribute by adding a delta value.

    character: a dictionary representing the character.
        Expected structure:
        {
            "name": str,
            "attributes": {
                "Might": int,
                "Agility": int,
                "Vitality": int,
                ...
            }
        }

    attribute_name: the name of the attribute to update (string)
    delta: the amount to add or subtract (integer)

    Returns the updated character dictionary.
    """

    if attribute_name not in character["attributes"]:
        raise ValueError("Unknown attribute")

    character["attributes"][attribute_name] += delta

    return character


### Tests

def test_update_existing_attribute():
    character = {
        "name": "Aelar",
        "attributes": {
            "Might": 10,
            "Agility": 8,
        },
    }

    updated = update_attribute(character, "Might", 5)

    assert updated["attributes"]["Might"] == 15


def test_update_unknown_attribute_raises_error():
    character = {
        "name": "Aelar",
        "attributes": {
            "Might": 10,
        },
    }

    try:
        update_attribute(character, "Strength", 5)
    except ValueError as e:
        assert str(e) == "Unknown attribute"
    else:
        raise AssertionError("Expected ValueError was not raised")
    
def test_passing_attribute_as_string():
    character = {
        "name": "Sturm",
        "attributes": {
            "Might": 70,
        },
    }

    try:
        update_attribute(character, "Might", 55)
    except ValueError as e:
        assert str(e) == "Unknown attribute"
    else:
        raise AssertionError("Expected ValueError was not raised")
    
    


# test_update_existing_attribute()
# test_update_unknown_attribute_raises_error()
# test_passing_attribute_as_string()
