
from rest_framework.viewsets import ModelViewSet
from goods.models import GoodsChannel,GoodsChannelGroup
from meiduo_admin.serializers.channel_serializer import *
from meiduo_admin.pages import MyPage
from rest_framework.decorators import action
from rest_framework.response import Response

# GET
# goods/channels/?page=1&pagesize=10

class ChannelViewSet(ModelViewSet):
    queryset = GoodsChannel.objects.all()
    serializer_class = ChannelModelSerializer
    pagination_class = MyPage

    # GET
    # goods/channel_types/
    @action(methods=['get'], detail=False)
    def channel_types(self, request):
        # 序列化返回频道分组所有数据
        group_queryset = GoodsChannelGroup.objects.all()
        s = ChannelGroupModelSerializer(group_queryset, many=True)
        return Response(s.data)


    # GET
    # goods/categories/
    # 获得一级分类
    @action(methods=['get'], detail=False)
    def categories(self, request):
        # 序列化返回所有一级分类的结果
        category1_queryset = GoodsCategory.objects.filter(parent=None)
        s = GoodsCategorySimpleSerializer(category1_queryset, many=True)
        return Response(s.data)










