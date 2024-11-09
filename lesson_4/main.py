# Automating the sending email actions

# from decouple import config
# import yagmail

# sender_email = config('SENDER_EMAIL')
# receiver_email = config('RECEIVER_EMAIL')
# password = config('PASSWORD')

# subject = 'How to automate sending emails.'

# contents = """
#     Hi!, Testing
#     automation of sending emails
# """

# yag = yagmail.SMTP(user = sender_email, password = password)
# yag.send(to=receiver_email, subject = subject, contents = contents)
# print('Email send')


# Extracting data from pdf
import fitz

with fitz.open('file.pdf') as pdf:
    for page in pdf:
        print(page.get_text())