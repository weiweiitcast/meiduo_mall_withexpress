
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# 定义一个分页器
class MyPage(PageNumberPagination):
    page_query_param = "page"
    page_size_query_param = "pagesize"
    page_size = 5
    max_page_size = 10

    def get_paginated_response(self, data):
        """
        自定义返回对数据格式
        :param data: 分页子集的序列化结果
        :return: 该函数返回对是一个响应对象
        """
        return Response({
            "counts": self.page.paginator.count, # 总页数
            "lists": data, # 当前分页的数据子集
            "page": self.page.number, # 第几页
            "pages": self.page.paginator.num_pages, # 总页数
            "pagesize": self.page_size, # 后台默认每页多少数据
        })