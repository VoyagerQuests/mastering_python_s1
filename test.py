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


def update_attribute(
    character: Character,
    attributes_to_update: Attributes,
) -> Character:
    current_attrs = character.attributes
    updates = attributes_to_update.model_dump(exclude_unset=True)

    for field_name, update_value in updates.items():
        if update_value is None:
            continue

        current_value = getattr(current_attrs, field_name)
        if current_value is None:
            raise ValueError(
                f"Cannot update '{field_name}' because the character has no current value set."
            )

        setattr(current_attrs, field_name, current_value + update_value)

    return character


attributes1 = Attributes(
    might=1, agility=1, vitality=1, insight=1, arcana=1, presence=1
)
silvara = Character(name="Silvara", attributes=attributes1)

print(silvara.model_dump_json())
update_attribute(silvara, Attributes(might=5))
print(silvara.model_dump_json())
