import re
from django.core.exceptions import ValidationError


# checking if a given phone number is valid in Iran
def validate_mobile_phone_number(phone_number):
    # example : 09121234567
    if not re.fullmatch(r'^09[\d]{9}$', phone_number):
        # if the phone number in not in the given format, it will raise an exception.
        raise ValidationError("This Phone Number is not Valid.")


# validating username to make sure space or special charecters are not in the entered username
def validate_username(username):
    if not re.fullmatch(r'[a-zA-Z0-9_]+', username):
        raise ValidationError('This Username is not Valid.')