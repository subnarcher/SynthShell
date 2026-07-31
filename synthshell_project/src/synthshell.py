import os
import sys
import time as teto
import threading as thr

guide = """
====================================================================
               QUICK START: USER CODES & GUIDE v1.0
                       Framework: SynthShell
                     develpoer: subnarcher
====================================================================
 STEP 1: IMPORT & CONFIGURATION (Initialization)
--------------------------------------------------------------------
At the very beginning of your main script, import the core engine and 
configure the metadata. The engine creator (subnarcher) cannot be 
changed — it is hardcoded law! However, you can change the project 
name and set yourself as the software author.

Example:
  import shell
  
  shell.s_shell("UltraShell")     # Set your shell display name
  shell.s_ver("1.0-alpha")         # Set your software version
  shell.s_author("Ultra-Maniac")       # Set your nickname (Software Author)

 STEP 2: CHOOSE YOUR EXECUTION MODE
--------------------------------------------------------------------
• MODE 1: Asynchronous Background (Console runs in background)
  Use this if your script processes automatic scripts (loggers, loop 
  tasks) but you still need concurrent terminal access for debugging.
  
  Code:
    shell.start_async() # Launches the terminal environment in a background thread
    
    while True:
        import time
        time.sleep(5)
        shell.log("The script is quietly executing background operations...")

• MODE 2: Interactive Software (Calculators, quizzes, user interfaces)
  Use this if the user has to input data sequentially. DO NOT trigger 
  start_async().
  
  Code:
    # Secure numeric and string inputs. Do not add trailing colons!
    num1 = shell.input_float("Enter first number") 
    op = shell.input_str("Enter operator")
    num2 = shell.input_float("Enter second number")
    
    # Passing arguments into the integrated engine calculator
    shell.calc(num1, op, num2)

 STEP 3: ANTI-CRASH SYSTEM (Recovery Mode)
--------------------------------------------------------------------
To keep your software from forcefully crashing and printing ugly raw 
Windows tracebacks, wrap your execution paths inside a try/except shield. 
If a crash occurs, the framework drops you safely into a recovery shell.

Example:
  try:
      # Your risky logic (file I/O, networking, or math)
      result = 10 / 0
  except Exception as error:
      shell.log(f"Critical error: {error}")
      print("\n[Crash] Main script failed! Dropping into recovery shell...")
      
      shell.start() # Hard blocking environment. Type 'show' to view the crash log!

====================================================================

"""
standart = """
====================================================================
                 SYSTEM STANDARDS & API GUIDELINES v1.0
                       Framework: SynthShell
                     developer: subnarcher
====================================================================

[1] THE GOLDEN RULE OF THREADING (Console Synchronization)
--------------------------------------------------------------------
The OS console is shared globally across the process. Simultaneous data
input in different threads is STRICTLY PROHIBITED, as it disrupts 
the input buffers and causes critical glitches.

• Scenario A (Background Utility / Logger):
  You are allowed to call shell.start_async(). The main script must 
  run silently using background tasks. The main thread MUST NOT trigger
  any input methods (input_str, input_int, etc.).
  
• Scenario B (Interactive Software / Calculators / Questionnaires):
  Calling shell.start_async() is STRICTLY PROHIBITED. The program 
  must execute linearly and request data sequentially using input functions.

[2] INTERFACE DESIGN STANDARDS (UX/UI)
--------------------------------------------------------------------
• Clean Text Rule: When passing a prompt string to any input method 
  (e.g., shell.input_float("text")), DO NOT append colons (:), arrows (>)
  or trailing spaces. The system pointer ">" is appended automatically.
  Correct:   shell.input_float("first number")
  Incorrect: shell.input_float("first number: > ")

• String Trimming Rule: All string values that control application logic
  (commands, operators, file paths) must be free of accidental spacing. 
  Always use the .strip() method to sanitize user inputs.

[3] EMERGENCY PROTOCOL (Recovery Mode)
--------------------------------------------------------------------
• If the main script crashes due to an unexpected exception, the application 
  must prevent raw Windows error traces from showing up to the user.
• Developers are required to wrap critical blocks inside a try/except clause.
• Upon exception, the error details are dumped into a log file, followed 
  by a HARD BLOCKING shell.start() call. This drops the user into an emergency 
  shell, allowing them to type "show" to instantly inspect the crash log.

====================================================================

"""


fw_shell = "SynthShell"
sw_shell = "Shell"
miku_teto = "subnarcher"
sw_ver = "unknown"
fw_ver = "1.0"
software_author = "unknown"


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


def start_async():

    flow = thr.Thread(target=start, daemon=True)
    flow.start()


