# 🐍 Mastering Python

Welcome, **Explorers**, to **Mastering Python**.

This repository is the central home for the *Mastering Python* series—a practical, episode-driven journey into modern Python development. The focus is on writing **clear**, **correct**, and **maintainable** Python using today’s best practices, with a strong emphasis on **type annotations**, **design clarity**, and **real-world patterns**.

Each episode builds on the previous one, gradually introducing concepts while keeping the code grounded and approachable.

---

## 🎬 Episodes

Each episode in the series has its **own Git branch**.  
The `main` branch represents the latest stable state, while individual episode branches capture the code exactly as it appeared during that episode.

Current episodes include:

- **Episode 1 – Foundations**  
  Getting things working with minimal structure. Establishing the baseline.

- **Episode 2 – Introducing Type Hints**  
  Demonstrating how Python’s type system improves clarity, tooling, and correctness.

> 📌 **Important:**  
> To explore an episode, simply check out its corresponding branch:
>
> ```bash
> git checkout episode-2
> ```

(Additional episodes will be added over time.)

---

## 🧭 How This Repository Is Organized

- **One repository**
- **One branch per episode**
- **Incremental progression**

This makes it easy to:
- Compare changes between episodes
- See *why* refactors were made
- Follow along at your own pace

---

## ⚙️ Dependency Management with `uv`

This repository uses **`uv`** for Python dependency and environment management.

A `uv.lock` file is included, allowing you to reproduce the exact dependency set used in each episode.

### Getting Started

1. **Install `uv`**  
   Follow the official instructions:  
   https://docs.astral.sh/uv/

2. **Sync dependencies**
   ```bash
   uv sync
   ```

3. **Run the project**
   ```bash
   uv run python main.py
   ```
   (or the appropriate command for the episode)

The lock file ensures consistency across machines and episodes.

---

## 🧠 What You’ll Learn

Throughout the series, you’ll explore:

- Python type hints and annotations
- How types improve tooling, AI assistance, and correctness
- Practical refactoring strategies
- Clean, readable API design
- Modern Python workflows

The goal is not just to *write Python*, but to **master it**.

---

## 🚀 Choose Your Path

- **Explorer Track**  
  Follow along, read the code, and observe the evolution.

- **Builder Track**  
  Check out each episode branch and implement the changes yourself.

- **Deep Dive Track**  
  Compare branches, experiment, and extend the ideas further.

---

Welcome aboard.  
Your journey into **Mastering Python** starts here.
