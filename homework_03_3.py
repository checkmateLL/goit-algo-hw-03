import re

def normalize_phone(phone_number):

    # Replacing (deleting) all possible characters except numbers and +
    pattern = r"[^\d+]"
    replacement = r""
    formatted_phone = re.sub(pattern, replacement, phone_number)

    # Checking how the number starts and formatting it to the schema +380
    if formatted_phone.startswith('+380'):
        return formatted_phone
    elif formatted_phone.startswith('38'):
        formatted_phone = '+' + formatted_phone
    elif formatted_phone.startswith('0'):
        formatted_phone = '+38' + formatted_phone

    return formatted_phone

    # Example
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)