import random
import smtplib
import ssl
import getpass

from colorama import Fore

a = r"""___________              .__.__              _________                                           
\_   _____/ _____ _____  |__|  |            /   _____/__________    _____   _____   ___________  
 |    __)_ /     \\__  \ |  |  |    ______  \_____  \\____ \__  \  /     \ /     \_/ __ \_  __ \ 
 |        \  Y Y  \/ __ \|  |  |__ /_____/  /        \  |_> > __ \|  Y Y  \  Y Y  \  ___/|  | \/ 
/_______  /__|_|  (____  /__|____/         /_______  /   __(____  /__|_|  /__|_|  /\___  >__|    
        \/      \/     \/                          \/|__|       \/      \/      \/     \/        """

print(Fore.BLUE + a + Fore.RESET)
print(f"By: {Fore.GREEN}@{Fore.RESET}InvisibleCat#00001")
print("Project page: https://github.com/InvisibleCatA1/Email-Spammer")

good = f"[{Fore.GREEN}+{Fore.RESET}] "
error = f"[{Fore.RED}E{Fore.RESET}] "
info = f"[{Fore.BLUE}I{Fore.RESET}] "
warn = f"[{Fore.YELLOW}!{Fore.RESET}] "
userinput = f"[{Fore.CYAN}?{Fore.RESET}] "

randomSubject = False
randomBody = False


def getUserInputBoolean(question):
    while True:
        answer = input(userinput + question + " [Y/n]: ")
        if answer.lower() == "y":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("Please enter 'y' or 'n'")


run = True


def sendEmail(fromEmail, toEmail, subject, message, server, port, auth=False, username=None, password=None):
    context = ssl.create_default_context()
    with smtplib.SMTP(server, port=port) as server:
        try:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            if auth:
                server.login(username, password)

            # server.mail(fromEmail)
            # server.rcpt(toEmail)
            # server.data(f"From: {fromEmail}\nTo: {toEmail}\nSubject: {subject}\n\n{message}")
            server.sendmail(fromEmail, toEmail, f"From: {fromEmail}\nTo: {toEmail}\nSubject: {subject}\n\n{message}")
            server.quit()
            print(f"{good}Email sent to: {toEmail}, From: {fromEmail}")
        except Exception as e:
            print(f"{error}{Fore.RED}Error: {Fore.RESET} {e}")



while run:
    print("[" + Fore.BLUE + "Main" + Fore.RESET + "] Menu")
    print("[1] - Send email")
    print("[2] - Spam emails")
    print("[3] - Exit")
    selection = input("> ")

    match selection:
        case "1":
            fromEmail = input(userinput + "Enter email to send from: ")
            if not fromEmail.__contains__("@"):
                print(f"{warn}Email " + fromEmail + "is not valid")
                continue
            toEmail = input(userinput + "Enter the email you want to send to: ")
            if not toEmail.__contains__("@"):
                print(f"{warn}Email " + toEmail + " is not valid")
                continue
            subject = input(userinput + "Subject: ")
            message = input(userinput + "Message: ")
            if getUserInputBoolean("Authenticate?"):
                username = input(userinput + "Username: ")
                #password = getpass.getpass(userinput + "Password: ")
                password = input(userinput + "Password: ")
                sendEmail(fromEmail, toEmail, subject, message, "smtp.gmail.com", 587, True, username, password)
            else:
                server = input(userinput + "Enter the server (blank for default): ")
                if server == "":
                    server = random.choice(["alt1.gmail-smtp-in.l.google.com", "alt2.gmail-smtp-in.l.google.com",
                                            "alt3.gmail-smtp-in.l.google.com", "alt4.gmail-smtp-in.l.google.com",
                                            "gmail-smtp-in.l.google.com"])
                port = input(userinput + "Enter the port (blank for default): ")
                if port == "":
                    port = 25

                sendEmail(fromEmail, toEmail, subject, message, server, port)
        case "2":
            emails = []
            if getUserInputBoolean("Use emails from file"):
                filepath = input(userinput + "Enter the filepath: ")
                filepath = filepath.replace("\"", "")
                if not filepath.__contains__(".txt"):
                    print(f"{error}Filepath must end with .txt")
                    continue
                try:
                    with open(filepath, "r") as f:
                        for email in f.readlines():
                            if not email.__contains__("@"):
                                print(f"{warn}Email " + email + " is not valid")
                            else:
                                emails.append(email.replace("\n", ""))
                except Exception as e:
                    print(error + "File does not exist")
                    continue
            else:
                while True:
                    email = input(userinput + "Enter email: ")
                    if not email.__contains__("@"):
                        print(f"{error}Email " + email + " is not valid")
                    else:
                        emails.append(email.replace("\n", ""))
                    if not getUserInputBoolean("Add another email?"):
                        break

            print("Emails: " + Fore.YELLOW + str(emails) + Fore.RESET)
            toEmail = input(userinput + "Enter the email you want to send to: ")
            if not toEmail.__contains__("@"):
                print(f"{warn}Email " + toEmail + " is not valid")
                continue

            subject = input(userinput + "Subject: ")
            message = input(userinput + "Message: ")

            server = input(userinput + "Enter the server (blank for default): ")
            if server == "":
                server = random.choice(["alt1.gmail-smtp-in.l.google.com", "alt2.gmail-smtp-in.l.google.com",
                                        "alt3.gmail-smtp-in.l.google.com", "alt4.gmail-smtp-in.l.google.com",
                                        "gmail-smtp-in.l.google.com"])
            port = input(userinput + "Enter the port (blank for default): ")
            if port == "":
                port = 25
            for email in emails:
                sendEmail(email, toEmail, subject, message, server, port)
            print(good + "Emails sent")

        case "3":
            print(info + "Exiting...")
            run = False
