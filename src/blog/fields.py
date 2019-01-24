from rest_framework.serializers import ValidationError
from rest_framework import serializers
import jdatetime


# custom jdatetime field
class JDateTimeField(serializers.Field):
    def __init__(self, allow_null=False, *args, **kwargs):
        super(JDateTimeField, self).__init__(*args, **kwargs)
        self.allow_null = allow_null

    def to_representation(self, value):
        return '%s-%s-%s %s:%s' % (value.year, value.month, value.day, value.hour, value.minute)

    def to_internal_value(self, data):
        # parsing data
        if (not self.allow_null) and (not data):
            raise ValidationError('This field may not be blank')
        date, time = data.split(' ')
        year, month, day = [int(col) for col in date.split("-")]
        hour, minute = [int(col) for col in time.split(":")]
        try:
            response = jdatetime.datetime(year, month, day,
                                          hour=hour, minute=minute)
            return response
        except Exception as e:
            raise ValidationError(e)
