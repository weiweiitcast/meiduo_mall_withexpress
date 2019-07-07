


from rest_framework import serializers
from orders.models import OrderInfo,OrderGoods
from goods.models import SKU


class OrderSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = [
            'order_id',
            'create_time',

            'status',
        ]

        # extra_kwargs = {
        #     # "order_id": {"required": False}
        #     "order_id": {"read_only": True},
        #     "status": {"required": True}
        # }


class SKUSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = [
            'name',
            'default_image'
        ]


class OrderGoodsSerializer(serializers.ModelSerializer):
    # 代表的是 与当前订单商品表 关联的 sku商品表单一对象呢
    sku = SKUSimpleSerializer(read_only=True)
    class Meta:
        model = OrderGoods
        fields = ['count', 'price', 'sku']


class OrderDetailSerializer(serializers.ModelSerializer):
    # 代表的是 当前订单对象，与之关联的所有 订单商品表对象（多个）
    skus = OrderGoodsSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()
    class Meta:
        model = OrderInfo
        fields = "__all__"
