

from goods.models import SPUSpecification
from rest_framework import serializers


class SpecSerializer(serializers.ModelSerializer):
    spu = serializers.StringRelatedField() # read_only=True
    spu_id = serializers.IntegerField()

    class Meta:
        model = SPUSpecification
        fields = ['id', 'name', 'spu', 'spu_id']

        # extra_kwargs = {
        #     "id": {"read_only": True},
        #     "spu": {"read_only": True}
        # }