from rest_framework import serializers
from .models import CustomUser


class CustomUserSerialzer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields = ('email','password')
        extra_kwargs ={
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        print(validated_data)
        user=CustomUser.objects.create(
            email=validated_data['email'],
            username=validated_data['email']

        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user
