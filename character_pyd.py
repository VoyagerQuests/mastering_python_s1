from typing import Literal #, Annotated
from pydantic import BaseModel, Field


AttributeName = Literal[
    "Might",
    "Agility",
    "Vitality",
    "Insight",
    "Arcana",
    "Presence",
]

#AttributeValue = Annotated[int, Field(ge=0, le=100)]

class Attributes(BaseModel):
    Might: int = Field(ge=0, le=100)
    Agility: int = Field(ge=0, le=100)
    Vitality: int = Field(ge=0, le=100)
    Insight: int = Field(ge=0, le=100)
    Arcana: int = Field(ge=0, le=100)
    Presence: int = Field(ge=0, le=100)


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
