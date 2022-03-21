from rest_framework import serializers
from ads.models import User
from users.models import Location


class UserSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = User
        exclude = ["password"]


class UserCreateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(required=False, many=True, read_only=True, slug_field='name')

    class Meta:
        model = User
        exclude = ["id"]
        extra_kwargs = {'password': {'write_only': True}}

        def is_valid(self, raise_exception=False):
            self._locations = self.initial_data.pop("locations")
            return super().is_valid(raise_exception=raise_exception)

        def create(self, validated_data):
            new_user = super().create(validated_data)

            for location_name in self._locations:
                location, _ = Location.objects.get_or_create(name=location_name)
                new_user.locations.add(location)

            new_user.save()
            return new_user


class UserUpdateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(required=False, many=True, read_only=True, slug_field='name')

    class Meta:
        model = User
        fields = "__all__"

        def is_valid(self, raise_exception=False):
            self._locations = self.initial_data.pop("locations")
            return super().is_valid(raise_exception=raise_exception)

        def create(self, validated_data):
            new_user = super().create(validated_data)

            for location_name in self._locations:
                location, _ = Location.objects.get_or_create(name=location_name)
                new_user.locations.add(location)

            new_user.update()
            return new_user


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