def start():
    while True:


        if fw_shell != "SynthShell" or miku_teto != "subnarcher":
            print("CRITICAL ERROR: Framework integrity compromised!")

            os._exit(1) 


        if os.name == 'nt':
            os.system('') 


        user_input = input(f"{sw_shell}>")


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
            case "guide":
                guide()
            case "standarts":
                standarts()
            case _:
                print("unknown command. try help")


def clear():
    os.system("cls")


def log(logs=None):
    if logs is None:
        logs = input(f"{sw_shell}>log>")
    print(logs)

    with open(sw_shell + "_logs.txt", "a", encoding="utf-8") as f:
        f.write(logs + "\n")


def phelp():
    print(f"{fw_shell} commands list")
    print("""
help - display this
log - display text and append in file Sytnhelllogs.txt
clear - clear shell
about - about shell
make - start to make file
sysinfo - display system information
delf - start to delete file
calc - calc num1 op num2
guide - create .txt file guide for using framework
standarts - create .txt file standarts for this framework
""")


def exitd(tm=None):
    if tm is None:
        exit()
    else:
        teto.sleep(tm)
        exit()


def about():
    print("About {wr_shell}")
    print(f"version: {fw_ver}")
    print(f"software author: {software_author}")
    print("======================================================")
    print(f"Shell creator: {miku_teto}")
    print(f"framework Shell name: {fw_shell}")


def make(f_path=None, f_name=None, f_mode=None, f_encoding=None, f_text=None):
    if f_name is None:
        f_path = input(f"{sw_shell}>make>path>")
        f_name = input(f"{sw_shell}>make>file_name>")
        f_mode = input(f"{sw_shell}>make>mode>")
        f_encoding = input(f"{sw_shell}>make>encoding>")
        f_text = input(f"{sw_shell}>make>file_text>")


    with open(f_path + "/" + f_name, f_mode, encoding=f_encoding) as f:
        f.write(f_text)
    

def sysinfo():
    print("SYSTEM INFO")

    print(f"Platform: {sys.platform}") 
    

    print(f"Python Version: {sys.version.split()[0]}") 
    
  
    print(f"Process ID: {os.getpid()}")


def input_str(text=""):
    return str(input(f"{sw_shell}>inputstr>{text}>"))


def input_int(text=""):
    try:
        return int(input(f"{sw_shell}>inpuntint>{text}>"))
    except Exception as e:
        print(f"Error: {e}")


def input_float(text=""):
    try:
        return float(input(f"{sw_shell}>inputfloat>{text}>"))
    except Exception as e:
        print(f"Error: {e}")


def inputf(text=""):    #unsafe
    try:
        return input(f"{sw_shell}>inputformated>{text}>")
    except Exception as e:
        print("Error: {e}")


def delf(f_path=None, f_name=None):
    if f_name is None or f_path is None:
        f_path = input(f"{sw_shell}>delete>file path>")
        f_name = input(f"{sw_shell}>delete>file name>")
    try:
        os.remove(f_path + "/" + f_name)
    except Exception as e:
        print("error {e}")
    

def calc(num1=None, op=None, num2=None):

    if num1 is None or op is None or num2 is None:
        try:
            num1 = float(input(f"{sw_shell}>calc>num1>"))
            op = (input(f"{sw_shell}>calc>op>"))
            num2 = float(input(f"{sw_shell}>calc>num2>"))
        except ValueError:
            print("Error")
    try:
        match op:
            case "+":
                print(num1 + num2)
            case "-":
                print(num1 - num2)
            case "*":
                print(num1 * num2)
            
            case "/":
                print(num1 / num2)
            case "**":
                print(num1 ** num2)
            case "//":
                print(num1 // num2)
            case "%":
                print (num1 % num2)
            case _:
                print("unknown operator")
    except ZeroDivisionError:
        print("inf")


def printf(text):
    print(f"{sw_shell}>printf>{text}")


def show(f_path=None, f_name=None, f_encoding=None):
    if f_name is None:
        f_path = input(f"{sw_shell}>file path>")
        f_name = input(f"{sw_shell}>file name>")
        f_encoding = input(f"{sw_shell}>encoding>")
    try:
        with open(f_path + "/" + f_name, "r", encoding=f_encoding) as f:
            text_data = f.read()
            printf(text_data)
    except Exception as error:
        printf(f"Error: {error}")


def standarts(f_path):
    if f_path is None:
        f_path = input(f"{fw_shell}>standarts>file path>")

    with open(f_path + "/" + f"{fw_shell}_standarts.txt", "w", encoding="utf8") as f:
        f.write(standarts)
    printf("standarts file.txt created")


def guide(f_path):
    if f_path is None:
        f_path = input(f"{fw_shell}>standarts>file path>")

    with open(f_path + "/" + f"{fw_shell}_guide.txt", "w", encoding="utf8") as f:
        f.write(guide)
    printf("guide file.txt created")