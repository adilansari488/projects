from os import system
from time import sleep
from random import randint


def start():
    fig_fonts = ('banner.flf', 'big.flf', 'block.flf', 'bubble.flf', 'digital.flf', 'ivrit.flf', 'lean.flf', 'mini.flf', 'mnemonic.flf',
                 'script.flf', 'shadow.flf', 'slant.flf', 'small.flf', 'smscript.flf', 'smshadow.flf', 'smslant.flf', 'standard.flf', 'term.flf')
    font_used = randint(0,len(fig_fonts))
    font_used = fig_fonts[font_used-1]
    system("figlet -f {} Welcome to our menu program".format(font_used))

def menu():
    print("""
   \t \t ---------------------------------------------
   \t \t| Press 0 for exit                            |
   \t \t| Press 1 for show date and time              |
   \t \t| Press 2 for ip address of any website       |
   \t \t| Press 3 for get a quote in fun way          |
   \t \t| Press 4 for check your private ip address   |
   \t \t| Press 5 for Docker Menu                     |
   \t \t| Press 6 for clear the terminal              |
   \t \t ---------------------------------------------
    """)

def date():
    system("date")

def webip():
    web = str(input("Please Enter Website Address : "))
    print("IP Address of {} is : ".format(web))
    system("ping -c 1 {} | grep -E -o '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' | head -n 1".format(web))


def funquote():
    cowsay_chars = ('beavis.zen', 'blowfish', 'bud-frogs', 'bunny', 'cheese', 'cower', 'default', 'dragon', 'dragon-and-cow', 'elephant', 'elephant-in-snake', 'eyes', 'flaming-sheep', 'fox', 'ghostbusters', 'head-in', 'hellokitty', 'kiss', 'kitty', 'koala', 'kosh', 'luke-koala', 'mech-and-cow', 'meow', 'milk', 'moofasa', 'moose', 'mutilated', 'ren', 'sheep', 'skeleton', 'small', 'stegosaurus', 'stimpy', 'supermilker', 'surgery', 'telebears', 'three-eyes', 'turkey', 'turtle', 'tux', 'udder', 'vader', 'vader-koala', 'www')
    random_chars = randint(0,len(cowsay_chars))
    random_chars = cowsay_chars[random_chars-1]
    system("cowsay -f {} `fortune`".format(random_chars))
    sleep(5)

def myip():
    print("Your Private IP Adress is : ")
    system("ifconfig enp0s3 | grep -E -o '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' | head -n 1")

def dmenu():
    print("-------------------------")
    print("  Welcome to Docker Menu")
    print("-------------------------\n")
    print("Press 1 to Check Locally Available Docker Images")
    print("Press 2 to check running containers")
    print("Press 3 for pull image from docker hub")
    print("Press 4 for creating custom docker image")
    print("Press 5 to kill running or exited containers")
    docker_option = int(input("\nPlease Enter Your Choice : "))

    if docker_option == 1 :
        system("docker images")

    if docker_option == 2 :
        system("docker ps")

    if docker_option == 3 :
        img = input("Please Enter exact docker image name you want to pull : ")
        system("docker pull {}".format(img))

    if docker_option == 4 :
        print("Welcome to Dockerfile editor...\n")
        print("Anytime type 'exit' without quotes to exit the editor.")
        editor = print("\nPlease Enter Your Dockerfile Commands below :\n")
        file = open('Dockerfile','w')
        while True :
            cmnd = input()
            if cmnd == "exit" :
                imgname = input("Please Enter image name you want to save as :")
                file.close()
                system("docker build -t {} .".format(imgname))
                break
            else :
                file.write(cmnd+"\n")
    if docker_option == 5 :
        print("Press 1 to kill all container")
        print("Press 2 to kill a specific container")
        kill_option = int(input("Please Enter Your Choice : "))
        
        if kill_option == 1 :
            system("docker ps -aq > dkrids")
            tempids = open('dkrids','r')
            idstr = ""
            for i in tempids :
                idstr += i
            tempids.close()
            system("rm -f dkrids y")
            idstr = idstr.replace('\n',' ')
            system("docker rm -f {}".format(idstr))
            print("Containers killed, their ids are given above:")
        if kill_option == 2 :
            print("Available Container ids are :")
            system("docker ps -aq") 
            img_id = input("Please enter id of the container : ")
            system("docker rm -f {}".format(img_id))

def clear():
    system("clear")

def main():
    start()
    option = None
    while option != 0 :
        menu()
        option = int(input("Enter Your Choice : "))
        if option == 0 :
            print("""Thank You for using our services...\n""")
            exit()
        elif option == 1 :
            date()
        elif option == 2 :
            #web = str(input("Please Enter Website Address : "))
            webip()
        elif option == 3 :
            funquote()
        elif option == 4 :
            myip()
        elif option == 5 :
            dmenu()
        elif option == 6 :
            clear()
        cont = input("Press enter to continue..")

main()









