from influxdb import InfluxDBClient
import random
import time
client = InfluxDBClient('localhost', 8086, database='qiao')
for i in range(100):
    # print(i)
    # print(int(20+i))
    time.sleep(2)
    json_body = [
        {
            'measurement': 'people1',
            'tags': {
                'name': 'qiao',
            },
            'fields': {
                'age': 100 - i
            }

        }
    ]
    client.write_points(json_body)


    # client.write()

data = client.query("select * from people", database='qiao')
print(len(data))


# error":"partial write: field type conflict: input field \"age\" on measurement \"people\" is type integer, already exists as type float dropped=1"}
