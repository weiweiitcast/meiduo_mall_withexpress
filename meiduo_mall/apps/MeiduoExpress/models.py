from django.db import models
from orders.models import OrderInfo
from users.models import User
# Create your models here.


class ExpressInfo(models.Model):
    order = models.ForeignKey(OrderInfo, related_name="express", verbose_name="订单编号", on_delete=models.CASCADE, null=False)
    staff = models.ForeignKey(User, related_name="express", verbose_name="业务员", on_delete=models.CASCADE, null=False)
    logistic_code = models.CharField(max_length=400, null=False, verbose_name="快递单号")
    shipper_code = models.CharField(max_length=10, null=False, verbose_name="物流公司编码")

    class Meta:
        db_table = 'tb_express_info'
        verbose_name = '物流信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.logistic_code