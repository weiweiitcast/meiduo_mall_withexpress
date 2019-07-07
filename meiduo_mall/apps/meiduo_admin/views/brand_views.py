

from rest_framework.viewsets import ModelViewSet
from goods.models import Brand
from meiduo_admin.serializers.brand_serializers import *
from meiduo_admin.pages import MyPage

# GET
# goods/brands/?page=1&pagesize=10

# POST
# goods/brands/

class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer
    pagination_class = MyPage