# Created by Tom5521 or Angel
# Under the GPL license 3.0

from os import getcwd, chdir, listdir
import os
from time import sleep as sl
import subprocess

current_directoy = getcwd()

hide = [">/dev/null 2>&1", "|ls > .out && rm -rf .out", "clear"]
sp = " "
All_text_cond = True
words = [
    "Installing ",  # 0
    "Installed",  # 1
    "Update Complete",  # 2
    "Updating repos",  # 3
    "...",  # 4
    "Updating",  # 5
    "Searching",  # 6
]
def sys(command):
    subprocess.run(command.split())

def clear():
    sys(hide[2])


class verbose:
    def all():
        hide[0] = ""
        hide[1] = ""
        hide[2] = ""
        global hide_all
        hide_all = True
        return hide_all

    def aur():
        hide[2] = ""
        hide[0] = ""

    def pacman():
        hide[1] = ""
        hide[2] = ""

    def quit_clear():
        hide[2] = ""


def installed():
    print(words[1])



def check(nombre_check):
    comprobator = False
    current_directoy = os.getcwd()
    os.chdir(current_directoy)
    os.system("clear")
    resultado_de_comprobacion = os.system("pacman -Q " + nombre_check + "> /tmp/tmp-check")
    with open("/tmp/tmp-check", "r") as optemp:
        readtemp = optemp.read()
        if nombre_check in readtemp:
            comprobator = True
        else:
            comprobator = False
    os.system("rm /tmp/tmp-check")
    return comprobator

def install(nombre_pacman, cond_1="", cond_2=""):
    match cond_1:
        case "-v":
            print(words[0] + nombre_pacman + words[4])
            sys("sudo pacman -S " + nombre_pacman + sp + cond_2 + sp + " --noconfirm")
            print(words[1])
        case _:
            clear()
            print(words[0] + nombre_pacman + words[4])
            sys(
                "sudo pacman -S "
                + nombre_pacman
                + " --noconfirm"
                + sp
                + cond_1
                + hide[1]
            )
            clear()
            installed()


def update():
    clear()
    print(words[3], words[4])
    sys("sudo pacman -Syy " + hide[0])
    clear()
    print(words[2])


def remove(removes, cond_1=""):
    if check(removes) == True:
        if "v" in cond_1:
            pass
            hide[0] = ""
        if "f" in cond_1:
            sys("sudo pacman -Rdd" + sp + removes + " --noconfirm" + hide[0])
        else:
            sys("sudo pacman -R" + sp + removes + " --noconfirm" + hide[0])
    else:
        print("El o los paquetes no se encontraron en su totalidad")
    hide[0] = ">/dev/null 2>&1"


class aur:
    def install(apps_aur, cond_1=""):
        global force
        force = False
        if "h" in cond_1:
            words[0, 4] = ""
        if "f" in cond_1:
            force = True
        for i in apps_aur.split():
            clear()
            url = "https://aur.archlinux.org/" + i + ".git"
            chdir("/tmp")
            if i in listdir("/tmp"):
                print("Already Cloned")
                sl(1)
                if force == True:
                    if "h" in cond_1 or hide_all == True:
                        pass
                    else:
                        print("but... Force is Activated :/")
                        sl(1)
                        print("removing original clone...")
                        sl(1)
                    sys("sudo rm -r " + i)
                    if "h" in cond_1:
                        pass
                    else:
                        print("cloning again...")
                    sys("git clone " + url + hide[0])
            else:
                print("Cloning " + i + words[4])
                sys("git clone " + url + hide[0])
            clear()
            chdir(i)
            print(words[0] + i + words[4])
            sys("makepkg -si --noconfirm" + hide[0])
            clear()
            chdir(current_directoy)
            installed()

    def manager(nombre_gestor, app_gestor, cond_1="", cond_2=""):
        match cond_1:
            case "-v":
                print(words[0] + app_gestor + words[4])
                sys(
                    nombre_gestor
                    + " -S"
                    + app_gestor
                    + sp
                    + cond_2
                    + sp
                    + " --noconfirm"
                )
                print(words[1])
            case "-s":
                sys(nombre_gestor + sp + app_gestor + hide[0])
            case _:
                clear()
                print(words[0] + app_gestor + words[4])
                sys(
                    nombre_gestor
                    + " -S"
                    + app_gestor
                    + " --noconfirm"
                    + sp
                    + cond_1
                    + hide[0]
                )
                clear()
                installed()

    def clone(names, route="", cond="", command=""):
        for i in names.split():
            if route == "":
                chdir("/tmp")
                print("No route selected\nCloning in /tmp...")
                if i in listdir("/tmp"):
                    print("Already Cloned")
                    sl(1)
            else:
                chdir(route)
            if "f" in cond:
                if i in listdir("/tmp") or listdir(route):
                    print("Already Cloned")
                    sl(1)
                    print("but... Force is Activated :/")
                    sl(1)
                    print("removing original clone...")
                    sl(1)
                    sys("sudo rm -r " + i)
            sys("git clone " + "https://aur.archlinux.org/" + i + ".git")
            if "i" in cond:
                chdir(i)
                sys("makepkg -si --noconfirm")
            if "c" in cond:
                sys(command)


def upgrade(condu_1="", condu_2=""):
    match condu_1:
        case "-v":
            print(words[5], words[4])
            sys("sudo pacman -Syu --noconfirm" + sp + condu_2)
        case _:
            clear()
            print(words[5], words[4])
            sys("sudo pacman -Syu --noconfirm" + sp + condu_1 + sp + hide[0])
            clear()
            print(words[2])


def get_list(list, cond1=""):
    if cond1 != "":
        options = [""]
        print(words[6], words[4])
        if "o" in cond1:
            options[0] = "Ss"
            if "e" in cond1:
                options[0] = "Si"
        elif "l" in cond1:
            options[0] = "Qs"
            if "e" in cond1:
                options[0] = "Q"
        sys("pacman -" + options[0] + sp + list)
    else:
        sys("pacman -Ss " + list)


def clone(link, route="", cond="", command=""):
    for i in link.split():
        if not route:
            chdir("/tmp")
            print("No route selected\nCloning in /tmp...")
        else:
            chdir(route)

        if i in listdir("/tmp") or listdir(route):
            if "f" in cond or hide_all == True:
                print("Already Cloned")
                sl(1)
                print("but... Force is Activated :/")
                sl(1)
                print("removing original clone...")
                sl(1)
                sys("sudo rm -r " + i)

        sys("git clone " + i)

        if "i" in cond:
            chdir(i)
            sys("makepkg -si --noconfirm")

        if "c" in cond:
            sys(command)


def upgrade_me():
    sys("pip install py-packarch --upgrade")
    sys("pip3 install py-packarch --upgrade")


def version():
    print("PY-PackArch \nCreated by Tom5521 \nVersion 1.9.2\nUnder the gpl-3.0 licence")


def info(package):
    sys("pacman -Si " + package)


def get_version(packages, cond=""):
    for i in packages.split():
        try:
            version = subprocess.check_output(["pacman", "-Q", i]).decode().split()[1]
            if "h" in cond:
                print(version)
            else:
                print(f"{i} is in version {version}")
        except subprocess.CalledProcessError as e:
            print(f"Error when trying to get {i} version: {e.stderr}")
    sys("rm /tmp/transpaced_data")

def manual():
    sys("xdg-open https://github.com/Tom5521/PY-PackArch/blob/master/README.md")
