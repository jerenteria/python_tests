# Passing function
def get_formatted_name(first, last):
    """Generate a neatly formatted full name"""
    full_name = f"{first} {last}"
    return full_name.title()

# Failing function due to the test functions is only looking for first and last name no middle names to fix we must make middle
# name optional instead of get_formatted_name2(first, middle, last): use get_formatted_name2(first, last, middle=''):
def get_formatted_name2(first, last, middle=''):
    """Generated a neatly formatted full name"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()