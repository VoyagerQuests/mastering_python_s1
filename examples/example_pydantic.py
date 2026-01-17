from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field

BaseAttrValue = Annotated[int, Field(ge=1, le=100)]
OptionalAttrValue = BaseAttrValue | None


class Attributes(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        populate_by_name=True,
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


class Character(BaseModel):
    name: str
    attributes: Attributes


def update_attributes(
    character: Character,
    new_attributes: Attributes,
) -> None:
    updates = new_attributes.model_dump(exclude_unset=True)

    for field, value in updates.items():
        setattr(character.attributes, field, value)


attributes1 = Attributes(
    might=1, agility=1, vitality=1, insight=1, arcana=1, presence=1
)
silvara = Character(name="Silvara", attributes=attributes1)

print(silvara.model_dump_json())
update_attributes(silvara, Attributes(might=5, arcana=10, presence=15))
print(silvara.model_dump_json())


