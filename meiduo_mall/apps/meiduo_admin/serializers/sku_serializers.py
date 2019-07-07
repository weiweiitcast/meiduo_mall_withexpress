
from rest_framework import serializers
from goods.models import SKU,SKUSpecification,\
    GoodsCategory,SPU,SPUSpecification,\
    SpecificationOption


class SKUSpecModelSerializer(serializers.ModelSerializer):
    spec_id = serializers.IntegerField()
    option_id = serializers.IntegerField()

    class Meta:
        model = SKUSpecification
        fields = ['spec_id', 'option_id']



# 定义SKU序列化器
class SKUModelSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    spu = serializers.StringRelatedField()
    spu_id = serializers.IntegerField()

    # specs代表的是与sku对象关联的所有的从表数据对象SKUSpecification
    specs = SKUSpecModelSerializer(many=True)

    class Meta:
        model = SKU
        fields = "__all__"



    def create(self, validated_data):

        # 最终目的：创建中间表数据（从表），主表数据首先必须得有

        # 1、获得规格及规格选项数据validated_data['specs']
        # [
        #    {spec_id:1,  option_id:10},
        #    {....}
        # ]
        spec_option = validated_data.pop("specs")

        # 1.1 新建sku对象
        sku = super().create(validated_data)

        # 2、根据spec_option创建中间表数据
        # [
        #   {sku_id: 6, spec_id:1,  option_id:10},
        #   {...}
        # ]
        for temp in spec_option:
            # temp: {spec_id:1,  option_id:10}
            temp['sku_id'] = sku.id
            SKUSpecification.objects.create(**temp)

        return sku


        # super().create(validated_data)是ModelSerializer提供的create方法
        # 问题是： 该方法没有能够帮助我们创建中间表数据，意味着规格选项信息丢失
        # return super().create(validated_data)

    def update(self, instance, validated_data):
        # 更新sku对象的时候，顺带着更新中间表数据

        # 1、获得规格及规格选项数据
        spec_option = validated_data.pop('specs')
        # 2、根据这些数据，更新中间表
        for temp in spec_option:
            # temp: {spec_id:4,  option_id:9}
            # 2.1 找到对应的中间表数据：当前更新的sku对象，对应的规格及规格选项
            m = SKUSpecification.objects.get(sku_id=instance.id, spec_id=temp['spec_id'])
            m.option_id = temp['option_id']
            m.save()

        # ModelSerializer提供的update方法无法更新中间表数据
        return super().update(instance, validated_data)



# 定义GoodsCategory序列化器
class GoodsCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ['id', 'name']

# 定义SPU序列化器
class SPUSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPU
        fields = ['id', 'name']


class SpecOptSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationOption
        fields = ['id', 'value']


# 定义SPUSpecification序列化器
class SPUSpecModelSerializer(serializers.ModelSerializer):
    spu = serializers.StringRelatedField()
    spu_id = serializers.IntegerField()

    # 与之关联的所有的从表对象
    options = SpecOptSerializer(many=True, read_only=True)

    class Meta:
        model = SPUSpecification
        fields = ['id', 'name', 'spu', 'spu_id', 'options']