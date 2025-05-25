from datetime import date


today = date.today()
bday = input("Enter your birthday [YYYY-MM-DD]: ")

bday = date.fromisoformat(bday)

age = today.year - bday.year

print("You are", age, "years old.")

