import re

def validate_passwords(input_string):
    # Split the input string by commas and strip whitespace
    passwords = [p.strip() for p in input_string.split(",")]
    valid_passwords = []

    for pwd in passwords:
        # Check length requirements (6 to 12 characters)
        if len(pwd) < 6 or len(pwd) > 12:
            continue
        
        # Check for at least one lowercase letter [a-z]
        if not re.search("[a-z]", pwd):
            continue
            
        # Check for at least one uppercase letter [A-Z]
        if not re.search("[A-Z]", pwd):
            continue
            
        # Check for at least one digit [0-9]
        if not re.search("[0-9]", pwd):
            continue
            
        # Check for at least one special character [$#@]
        if not re.search("[$#@]", pwd):
            continue
            
        # If all checks pass, add to the valid list
        valid_passwords.append(pwd)

    # Join the valid passwords with commas and print
    print(",".join(valid_passwords))

# Example Usage
user_input = "ABd1234@1,a F1#,2w3E*,2We3345"
validate_passwords(user_input)