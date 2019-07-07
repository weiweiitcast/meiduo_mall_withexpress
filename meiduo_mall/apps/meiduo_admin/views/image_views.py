
from rest_framework.viewsets import ModelViewSet
from goods.models import SKUImage,SKU
from meiduo_admin.serializers.image_serializer import *
from meiduo_admin.pages import MyPage
from rest_framework.decorators import action
from rest_framework.response import Response

# GET
# skus/images/
class ImageViewSet(ModelViewSet):
    queryset = SKUImage.objects.all()
    serializer_class = ImageSerializer
    pagination_class = MyPage


    # GET
    # skus/simple/
    @action(methods=['get'], detail=False)
    def simple(self, request):
        # 序列化返回新建图片对象，可选的sku商品
        sku_queryset = SKU.objects.all()
        s = SKUSimpleSerializer(sku_queryset, many=True)
        return Response(s.data)