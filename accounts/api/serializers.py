from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model() 

class CustomeUserSerializer(UserSerializer):
    class Meta:
        model = UserModel
        fields = ['id','name','email','dob']
        read_only_fields = ['id']