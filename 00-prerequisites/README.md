# 00 — Prerequisites & Terminal Setup

[⬅️ Home](../README.md) · **00 — Prerequisites** · [Next: 01 — Installation ➡️](../01-installation/README.md)

---

Before installing `uv`, setting up your terminal properly ensures you won't hit confusing errors like `"command not found"` or `"running scripts is disabled on this system"`.

This quick 2-minute setup prevents 95% of common beginner setup issues.

---

## 🧭 Step 1: Know Your Terminal & Shell

Python tools run from your command line. Identify which shell you are using:

| Operating System | Terminal / Shell | How to Open | Notes |
|---|---|---|---|
| **Windows** | **PowerShell** *(Recommended)* | Press `Win + X` ➔ Choose **Terminal** or **PowerShell** | Modern default on Windows 10/11 |
| **Windows** | **Command Prompt (CMD)** | Press `Win + R` ➔ Type `cmd` ➔ Press `Enter` | Classic Windows shell |
| **macOS** | **Zsh** *(Default)* | Press `Cmd + Space` ➔ Type `Terminal` ➔ Press `Enter` | Default on macOS Catalina & newer |
| **Linux / WSL** | **Bash** or **Zsh** | Open your system terminal or launch `wsl` on Windows | Standard Linux environment |

---

## 🪟 Windows Setup: PowerShell vs. Command Prompt (CMD)

Windows has two main command-line interfaces: **PowerShell** (blue/black icon, modern) and **Command Prompt / CMD** (black icon with `C:\>`).

### 1. If using PowerShell: Fixing the Execution Policy
By default, Windows PowerShell restricts running downloaded scripts. If you try to run the `uv` installer without adjusting this, you may see:

```powershell
File ... cannot be loaded because running scripts is disabled on this system.
```

**The Fix (Safe for Beginners):**
Open **PowerShell** and run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

> [!NOTE]
> **Why set this now?**
> While the `uv` installer runs with a bypass flag, you will still need this policy whenever you activate Python virtual environments in PowerShell (e.g., `.venv\Scripts\Activate.ps1`). Configuring `RemoteSigned` now prevents frustrating permission errors later!
> `-Scope CurrentUser` applies only to your user account without requiring Administrator privileges.
> `RemoteSigned` allows you to run locally created scripts while ensuring downloaded scripts are signed.

**Verify Your Policy:**
```powershell
Get-ExecutionPolicy
```
If it outputs `RemoteSigned` or `Unrestricted`, your PowerShell is ready!

### 2. If using Command Prompt (CMD)
* **Execution policies do not apply to CMD** — CMD does not block scripts the same way PowerShell does.
* However, the standard `irm | iex` command is PowerShell syntax. In CMD, you can either:
  1. Use **Winget** directly: `winget install --id=astral-sh.uv -e`
  2. Or invoke PowerShell from CMD: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

---

## 🍎 macOS & 🐧 Linux Setup: Shell Configuration & PATH

When `uv` installs on macOS and Linux, it places its executable inside `~/.local/bin`. Most modern shells include this in your `PATH` automatically, but let's confirm.

### Check Your Current Shell
Open your terminal and run:
```bash
echo $SHELL
```
* If you see `/bin/zsh`, your configuration file is `~/.zshrc`.
* If you see `/bin/bash`, your configuration file is `~/.bashrc`.

### Ensuring `~/.local/bin` is in Your PATH
If you ever get `uv: command not found` after installing, add `~/.local/bin` to your PATH:

```bash
# For macOS / Linux using Zsh:
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# For Linux using Bash:
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

---

## 💡 What is `PATH`? (A 30-Second Mental Model)

When you type `uv` or `python` into your terminal, your computer doesn't search your entire hard drive. Instead, it looks only inside the folders listed in a special system variable called **`PATH`**.

* If the folder containing `uv` is listed in your `PATH`, your terminal finds it instantly.
* If it is not listed, your terminal says: `uv: command not found` or `'uv' is not recognized as an internal or external command`.

### How to check if a command is in your PATH:

| Platform | Command to test |
|---|---|
| **Windows (PowerShell)** | `Get-Command uv` |
| **Windows (CMD)** | `where uv` |
| **macOS & Linux** | `which uv` |

> [!TIP]
> **The Golden Rule for Beginners:**
> Whenever you install a new CLI tool (like `uv`), **close and reopen your terminal window**. This forces your shell to reload its `PATH` and recognize newly installed commands!

---

## ✅ Readiness Checkpoint

Answer these questions before moving to installation:
1. **Windows PowerShell users:** Have you run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`?
2. **Windows CMD users:** Know that you can use `winget` or call PowerShell directly.
3. **All users:** Do you know how to open a fresh terminal window?

Once ready, head directly to **[01-installation](../01-installation/README.md)**!
