


from goods.models import SpecificationOption,SPUSpecification
from rest_framework.viewsets import ModelViewSet
from meiduo_admin.serializers.option_serializers import *
from meiduo_admin.pages import MyPage
from rest_framework.generics import ListAPIView
from meiduo_admin.serializers.spec_serializers import SpecSerializer

class OptionViewSet(ModelViewSet):
    queryset = SpecificationOption.objects.all()
    serializer_class = OptionSerializer
    pagination_class = MyPage



class SpecSimpleView(ListAPIView):
    queryset = SPUSpecification.objects.all()
    serializer_class = SpecSerializer