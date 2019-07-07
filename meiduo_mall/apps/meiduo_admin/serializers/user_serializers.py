

# 创建一个序列化器，用于序列化User模型类
# id，username，mobile，email

from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password



class UserModleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',

            'username',
            'mobile',
            'email',

            'password'
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
        }


    def create(self, validated_data):
        # 调整
        # 密码改成加密的
        # 创建的是超级管理员
        # password = validated_data['password'] # 明文
        # validated_data['password'] = make_password(password) # 有效数据中的明文重新赋值为密文
        # validated_data['is_staff'] = True
        # return self.Meta.model.objects.create(**validated_data)

        return self.Meta.model.objects.create_superuser(**validated_data)


