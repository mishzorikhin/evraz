import time
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "ztz72hWlSSReThLxuDvaZRCtcDAo2nEJUzvNEEPR632Em8AfevXKWgSTy1NfJNJOCy3f7QxVaO9hl5wnmB9g0Q=="
org = "Influx_test_db"
bucket = "evraz_data"

client = InfluxDBClient(url="http://127.0.0.1:8086", token=token, timeout=100000)

write_api = client.write_api(write_options=SYNCHRONOUS)


def send_data(data: dict):
    print("send")
    for i in data:
        if i != "moment":
            print(i[13:])
            print(data[i], type(data[i]))
            print(data["moment"])
            if data[i] is None:
                dat = 0.0
                
            else:
                dat = data[i]

            point = Point("Exgauster").tag("host", str(i[13:])).field("float", float(dat)).time(
                data["moment"])
            write_api.write(bucket, org, point)
            print("write_api")
