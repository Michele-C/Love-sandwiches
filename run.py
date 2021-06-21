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

def get_sales_data():
    """
        Get sales figure input from user
    """
    print( "Please enter sales data from last market")
    print("Data should be 6 numbers, separated by commas")     
    print ( "Example: 2,3,4,5,6\n")	

    data_str = input("Enter your input here:")
    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises a ValueERROR if strings cannot be converted to int or if exacely 6 numbers 
    are not entered. 
    """
    try:
        [int(value) for  value in values]
        if len(values) != 6:
            raise ValueError(
                f"We expect 6 values and we only got {len(values)}"
                )

    except ValueError as e:
        print(f'Invalid data: {e}. Please try again.\n')

get_sales_data()


