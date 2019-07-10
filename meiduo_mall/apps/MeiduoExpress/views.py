from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import PlaceOrderSerializer
from .tasks import meiduo_place_order
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import ExpressInfo
from meiduo_mall.libs.meiduo_express import MeiduoExpress
from users.models import User
from orders.models import OrderInfo
# Create your views here.


class MeiduoExpViewSet(ViewSet):

    def get_permissions(self):
        if self.action == "place_order" or self.action == "userinfo":
            return [IsAdminUser()]
        elif self.action == "prompt_check":
            return [IsAuthenticated()]


    # GET
    # /express/(?P<pk>\d+)/userinfo/
    @action(methods=['get'], detail=True)
    def userinfo(self, request, pk):
        Sender = request.user
        Reveiver = User.objects.get(orders__order_id=pk)

        return Response({
                "Sender": {
                    "Name": Sender.username,
                    "Mobile": Sender.mobile,
                    "ProvinceName": Sender.default_address.province.name,
                    "CityName": Sender.default_address.city.name,
                    "ExpAreaName": Sender.default_address.district.name,
                    "Address": Sender.default_address.detail_address

                },
                "Receiver": {
                    "Name": Reveiver.username,
                    "Mobile": Reveiver.mobile,
                    "ProvinceName": Reveiver.default_address.province.name,
                    "CityName": Reveiver.default_address.city.name,
                    "ExpAreaName": Reveiver.default_address.district.name,
                    "Address": Reveiver.default_address.detail_address
                }
            })

    # POST
    # /express/place_order/
    @action(methods=['post'], detail=False)
    def place_order(self, request):
        ps = PlaceOrderSerializer(data=request.data)
        ps.is_valid(raise_exception=True)
        # meiduo_place_order.delay(ps.validated_data, staff_id=request.user.id)

        mp = MeiduoExpress()
        res = mp.place_order(ps.validated_data)
        print(res)
        if res.get('Success'):
            ExpressInfo.objects.create(
                order_id=res['Order']['OrderCode'],
                staff_id=request.user.id,
                logistic_code=res['Order']['LogisticCode'],
                shipper_code=res['Order']['ShipperCode']
            )

            return Response({"result":True})

        return Response({"result":True})

    # GET
    # /express/(?P<pk>\d+)/prompt_check/
    @action(methods=['get'], detail=True)
    def prompt_check(self, request, pk):
        expinfo = ExpressInfo.objects.get(order_id=pk)
        mp = MeiduoExpress()
        res = mp.prompt_check(request_data={
            "OrderCode": expinfo.order_id,
            "ShipperCode": expinfo.shipper_code,
            "LogisticCode": expinfo.logistic_code,
        })
        return Response(res)
















