# Import necessary libraries
from platformdirs import user_data_dir  # Import a library for directory management
import requests  # Import the requests library for making HTTP requests
import json  # Import the JSON library for handling JSON data
import pymysql  # Import the pymysql library for MySQL database interaction

# Define the headers for the HTTP request to the API
headers = {
    "app-id": "6514fd46392a65cf6191a4fe"
}

# Make an HTTP GET request to the API to fetch user data
response = requests.get("https://dummyapi.io/data/v1/user", headers=headers)

# Check if the API request was successful (status code 200)
if (response.status_code == 200):
    print('Success')  # Print a success message to the console
else:
    print('Failed: ', response.status_code)  # Print an error message with the HTTP status code

# Parse the JSON response from the API into a Python dictionary
data = json.loads(response.content)

# Connect to the MySQL database
db = pymysql.connect(host='localhost', user='root', password='PASSWORD', db='my_database', port=3307)

# Create a cursor object for executing SQL commands
cursor = db.cursor()

# Create a 'users' table in the database if it doesn't already exist
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INT NOT NULL AUTO_INCREMENT, title VARCHAR(255) NOT NULL, firstName VARCHAR(255) NOT NULL, lastName VARCHAR(255) NOT NULL, picture VARCHAR(255) NOT NULL, PRIMARY KEY (id));')

# Iterate through the user data obtained from the API response
for user in user_data_dir['data']:  # Note: Should be 'data' from the 'data' variable, not 'user_data_dir'
    # Insert user data into the 'users' table in the database
    cursor.execute('INSERT INTO users (title, firstName, lastName, picture) VALUES (%s, %s, %s, %s)', (user['title'], user['firstName'], user['lastName'], user['pictuure']))

# Commit the changes to the database
db.commit()

# Close the cursor and the database connection
cursor.close()
db.close()
