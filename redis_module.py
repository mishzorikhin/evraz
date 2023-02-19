from typing import NoReturn

import redis as redis

r = redis.StrictRedis(
    host="46.146.220.208",
    port=6379,
    password="54321Redis12345",
    decode_responses=True,
    db=15
)


def save_data(data: dict) -> NoReturn:
    print("Start")
    r.flushdb()

    pipeline = r.pipeline()
    pipeline.set("moment", data["moment"])

    for i in data:
        if i != "moment":
            pipeline.set(str(i[13:]), float(data[i]))

    results = pipeline.execute()
    print(results)

    print("Stop")
