import smtplib

conn = smtplib.SMTP('imap.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('Your_Email_id', 'Password')
message = input("Enter Your message")

conn.sendmail('Sender Email ID','Recivers Email id', message)
conn.quit()