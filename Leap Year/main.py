def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(years, months):
    """ These are called Docstrings: This gives an overview of what this function does.
    They also appear when calling the function like the documentation of functions like len() do. """
    if months > 12 or months < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(years) and months == 2:
        return 29
    else:
        return month_days[months - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
print(days_in_month(years=year, months=month))
