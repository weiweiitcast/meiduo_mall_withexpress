

from rest_framework.generics import ListAPIView,DestroyAPIView,CreateAPIView,RetrieveAPIView
from goods.models import SKU,SPUSpecification
from meiduo_admin.serializers.sku_serializers import *
from meiduo_admin.pages import MyPage
from goods.models import GoodsCategory
from rest_framework.viewsets import ModelViewSet


# GET
# skus/?keyword=<名称|副标题>&page=<页码>&page_size=<页容量>


# DELETE
# skus/(?P<pk>\d+)/


class SKUView(ModelViewSet):
    queryset = SKU.objects.all()
    serializer_class = SKUModelSerializer
    pagination_class = MyPage


    def get_queryset(self):
        keyword = self.request.query_params.get("keyword")
        if keyword:
            return self.queryset.filter(name__contains=keyword)
        return self.queryset.all()



class GoodsCategoryView(ListAPIView):
    queryset = GoodsCategory.objects.filter(parent_id__gt=37)
    serializer_class = GoodsCategoryModelSerializer

class SPUSimpleView(ListAPIView):
    queryset = SPU.objects.all()
    serializer_class = SPUSimpleSerializer


class SpecOptView(ListAPIView):
    queryset = SPUSpecification.objects.all()
    serializer_class = SPUSpecModelSerializer

    def get_queryset(self):
        spu_id = self.kwargs.get("pk")
        return self.queryset.filter(spu_id=spu_id)









