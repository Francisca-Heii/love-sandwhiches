import json
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

#Creating a function to collect the sales data from the user #
# then create a Dock string below the function to describe what our get_sales_data function is going to do#
# A Python function description goes  between triple double quotes#

def get_sales_data():
    '''
    Get sales figures input from the user
    '''

# Instruct the user to rpvide us with their sales data, will then let them know we are looking for 6 numbers separated by comma#
print("Please enter sales data from the last market.")
print("Data should be six numbers, separated by comma.")
print("Example 10,20,30,40,50,60\n")

# Next, use the input() method to get our sales  data from the user in the terminal #
# The value the user provides will be returned to us as a string,#
# so we’ll name this variable data_str, str being short for string.#

data_str = input("Enter your data here: ")
print(f"The data provided is{data_str}")  # check that we are getting a value assigned here, we print the data_str provided back to the terminal,#

# Since our code is inside the get_sales_data  function, we need to remember to call it#
# so that when we run our file the code  inside the function will also run.#
get_sales_data()

#Let’s check that by running our code. Do you  remember the command to run our Python file? ptyhon3 run.py#


