from django.core.exceptions import ValidationError


def validate_tags(tags_json):
    if not tags_json:
        return None
    # just validate that tags_jason has depth of 1
    # checking if a tags_json is a json array.
    if not isinstance(tags_json, list):
        raise ValidationError("Only array json is valid.")
    # checking each item to be string.
    for item in tags_json:
        if not isinstance(item, str):
            raise ValidationError("A nested json is not allowed.")

