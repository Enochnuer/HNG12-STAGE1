Numberapp is a Django-powered web application that analyzes a given number and provides intriguing mathematical properties along with a fun fact. It offers a quick and engaging way to explore the characteristics of numbers in an educational format


Features
Number Classification: Classifies a number based on its mathematical properties.
Mathematical Properties:
Checks if the number is prime.
Checks if the number is perfect.
Determines if the number is an Armstrong number.
Identifies if the number is even or odd.
Calculates the sum of its digits.
Fun Fact: Provides a fun fact about the number.
Error Handling: Handles invalid inputs gracefully.


API Endpoint
Request
Make a GET request to the following endpoint:

/api/classify-number?number=any positive whole number
Response
Success (200 OK):
{
  "number": 9,
  "is_prime": False,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 9,
  "fun_fact": "9 is the highest single-digit number in the decimal system."
}


Error (400 BAD REQUEST):
{
  "number": a,
  "error": true
}

Installation
Clone the Repo: - git clone https://github.com/your-username/numberapp.git
cd numberapp
Install Dependencies:
Install the required packages from requirements.txt:
pip install -r requirements.txt
Start the Development Server:
python manage.py runserver

Backlink -> https://hng.tech/hire/python-developers