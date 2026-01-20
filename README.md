# 🐍 Mastering Python — Episode: Type Hints

Welcome, **Explorers**, to **Mastering Python: Type Hints**.

This branch contains the full content for a single **Mastering Python — Season 1** episode, focused on **Python type hints / annotations** and how they improve **clarity**, **tooling**, and **correctness** in real codebases.

It also demonstrates how you can combine **type hints with Pydantic** to reduce framework boilerplate, add runtime validation, and make “framework-style” development (FastAPI-like patterns) significantly easier.

This episode includes a dedicated section on **what has changed in Python 3.14**, including modern annotation behavior and syntax improvements that impact everyday development.

---

## 🧭 How This Repository Is Organized

- **One repository for the series** https://github.com/VoyagerQuests/mastering_python_s1
- **One branch per episode** mastering_python_type_hints
- **Every episode's code and content stands on it's own**
- **You do not have to watch previous episodes to follow along**

## 🎬 About This Branch

- The branch captures the code and materials **exactly as shown in the episode**
- The episode is broken into multiple **topics**, each supported by presentations and runnable examples

> 📌 **How to view this episode**
>
> The code accompanies a YouTube video - to view the full episode, visit: https://youtube.com/@voyagerquests 
If you would like to access the code then clone the Mastering Python Season 1 GitHub repository and checkout this episode's branch using the following commands:
```bash
git clone https://github.com/VoyagerQuests/mastering_python_s1
cd mastering_python_s1/
git switch mastering_python_type_hints
``````

**Presentations**
The presentations were created using Quarto 1.9.16 and six presentations are available in the `presentations/` directory. To render the presentation locally, ensure you have Quarto installed (https://quarto.org/) and run the following command from the root of the repository:
quarto preview ./presentations/01presentation_foundational_types.qmd - there are six of these files.

**Code**
The following runnable code examples can be found in the repository root.
./api.py - A FastAPI api application demonstrating how the FastAPI framework can leverage type hints and Pydantic models to make api creation incredibly simple.
./cli - A Fire CLI application demonstrating how Fire can leverage Pydantic to create CLIs automatically from annotated functions and classes.
./models.py - This is a simple example of application layer use case logic and DTO models using Pydantic with domain layer models also defined in Pydantic.



```bash
---

## 🧠 Topics Covered in This Episode

This episode is structured as a progression from foundational typing → expressive contracts → runtime validation → modern typing features.

### 1) Foundational Types and Collections
- Why “no types” leads to silent misuse
- Basic annotations: `int`, `float`, `bool`, `str`, `bytes`, `None`
- Built-in collections: `list[T]`, `tuple[T1, T2]`, `tuple[T, ...]`, `set[T]`, `dict[K, V]`

### 2) Unions, Optional, and Collection ABCs
- `int | str` and `int | None` (modern union syntax)
- Choosing behavioral types from `collections.abc`:
  - `Iterable`, `Iterator`, `Sequence`, `Collection`, `Container`, `Reversible`
- Refactoring from “works for my list” to “works for any iterable of strings”

### 3) Literal & TypedDict
- `Literal[...]` for restricting values to an exact set (great for keys / commands)
- `TypedDict` for describing dictionary shapes (especially JSON-like payloads)
- Using the type checker to catch structural mistakes early

### 4) From TypedDict to Pydantic
- `Annotated[...]` + `Field(...)` to attach validation constraints
- Building Pydantic models that enforce runtime data integrity
- Aliases, `populate_by_name`, and safer parsing of external input
- Partial updates using `model_dump(exclude_unset=True, exclude_none=True)`

### 5) Behavioral and Generic Typing
- `Callable[[...], ...]` for higher-order functions
- Generics (`def f[T](...) -> ...`) for reusable, type-safe APIs
- `Protocol` for structural typing (“if it walks like a duck…”)

### 6) What Has Changed (Modern Python, including 3.14)
- Built-in generic collections (`list[int]`, `dict[str, int]`)
- Modern union syntax (`|`)
- Modern type parameter syntax (Python 3.12+)
- Type alias statements (`type X = ...`)
- **Python 3.14 annotation behavior (PEP 649)**: lazy evaluation by default and what that changes in practice

---

## ⚙️ Dependency Management with `uv`

This repository uses **`uv`** for dependency and environment management.

A `uv.lock` file is included, allowing you to reproduce the exact dependency set used for this episode.

### Getting Started

1. **Install `uv`**  
   Follow the official instructions:  
   https://docs.astral.sh/uv/

2. **Sync dependencies**
   ```bash
   uv sync
