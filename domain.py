from typing import Literal, Annotated

from pydantic import BaseModel, Field, ConfigDict


# -----------------------------
# Application & Domain models
# -----------------------------

AttributeName = Literal[
    "Might",
    "Agility",
    "Vitality",
    "Insight",
    "Arcana",
    "Presence",
]

AttributeValue = Annotated[int, Field(ge=0, le=120)]


class Attributes(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    Might: AttributeValue
    Agility: AttributeValue
    Vitality: AttributeValue
    Insight: AttributeValue
    Arcana: AttributeValue
    Presence: AttributeValue


class Character(BaseModel):
    name: str
    attributes: Attributes


def update_attribute(
    character: Character,
    attribute_name: AttributeName,
    delta: int,
) -> Character:
    current_value = getattr(character.attributes, attribute_name)
    new_value = current_value + delta

    # Re-assignment triggers Pydantic validation
    setattr(character.attributes, attribute_name, new_value)

    return character