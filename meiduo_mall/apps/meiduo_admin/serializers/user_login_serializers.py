

from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_jwt.utils import jwt_encode_handler,\
    jwt_payload_handler


# 定义一个序列化器，完成传统段身份认证逻辑
class UserLoginSerializer(serializers.Serializer):
    # 类属性，定义除校验段字段
    username = serializers.CharField(max_length=20)
    password = serializers.CharField()

    def validate(self, attrs):
        # attrs前端传来的所有数据
        # username = attrs.get("username")
        # password = attrs.get("password")

        # 1、根据用户名和密码完成身份认证
        # authenticate(username=username, password=password)
        user = authenticate(**attrs)

        # 2、认证失败，数据校验失败
        if not user:
            raise serializers.ValidationError("用户认证失败！")

        # 3、认证成功，要签发token
        # 3.1、获得payload
        payload = jwt_payload_handler(user)
        # 3.2、获得token
        jwt_token = jwt_encode_handler(payload)

        return {
            "user": user,
            "jwt_token": jwt_token
        }


