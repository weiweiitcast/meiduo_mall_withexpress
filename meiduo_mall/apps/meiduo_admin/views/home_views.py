






from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from users.models import User
from orders.models import OrderInfo
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import timedelta
import pytz
from django.conf import settings
from meiduo_admin.serializers.home_serializers import *
from rest_framework.permissions import IsAdminUser


# 定义视图接口的原则：
# 同类功能尽可能放在一个视图中完成
# 对同一个资源对处理尽可能方在一个视图中完成
class HomeView(ViewSet):
    permission_classes = [IsAdminUser]

    # GET
    # statistical/total_count/
    @action(methods=['get'], detail=False)
    def total_count(self, request):
        # 1、获得User用户数量
        count = User.objects.filter(is_active=True).count()
        # 2、当天查询日期
        # timezone.now() --> 2019-6-17 12：12：12
        date = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)).date()
        return Response({
            "count": count,
            "date": date
        })

    # GET
    # statistical/day_increment/
    @action(methods=['get'], detail=False)
    def day_increment(self, request):
        # 1、当日日期
        cur_date = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)) # 2019-6-18 15:26:56 "Asia/Shanghai" --> 2019-6-18 07:20:56 "UTC"
        # print("cur_date:", cur_date)
        # 2、顾虑除当天新建的用户数量
        # print("零时间： ", cur_date.replace(hour=0, minute=0, second=0))
        count = User.objects.filter(
            date_joined__gte = cur_date.replace(hour=0, minute=0, second=0) # 2019-6-18 0:0:0 "Asia/Shanghai"
        ).count()
        # 3、构建返回数据
        return Response({
            "count": count,
            "date": cur_date.date() # 2019-6-18
        })

    # GET
    # statistical/day_active/
    @action(methods=['get'], detail=False)
    def day_active(self, request):
        # 1、当日日期
        cur_date = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)) # Shanghai  2019-6-18  16:10:34  --->  UTC   2019-6-18  8:04:34
        # 2、根据当日日期过滤出，当体登陆的用户
        # UTC  2019-6-18  0：0：0  --->  UTC  2019-6-17  15：54：0 --> Shanghai  2019-6-18  0：0：0
        shanghai_0_utc =  cur_date.replace(hour=0, minute=0, second=0)

        count = User.objects.filter(
            last_login__gte = shanghai_0_utc
        ).count()

        # 3、构建响应对象
        return Response({
            "count": count,
            "date": cur_date.date()
        })


    # GET
    # statistical/day_orders/
    @action(methods=['get'], detail=False)
    def day_orders(self, request):
        # 1、获得当天日期
        cur_date = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE))
        # 2、获得日下单用户数量
        # 查询的条件(日期，订单表)、查询的目标数据(用户表)
        # 订单表 --> 用户表
        # 从    -->  主

        # 上海的零点（使用UTC时间表示的）
        shanghai_0_utc = cur_date.replace(hour=0, minute=0, second=0)

        # 从从表入手查询
        # order_list = OrderInfo.objects.filter(create_time__gte=shanghai_0_utc)
        # 从订单表中获得关联的主表数据对象（用户）
        # user_list = []
        # for order in order_list:
            # order是订单对象
            # user_list.append(order.user)

        # 去重,计算用户数量
        # count = len(set(user_list))


        # 从主表入手查询用户数量
        user_list = User.objects.filter(
            orders__create_time__gte = shanghai_0_utc
        ) # queryset集合，主表对象没有去重
        # 去重
        count = len(set(user_list))


        # 构建返回数据
        return Response({
            "count": count,
            "date": cur_date.date()
        })


    # GET
    # statistical/month_increment/
    @action(methods=['get'], detail=False)
    def month_increment(self, request):
        # 功能： 最近30天，每一天的新增用户

        # 1、获得当天的零时(零时,并且是上海时区的零时)
        # 6-20  5:00  -->  6-19 21：00 --> 6-19 0:0:0

        # 6-19 21：00  -->  6-20  5:00 --> 6-20 0:0:0
        cur_date = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)).replace(hour=0,minute=0,second=0)
        # 2、启始日期 #  5-20 00:00
        start_date = cur_date - timedelta(days=29) #  5-20 00:00:00

        # 3、循环遍历出每一天，根据每一天过滤出新增用户数量，记录
        result_list = []
        for index in range(30):
            calc_date = start_date + timedelta(days=index)
            # 根据calc_date日期，查询出改日期，新建的用户数量
            count = User.objects.filter(
                date_joined__gte=calc_date,
                date_joined__lt=calc_date + timedelta(days=1)
            ).count()
            result_list.append({
                "count": count,
                "date": calc_date.date()
            })

        # 4、返回数据
        return Response(result_list)


    # GET
    # statistical/goods_day_views/
    @action(methods=['get'], detail=False)
    def goods_day_views(self, request):
        # 1、过滤出当天访问的数据对象
        cur_date = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)).replace(hour=0, minute=0, second=0)
        goods_visit_queryset= GoodsVisitCount.objects.filter(create_time__gte=cur_date)

        # 2、调用序列化器对数据对象序列化处理
        serializer = GoodsVisitSerializer(goods_visit_queryset, many=True)

        # 3、返回数据
        return Response(serializer.data)








