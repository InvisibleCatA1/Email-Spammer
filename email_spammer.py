import random
import ssl
import smtplib
import getpass
from datetime import datetime
from email.mime.multipart import *

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
run = True
servers = ["alt1.gmail-smtp-in.l.google.com", "alt2.gmail-smtp-in.l.google.com",
           "alt3.gmail-smtp-in.l.google.com", "alt4.gmail-smtp-in.l.google.com",
           "gmail-smtp-in.l.google.com"]


def getUserInputBoolean(question):
    while True:
        answer = input(userinput + question + " [Y/n]: ")
        if answer.lower() == "y":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("Please enter 'y' or 'n'")


def sendEmail(fakeEmail, toEmail, subject, content, server, port, auth=False, username=None, password=None):
    context = ssl.create_default_context()
    with smtplib.SMTP(server, port=port) as s:
        try:
            s.ehlo()
            # noah.newman@watershedschool.org
            s.starttls(context=context)
            s.ehlo()
            if auth:
                s.login(username, password)
                name = input(userinput + "Enter your for fake ac: ")
                payload = MIMEText(content)
                payload.set_charset("utf-8")

                payload["From"] = name + " <" + fromEmail + ">"
                payload['Subject'] = subject
                payload["To"] = f"{toEmail.split('@')[0]} <{toEmail}>"
                payload['Content-Type'] = "text/html; charset=utf-8"
                # server.sendmail(fromEmail, toEmail, payload.as_string())
                s.send_message(from_addr=username, to_addrs=toEmail, msg=payload)
            else:
                messageSend = f"From: {fakeEmail.split('@')[0]} <{fakeEmail}>\nT: {toEmail.split('@')[0]} <{toEmail}>\nSubject: {subject}\n\n{content}"

                s.sendmail(fakeEmail, toEmail, messageSend.encode())
                s.close()
            print(
                f"{good}Email sent to: {Fore.CYAN}{toEmail}{Fore.RESET}, From: {Fore.CYAN}{fakeEmail}{Fore.RESET}, Subject: {Fore.GREEN}{subject}{Fore.RESET}, Server: {Fore.YELLOW}{server}:{port}{Fore.RESET}, Auth: {Fore.BLUE}{auth}{Fore.RESET}, Time: {Fore.BLUE}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}")
        except Exception as e:
            print(f"{error}{Fore.RED}Error ({fakeEmail}): {Fore.RESET} {e}")


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
            msg = input(userinput + "Message: ")
            server = input(userinput + "Enter the server (blank for default): ")
            if server == "":
                server = random.choice(servers)
            port = input(userinput + "Enter the port (blank for default): ")
            if port == "":
                port = 25
            if getUserInputBoolean("Authenticate?"):
                username = input(userinput + "Username (Email): ")
                password = input(userinput + "Password: ")
                sendEmail(fromEmail, toEmail, subject, msg, "smtp.gmail.com", 25, True, username, password)
            else:

                sendEmail(fromEmail, toEmail, subject, msg, server, port)
        case "2":
            emails = []
            subjects = []
            contents = []
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
            if getUserInputBoolean("Use random subjects?"):
                if getUserInputBoolean("Use subjects from file?"):
                    filepath = input(userinput + "Enter the filepath: ")
                    filepath = filepath.replace("\"", "")
                    if not filepath.__contains__(".txt"):
                        print(f"{error}Filepath must end with .txt")
                        continue
                    try:
                        with open(filepath, "r") as f:
                            for sub in f.readlines():
                                subjects.append(sub.replace("\n", ""))
                    except Exception as e:
                        print(error + "File does not exist")
                        continue
                else:
                    while True:
                        sub = input(userinput + "Enter subject: ")
                        subjects.append(sub.replace("\n", ""))
                        if not getUserInputBoolean("Add another subject?"):
                            break
                print(f"{info}Subjects: {Fore.YELLOW}{subjects}{Fore.RESET}")
            else:
                subjects.append(input(userinput + "Enter subject: "))

            if getUserInputBoolean("Use random contents?"):
                if getUserInputBoolean("Use random contents from file?"):
                    filepath = input(userinput + "Enter the filepath: ")
                    filepath = filepath.replace("\"", "")
                    if not filepath.__contains__(".txt"):
                        print(f"{error}Filepath must end with .txt")
                        continue
                    try:
                        with open(filepath, "r") as f:
                            for content in f.readlines():
                                contents.append(content.replace("\n", ""))
                    except Exception as e:
                        print(error + "File does not exist")
                        continue
                else:
                    while True:
                        content = input(userinput + "Enter content: ")
                        contents.append(content)
                        if not getUserInputBoolean("Add another content?"):
                            break
                print(f"{info}Contents: {Fore.YELLOW}{contents}{Fore.RESET}")
            else:
                contents.append(input(userinput + "Enter content: "))

            toEmail = input(userinput + "Enter the email you want to send to: ")
            if not toEmail.__contains__("@"):
                print(f"{warn}Email " + toEmail + " is not valid")
                continue

            serverStr = input(userinput + "Enter the server (blank for default): ")
            if serverStr == "":
                serverStr = random.choice(["alt1.gmail-smtp-in.l.google.com", "alt2.gmail-smtp-in.l.google.com",
                                           "alt3.gmail-smtp-in.l.google.com", "alt4.gmail-smtp-in.l.google.com",
                                           "alt5.gmail-smtp-in.l.google.com",
                                           "gmail-smtp-in.l.google.com"])
            port = input(userinput + "Enter the port (blank for default): ")
            if port == "":
                port = 25

            if getUserInputBoolean("Authenticate?"):
                username = input(userinput + "Enter the username: ")
                password = input(userinput + "Enter the password: ")

            count = 1
            if getUserInputBoolean("Send multiple emails per account?"):
                count = int(input(userinput + "Enter the number of emails to send: "))
            print(f"{info}Sending {count} {'emails' if count > 1 else 'email'} per account")
            for email in emails:
                for i in range(count):
                    email = random.choice(emails)
                    content = random.choice(contents)
                    content = content.replace("{toEmail}", toEmail)
                    content = content.replace("{toName}", toEmail.split("@")[0])
                    content = content.replace("{fromEmail}", email)
                    content = content.replace("{fromName}", email.split("@")[0])
                    content = content.replace("{randomEmail}", random.choice(emails))
                    content = content.replace("{randomName}", random.choice(emails).split("@")[0])
                    subject = random.choice(subjects)
                    subject = subject.replace("{toEmail}", toEmail)
                    subject = subject.replace("{toName}", toEmail.split("@")[0])
                    subject = subject.replace("{fromEmail}", email)
                    subject = subject.replace("{fromName}", email.split("@")[0])
                    subject = subject.replace("{randomEmail}", random.choice(emails))
                    subject = subject.replace("{randomName}", random.choice(emails).split("@")[0])
                    sendEmail(email, toEmail, subject, content, random.choice(servers), port)
            print(good + "Emails sent")

        case "3":
            print(info + "Exiting...")
            run = False
