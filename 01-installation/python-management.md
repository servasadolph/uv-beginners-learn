# Managing Python Versions with `uv`

Historically, Python beginners faced significant headaches managing Python:
- Downloading installers from `python.org` and forgetting to check *"Add Python to PATH"*.
- System Python conflicts and permission errors (`sudo pip`).
- Needing third-party tools like `pyenv`, `asdf`, or Anaconda just to test a different Python version.

**With `uv`, all of this is solved in a single tool.** `uv` can download, install, pin, and switch between standalone Python versions automatically without touching your system's global files.

---

## 🔎 1. Discovering Python Versions (`uv python list`)

To see what Python versions are available to download or already installed on your machine:

```bash
uv python list
```

**What you will see:**
* A list of Python releases (3.8, 3.9, 3.10, 3.11, 3.12, 3.13, PyPy).
* Versions already downloaded on your machine will be labeled with their file path.
* Downloadable versions will be shown ready for installation.

---

## 📥 2. Installing Python with One Command (`uv python install`)

Need Python 3.12? You don't need a browser or an installer wizard. Just run:

```bash
uv python install 3.12
```

`uv` downloads an optimized, standalone Python executable directly to your user cache directory.

Want to install another version to test compatibility?
```bash
uv python install 3.11
uv python install 3.13
```

---

## 📌 3. Pinning a Project's Python Version (`uv python pin`)

When working on a project, you often want to ensure everyone on your team (or your future self) uses the exact same Python version.

Inside any project folder, run:

```bash
uv python pin 3.12
```

**What happens?**
`uv` creates a `.python-version` file containing `3.12`. Whenever you run `uv run` or `uv sync` in this directory, `uv` will automatically use Python 3.12 without you having to configure anything else!

---

## 📍 4. Finding Where Python Is (`uv python find`)

To locate the active Python binary that `uv` will use:

```bash
uv python find
```

To locate a specific version:
```bash
uv python find 3.12
```

---

## 🗑️ 5. Uninstalling a Python Version (`uv python uninstall`)

If you want to free up disk space by removing an older Python version:

```bash
uv python uninstall 3.10
```

---

## 💡 Key Takeaway for Beginners

> [!TIP]
> You **never** need to worry about installing Python before using `uv`.
> If you run `uv init my-project` or `uv run script.py`, `uv` will automatically fetch and install the required Python version in the background if you don't already have it!

---

## ⏭️ Ready for Your First Project?

Head over to **[02-first-project](../02-first-project/README.md)** to create your first `uv` project with `pyproject.toml` and `uv run`!
