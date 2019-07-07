

from rest_framework import serializers
from goods.models import Brand
from fdfs_client.client import Fdfs_client
from django.conf import settings



class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'id',
            'name',
            'logo',
            'first_letter'
        ]


    def create(self, validated_data):
        """
        补充上传fdfs的业务逻辑
        :param validated_data:
        :return:
        """
        # logo就是校验过后的"图片对象"
        logo = validated_data.pop('logo')

        # 1、获得fdfs链接对象
        conn = Fdfs_client(settings.FDFS_CONFIG_PATH)
        # 2、上传文件
        content = logo.read() # bytes
        result = conn.upload_by_buffer(content)

        # 3、判断是否上传成功
        if not result.get("Status") == "Upload successed.":
            raise serializers.ValidationError("上传失败")

        # 4、如果成功，获得fdfs文件标示
        url = result.get("Remote file_id")

        validated_data['logo'] = url
        # 5、更新当前的品牌对象的logo字段
        return super().create(validated_data)
        # instance =  super().create(validated_data)
        # instance.logo = url
        # return instance

    def update(self, instance, validated_data):
        """
        补充更新品牌，上传图片逻辑
        :param instance:
        :param validated_data:
        :return:
        """

        # logo就是校验过后的"图片对象"
        logo = validated_data.pop('logo')

        # 1、获得fdfs链接对象
        conn = Fdfs_client(settings.FDFS_CONFIG_PATH)
        # 2、上传文件
        content = logo.read()  # bytes
        result = conn.upload_by_buffer(content)

        # 3、判断是否上传成功
        if not result.get("Status") == "Upload successed.":
            raise serializers.ValidationError("上传失败")

        # 4、如果成功，获得fdfs文件标示
        url = result.get("Remote file_id")

        instance.logo = url
        instance.save()
        return instance







