
from django.conf.urls import url, include
from .views import MeiduoExpViewSet


urlpatterns = [
    url(r'^place_order/', MeiduoExpViewSet.as_view({'post':'place_order'})),
]
