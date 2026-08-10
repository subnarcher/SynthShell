import shlex
import subprocess

ERROR_BOOKS = {
    ValueError: "Invalid data format or unacceptable value entered.",
    TypeError: "Data type mismatch: Operation is not allowed.",
    NameError: "Internal system error: Reference to undefined name.",
    AttributeError: "Internal system error: Invalid object attribute or property reference.",
    
    FileNotFoundError: "The specified file or directory path was not found.",
    PermissionError: "Access denied: Insufficient system privileges to perform the operation.",
    IsADirectoryError: "System conflict: Reading a directory as a file is impossible.",
    NotADirectoryError: "System conflict: The specified object is not a directory.",
    FileExistsError: "Operation aborted: A file or directory with this name already exists.",
    
    IndexError: "Parsing error: Missing required command arguments.",
    KeyError: "Requested system configuration key or command not found.",
    
    ZeroDivisionError: "Mathematical error: Division by zero is undefined.",
    OverflowError: "Arithmetic overflow: Out of system register boundaries.",
    
    LookupError: "Unknown encoding type specified.",
    UnicodeDecodeError: "Decoding error: Encoding conflict while reading file content.",
    UnicodeEncodeError: "Write failure: Unable to encode text in the selected encoding.",
    
    OSError: "OS failure: Failed to execute system call.",
    ChildProcessError: "Process error: Subprocess execution failed.",
    subprocess.CalledProcessError: "Subprocess runtime failure: External program returned an error code.",
    subprocess.TimeoutExpired: "Subprocess timeout: External program execution exceeded time limit.",
    
    MemoryError: "Critical system failure: Out of memory resources.",
    KeyboardInterrupt: "Operation interrupted by user."
}


def error_msg(e):
    err_type = type(e)
    if err_type in ERROR_BOOKS:
        return ERROR_BOOKS[err_type]

    return f"System panic: Unexpected execution error [Code: {err_type.__name__}]."