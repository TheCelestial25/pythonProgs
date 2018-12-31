import csv
import smtplib
from settings import SENDER_EMAIL, SENDER_PASSWORD

ACCEPTED_MSG = """
Hi {}!

We are thrilled to inform you that you have been selected for our programming workshop.

Your coach is {}.

Can't wait to see you there!

Thank you,
Workshop Organisers
"""

REJECTED_MSG = """
Hi {}!

We are sorry, due to a large number of applications we could not fit you in the workshop.

See you next time!

Thank you,
Workshop Organisers
""" 

with open('Book1.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	next(csv_reader)
	smtp = smtplib.SMTP('smtp.gmail.com')
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	smtp.login(SENDER_EMAIL, SENDER_PASSWORD)

	msg = None
	subject = None

	for row in csv_reader:
		name, email, accepted, coach, language = row
		if accepted == "Yes":
			msg = ACCEPTED_MSG.format(name, coach)
			subject = "WORKSHOP APPLICATION - ACCEPTED"
		else:
			msg = REJECTED_MSG.format(name)
			subject = "WORKSHOP APPLICATION - Not this time"
		
		email_msg = "Subject: {} \n\n{}".format(subject, email_msg)
		smtp.sendmail(SENDER_EMAIL, email, msg)
	smtp.quit()