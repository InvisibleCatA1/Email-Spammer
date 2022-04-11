import random
import smtplib
import ssl

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


def sendEmail(fromEmail, toEmail, subject, message, server, port):
    context = ssl.create_default_context()
    with smtplib.SMTP(server, port=port) as server:
        try:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.mail(fromEmail)
            server.rcpt(toEmail)
            server.data(f"From: {fromEmail}\nTo: {toEmail}\nSubject: {subject}\n\n{message}")
            server.quit()
        except Exception as e:
            print(f"{Fore.RED}Error: {Fore.RESET} {e}")
            return False
        finally:
            print(f"[{Fore.GREEN}S{Fore.RESET}] Email sent to: {toEmail}, From: {fromEmail}")


while run:
    print("[" + Fore.BLUE + "Main" + Fore.RESET + "] Menu")
    print("[1] - Send email")
    print("[2] - Spam emails")
    print("[3] - Exit")
    selection = input("> ")

    match selection:
        case "1":
            fromEmail = input("Enter email to send from: ")
            if not fromEmail.__contains__("@"):
                print(f"[{Fore.RED}E{Fore.RESET}] Email " + fromEmail + "is not valid")
                continue
            toEmail = input("Enter the email you want to send to: ")
            if not toEmail.__contains__("@"):
                print(f"[{Fore.RED}E{Fore.RESET}] Email " + toEmail + " is not valid")
                continue
            subject = input("Subject: ")
            message = input("Message: ")
            if getUserInputBoolean("Authenticate?"):
                print("test")
            else:
                server = input("Enter the server (blank for default): ")
                if server == "":
                    server = random.choice(["alt1.gmail-smtp-in.l.google.com", "alt2.gmail-smtp-in.l.google.com",
                                            "alt3.gmail-smtp-in.l.google.com", "alt4.gmail-smtp-in.l.google.com",
                                            "gmail-smtp-in.l.google.com"])
                port = input("Enter the port (blank for default): ")
                if port == "":
                    port = 25

                sendEmail(fromEmail, toEmail, subject, message, server, port)
        case "2":
            emails = []
            if getUserInputBoolean("Use emails from file"):
                filepath = input("Enter the filepath: ")
                try:
                    with open(filepath, "r") as f:
                        for email in f.readlines():
                            if not email.__contains__("@"):
                                print(f"[{Fore.RED}E{Fore.RESET}] Email " + email + " is not valid")
                            else:
                                emails.append(email.replace("\n", ""))
                except Exception as e:
                    print("Error: File does not exist")
                    continue
            else:
                while True:
                    email = input("Enter email: ")
                    if not email.__contains__("@"):
                        print(f"[{Fore.RED}E{Fore.RESET}] Email " + email + " is not valid")
                    else:
                        emails.append(email.replace("\n", ""))
                    if not getUserInputBoolean("Add another email?"):
                        break

            print("Emails: " + Fore.YELLOW + str(emails) + Fore.RESET)
            toEmail = input("Enter the email you want to send to: ")
            if not toEmail.__contains__("@"):
                print(f"[{Fore.RED}E{Fore.RESET}] Email " + toEmail + " is not valid")
                continue
            subject = input("Subject: ")
            message = input("Message: ")
            server = input("Enter the server (blank for default): ")
            if server == "":
                server = random.choice(["alt1.gmail-smtp-in.l.google.com", "alt2.gmail-smtp-in.l.google.com",
                                        "alt3.gmail-smtp-in.l.google.com", "alt4.gmail-smtp-in.l.google.com",
                                        "gmail-smtp-in.l.google.com"])
            port = input("Enter the port (blank for default): ")
            if port == "":
                port = 25
            for email in emails:
                sendEmail(email, toEmail, subject, message, server, port)

        case "3":
            print("Exiting...")
            run = False


