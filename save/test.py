from datetime import datetime

timestamp = 1545730073
timestamp = 1623947640 # 2021-06-17 12:34:00
timestamp = 1623947700 # 2021-06-17 12:35:00
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))