
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    Name = serializers.CharField()
    Tel = serializers.CharField(required=False)
    Mobile = serializers.CharField(required=False)
    ProvinceName = serializers.CharField()
    CityName = serializers.CharField()
    ExpAreaName = serializers.CharField()
    Address = serializers.CharField()


    def validate(self, attrs):
        if not (attrs.get('Mobile') or attrs.get('Tel')):
            raise serializers.ValidationError("手机和电话必须有一个！")
        return attrs

class CommoditySerializer(serializers.Serializer):
    GoodsName = serializers.CharField()


class PlaceOrderSerializer(serializers.Serializer):
    OrderCode = serializers.CharField()
    ShipperCode = serializers.CharField()
    PayType = serializers.IntegerField()
    ExpType = serializers.IntegerField()
    Sender = UserSerializer()
    Receiver = UserSerializer()
    Commodity = CommoditySerializer(many=True)
    Quantity = serializers.IntegerField()