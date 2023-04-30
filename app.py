from datetime import datetime, timedelta

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# prompt the visitor to enter their name and date of birth
name = input("Enter your name: ")
dob_str = input("Enter your date of birth (DD-MM-YYYY): ")

# parse the input string into a date object
dob = datetime.strptime(dob_str, '%d-%m-%Y').date()

# calculate the age based on the date of birth
age = calculate_age(dob)

# generate a pickup line based on the name and age
if age < 18:
    pickup_line = "Hey, " + name + "! Did you get your learner's permit yet?"
elif age < 25:
    pickup_line = "Hey, " + name + "! Are you a student? You look too smart to be anything else."
elif age < 40:
    pickup_line = "Hey, " + name + "! Are you a magician? Because every time I look at you, everyone else disappears."
else:
    pickup_line = "Hey, " + name + "! You must be a fossil, because you've been on my mind for ages."

# print out the resulting pickup line
print(pickup_line)
