from datetime import datetime

def get_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value
        else:
            print("The field cannot be empty!")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt)) # asks for input, converts it to integer and returns it at the same time!

        except ValueError:
            print("Invalid number")

def get_timestamp():
    return datetime.now().strftime("%d-%m-%Y | %H:%M") # get scurrent date and time, then formats it into readable string
