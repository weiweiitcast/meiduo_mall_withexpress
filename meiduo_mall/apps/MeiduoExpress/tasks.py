from meiduo_mall.libs.meiduo_express import MeiduoExpress
from .models import ExpressInfo
import celery

@celery.task
def meiduo_place_order(data):
    mp = MeiduoExpress()
    res = mp.place_order(data)

    if res['Success']:
        ExpressInfo.objects.create(
            order_id = res['Order']['OrderCode'],
            staff_id = data['Sender']['id'],
            logistic_code = res['Order']['LogisticCode']
        )
        return True

    return False