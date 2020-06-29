import smtplib

sender_email = 'ardaasar0@gmail.com'
sender_password = 'arda3467'

def send_email():
    receiver = input('Receiver Email:')
    message = input('Your Message:')
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
        server.login(sender_email,sender_password)
        server.sendmail(sender_email,receiver,message)
        print('Succesful')
send_email()