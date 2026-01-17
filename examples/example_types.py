# ============================================================
# types.py
# Examples of Python type hints / annotations by category
# Python 3.14-style (modern unions, no import side effects)
# ============================================================

from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from datetime import datetime
from decimal import Decimal
from ipaddress import IPv4Address
from pathlib import Path
from types import ModuleType
from typing import Any, Protocol, TypedDict, TypeGuard
from uuid import UUID

import math


# ------------------------------------------------------------
# 1. Built-in classes: int, str, list, dict, tuple
# ------------------------------------------------------------


def square(x: int) -> int:
    return x * x


def greet(name: str) -> str:
    return f"Hello {name}"


scores: list[int] = [85, 90, 78]
ages: dict[str, int] = {"Alice": 30, "Bob": 25}
point: tuple[int, int] = (10, 20)


# ------------------------------------------------------------
# 2. Standard library classes: datetime, pathlib, uuid, decimal, ipaddress
# ------------------------------------------------------------


def is_future(ts: datetime) -> bool:
    return ts > datetime.now()


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_user(user_id: UUID) -> None:
    print(user_id)


def apply_tax(amount: Decimal) -> Decimal:
    return amount * Decimal("1.15")


def is_local(ip: IPv4Address) -> bool:
    return ip.is_private


# ------------------------------------------------------------
# 3. Third-party classes (example: Pydantic)
# Wrapped so the file works without third-party installs.
# ------------------------------------------------------------

try:
    from pydantic import BaseModel

    class User(BaseModel):
        id: int
        name: str

    def save_user(user: User) -> None:
        print(user.id)

    class Product(BaseModel):
        sku: str
        price: float

    def discount(product: Product) -> float:
        return product.price * 0.9

    def serialize(model: BaseModel) -> dict[str, Any]:
        return model.model_dump()

except ImportError:
    # Pydantic not installed; keep the rest of the file importable.
    pass


# ------------------------------------------------------------
# 4. User-defined classes
# ------------------------------------------------------------


class Character:
    def __init__(self, name: str, level: int) -> None:
        self.name = name
        self.level = level


def promote(c: Character) -> None:
    c.level += 1


def clone(c: Character) -> Character:
    return Character(c.name, c.level)


party: list[Character] = []


def strongest(characters: list[Character]) -> Character:
    return max(characters, key=lambda c: c.level)


# ------------------------------------------------------------
# 5. Abstract Base Classes (collections.abc)
# ------------------------------------------------------------


def sum_all(values: Iterable[int]) -> int:
    return sum(values)


def first(seq: Sequence[str]) -> str:
    return seq[0]


def print_items(data: Mapping[str, int]) -> None:
    for k, v in data.items():
        print(k, v)


def run(fn: Callable[[], None]) -> None:
    fn()


def drain(it: Iterator[int]) -> int:
    """Consume an iterator and return how many items were seen."""
    count = 0
    for _ in it:
        count += 1
    return count


# ------------------------------------------------------------
# 6. typing + types constructs
# ------------------------------------------------------------


def average(values: list[int]) -> float:
    return sum(values) / len(values)


def maybe_name(flag: bool) -> str | None:
    return "Alice" if flag else None


def parse(value: int | str) -> int:
    return int(value)


class HasId(Protocol):
    id: int


def print_id(obj: HasId) -> None:
    print(obj.id)


class Config(TypedDict):
    debug: bool
    host: str


def load(cfg: Config) -> None:
    print(cfg["host"])


def is_int_list(xs: list[object]) -> TypeGuard[list[int]]:
    return all(isinstance(x, int) for x in xs)


def inspect_module(mod: ModuleType) -> str:
    return mod.__name__


if __name__ == "__main__":
    print(inspect_module(math))
