def ageCalculator(y , m , d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y , m , d)
    age = int((today - dob).days/ 365.25)
    print("your age is:",age)
while True:
   y = int(input("Enter the year:"))
   m = int(input("Enter the month:"))
   d = int(input("Enter the day:"))
   ageCalculator(y , m , d)
