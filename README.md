# 🚀 `uv` for Beginners: Modern Python Made Simple & Lightning Fast

> An open-source, step-by-step practical guide to mastering **Astral's `uv`** on **Windows (PowerShell & CMD)**, **macOS**, and **Linux**.

---

## 🤔 What is `uv` & Why Should Beginners Care?

If you've ever tried learning Python, you've probably felt overwhelmed by packaging tools:
* *"Do I need `pip` or `pip3`?"*
* *"How do virtual environments work (`python -m venv`)?"*
* *"Why doesn't my terminal find Python?"*
* *"Do I need `pyenv`, `conda`, `poetry`, or `pipx`?"*

**`uv` replaces all of them with a single, blazingly fast tool written in Rust.**

### The 10-Second Comparison

| What you want to do | The Old Way 🐢 | The Modern `uv` Way ⚡ |
|---|---|---|
| **Install Python** | Visit `python.org`, run installer, pray PATH works | `uv python install 3.12` |
| **Create a project** | Create folder, run `python -m venv .venv`, activate | `uv init my-project` |
| **Install a library** | Activate venv, run `pip install pandas`, update `requirements.txt` | `uv add pandas` *(automatically manages venv & lockfile)* |
| **Run your code** | Remember to activate venv, run `python main.py` | `uv run main.py` *(automatically runs in project venv)* |
| **Run Jupyter / Notebooks** | Install `ipykernel`, register kernel name, link VS Code | `uv add --dev ipykernel` ➔ select `.venv` in VS Code |
| **Run a single script with deps** | Create temporary venv, install deps, run script | `uv run script.py` *(reads inline dependencies automatically)* |
| **Run a CLI tool (e.g. Ruff/Black)** | Install globally with `pipx install ruff` | `uvx ruff check .` *(zero installation needed)* |

---

## 🗺️ Learning Roadmap

Follow the sections in order, or jump directly to what you need today:

| Module | What You Will Learn | Platform Support |
|---|---|:---:|
| **[00 — Prerequisites](00-prerequisites/README.md)** | Fix PowerShell ExecutionPolicy, CMD setup, PATH basics, and terminal restarts | 🪟 Windows · 🍎 macOS · 🐧 Linux |
| **[01 — Installation & Python Setup](01-installation/README.md)** | Install `uv` in 10s and manage Python versions with `uv python` | 🪟 Windows · 🍎 macOS · 🐧 Linux |
| **[02 — Your First Project](02-first-project/README.md)** | `uv init`, `pyproject.toml`, `uv.lock`, and running code with `uv run` | All platforms |
| **[03 — Jupyter & VS Code Setup](03-jupyter-setup/README.md)** | Bulletproof kernel setup in VS Code & JupyterLab | All platforms |
| **[04 — Dependency Management](04-dependency-mgmt/README.md)** | Adding (`uv add`), dev tools (`--dev`), removing, and lockfiles (`uv sync`) | All platforms |
| **[05 — Single-File Scripts](05-single-file-scripts/README.md)** | PEP 723 inline script metadata — run scripts with dependencies without a project | All platforms |
| **[06 — Tools & `uvx`](06-tools-and-uvx/README.md)** | Run linters, formatters, and CLIs instantly with `uvx` | All platforms |
| **[07 — Migration Guide](07-migration/README.md)** | Migrate existing `requirements.txt`, `pip`, or Conda environments in 60s | All platforms |

---

## ⚡ 1-Minute Cross-Platform Cheat Sheet

Copy-paste commands tailored for your shell:

### 1. Installation

<details open>
<summary><b>Click to expand installation commands</b></summary>

* **Windows (PowerShell):**
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```
* **Windows (Command Prompt / CMD):**
  ```cmd
  winget install --id=astral-sh.uv -e
  ```
* **macOS & Linux (Terminal / Bash / Zsh):**
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

*(Always close and reopen your terminal after installing!)*
</details>

### 2. Daily Commands

| Task | Command |
|---|---|
| **Check `uv` version** | `uv --version` |
| **Update `uv` to latest** | `uv self update` |
| **Install Python 3.12** | `uv python install 3.12` |
| **Create new project** | `uv init my-app` |
| **Add a library (e.g., requests)** | `uv add requests` |
| **Add a dev tool (e.g., pytest)** | `uv add --dev pytest` |
| **Run your project** | `uv run hello.py` |
| **Run a one-off tool** | `uvx ruff check .` |

---

## 🎯 Choose Your Path

* 🎓 **Complete Beginner?** Start at **[00 — Prerequisites](00-prerequisites/README.md)**.
* 📊 **Data Science Student?** Check out **[03 — Jupyter Setup](03-jupyter-setup/README.md)** and the pre-configured **[examples/data-science-jupyter](examples/data-science-jupyter/)**.
* ⚡ **Writing Quick Automation Scripts?** See **[05 — Single-File Scripts](05-single-file-scripts/README.md)**.
* 📦 **Upgrading an Existing Project?** Jump straight to **[07 — Migration Guide](07-migration/README.md)**.

---

## ❓ Common Questions & Troubleshooting

Hit a snag? Check our **[FAQ & Troubleshooting Guide](FAQ.md)** for quick fixes to common beginner roadblocks (like VS Code interpreter selection, proxy issues, and path errors).

---

## 🤝 Project & Community

This guide is open-source and maintained on GitHub:
👉 **[github.com/servasadolph/uv-beginners-learn](https://github.com/servasadolph/uv-beginners-learn)**

Feedback, suggestions, and pull requests are warmly welcomed!
