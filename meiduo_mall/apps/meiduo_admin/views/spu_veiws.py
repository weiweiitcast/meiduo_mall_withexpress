
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from goods.models import SPU,Brand
from meiduo_admin.serializers.spu_serializers import *
from meiduo_admin.pages import MyPage

# GET
# goods/?keyword=<名称|副标题>&page=<页码>&page_size=<页容量>
# 获得所有SPU对象序列化数据

# POST
# goods/
# 创建单一的spu数据对象

class SPUViewSet(ModelViewSet): # list,create,destroy
    queryset = SPU.objects.all()
    serializer_class = SPUModelSerializer
    pagination_class = MyPage



# GET
# goods/brands/simple/
# 获得所有brand数据
class BrandSimpleView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSimpleSerializer




# GET
# goods/channel/categories/
# 处理获得一级分类所有数据的接口
class GoodsCategoryView(ListAPIView):
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodsCategorySimpleSerializer


    def get_queryset(self):
        parent_id = self.kwargs.get("pk")

        if parent_id:
            # 如果请求路径中有pk： 处理的是二级或三级分类（跟据pk）
            return self.queryset.filter(parent_id=parent_id)

        # 如果请求的路径中没有pk：处理的一级分类数据集
        return self.queryset.filter(parent=None)












