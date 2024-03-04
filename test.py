import requests

# Define the API URL
api_url = 'https://firstdeploy-cfxhxnpgwq-uc.a.run.app'  # Replace 'your-api-url' with the actual API URL

# Define the form data
form_data = {
    'Question1': 'What is RESTful web services?',
    'Answer1': 'RESTful web services follow the principles of REST, using standard HTTP methods for CRUD operations on resources.',
    'Question2': 'What is the purpose of the "this" keyword in Java?',
    'Answer2': '"this" refers to the current instance, distinguishing between instance variables and parameters with the same name.'
}

# Send a POST request to the API
response = requests.post(api_url, data=form_data)

# Check if the request was successful
if response.status_code == 200:
    # Print the response data
    print(response.json())
else:
    print('Error: Failed to make a request. Status Code:', response.status_code)