import csv, smtplib, ssl, getpass

message = """Subject: Your grade

Hi {name}, your grade is {grade}"""
from_name = 'Daniel Alejandro Escobar Prieto'
from_addresse_mail = input('Email: ')
password = getpass.getpass(prompt='Password: ', stream=None) 
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_addresse_mail, password)
    with open("contacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, grade in reader:
            server.sendmail(
                from_name,
                email,
                message.format(name=name,grade=grade),
            )
