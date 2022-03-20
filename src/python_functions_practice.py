def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

def number_to_full_month_name(month_number):
    return months[month_number]

def number_to_short_month_name(month_number):
    return months[month_number][0:3]

def cube_volume(cube_side):
    return cube_side ** 3

def reverse_string(string):
    reversed_string = ""
    for letter in string:
        reversed_string = letter + reversed_string
    return reversed_string

def fahrenheit_to_celsius(f_temp):
    c_temp = (((f_temp - 32) * 5) / 9)
    return c_temp