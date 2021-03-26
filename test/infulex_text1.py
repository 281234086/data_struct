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
            'measurement': 'people2',
            'tags': {
                'name': 'qiao',
            },
            'fields': {
                'age': i +1
            }

        }
    ]
    client.write_points(json_body)
    client.create_continuous_query()


    # client.write()

data = client.query("select * from people1", database='qiao')
print(len(data))


# error":"partial write: field type conflict: input field \"age\" on measurement \"people\" is type integer, already exists as type float dropped=1"}
