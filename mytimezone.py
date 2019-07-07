




# 时间对象
# 属性： 年月底  十分秒  时区
# 方法： +、-

from datetime import datetime,timedelta
import pytz

# datetime: 包含了  年月底  十分秒 --> 时间点类
# timedelta: 时间段类


# 时间点对象
# 一个 表示  "上海时间2019年6月18日17点30分15秒"  时间对象
mytzinfo = pytz.timezone("Asia/Shanghai")
mytime = datetime(year=2019, month=6, day=18, hour=17, minute=30, second=15, tzinfo=mytzinfo)

# 昨天的一个时间点
yesterday = mytime - timedelta(days=1, seconds=10)

print(mytime)
print(yesterday)


# 关于时区转化
utc_zone = pytz.timezone("UTC")
utc_time = mytime.astimezone(tz=utc_zone)
print(utc_time)