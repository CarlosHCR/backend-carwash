"""
API V1: account Serializers
"""
###
# Libs
###
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from app.accounts.models import User


###
# Serializers
###
class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.phone_number = self.validated_data.get('phone_number', '')
        user.save(update_fields=['first_name', 'last_name', 'phone_number',])


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email',  'username', 'first_name',
                  'last_name', 'phone_number', 'role')
        read_only_fields = ('email', 'username', 'role')


class UserDetailsByRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('email', 'username', 'password')
