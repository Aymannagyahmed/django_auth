from user.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    
    # object level valedation 
    def validate(self,data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('password doesn\'t match ')
        return data
        
    def create(self,validated_data):
        user = User.objects.create_user(username=validated_data['username'],password=validated_data['password'],)
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}