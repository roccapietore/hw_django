from rest_framework import serializers


class NotTrueValidator:
    def __call__(self, value: bool):
        if value:
            raise serializers.ValidationError("Field IS_PUBLISHED must be False, not True")
