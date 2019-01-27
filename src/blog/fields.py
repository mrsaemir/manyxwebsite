from rest_framework.serializers import ValidationError
from rest_framework import serializers
import jdatetime


# custom jdatetime field
class JDateTimeField(serializers.Field):
    # auto now sets time to now automatically.
    def __init__(self, allow_null=False, auto_now=False, *args, **kwargs):
        super(JDateTimeField, self).__init__(*args, **kwargs)
        self.allow_null = allow_null
        self.auto_now = auto_now

    def to_representation(self, value):
        return '%s-%s-%s %s:%s' % (value.year, value.month, value.day, value.hour, value.minute)

    def to_internal_value(self, data):
        # if data is None and auto_now is True. automatically set to now
        if self.auto_now and (not data):
            response = jdatetime.datetime.now()
            return response
        # parsing data
        if (not self.allow_null) and (not data):
            raise ValidationError('This field may not be blank')
        # parsing data
        try:
            date, time = data.split(' ')
            year, month, day = [int(col) for col in date.split("-")]
            hour, minute = [int(col) for col in time.split(":")]
        except Exception:
            raise ValidationError('Datetime should be in YYYY-MM-DD HH:MM format.')
        try:
            response = jdatetime.datetime(year, month, day,
                                          hour=hour, minute=minute)
            return response
        except Exception as e:
            raise ValidationError(e)
