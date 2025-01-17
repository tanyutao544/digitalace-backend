from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        # use the following command to easily
        # retrieve all fields of User:
        # [f.name for f in User._meta.fields]
        fields = (
            # "id",
            "password",
            # "last_login",
            # "is_superuser",
            # "company",
            # "is_active",
            # "is_staff",
            "email",
            "name",
            # "department",
            # "role",
            # "image",
            # "resume",
            # "first_name",
            # "last_name",
            # "residential_address",
            # "postal_code",
            # "ic_no",
            # "nationality",
            # "gender",
            # "date_of_birth",
            # "date_of_commencement",
            # "date_of_cessation",
        )
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    # TODO: create employee by POST /employees/
    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""

    email = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password,
        )
        if not user:
            msg = _("Unable to authenticate with provided credentials")
            raise serializers.ValidationError(msg, code="authentication")

        attrs["user"] = user
        return attrs
