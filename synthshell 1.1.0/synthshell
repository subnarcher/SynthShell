import subprocess
import os
import sys
import time as teto

sw_shell = "Shell"
sw_ver = "unknown"
software_author = "unknown"


unsafe_mode = [False]
custom_commands = {}

def s_ver(name):
    global sw_ver
    if name == "":
        sw_ver = "unknown"
    else:
        sw_ver = name


def s_author(name):
    global software_author
    if name == "":
        software_author = "unknown"
    else:
        software_author = name


def s_shell(name):
    global sw_shell
    if name == "":
        sw_shell = "Shell"
    else:
        sw_shell = name


def unsafe(state: bool):
    unsafe_mode[0] = state


def _check_unsafe(e):
    if unsafe_mode[0]:
        raise e


def printf(text):
    print(f"{sw_shell}>printf>{text}")


def input_str(text=""):
    return str(input(f"{sw_shell}>inputstr>{text}>"))


def input_int(text=""):
    try:
        return int(input(f"{sw_shell}>inputint>{text}>"))
    except Exception as e:
        _check_unsafe(e)
        printf(f"Error: {e}")


def input_float(text=""):
    try:
        return float(input(f"{sw_shell}>inputfloat>{text}>"))
    except Exception as e:
        _check_unsafe(e)
        printf(f"Error: {e}")


def inputf(text=""):
    try:
        return input(f"{sw_shell}>inputformated>{text}>")
    except Exception as e:
        _check_unsafe(e)
        printf(f"Error: {e}")


def start():
    while True:
        user_input = input(f"{os.getcwd()}>{sw_shell}> ").strip()

        match user_input:
            case "help":
                phelp()
            case "clear":
                clear()
            case "log":
                log()
            case "":
                print("")
            case "exit":
                return
            case "about":
                about()
            case "make":
                make()
            case "sysinfo":
                sysinfo()
            case "del":
                delf()
            case "calc":
                calc()
            case "show":
                show()
            case "warp":
                warp()
            case "scan":
                scan()
            case "run":
                run()
            case _:
                if user_input in custom_commands:
                    custom_commands[user_input]()
                else:
                    printf('unknown command. Try "help"')


def add_command(cmd_name, func_object):
    custom_commands[cmd_name] = func_object


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def plog(logs=None):
    if logs is None:
        logs = inputf("log>")
    printf(logs)
    try:
        with open(sw_shell + "_logs.txt", "a", encoding="utf-8") as f:
            f.write(logs + "\n")
    except Exception as e:
        _check_unsafe(e)
        printf(f"Error: {e}")


def log(logs=None):
    if logs is None:
        logs = inputf("log>")
    try:
        with open(sw_shell + "_logs.txt", "a", encoding="utf-8") as f:
            f.write(logs + "\n")
    except Exception as e:
        _check_unsafe(e)
        printf(f"Error: {e}")


def phelp():
    printf("SynthShell commands list")
    printf(
        f""" 
help - display this 
log - append text in file {sw_shell}log.txt 
clear - clear shell 
about - about shell 
make - start to make file 
sysinfo - display system information 
delf - start to delete file 
calc - calc num1 op num2 
show - display text/code file
warp - move to path
scan - scan folder
run - run file
"""
    )


def exits(tm=None):
    if tm is None:
        exit()
    else:
        teto.sleep(tm)
        exit()


def about():
    printf(f"About {sw_shell}")
    printf(f"version: 1.1.0")
    printf(f"software author: {software_author}")
    print("======================================================")
    printf(f"Shell creator: subnarcher")
    printf(f"framework Shell name: SynthShell")
    printf(f"License: MIT License")
    printf(f"Source Code and more information: https://github.com/subnarcher/SynthShell")


def make(path=None, name=None, mode=None, encoding=None, text=None):
    try:
        if path is None:
            path = inputf("make>path>")
        if name is None:
            name = inputf("make>file_name>")
        if mode is None:
            mode = inputf("make>mode>")
        if encoding is None:
            encoding = inputf("make>encoding>")
        if text is None:
            text = inputf("make>file_text>")
        with open(path + "/" + name, mode, encoding=encoding) as f:
            f.write(text)
    except Exception as e:
        _check_unsafe(e)
        printf(f"Error: {e}")


def sysinfo():
    printf("SYSTEM INFO")
    printf(f"Platform: {sys.platform}")
    printf(f"Python Version: {sys.version.split()[0]}")
    printf(f"Process ID: {os.getpid()}")


def delf(path=None, name=None):
    if path is None:
        path = inputf("delete>file path>")
    if name is None:
        name = inputf("delete>file name>")
    try:
        os.remove(path + "/" + name)
    except Exception as e:
        _check_unsafe(e)
        printf(f"error {e}")


def calc(num1=None, op=None, num2=None):
    try:
            if num1 is None:
                num1 = input_float("calc>num1>")
            if op is None:
                op = inputf("calc>op>")
            if num2 is None:
                num2 = input_float("calc>num2>")
    except Exception as e:
        _check_unsafe(e)
        printf(f"Error: {e}")
        return
    try:
        match op:
            case "+":
                printf(num1 + num2)
            case "-":
                printf(num1 - num2)
            case "*":
                printf(num1 * num2)
            case "/":
                printf(num1 / num2)
            case "**":
                printf(num1 ** num2)
            case "//":
                printf(num1 // num2)
            case "%":
                printf(num1 % num2)
            case _:
                printf("unknown operator")
    except ZeroDivisionError:
        printf("inf")


def show(path=None, name=None, encoding=None):
    if path is None:
        path = inputf("file path>")
    if name is None:
        name = inputf("file name>")
    if encoding is None:
        encoding = inputf("encoding>")
    try:
        with open(path + "/" + name, "r", encoding=encoding) as f:
            text_data = f.read()
            printf(text_data)
    except Exception as e:
        _check_unsafe(e)
        printf(f"Error: {e}")


def warp(path=None):
    if path is None:
        path = inputf("path")
    try:
        os.chdir(path)
    except Exception as e:
        _check_unsafe(e)
        printf(f"Error: {e}")


def scan(path=None, mode=None):
    try:
        if path is None:
            path = inputf("path")
        if mode is None:
            mode = inputf("mode")
        
        files = list(os.scandir(path))

        if mode == "items":
            filtered = filter(lambda x: x.is_file(), files)
        
            result = list(map(lambda x: x.name, filtered))
            printf(result)

        if mode == "dirs":
            filtered = filter(lambda x: x.is_dir(), files)
            result = list(map(lambda x: x.name, filtered))
            printf(result)

        if mode == "all":

            result = list(map(lambda x: x.name, files))
            printf(result)


    except Exception as e:
        _check_unsafe(e)
        printf(f"Error: {e}")


def run(name=None):
    if name is None:
        name = inputf("run")
    try:
        subprocess.Popen(name, shell=True)
    except Exception as e:
        printf(f"Error: {e}")
