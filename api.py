from typing import Literal, Annotated

from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict

from domain import Character, update_attribute


# -----------------------------
# FastAPI setup
# -----------------------------

app = FastAPI()

@app.post("/characters", response_model=Character)
def create_character(character: Character) -> Character:
    return character

