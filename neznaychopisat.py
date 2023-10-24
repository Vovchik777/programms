import smtplib
import os
def send_email(message):
    sender = "romakibasov@gmail.com"
    password = "#########"

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    try:
        server.login(sender,password)
        server.sendmail(sender,'vnovoid@gmail.com',message)

        return 'Отправлено!'

    except Exception as _ex:
        return f'{_ex}\nCheck you login or parol'


def main():
    message = input('Введите сообщение')
    print(send_email(message = message))

if __name__ =='__main__':
    main()

