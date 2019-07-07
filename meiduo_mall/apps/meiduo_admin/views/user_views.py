

from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView,CreateAPIView
from users.models import User
from meiduo_admin.serializers.user_serializers import *
from rest_framework.response import Response
from meiduo_admin.pages import MyPage

# GET
# users/?keyword=<搜索内容>&page=<页码>&pagesize=<页容量>
# 业务逻辑：获得多个数据对象

class UserView(ListAPIView, CreateAPIView):# (GenericAPIView):
    # 处理的数据集
    queryset = User.objects.all()
    # 序列化器
    serializer_class = UserModleSerializer
    # 配置分页器
    pagination_class = MyPage

    def get_queryset(self):
        """
        实现自定义获得的数据集
        :return: 数据集
        """
        # 1、判断字符串参数中有没有keyword值
        keyword = self.request.query_params.get("keyword")
        # 2、如果有的话，需要根据keyword过滤，返回过滤后的数据集
        if keyword:
            return self.queryset.filter(username__contains=keyword)
        # 3、如果没有的话，默认返回self.queryset.all()
        return self.queryset.all() # all() 目的在于使用缓存


    # def get(self, request):
    #     # 获得数据集
    #     user_queryset = self.get_queryset()
    #
    #     # 对该数据集进行分页处理，得到一个子集
    #     page = self.paginate_queryset(user_queryset) # page=1&pagesize=3
    #
    #     # 对该子集进行序列化处理
    #     if page:
    #         page_serializer = self.get_serializer(page, many=True)
    #
    #         # 传入分页子集序列化结果，构建最终序列化返回对数据格式, 返回的结果是一个响应对象
    #         return self.get_paginated_response(page_serializer.data)
    #
    #
    #     # 如果分页失败，就当不分页，默认返回所有数据
    #     serializer = self.get_serializer(user_queryset, many=True)
    #     return Response(serializer.data)










