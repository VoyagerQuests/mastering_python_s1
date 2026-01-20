import fire
import sys
from domain import Attributes, CreateCharacterRequestDTO, create_character_use_case

sys.tracebacklimit = 0 # Hide traceback for cleaner CLI output

# ============================================================================
# CLI Interface in Deliver Layer
# ============================================================================
# Usage:
# uv sync
# uv pip install -e . 
# character create --name "Aria Stormblade" --Might 70 --Agility 80 --Vitality 60 --Insight 75 --Arcana 40 --Presence 85



class CharacterCLI:
    def create(self, name: str, **kwargs):
        attributes = Attributes(**kwargs)
        
        request = CreateCharacterRequestDTO(name=name, attributes=attributes)
        response = create_character_use_case(request)
        
        return response.model_dump()

def main() -> None:
    fire.Fire(CharacterCLI)


if __name__ == "__main__":
    main()