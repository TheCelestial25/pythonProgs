import csv

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

	msg = None

	for row in csv_reader:
		name, email, accepted, coach, language = row
		if accepted == "Yes":
			msg = ACCEPTED_MSG.format(name, coach)
		else:
			msg = REJECTED_MSG.format(name)

		print("Send email to: {}".format(email))
		print("Email content: \n{}".format(msg))