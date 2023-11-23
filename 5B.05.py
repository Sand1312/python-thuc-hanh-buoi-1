from datetime import datetime

def calculate_age_of_person(date_of_birth):
    age = datetime.now().year - date_of_birth
    return age

date_of_birth = int(input())
age = calculate_age_of_person(date_of_birth)
print(f"This year, your age is {age}")
