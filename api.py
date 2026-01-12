from fastapi import FastAPI
from domain import Character


# -----------------------------
# FastAPI setup
# -----------------------------

app = FastAPI()

@app.post("/characters", response_model=Character)
def create_character(character: Character) -> Character:
    return character

