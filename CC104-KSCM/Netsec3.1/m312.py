year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    # Write the if-elif-elif-else block here.
    if year % 400 == 0:
        print(f"{year} is a leap year.")
    elif year % 4 == 0 and year % 100 != 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
