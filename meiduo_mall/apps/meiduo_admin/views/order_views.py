
from rest_framework.viewsets import ModelViewSet
from orders.models import OrderInfo
from meiduo_admin.serializers.order_serializers import *
from meiduo_admin.pages import MyPage


class OrderViewSet(ModelViewSet):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderSimpleSerializer
    pagination_class = MyPage


    def get_queryset(self):
        keywork = self.request.query_params.get("keyword")
        if keywork:
            return self.queryset.filter(order_id__contains=keywork)
        return self.queryset.all()


    def get_serializer_class(self):
        # 根据不同的请求，选用不同的序列化器去处理
        # list --> OrderSimpleSerializer
        # retrieve --> OrderDetailSerializer
        if self.action == "retrieve":
            return OrderDetailSerializer
        return self.serializer_class