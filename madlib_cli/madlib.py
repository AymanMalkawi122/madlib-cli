import errno
import os
import re
from pyfiglet import Figlet


def strip_text(txt):
    return re.sub("{[^}]*}", "{}", txt)


def get_parts(txt):
    parts = re.findall("{[^}]*}", txt)

    for i, part in enumerate(parts):
        parts[i] = re.sub("[{}]", "", part)

    return tuple(parts)


def read_template(path):
    if not os.path.exists(path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
    with open(path, "r") as f:
        lines = f.read()
    return lines

def write_template(path,txt):
    if not os.path.exists(path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
    with open(path, "w") as f:
        lines = f.write(txt)
    return lines


def parse_template(txt):
    print(txt, "debug")
    return (strip_text(txt), get_parts(txt))


def merge(txt, parts):
    for part in parts:
        txt = txt.replace("{}", f"{part}", 1)

    return txt


text = ""
choice = ""

if __name__ == "__main__":
    quit_flag = False
    write_template("assets/result.txt","empty file")

    def print_commands():
        commands = r"""
Commands
---------------------------------------------------------------------------------------------------------------------

1. read file: read text file

---------------------------------------------------------------------------------------------------------------------

2. play: populate your text with the apropriate input 

---------------------------------------------------------------------------------------------------------------------

3. display: display the result of your input merged with the text file input

---------------------------------------------------------------------------------------------------------------------

4. help: display all commands in madlib-cli

---------------------------------------------------------------------------------------------------------------------

5. quit: exit from madlib-cli

---------------------------------------------------------------------------------------------------------------------
"""
        print(commands)

    def print_menu():
        custom_fig = Figlet(font="big")
        print(
            custom_fig.renderText(" Mad lib "),
            """
**********************************************
**                                          **
**  Welcome to the Madlib Game              **
**  See the list of commands bellow         **
**                                          **
**  To display commands again, type "help"  **
**  To quit at any time, type "quit"        **
**                                          **
**********************************************
""",
        )
        print_commands()

    def read():
        global text
        text = read_template("assets/defult.txt")
        print("\nResult:\n", text, "\n")

    def play():
        global text

        extacted_txt, input_list = parse_template(text)
        parts=[]
        if(input_list):
            print("inseart the following\n")
            for i, prompt in enumerate(input_list):
                print(f"give me a {prompt}\n")
                usr_input = input(f">({prompt}) ")
                parts.append(str(usr_input))

            write_template("assets/result.txt",merge(extacted_txt,parts))
            print ("Done!")
        else:
            print("text is empty or invalid format")


    def display():
        print(read_template("assets/result.txt"))

    commands = {
        "read": read,
        "play": play,
        "display": display,
        "help": print_commands,
    }
    print_menu()

    while not quit_flag:
        choice = input("> ")

        if choice == "quit":
            print("\nExiting\n")
            quit_flag = True

        elif choice in commands.keys():
            commands[choice]()
