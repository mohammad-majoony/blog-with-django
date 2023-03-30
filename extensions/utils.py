from . import jalali
from django.utils import timezone

def persian_number(str_number) :
    number = {
        "0" : "۰" ,
        "1" : "۱" ,
        "2" : "۲" ,
        "3" : "۳" ,
        "4" : "۴" ,
        "5" : "۵" ,
        "6" : "۶" ,
        "7" : "۷" ,
        "8" : "۸" ,
        "9" : "۹" ,
    }
    
    for e , p in number.items() :
        str_number = str_number.replace(e , p)
        
    return str_number

def jalali_converter(time) :
    time = timezone.localtime(time)
    # months = ['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن']
    time_str = "{},{},{}".format(time.year , time.month , time.day)
    time_tuple = jalali.Gregorian(time_str).persian_tuple()
    output = "{}/{}/{} , {} : {}".format(time_tuple[0] , time_tuple[1] , time_tuple[2] , time.hour , time.minute)
    
    return persian_number(output)
