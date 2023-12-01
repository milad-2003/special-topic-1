"""
ملاقات نوروزی

به مناسبت عید نوروز سه دوست قدیمی می خواهند همدیگر را ملاقات کنند. آذرمهر
آذرگون و مهرآیین قصد دارند در یک نقطه همدیگر را ملاقات کنند. منزل این سه نفر روی
خط راست قرار دارد.
(ها x محور)
قرار دارد، خانه ی آذرگون در نقطه ی x1 خانه ی آذرمهر در نقطه ی
قرار دارد. آنها در مجموع می خواهند x3 قرار دارد و خانه ی مهرآیین در نقطه ی x2
کمترین مسافتی که x1 x2 x3 کمترین مسافت را طی کنند. با در دست داشتن
این سه در مجموع باید طی کنند تا در یک نقطه همدیگر را ملاقات کنند را محاسبه کنید
در صورتی که جواب عدد صحیح شد آن را بدون نقطه ی عدد اعشاری چاپ کنید
مثلا اگر جواب 6.0 شد، باید عدد 6 در خروجی چاپ شود.
دقت کنید که مسافت مورد نظر است نه مکانی که قرار است همدیگر را ملاقات کنند

ورودی نمونه:
6 9 10

خروجی نمونه:
4
"""

locations = input("Enter three numbers for x1, x2 and x3, separated with spaces: ")
locations_list = sorted([float(x) for x in locations.split(" ")])
result = (locations_list[1] - locations_list[0]) + (locations_list[2] - locations_list[1])
if result == int(result):
    print(int(result))
else:
    print(result)
