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


def validate_tags(tags_json):
    # just validate that tags_jason has depth of 1
    # meaning that both key and value
    # checking if a tags_json is a json array.
    if not isinstance(tags_json, list):
        raise ValidationError("Only array json is valid.")
    # checking each item to be string.
    for item in tags_json:
        if not isinstance(item, str):
            raise ValidationError("A nested json is not allowed.")


def validate_social(social_json):
    from django.core.validators import URLValidator
    # just validate that tags_jason has depth of 1
    # meaning that both key and value
    # and ensure that each value contains a full url in relation to it's key
    # example : "twitter": "https://twitter.com/user
    # checking if social_json is a dictionary and is not a list.
    if not isinstance(social_json, dict):
        raise ValidationError("Json not valid. (Non dictionary like object)")
    # checking each key and value to be string.
    for k, v in social_json.items():
        if (not isinstance(k, str)) or (not isinstance(v, str)):
            raise ValidationError("A nested json is not allowed.")
        # checking if a valid value is entered
        # each value should be a valid internet address like:
        # http(s)://url.domain/sth/sth_else
        url_validator = URLValidator()
        try:
            url_validator(v)
        except:
            raise ValidationError("(%s) url is not valid. example:http(s)://url.domain/sth/sth_else" % v)

