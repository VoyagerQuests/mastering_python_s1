from fastapi import FastAPI
from domain import CharacterModel, CreateCharacterRequestDTO, CreateCharacterResponseDTO, create_character_use_case

# ============================================================================
# API Interface in Deliver Layer
# ============================================================================
# Usage:
# uv sync 
# uv run fastapi dev

app = FastAPI()


@app.post("/characters", response_model=CreateCharacterResponseDTO)
def create_character(
    request: CreateCharacterRequestDTO,
) -> CreateCharacterResponseDTO:
    return create_character_use_case(request)
