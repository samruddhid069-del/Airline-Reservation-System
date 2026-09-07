def validate_number(value, name):

    try:
        return int(value)
    except:
        print(f"Invalid {name}. Please enter a number.")
        return None


def validate_float(value, name):

    try:
        return float(value)
    except:
        print(f"Invalid {name}. Please enter a valid amount.")
        return None


def validate_string(value, name):

    if value.strip() == "":
        print(f"{name} cannot be empty.")
        return None
    return value