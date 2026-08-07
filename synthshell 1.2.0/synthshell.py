import shlex
import subprocess
import os
import sys
import time as teto
import random as miku
from shell_errors import error_msg


config = {
"software": "Shell",
"software_devs": "unknown",
"software_ver": "unknown",
}


def set_config(software=None, developers=None, version=None,):
    if software is None:
        pass
    else:
        config["software"] = software

    if developers is None:
        pass
    else:
        config["software_devs"] = developers

    if version is None:
        pass
    else:
        config["software_ver"] = version

    return software, developers, version


unsafe_mode = [False]
custom_commands = {}

def unsafe(state: bool):
    unsafe_mode[0] = state


def _check_unsafe(e):
    if unsafe_mode[0]:
        raise e


def printf(text):
    print(f"{config["software"]}>printf>{text}")


def input_str(text=""):
    return str(input(f"{config["software"]}>inputstr>{text}>"))


def input_int(text=""):
    try:
        return int(input(f"{config["software"]}>inputint>{text}>"))
    except Exception as e:
        _check_unsafe(e)
        print(f"Error: {error_msg(e)}")


def input_float(text=""):
    try:
        return float(input(f"{config["software"]}>inputfloat>{text}>"))
    except Exception as e:
        _check_unsafe(e)
        print(f"Error: {error_msg(e)}")


def inputf(text=""):
    try:
        return input(f"{config["software"]}>inputformated>{text}>")
    except Exception as e:
        _check_unsafe(e)
        print(f"Error: {error_msg(e)}")


def start(mode=None):

    if mode == "off":
        pass
    else:
        print("SynthShell v1.2.0 loaded.")
        print('Type "help", "about" for more information.\n')
        custom_commands["about"] = about

    while True:
        try:
            user_input = input(f"{os.getcwd()}>{config["software"]}> ").strip()
        
            if not user_input:
                continue

        
            tokens = shlex.split(user_input) 
            cmd = tokens[0]
            args = tokens[1:]

            match cmd:
                case "help":
                    phelp()
                case "clear":
                    clear()
                case "log":
                    if not args:
                        log()
                    else:
                        log(args[0])
                case "":
                    print("")
                case "exit":
                    exits()
                case "about":
                    about()
                case "make":
                    if not args:
                        make()
                    else:
                        make(args[0], args[1], args[2], args[3], args[4])
                case "sysinfo":
                    sysinfo()
                case "del":
                    if not args:
                        delf()
                    else:
                        delf(args[0], args[1])
                case "calc":
                    if not args:
                        calc()
                    else:
                        calc(args[0], args[1], args[2])
                case "show":
                    if not args:
                        show()
                    else:
                        show(args[0], args[1], args[2],)
                case "warp":
                    if not args:
                        warp()
                    else:
                        warp(args[0])
                case "scan":
                    if not args:
                        scan()
                    else:
                        scan(args[0], args[1])
                case "run":
                    if not args:
                        run()
                    else:
                        run(args[0])
                case "rename":
                    if not args:
                        rename()
                    else:
                        rename(args[0], args[1], args[2])
                case "folder":
                    if not args:
                        folder()
                    else:
                        folder(args[0], args[1], args[2])
                case "hex":
                    if not args:
                        hex()
                    else:
                        hex(args[0], args[1], args[2])
                case "off":
                    if not args:
                        off()
                    else:
                        off(args[0])
                case "multitup":
                    if not args:
                        multitup()
                    else:
                        multitup(args[0], args[1], args[2], args[3], args[4])
                case _:
                    if cmd in custom_commands:
                        custom_commands[cmd](*args)
                    else:
                        print(f'"{cmd}" is not a command')
        except BaseException as e:
            _check_unsafe(e)
            print(f"Error: {error_msg(e)}")

def add_command(cmd_name, func_object):
    custom_commands[cmd_name] = func_object


def start_core(mode=None):

    if mode == "off":
        pass
    else:
        print("SynthShell v1.2.0.")
        print('Type "help", "about" for more information.\n')
        custom_commands["about"] = about
    
    while True:
            try:
                user_input = input(f"{os.getcwd()}>{config["software"]}> ").strip()
            
                if not user_input:
                    continue
    
                tokens = shlex.split(user_input) 
                cmd = tokens[0]
                args = tokens[1:]

                if cmd in custom_commands:
                    try:
                        custom_commands[cmd](*args)
                    except Exception as e:
                        _check_unsafe(e)
                        print(f"Error: {error_msg(e)}")
                else:
                    print(f'"{cmd}" is not a command')

            except BaseException as e:
                        _check_unsafe(e)
                        print(f"Error: {error_msg(e)}")

    
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
        with open(config["software"] + "_logs.txt", "a", encoding="utf-8") as f:
            f.write(logs + "\n")
    except Exception as e:
        _check_unsafe(e)
        print(f"Error: {error_msg(e)}")


def log(logs=None):
    if logs is None:
        logs = inputf("log>text")
    try:
        with open(config["software"] + "_logs.txt", "a", encoding="utf-8") as f:
            f.write(logs + "\n")
    except Exception as e:
        _check_unsafe(e)
        print(f"Error: {error_msg(e)}")


def phelp(text=None):
    print("SynthShell help list")
    print(
        f""" 
help - display this 
log - append text in file {config["software"]} + log.txt 
clear - clear shell 
about - about shell 
make - start to make file 
sysinfo - display system information 
delf - start to delete file 
calc - calc num1 op num2 
show - display file text
warp - move to path
scan - scan folder
run - run file
rename - rename file
folder - create or delete folder
hex - display file hex-dump
off - shutdown the system
multitup - universal file manager (read/make/hex (only 128 bytes))
""")

    if text is None or text == "":
        pass
    else:
        print(f"Custom help list:")
        print(text)

