# SynthShell

**SynthShell** is a lightweight interactive framework-shell for rapid development of console software and automation scripts. It is written in pure Python with zero heavy external dependencies. Ideal for building custom CLI utilities for free.

The developer receives a clean modular architecture, while the end-user gets a predictable step-by-step interface that guides them sequentially through interactive input prompts.

## Installation
```python
pip install synthshell
```

## Core API Methods

### Configuration & Extensions
* **`s_shell(name)`** - Updates the main terminal prompt string (e.g., changing it to `myshell>`).
* **`s_ver(name)`** - Sets the custom version string of your software (displayed inside the `about` menu).
* **`s_author(name)`** - Registers your custom nickname as the software author.
* **`add_command(cmd_name, func_object)`** - Dynamically registers a custom function as an executable command inside the engine using global dictionary mapping (no global keywords required).

### Core Engine & Interface
* **`start()`** - Executes the main hard-blocking infinite loop of the terminal environment to parse input.
* **`printf(text)`** - Prints a stylized text output prefixed with the current active shell name.
* **`clear()`** - Wipes the terminal screen history completely (compatible with both Windows and Linux OS).
* **`about()`** - Displays technical metadata, software author, framework creator (subnarcher), MIT License terms, and the official source code repository.
* **`sysinfo()`** - Prints underlying system statistics including platform, Python runtime version, and current Process ID.
* **`exitd(tm)`** - Terminates the process execution environment (supports optional execution delays handled via `teto.sleep`).
* **`input_str(text)`** - Requests a plain string value. Automatically prefixes the line with `sw_shell>inputstr>text>`.
* **`input_int(text)`** - Requests an integer value. Protected by an internal try/except block. If a non-integer is entered, it catches the exception, prints a clean error message, and prevents a raw crash.
* **`input_float(text)`** - Requests a floating-point number. Also protected by an internal try/except block to safely catch parsing errors without breaking the execution flow.
* **`inputf(text)`** - Unsafe/formatted input proxy. Used internally for sequential step-by-step data collection across operations (like `make`, `calc`, and `show`). It relies on `_check_unsafe(e)` to determine whether to mute errors or pass them to the developer.

### Filesystem & Utility Operations
* **`warp(path)`** - Shifts the active directory environment to the specified target disk destination (native `cd` behavior).
* **`scan(path, mode)`** - Inspects target folder directories. Supported filtering flags: `items` (files only), `dirs` (folders only), or `all` (everything).
* **`make(path, name, mode, encoding, text)`** - Spawns or rewrites a specified file. If positional parameters evaluate to None, it triggers sequential fallback prompts to collect inputs interactively.
* **`show(path, name, encoding)`** - Parses the entire content array of a text file and flushes it straight into the active stdout stream.
* **`delf(path, name)`** - Forces permanent file removal operations from the storage drive.
* **`log(logs)`** - Safely writes diagnostic records directly into the active shell history file utilizing append data streams (`"a"` mode).
* **`calc(num1, op, num2)`** - Built-in evaluation calculator handling basic operators (`+`, `-`, `*`, `/`, `**`, `//`, `%`) wrapped with integrated zero-division panic blocks.
* **`run(name)`** - Spawns separate detached subprocess modules or operating system commands using system management tools.

### Error Handling & Safety
* **`unsafe(state)`** - Globally alters the debugging environment status parameter.
* **`_check_unsafe(e)`** - Evaluation proxy. If the unsafe state resolves to True, it terminates safe execution and actively throws raw exception traces (`raise e`) to developers for debugging.

---
License: **MIT License** (The hardcoded framework creator attribution `subnarcher` must remain intact inside the `about` method).
