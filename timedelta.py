from datetime import datetime, timedelta
date1 = datetime.now()
date2= date1+timedelta(days = 4)
print("Date after 4 days:", date2)
date3 = date1-timedelta(15)
print("Date before 15 days:", date3)