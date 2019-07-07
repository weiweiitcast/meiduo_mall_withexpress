


from goods.models import SPU,SPUSpecification,SpecificationOption
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


a = {}

# 序列化SPU
# {
#     "id": 1,
#     "name": iphone8,
#
#     "specs": [
#         {
#             "name": "颜色"
#             "options": [
#                   {"id": xxx,  "value": 红色}，
#                   {"id": xxx,  "value": 蓝色}
#               ]
#         },
#
#         {
#             "name": "内存"
#             "options": [
#                   {"id": xxx,  "value": 18G}
#                   {"id": xxx,  "value": 36G}
#               ]
#         }
#     ]
# }

class OptionsSerializer(serializers.ModelSerializer):
    class  Meta:
        model = SpecificationOption
        fields = ['id', 'value']


class SpecSerializer(serializers.ModelSerializer):
    options = OptionsSerializer(many=True)
    class Meta:
        model = SPUSpecification
        fields = ['name', 'options']

class SPUSerializer(serializers.ModelSerializer):
    specs = SpecSerializer(many=True)
    class Meta:
        model = SPU
        fields = ['id', 'name', 'specs']


class MyView(APIView):
    def get(self, request):
        spus = SPU.objects.all()
        s = SPUSerializer(spus, many=True)
        return Response(s.data)