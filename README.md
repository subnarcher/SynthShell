# SynthShell Core v1.0.0

A asynchronous background and emergency shell framework for Python automation, scripting, and recovery control. Built with low-level Type-B inputs and hardened anti-tampering protection.

---

## Features

* **Asynchronous Engine (`start_async`)**: Spawns a fully independent interactive terminal in a background thread without blocking the main script execution.
* **Emergency Recovery Mode**: Can be deployed inside a global `try/except` block to act as a crash-dump shell (Drop to Shell) for instant system diagnostic and tracking.
* **Type-B Safe Inputs**: Independent secure wrappers (`input_str`, `input_int`, `input_float`) with built-in validation. Prevents `NoneType` runtime crashes.
* **File Automations**: Native, sandboxed commands for internal file operations (`make`, `delf`, `show`) without exposing dangerous high-level entry points.
* **Anti-Tampering Shield**: Strict integrity check on the core runtime engine properties. Triggers a silent termination via `os._exit(0)` if authorship is violated.

---

## Installation

```bash
pip install synthshell
```

---

## Usage Examples

### 1. Interactive Application (Calculators, Quizzes)
*Do not invoke `start_async()` when running interactive user loops to prevent console stream desynchronization.*

```python
import synthshell_core as shell

# Configure the software environment metadata
shell.s_shell("CalcShell")
shell.s_ver("1.0.0")
shell.s_author("your_nickname")

# Safe Type-B input usage (Trims spaces automatically)
num1 = shell.input_float("first number")
op = shell.input_str("operator")
num2 = shell.input_float("second number")

# Process natively via the internal safe evaluator
shell.calc(num1, op, num2)
```

### 2. Background Routine (Loggers, Daemon Bots)
*Launches an isolated management console while the main loop executes background tasks.*

```python
import shell
import time

shell.s_shell("SynthBot")
shell.start_async() # Spawns the terminal environment into a background thread

while True:
    time.sleep(5)
    shell.log("The script is quietly executing background operations...")
```

### 3. Recovery Console (Anti-Crash Fallback)
*Prevents raw Windows error traces from interrupting execution, dropping the owner directly into the command line.*

```python
import shell

shell.s_shell("RecoveryShell")

try:
    # Risky code path
    result = 10 / 0
except Exception as error:
    shell.log(f"Critical execution failure: {error}")
    print("\n[CRITICAL] Main script failed! Dropping into emergency shell...")
    
    shell.start() # Hard blocking fallback console. Type 'show' to view logs!
```

---

## Core Console Commands

* `show` — Read and view files instantly. Features smart default mapping to `{sw_shell}_logs.txt`.
* `make` — Programmatic sandboxed file creation.
* `del` — Secure file erasure wrapped inside access guards.
* `calc` — `eval()`-free secure mathematical parser.
* `sysinfo` — Instant environment reconnaissance (PID, OS, Platform).
* `standarts` / `guide` — Automated local generation of development guidelines and manual files.
* `clear` — Cross-platform screen wiper for quick terminal cloaking.

---

## License & Copyright

Developed globally by **subnarcher**. Hardcoded core rules cannot be modified. Released under the open and free **MIT License**.
