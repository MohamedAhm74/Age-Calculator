print("\t\t\t\t" + "=" * 60)
print("\t\t\t\t===================== Age Claculator =======================" )
print("\t\t\t\t" + "=" * 60)
# Collect Age Data
age = int(input("Please Enter Your Age : ").strip())
# Collect Age Unit
unit = input("Please Enter Age Uint : Months | Weeks | Days | Hours | Minutes | Seconds  : ").strip().lower()

# Get Age Units 

age_in_months = age * 12
age_in_weeks = age_in_months * 4
age_in_days = age * 365.25
age_in_hours = age_in_days * 24
age_in_minute = age_in_hours * 60
age_in_second = age_in_minute * 60

if unit == "months" or unit == "month" :
    print("Hello , You choosed Months")
    print(f"Your Age in Months is {age_in_months} Month")
elif unit == 'weeks' or unit == 'week':
    print("Hello , You choosed Weeks")
    print(f"Your Age in Weeks is {age_in_weeks} Week")
elif unit == 'days' or unit == 'day' :
    print("Hello , You choosed Days")
    print(f"Your Age in Days is {age_in_days} Day")
elif unit == 'hours' or unit == 'hour':
    print("Hello , You choosed Hours")
    print(f"Your Age in Hours is {age_in_hours} Hour")
elif unit == 'minutes' or unit == 'minute':
    print("Hello , You choosed Minutes")
    print(f"Your Age in Minutes is {age_in_minute} Minute")
elif unit == 'seconds' or unit == 'second':
    print("Hello , You choosed Seconds")
    print(f"Your Age in Seconds is {age_in_second} Second")