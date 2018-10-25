from rest_framework.exceptions import APIException
from rest_framework import serializers
import jdatetime


# custom jdate field that supports jalali date
class JDateField(serializers.Field):

    def __init__(self, allow_null=False, *args, **kwargs):
        super(JDateField, self).__init__(*args, **kwargs)
        self.allow_null = allow_null

    def to_representation(self, value):
        return '%s-%s-%s' % (value.year, value.month, value.day)

    def to_internal_value(self, data):
        # parsing data
        if (not self.allow_null) and (not data):
            raise APIException('This field may not be blank.')
        year, month, day = [int(col) for col in data.split('-')]
        try:
            response = jdatetime.date(year, month, day)
            return response
        except Exception as e:
            raise APIException(e)
