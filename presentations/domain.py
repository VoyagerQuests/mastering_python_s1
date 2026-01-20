#| code-line-numbers: ""
from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field
from nanoid import generate

BaseAttrValue = Annotated[int, Field(ge=1, le=100)]
OptionalAttrValue = BaseAttrValue | None


class Attributes(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        populate_by_name=True,
        extra="forbid",
    )

    might: Annotated[
        OptionalAttrValue, Field(alias="Might", description="Physical strength")
    ] = None
    agility: Annotated[
        OptionalAttrValue, Field(alias="Agility", description="Speed and reflexes")
    ] = None
    vitality: Annotated[
        OptionalAttrValue, Field(alias="Vitality", description="Health and endurance")
    ] = None
    insight: Annotated[
        OptionalAttrValue, Field(alias="Insight", description="Perception and discernment")
    ] = None
    arcana: Annotated[
        OptionalAttrValue, Field(alias="Arcana", description="Master arcane subjects")
    ] = None
    presence: Annotated[
        OptionalAttrValue, Field(alias="Presence", description="Charisma and influence")
    ] = None


# Domain Layer Class
class CharacterModel(BaseModel):
    id: str
    name: str
    attributes: Attributes

# Data Transfer Object Models
class CreateCharacterRequestDTO(BaseModel):
    name: str
    attributes: Attributes

class CreateCharacterResponseDTO(BaseModel):
    id: str
    name: str
    attributes: Attributes

# Application Layer Functions
def generate_character_id() -> str:
    return "char_" + generate(size=10)

def update_attributes(
    character: CharacterModel,
    new_attributes: Attributes,
) -> None:
    updates = new_attributes.model_dump(exclude_unset=True, exclude_none=True)

    for field, value in updates.items():
        setattr(character.attributes, field, value)

def create_character_use_case(
    request: CreateCharacterRequestDTO,
) -> CreateCharacterResponseDTO:
    # Convert DTO → domain model
    character = CharacterModel(
        id=generate_character_id(),
        name=request.name,
        attributes=request.attributes,
    )
    # Convert domain → response DTO
    return CreateCharacterResponseDTO(
        id=character.id,
        name=character.name,
        attributes=character.attributes,
    )