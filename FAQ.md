# ❓ Frequently Asked Questions (FAQ) & Common Mistakes

[⬅️ Back to Main Guide](README.md)

---

### 1. Terminal & Installation Issues

<details>
<summary><b>Q: I installed <code>uv</code>, but my terminal says <code>'uv' is not recognized</code> or <code>command not found: uv</code>.</b></summary>

**Solution:**
1. **Restart your terminal:** Close your terminal window completely and open a new one. Modern shells only refresh their `PATH` when opened fresh.
2. If restarting doesn't work:
   * **Windows:** Ensure `%USERPROFILE%\.local\bin` or `%USERPROFILE%\.cargo\bin` is in your environment `PATH`.
   * **macOS / Linux:** Run `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc` (or `~/.bashrc`), then run `source ~/.zshrc`.
</details>

<details>
<summary><b>Q: In PowerShell, I see <code>File ... cannot be loaded because running scripts is disabled on this system</code>.</b></summary>

**Solution:**
Run this single command in PowerShell to allow locally signed developer scripts:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
*(This only affects your user account and does not require administrator privileges.)*
</details>

---

### 2. Editor & IDE (VS Code / PyCharm)

<details>
<summary><b>Q: In VS Code, I see yellow squiggly lines: <code>Import "pandas" could not be resolved</code>. Where is my Python interpreter?</b></summary>

**Solution:**
When you run `uv add <package>` or `uv run`, `uv` creates a virtual environment inside a hidden folder named `.venv` in your project root.
1. In VS Code, press `Ctrl + Shift + P` (or `Cmd + Shift + P` on Mac).
2. Type **`Python: Select Interpreter`** and press Enter.
3. Choose the interpreter pointing to your project's `.venv`:
   * **Windows:** `./.venv/Scripts/python.exe`
   * **macOS / Linux:** `./.venv/bin/python`
</details>

<details>
<summary><b>Q: How do I select the right kernel in a Jupyter Notebook in VS Code?</b></summary>

**Solution:**
In the top right corner of your notebook (`.ipynb`), click **"Select Kernel"** ➔ **"Python Environments..."** ➔ Select the one labeled `.venv (Python 3.12)`.
</details>

---

### 3. General `uv` Questions

<details>
<summary><b>Q: Do I still need Anaconda, Miniconda, or standard Python from python.org?</b></summary>

**Answer:**
No! `uv` has built-in Python version management. Running `uv python install 3.12` downloads a standalone, high-performance Python release directly. You don't need any other Python installer.
</details>

<details>
<summary><b>Q: Should I commit <code>uv.lock</code> to Git?</b></summary>

**Answer:**
**Yes!** Committing `uv.lock` ensures that anyone else who clones your repository (or your deployment server) installs the exact same package versions, preventing `"works on my machine"` bugs.
</details>

<details>
<summary><b>Q: Should I commit <code>.venv/</code> to Git?</b></summary>

**Answer:**
**No, never!** The `.venv` folder contains binaries specific to your computer and operating system. Our `.gitignore` automatically ignores `.venv/`. Other developers just need to run `uv sync` to build their own local `.venv` in seconds.
</details>
