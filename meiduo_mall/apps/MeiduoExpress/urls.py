
from django.conf.urls import url, include
from .views import MeiduoExpViewSet
from rest_framework.routers import SimpleRouter


urlpatterns = [
    # url(r'^express/place_order/', MeiduoExpViewSet.as_view({'post':'place_order'})),
]

router = SimpleRouter()
router.register(prefix="express", viewset=MeiduoExpViewSet, base_name='express')
urlpatterns += router.urls
