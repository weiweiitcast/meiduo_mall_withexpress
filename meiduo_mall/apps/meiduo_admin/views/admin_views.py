
from rest_framework.viewsets import ModelViewSet
from users.models import User
from meiduo_admin.serializers.admin_serializers import *
from meiduo_admin.pages import MyPage
from rest_framework.response import Response


class AdminViewSet(ModelViewSet):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = AdminSerializer
    pagination_class = MyPage


    # GET
    # permission/groups/simple/
    def simple(self, request):
        groups = Group.objects.all()
        s = AdminGroupSerializer(groups, many=True)
        return Response(s.data)






