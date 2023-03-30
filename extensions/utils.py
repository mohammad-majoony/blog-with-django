from . import jalali
from django.utils import timezone
def jalali_converter(time) :
    
    time = timezone.localtime(time)
    # months = ['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن']
    
    
    time_str = "{},{},{}".format(time.year , time.month , time.day)
    time_tuple = jalali.Gregorian(time_str).persian_tuple()
    output = "{}/{}/{} , {}:{}".format(time_tuple[0] , time_tuple[1] , time_tuple[2] , time.hour , time.minute)
    return output 