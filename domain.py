from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field
from nanoid import generate


# ============================================================================
# Reusable Annotated field definitions (define once, reuse everywhere)
# ============================================================================

# Core identifiers / strings
CharacterId = Annotated[
    str,
    Field(
        description="System-generated character identifier.",
        examples=["char_Kd9F2aL0Qx"],
    ),
]

CharacterName = Annotated[
    str,
    Field(
        min_length=1,
        max_length=80,
        description="Character name.",
        examples=["Aria"],
    ),
]

# Attribute values
AttrValue = Annotated[
    int,
    Field(
        ge=1,
        le=100,
        description="Attribute value.",
    ),
]
OptionalAttrValue = AttrValue | None

# Attribute fields (carry alias + per-field description)
Might = Annotated[OptionalAttrValue, Field(alias="Might", description="Physical strength")]
Agility = Annotated[OptionalAttrValue, Field(alias="Agility", description="Speed and reflexes")]
Vitality = Annotated[OptionalAttrValue, Field(alias="Vitality", description="Health and endurance")]
Insight = Annotated[OptionalAttrValue, Field(alias="Insight", description="Perception and discernment")]
Arcana = Annotated[OptionalAttrValue, Field(alias="Arcana", description="Master arcane subjects")]
Presence = Annotated[OptionalAttrValue, Field(alias="Presence", description="Charisma and influence")]


# ============================================================================
# Domain Layer Example
# ============================================================================

class Attributes(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        populate_by_name=True,  # accept field names and aliases
        extra="forbid",
    )

    might: Might = None
    agility: Agility = None
    vitality: Vitality = None
    insight: Insight = None
    arcana: Arcana = None
    presence: Presence = None


class CharacterModel(BaseModel):
    id: CharacterId
    name: CharacterName
    attributes: Attributes


class CreateCharacterRequestDTO(BaseModel):
    name: CharacterName
    attributes: Attributes


class CreateCharacterResponseDTO(BaseModel):
    id: CharacterId
    name: CharacterName
    attributes: Attributes


# ============================================================================
# Application layer
# ============================================================================

def generate_character_id() -> str:
    return "char_" + generate(size=10)


def update_attributes(character: CharacterModel, new_attributes: Attributes) -> None:
    updates = new_attributes.model_dump(exclude_unset=True, exclude_none=True)
    for field, value in updates.items():
        setattr(character.attributes, field, value)


def create_character_use_case(request: CreateCharacterRequestDTO) -> CreateCharacterResponseDTO:
    character = CharacterModel(
        id=generate_character_id(),
        name=request.name,
        attributes=request.attributes,
    )
    return CreateCharacterResponseDTO(
        id=character.id,
        name=character.name,
        attributes=character.attributes,
    )