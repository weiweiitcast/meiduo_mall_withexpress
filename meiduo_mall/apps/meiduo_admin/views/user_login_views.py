

from rest_framework.views import APIView
from meiduo_admin.serializers.user_login_serializers import UserLoginSerializer
from rest_framework.response import Response

# 实现用户登陆请求：用户数据校验（用户名和密码）
# 签发jwt_token
class UserLoginView(APIView):
    def post(self, request):
        # 1、身份认证，签发token
        serializer = UserLoginSerializer(data=request.data)
        # 1.1 启动校验流程
        serializer.is_valid(raise_exception=True)

        # serializer.validated_data有效数据经过校验之后获得，validate函数返回值
        # 2、构造响应对象，构造返回的数据格式
        return Response({
            "username": serializer.validated_data.get("user").username,
            "user_id": serializer.validated_data.get("user").id,
            "token": serializer.validated_data.get("jwt_token")
        })