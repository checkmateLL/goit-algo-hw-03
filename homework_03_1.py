from datetime import datetime, timedelta

def get_days_from_today(date):
    try:
         # Trying to convert string to date
        string_to_date = datetime.strptime(date, "%Y-%m-%d")

        # If there is an error during conversion, message informs user about this error
    except ValueError:
        print(f"Input date is in incorrect format. Valid data format is YYYY-MM-DD.") 
        return None
    
    today_date = datetime.today()    
    days_to_today = (today_date - string_to_date).days
    return days_to_today


    # Example
difference_in_dates = get_days_from_today("2023-10-16")
print(difference_in_dates)