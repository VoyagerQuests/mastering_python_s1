from typing import TypedDict, Literal


AttributeName = Literal[
    "Might",
    "Agility",
    "Vitality",
    "Insight",
    "Arcana",
    "Presence",
]


class Attributes(TypedDict):
    Might: int
    Agility: int
    Vitality: int
    Insight: int
    Arcana: int
    Presence: int


class Character(TypedDict):
    name: str
    attributes: Attributes


def update_attribute(
    character: Character,
    attribute_name: AttributeName,
    delta: int,
) -> Character:
    character["attributes"][attribute_name] += delta
    return character
