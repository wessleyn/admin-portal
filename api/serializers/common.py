from rest_framework import serializers, renderers
from phonenumber_field.serializerfields import PhoneNumberField

class PhoneNumberSerializer(serializers.Serializer):
    number = PhoneNumberField(region="ZW")

    def get_value(self):
        return self.data['number'] if self.is_valid() else None