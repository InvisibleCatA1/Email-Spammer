import smtplib

from colorama import Fore
from easygui import fileopenbox

a = r"""___________              .__.__              _________                                           
\_   _____/ _____ _____  |__|  |            /   _____/__________    _____   _____   ___________  
 |    __)_ /     \\__  \ |  |  |    ______  \_____  \\____ \__  \  /     \ /     \_/ __ \_  __ \ 
 |        \  Y Y  \/ __ \|  |  |__ /_____/  /        \  |_> > __ \|  Y Y  \  Y Y  \  ___/|  | \/ 
/_______  /__|_|  (____  /__|____/         /_______  /   __(____  /__|_|  /__|_|  /\___  >__|    
        \/      \/     \/                          \/|__|       \/      \/      \/     \/        """

print(Fore.BLUE + a + Fore.RESET)
print(f"By: {Fore.GREEN}@{Fore.RESET}InvisibleCat#00001")
print("Project page: https://github.com/InvisibleCatA1/Email-Spammer")


def getUserInputBoolean(question):
    while True:
        answer = input(question + " [Y/n]: ")
        if answer.lower() == "y":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("Please enter 'y' or 'n'")
run = True


def sendEmail(fromEmail, toEmail, subject, message):
    server = smtplib.SMTP('gmail-smtp-in.l.google.com:25')
    server.starttls()
    server.ehlo("example.com")
    server.mail(fromEmail)
    server.rcpt(toEmail)
    server.data(f"From: {fromEmail}\nTo: {toEmail}\nSubject: {subject}\n\n{message}")
    server.quit()


while run:
    print("[" + Fore.BLUE + "Main" + Fore.RESET + "] Menu")
    print("[1] - Send email")
    print("[2] - Spam emails")
    print("[3] - Exit")
    selection = input("> ")

    match selection:
        case "1":
            fromEmail = input("From email: ")
            if not fromEmail.__contains__("@"):
                print("Please enter a valid email")
                continue
            toEmail = input("To email: ")
            if not toEmail.__contains__("@"):
                print("Please enter a valid email")
                continue
            subject = input("Subject: ")
            message = input("Message: ")
            sendEmail(fromEmail, toEmail, subject, message)