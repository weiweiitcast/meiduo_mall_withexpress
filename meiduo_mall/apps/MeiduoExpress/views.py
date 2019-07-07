from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import PlaceOrderSerializer
from .tasks import meiduo_place_order
# Create your views here.


class MeiduoExpViewSet(ViewSet):

    # POST
    # /express/place_order/
    @action(methods=['post'], detail=False)
    def place_order(self, request):
        ps = PlaceOrderSerializer(data=request.data)
        ps.is_valid(raise_exception=True)
        meiduo_place_order.delay(ps.data)
        return Response({"result":True})