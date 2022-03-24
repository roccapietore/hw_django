from datetime import date
from dateutil.relativedelta import relativedelta
from rest_framework import serializers
from users.models import min_user_age


class CheckUsersAgeValidator:
    def __call__(self, value: date):
        difference_in_age = relativedelta(date.today(), value).years
        if difference_in_age < min_user_age:
            raise serializers.ValidationError("User is too young for adding ad")


class CheckEmailDomain:
    def __call__(self, value: str):
        if value.endswith("rambler.ru"):
            raise serializers.ValidationError("User can`t use this domain")


