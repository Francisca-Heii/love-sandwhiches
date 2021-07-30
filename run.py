import json
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Get sales figures input from the user.
    Run a while loop to collect a valid of data from the user
    via terminial, which must be a string of six numbers separated
    by commas, the loop will repeadly request data, until is valid.
    '''
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by comma.")
        print("Example 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print("Data is valid!")
            break
    return sales_data 



#  create a new function  to handle our validation validate_data() pass it a parameter  of “values” #
def validate_data(values):
    '''
    Inside the try, converts all string values into intergers.
    Raise ValueError if strings cannot can not converted into int
    or if there arent exactly six values.
    '''
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
        f"Exactly six values required, you provided {len(values)}"
        )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True     


def update_sales_worksheet(data): #And as always the new function needs  a docstring to explain what it does. Is a good habit to get into early#
    '''
    Update sales worksheet, add new row with the list data provided.
    '''
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")


def calculate_surplus_data(sales_row):
    '''
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure is substracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when the stock was sold out.
    '''
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data


def main():
    '''
    Run all program functions
    '''
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data) #calling a function#
    new_surplus_data = calculate_surplus_data(sales_data)
    print(new_surplus_data)

print("Welcome to our love sandwhich Data Automation")
main()


