
from django.conf.urls import url, include
from .views.user_login_views import *
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import SimpleRouter
from meiduo_admin.views.home_views import *
from rest_framework.routers import SimpleRouter
from meiduo_admin.views.user_views import *
from meiduo_admin.views.sku_views import *
from meiduo_admin.views.spu_veiws import *
from meiduo_admin.views.spec_views import *
from meiduo_admin.views.option_views import *
from meiduo_admin.views.myviews import *
from meiduo_admin.views.channel_views import *
from meiduo_admin.views.brand_views import *
from meiduo_admin.views.image_views import *
from meiduo_admin.views.order_views import *
from meiduo_admin.views.perm_views import *
from meiduo_admin.views.group_views import *
from meiduo_admin.views.admin_views import *


urlpatterns = [
    # url(r'^authorizations/$', UserLoginView.as_view())

    # obtain_jwt_token给我们返回给前端的数据只有token，没有额外的数据
    url(r'^authorizations/$', obtain_jwt_token),
    # url(r'^statistical/total_count/$', HomeView.as_view({"get":"total_count"})),

    # 用户数据展示和新增用户
    url(r'^users/$', UserView.as_view()),

    # sku商品表增上改查
    url(r'^skus/$', SKUView.as_view({"get":"list", "post":"create"})),
    url(r'^skus/(?P<pk>\d+)/$', SKUView.as_view({"delete":"destroy", "get":"retrieve", "put":"update"})),
    # sku三级分类
    url(r'^skus/categories/$', GoodsCategoryView.as_view()),
    # sku所属spu
    url(r'^goods/simple/$', SPUSimpleView.as_view()),
    # sku商品规格
    url(r'^goods/(?P<pk>\d+)/specs/$', SpecOptView.as_view()),

    # spu商品所有数据,新建单一资源
    url(r'^goods/$', SPUViewSet.as_view({"get":"list", 'post':'create'})),
    # spu商品单一对象删除,获得单一对象数据
    url(r'^goods/(?P<pk>\d+)/$', SPUViewSet.as_view({'delete':'destroy', 'get':'retrieve', "put":'update'})),

    # 获得spu商品对应可选对品牌信息
    url(r'^goods/brands/simple/$', BrandSimpleView.as_view()),
    # 获得一级分类信息
    url(r'^goods/channel/categories/$', GoodsCategoryView.as_view()),
    # 获得二级或三级分类信息
    url(r'^goods/channel/categories/(?P<pk>\d+)/$', GoodsCategoryView.as_view()),

    # 获得规格所有数据
    # url(r'^goods/specs/$', SpecViewSet.as_view({"get":"list", "post":"create"})),
    # 单一规格资源的删除,获得单一资源,更新单一资源
    # url(r'^goods/specs/(?P<pk>\d+)/$', SpecViewSet.as_view({'delete':'destroy',
    #                                                         'get':'retrieve',
    #                                                         'put':'update'})),

    # 获得规格选项所有数据，新建单一资源
    url(r'^specs/options/$', OptionViewSet.as_view({"get":"list", 'post':'create'})),
    # 删除规格选项的单一数据
    url(r'^specs/options/(?P<pk>\d+)/$', OptionViewSet.as_view({'delete': 'destroy',
                                                                'get':'retrieve',
                                                                'put':'update'})),

    # 获得规格所有的信息
    url(r'^goods/specs/simple/$', SpecSimpleView.as_view()),



    url(r'^myview/$', MyView.as_view()),

    # 获得频道的所有数据
    url(r'^goods/channels/$', ChannelViewSet.as_view({"get":"list", 'post':'create'})),
    # 获得单一频道数据
    url(r'^goods/channels/(?P<pk>\d+)/$', ChannelViewSet.as_view({'get':'retrieve',
                                                                  'put':'update',
                                                                  'delete':'destroy'})),

    # 获得频道所有分组数据
    url(r'^goods/channel_types/$', ChannelViewSet.as_view({"get":"channel_types"})),
    # 获得频道可选的一级分类
    url(r'^goods/categories/$', ChannelViewSet.as_view({"get":"categories"})),


    # 获得品牌所有信息,数据新建
    url(r'^goods/brands/$', BrandViewSet.as_view({"get":"list", 'post':'create'})),
    # 删除对象
    url(r'^goods/brands/(?P<pk>\d+)/$', BrandViewSet.as_view({'delete': 'destroy',
                                                              'get':'retrieve',
                                                              'put':'update'})),

    # 获得图片所有数据
    url(r'^skus/images/$', ImageViewSet.as_view({"get":"list", 'post':'create'})),
    url(r'^skus/images/(?P<pk>\d+)/$', ImageViewSet.as_view({'get':'retrieve',
                                                             'put':'update',
                                                             'delete':'destroy'})),

    # 获得新建图片可选sku商品
    url(r'^skus/simple/$', ImageViewSet.as_view({"get":"simple"})),

    # 获得订单所有数据
    url(r'^orders/$', OrderViewSet.as_view({"get":"list"})),
    url(r'^orders/(?P<pk>\d+)/$', OrderViewSet.as_view({"get":"retrieve"})),
    url(r'^orders/(?P<pk>\d+)/status/$', OrderViewSet.as_view({"patch":"partial_update"})),

    # 获得所有权限数据
    url(r'^permission/perms/$', PermViewSet.as_view({'get':'list', 'post':'create'})),
    url(r'^permission/perms/(?P<pk>\d+)/$', PermViewSet.as_view({'get':'retrieve',
                                                                 'put':'update',
                                                                 'delete':'destroy'})),
    # 获得新建权限可选类型
    url(r'^permission/content_types/$', PermViewSet.as_view({'get':'content_types'})),

    # 获得分组所有数据
    url(r'^permission/groups/$', GroupViewSet.as_view({'get':'list', 'post':'create'})),
    url(r'^permission/groups/(?P<pk>\d+)/$', GroupViewSet.as_view({'get':'retrieve',
                                                                   'put':'update',
                                                                   'delete':'destroy'})),
    # 获得新建分组可选权限
    url(r'^permission/simple/$', GroupViewSet.as_view({'get':'simple'})),

    # 获得超级管理员数据
    url(r'^permission/admins/$', AdminViewSet.as_view({'get':'list', 'post':'create'})),

    url(r'^permission/admins/(?P<pk>\d+)/$', AdminViewSet.as_view({'get':'retrieve',
                                                                   'delete':'destroy',
                                                                   'put':'update'})),
    # 获得新建管理员可选分组
    url(r'^permission/groups/simple/$', AdminViewSet.as_view({'get':'simple'})),
]


router = SimpleRouter()
router.register(prefix="statistical", viewset=HomeView, base_name="home")
router.register(prefix='goods/specs', viewset=SpecViewSet, base_name='specs')
urlpatterns += router.urls
