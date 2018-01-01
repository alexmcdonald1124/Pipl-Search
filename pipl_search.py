import csv
import json
from piplapis.search import SearchAPIRequest

# Define configuration file
config_file = json.load(open('configs/config.json'))

# Create list of email addresses with file input
with open('emails.txt', 'r') as input_file:
	emails = input_file.readlines()

# Prep CSV with column headers
with open('output.csv', 'wb') as csvfile:
	results_writer = csv.writer(csvfile)
	results_writer.writerow(['Email Address'] + ['Real Name'] + ['Job Description'] + ['Phone'] + ['Country'] + ['URL'] + ['Username'] + ['User ID'])

# Iterate list of email addresses
for email in emails:

	# Business search
	search = SearchAPIRequest(email=email, api_key=config_file['api_key'])
	response = search.send()

	# Define results
	name = response.name
	job = response.job
	phone = response.phone
	country = response.origin_country
	url = response.url
	username = response.username
	user_id = response.user_id

	# Print results to terminal
	print('Email %s' % email)
	print('Name: %s' % name)
	print('Job %s' % job)
	print('Phone %s' % phone)
	print('Country %s' % country)
	print('URL %s' % url)
	print('Username %s' % username)
	print('User ID: %s' % user_id)
	print('\n')

	# Write results to CSV
	with open('output.csv', 'a') as csvfile:
		results_writer = csv.writer(csvfile)
		results_writer.writerow([email] + [name] + [job] + [phone] + [country] + [url] + [username] + [user_id])