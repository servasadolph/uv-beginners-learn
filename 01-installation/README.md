# 01 — Installing `uv` & Keeping It Updated

Installing `uv` takes less than 10 seconds. It is a single, self-contained binary written in Rust—it does **not** require an existing Python installation or a C compiler to install.

---

## 🚀 Recommended Installation Methods

Select the instructions for your operating system:

### 🪟 Windows (PowerShell & Command Prompt)

Choose the shell you prefer on Windows:

#### Option A: Windows PowerShell (Recommended)
Open **PowerShell** and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Option B: Windows Command Prompt (CMD)
Open **Command Prompt (CMD)** and run either:

*Via Windows Package Manager (Winget):*
```cmd
winget install --id=astral-sh.uv -e
```

*Or via the official Astral installer invoked from CMD:*
```cmd
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

### 🍎 macOS & 🐧 Linux

Open your **Terminal** and run:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

*Alternative for macOS (Homebrew):*
```bash
brew install uv
```

> [!TIP]
> **A Note on Security & Trust:**
> The `curl | sh` and `irm | iex` installation pattern is standard for modern developer tools (like Rust, NVM, and uv). It downloads and executes the installer directly from Astral's verified HTTPS domain (`astral.sh`) within your user profile without requiring administrator (`sudo`) access.
> If you prefer to inspect scripts before executing them, you can open `https://astral.sh/uv/install.ps1` or `https://astral.sh/uv/install.sh` in your browser to view the source code.

---

## 🔄 Step 2: Restart Your Terminal

Once the installation finishes, **close your terminal window and open a new one** (whether using PowerShell, Command Prompt, or Terminal on macOS/Linux).
This ensures your shell reloads its `PATH` variable and discovers the new `uv` command.

---

## 🔍 Step 3: Verification (10-Second Sanity Check)

Run this command in your fresh terminal (PowerShell, CMD, or Bash/Zsh):

```bash
uv --version
```

**Expected output:**
```text
uv 0.5.15
```

*(The exact version number may be newer depending on when you install—any version number printed confirms success!)*

If you see any version number printed, **congratulations! `uv` is successfully installed and ready.**

> [!NOTE]
> If you get `'uv' is not recognized` (Windows PowerShell or CMD) or `command not found: uv` (macOS/Linux), review **[00-prerequisites](../00-prerequisites/README.md)** to verify your `PATH` setup.

---

## ⚡ Keeping `uv` Updated

`uv` releases performance improvements and new features frequently. To update `uv` to the latest version at any time, run:

```bash
uv self update
```

*(If you installed via `brew` or `winget`, you can also use `brew upgrade uv` or `winget upgrade astral-sh.uv`.)*

---

## 📋 Quick Comparison: Installation Methods

| Platform / Shell | Primary Method (Recommended) | Alternative |
|---|---|---|
| **Windows (PowerShell)** | `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` | `winget install --id=astral-sh.uv -e` |
| **Windows (CMD)** | `winget install --id=astral-sh.uv -e` | `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` |
| **macOS** | `curl -LsSf https://astral.sh/uv/install.sh \| sh` | `brew install uv` |
| **Linux / WSL** | `curl -LsSf https://astral.sh/uv/install.sh \| sh` | System package manager / Cargo |

---

## ⏭️ Next Step

Now that `uv` is installed, you don't even need to download Python manually from python.org! Learn how `uv` automatically manages Python versions in:

👉 **[Managing Python Versions with `uv`](python-management.md)**
