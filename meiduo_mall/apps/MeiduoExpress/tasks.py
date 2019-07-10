from meiduo_mall.libs.meiduo_express import MeiduoExpress
from .models import ExpressInfo
import celery

@celery.task
def meiduo_place_order(data, staff_id):
    mp = MeiduoExpress()
    res = mp.place_order(data)

    if res.get('Success'):
        ExpressInfo.objects.create(
            order_id = res['Order']['OrderCode'],
            staff_id = staff_id,
            logistic_code = res['Order']['LogisticCode'],
            shipper_code = res['Order']['ShipperCode']
        )
        return True

    return False