def exits(tm=None):
    if tm is None:
        os._exit(0)
    else:
        teto.sleep(tm)
        os._exit(0)


def about():
    printf(f"About {config["software"]}")
    printf(f"version: {config["software_ver"]}")
    printf(f"software author: {config["software_devs"]}")
    print("======================================================")
    printf(f"Framework creator: subnarcher")
    printf(f"framework Shell name: SynthShell")
    printf(f"framework version: 1.2.0")
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

        match mode:
            case "w":
                mode = "w"
            case "a":
                mode = "a"
            case "e":
                mode = "x"
            case "wb":
                mode = "wb"
            case "ab":
                mode = "ab"
            case _:
                print("Error: unknown mode")
                return
            
        with open(os.path.join(path, name), mode, encoding=encoding) as f:
            f.write(text)
    except Exception as e:
        _check_unsafe(e)
        print(f"Error: {error_msg(e)}")


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
        os.remove(os.path.join(path, name))
    except Exception as e:
        _check_unsafe(e)
        print(f"error {error_msg(e)}")


def calc(num1=None, op=None, num2=None):
    try:
            if num1 is None:
                num1 = input_float("calc>num1")

            if num1 is None:
                return
            
            if op is None:
                op = inputf("calc>op>")

            if op is None:
                return
            
            if num2 is None:
                num2 = input_float("calc>num2")

            if num2 is None:
                return
    except Exception as e:
        _check_unsafe(e)
        print(f"Error: {error_msg(e)}")
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
        path = inputf("show>path")

    if name is None:
        name = inputf("show>name")

    if encoding is None:
        encoding = inputf("show>encoding")

    if encoding is True or encoding is False or encoding == "":
        encoding = "utf8"

    try:
        with open(os.path.join(path, name), "r", encoding=encoding) as f:
            text_data = f.read()
            printf(text_data)
    except Exception as e:
        _check_unsafe(e)
        print(f"Error: {error_msg(e)}")


def warp(path=None):
    if path is None:
        path = inputf("warp>path")

    try:
        os.chdir(path)
    except Exception as e:
        _check_unsafe(e)
        print(f"Error: {error_msg(e)}")


def scan(path=None, mode=None):
    try:
        if path is None:
            path = inputf("scan>path")
        if mode is None:
            mode = inputf("scan>mode")
        
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
        print(f"Error: {error_msg(e)}")


def run(name=None):
    if name is None:
        name = inputf("run>name")
    try:
        subprocess.Popen(name, shell=True)
    except Exception as e:
        print(f"Error: {error_msg(e)}")


def rename(path=None, name=None, text=None):
    if path is None:
        path = inputf("rename>path")

    if name is None:
        name = inputf("rename>name")

    if text is None:
        text = inputf("rename>text")

    os.rename(os.path.join(path, name), os.path.join(path, text))


def folder(path=None, name=None, mode=None):
    if path is None:
        path = inputf("folder>path")

    if name is None:
        name = inputf("folder>name")

    if mode is None:
        mode = inputf("folder>mode")

    if mode == "mf":
        try:
            os.mkdir(os.path.join(path, name))
        except Exception as e:
            _check_unsafe(e)
            print(f"Error: {error_msg(e)}")

    if mode == "df":
        try:
            os.rmdir(os.path.join(path, name))
        except Exception as e:
            _check_unsafe(e)
            print(f"Error: {error_msg(e)}")


def hex(path=None, name=None, byte=None):

    if path is None:
        path = inputf("hex>path")

    if name is None:
        name = inputf("hex>name")

    if byte is None:
        byte = int(inputf("hex>bite"))
    try:
        with open(os.path.join(path, name), "rb") as f:
            data = f.read(int(byte))

        printf(data.hex(" "))

    except Exception as e:
        _check_unsafe(e)
        print(f"Error: {error_msg(e)}")


def off(tm=0):
    try:
        tm = int(tm)
    except Exception as e:
        _check_unsafe(e)
        print(f"Error: {error_msg(e)}")
        return
    
    if os.name == "nt":
        os.system(f"shutdown /s /t {tm}")
    if os.name == "posix":
        if tm == 0:
            os.system("shutdown -h now")
        else:
            os.system(f"shutdown -h +{tm}")


def multitup(path=None, name=None, mode=None, encoding=None, text=None):
    if path is None:
        path = inputf("multitup>path")

    if name is None:
        name = inputf("multitup>name")

    if mode is None:
        mode = inputf("multitup>mode")

    if encoding is None:
        encoding = inputf("multitup>encoding or skip")

    if text is None:
        text = inputf("multitup>text or skip")
    if mode == "r" or mode == "rb":
        text = False

    match mode:
        case "w":
            mode = "w"
        case "a":
            mode = "a"
        case "r":
            mode = "r"
        case "e":
            mode = "x"
        case "wb":
            mode = "wb"
            encoding = None
        case "ab":
            mode = "ab"
            encoding = None
        case "rb":
            mode = "rb"
            encoding = None
            text = None
        case "rw":
            mode = "r+"
        case "rwc":
            mode = "w+"
        case "ar":
            mode = "a+"
        case _:
            print("Error: unknown mode")
            return
        
    try:
        with open(os.path.join(path, name), mode, encoding=encoding) as f:
            if text is False and mode == "r":
                show(path=path, name=name, encoding=encoding)
                return
            
            if mode == "rb":
                hex(path=path, name=name, byte=128)
                return
            
            f.write(text)
    except Exception as e:
        _check_unsafe(e)
        print(f"Error: {error_msg(e)}")
