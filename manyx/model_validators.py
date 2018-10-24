import re
from django.core.exceptions import ValidationError


# checking if a given phone number is valid in Iran
def validate_mobile_phone_number(phone_number):
    # example : 09121234567
    if not re.search(r'^09[\d]{9}$', phone_number):
        # if the phone number in not in the given format, it will raise an exception.
        raise ValidationError("شماره موبایل صحیح نمیباشد.")


# checking if a social id only contains username(not domain or protocol or anything else)
def social_validator(social_id):
    if ('http', '/', 'www', ':') in social_id:
        # social id should not contain information about domain or protocol of the target site.
        raise ValidationError("تنها نام کاربری را وارد کنید.")

