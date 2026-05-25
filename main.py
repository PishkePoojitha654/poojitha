print("HELLO")
from datetime import datetime
current_year = datetime.now().year
name=input("enter your name")
birth_year=int(input("enter your birth year"))
current_age=current_year-birth_year
print("your current age is:",current_age)