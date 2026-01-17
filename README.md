# 🐍 Mastering Python

Welcome, **Explorers**, to **Mastering Python**.

This repository is the central home for the *Mastering Python* series—a practical, episode-driven journey into modern Python development. The focus is on writing **clear**, **correct**, and **maintainable** Python using today’s best practices, with a strong emphasis on **type annotations**, **design clarity**, and **real-world patterns**.

Each episode builds on the previous one, gradually introducing concepts while keeping the code grounded and approachable.

---

## 🎬 Episodes

Each episode in the series has its **own Git branch**.  
The `main` branch contains information about the series and various episodes, while individual episode branches capture the code exactly as it appeared during that episode.

Current episodes include:

- **Episode 1 – Mastering uv**  
  An overview of the crazy amazing uv package management tool and how you can use it to manage packages and virtual environments.

- **Episode 2 – Mastering Type Hints**  
  Demonstrating how Python’s type system improves clarity, tooling, and correctness - we also touch on Pydantic in this episode.

> 📌 **Important:**  
> To explore an episode browse to the branch on GitHub and start with the ReadMe file. All episodes have accompanying YouTube Episodes which you can find at youtube.com/@voyagerquests
>
> ```bash
> git checkout episode-2
> ```

(Additional episodes will be added over time.)

---

## 🧭 How This Repository Is Organized

- **One repository for the series**
- **One branch per episode**
- **Every episode's code and content stands on it's own**
- **You do not have to watch previous episodes to follow along**

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

Welcome aboard.  
Your journey into **Mastering Python** starts here.

## License

This project is licensed under the MIT License.
You are free to use, modify, and reuse the code in your own projects,
including commercial ones. See the [LICENSE](LICENSE) file for details.