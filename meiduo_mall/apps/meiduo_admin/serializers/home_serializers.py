
from goods.models import GoodsVisitCount
from rest_framework import serializers

# 定义一个用来序列化GoodsVisitCount模型类
# category
# count


class GoodsVisitSerializer(serializers.ModelSerializer):
    # category = serializers.PrimaryKeyRelatedField() # 主键
    category = serializers.StringRelatedField() # 默认read_only=True
    class Meta:
        model = GoodsVisitCount
        fields = ['category', 'count']