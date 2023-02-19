from typing import List
from sensors_processing.exhauster_1 import check_data_1
from sensors_processing.exhauster_2 import check_data_2
from sensors_processing.exhauster_3 import check_data_3
from sensors_processing.exhauster_4 import check_data_4

import redis

r = redis.StrictRedis(
    host="46.146.220.208",
    port=6379,
    password="54321Redis12345",
    decode_responses=True,
    db=15
)


def get_redis_data(tags: List[str]) -> dict:
    answer: dict = {}
    for i in tags:
        answer[i] = float(r.get(i))
    return answer


def get_moment():
    return r.get("moment")


def get_first_date():
    warning_1: list = []
    warning_2: list = []
    warning_3: list = []
    warning_4: list = []
    warning_5: list = []
    warning_6: list = []

    ######################
    ##Эксгаустер 1

    sensor_1_1: dict = {
        "title": "п-к, №1",
        "signals": {
            "temp": check_data_1(
                type_sensors="temp",
                number_sensors=1,
                data_sensors=get_redis_data(["[2:27]"])),

            "vibr": check_data_1(
                type_sensors="vibr",
                number_sensors=1,
                data_sensors=get_redis_data([
                    "[2:2]",
                    "[2:0]",
                    "[2:1]",
                    "[2:163]",
                    "[2:161]",
                    "[2:162]",
                    "[2:139]",
                    "[2:137]",
                    "[2:138]"
                ]))
        }
    }

    if sensor_1_1["signals"]["temp"] != 0 or sensor_1_1["signals"]["vibr"] != 0:
        warning_1.append(sensor_1_1)

    sensor_1_2: dict = {
        "title": "п-к, №2",
        "signals": {
            "temp": check_data_1(
                type_sensors="temp",
                number_sensors=2,
                data_sensors=get_redis_data(["[2:28]"])),

            "vibr": check_data_1(
                type_sensors="vibr",
                number_sensors=2,
                data_sensors=get_redis_data([
                    "[2:5]",
                    "[2:3]",
                    "[2:4]",
                    "[2:166]",
                    "[2:164]",
                    "[2:165]",
                    "[2:142]",
                    "[2:140]",
                    "[2:141]"
                ]))
        }
    }

    if sensor_1_2["signals"]["temp"] != 0 or sensor_1_2["signals"]["vibr"] != 0:
        warning_1.append(sensor_1_2)

    sensor_1_3: dict = {
        "title": "п-к, №3",
        "signals": {
            "temp": check_data_1(
                type_sensors="temp",
                number_sensors=3,
                data_sensors=get_redis_data(["[2:29]"])),
        }
    }

    if sensor_1_3["signals"]["temp"] != 0:
        warning_1.append(sensor_1_3)

    sensor_1_4: dict = {
        "title": "п-к, №4",
        "signals": {
            "temp": check_data_1(
                type_sensors="temp",
                number_sensors=4,
                data_sensors=get_redis_data(["[2:30]"])),
        }
    }

    if sensor_1_4["signals"]["temp"]:
        warning_1.append(sensor_1_4)

    sensor_1_5: dict = {
        "title": "п-к, №5",
        "signals": {
            "temp": check_data_1(
                type_sensors="temp",
                number_sensors=5,
                data_sensors=get_redis_data(["[2:31]"])),
        }
    }

    if sensor_1_5["signals"]["temp"] != 0:
        warning_1.append(sensor_1_5)

    sensor_1_6: dict = {
        "title": "п-к, №6",
        "signals": {
            "temp": check_data_1(
                type_sensors="temp",
                number_sensors=6,
                data_sensors=get_redis_data(["[2:32]"])),
        }
    }

    if sensor_1_6["signals"]["temp"]:
        warning_1.append(sensor_1_6)

    sensor_1_7: dict = {
        "title": "п-к, №7",
        "signals": {
            "temp": check_data_1(
                type_sensors="temp",
                number_sensors=7,
                data_sensors=get_redis_data(["[2:33]"])),

            "vibr": check_data_1(
                type_sensors="vibr",
                number_sensors=7,
                data_sensors=get_redis_data([
                    "[2:8]",
                    "[2:6]",
                    "[2:7]",
                    "[2:169]",
                    "[2:167]",
                    "[2:168]",
                    "[2:145]",
                    "[2:143]",
                    "[2:144]"
                ]))
        }
    }

    if sensor_1_7["signals"]["temp"] != 0 or sensor_1_7["signals"]["vibr"] != 0:
        warning_1.append(sensor_1_7)

    sensor_1_8: dict = {
        "title": "п-к, №8",
        "signals": {
            "temp": check_data_1(
                type_sensors="temp",
                number_sensors=8,
                data_sensors=get_redis_data(["[2:34]"])),

            "vibr": check_data_1(
                type_sensors="vibr",
                number_sensors=8,
                data_sensors=get_redis_data([
                    "[2:11]",
                    "[2:9]",
                    "[2:10]",
                    "[2:172]",
                    "[2:170]",
                    "[2:171]",
                    "[2:148]",
                    "[2:146]",
                    "[2:147]"
                ]))
        }
    }

    if sensor_1_8["signals"]["temp"] != 0 or sensor_1_8["signals"]["vibr"] != 0:
        warning_1.append(sensor_1_8)

    sensor_1_9: dict = {
        "title": "п-к, №9",
        "signals": {
            "temp": check_data_1(
                type_sensors="temp",
                number_sensors=9,
                data_sensors=get_redis_data(["[2:35]"])),
        }
    }

    if sensor_1_9["signals"]["temp"] != 0:
        warning_1.append(sensor_1_9)

    sensor_1_10: dict = {
        "title": "Уровень масла",
        "signals": {
            "oil_level": check_data_1(
                type_sensors="oil_level",
                number_sensors=10,
                data_sensors=get_redis_data(["[4:0]"])),
        }
    }

    if sensor_1_10["signals"]["oil_level"] != 0:
        warning_1.append(sensor_1_10)

    sensor_1_11: dict = {
        "title": "Давление масла",
        "signals": {
            "oil_pressure": check_data_1(
                type_sensors="oil_pressure",
                number_sensors=10,
                data_sensors=get_redis_data(["[4:1]"])),
        }
    }

    if sensor_1_11["signals"]["oil_pressure"] != 0:
        warning_1.append(sensor_1_11)

    sensors_1 = [
        sensor_1_1,
        sensor_1_2,
        sensor_1_3,
        sensor_1_4,
        sensor_1_5,
        sensor_1_6,
        sensor_1_7,
        sensor_1_8,
        sensor_1_9,
        sensor_1_10,
        sensor_1_11
    ]

    ######################
    ## Эксгаустер 2

    sensor_2_1: dict = {
        "title": "п-к, №1",
        "signals": {
            "temp": check_data_2(
                type_sensors="temp",
                number_sensors=1,
                data_sensors=get_redis_data(["[2:43]"])),

            "vibr": check_data_2(
                type_sensors="vibr",
                number_sensors=1,
                data_sensors=get_redis_data([
                    "[2:14]",
                    "[2:12]",
                    "[2:13]",
                    "[2:211]",
                    "[2:209]",
                    "[2:210]",
                    "[2:187]",
                    "[2:185]",
                    "[2:186]"
                ]))
        }
    }

    if sensor_2_1["signals"]["temp"] != 0 or sensor_2_1["signals"]["vibr"] != 0:
        warning_2.append(sensor_2_1)

    sensor_2_2: dict = {
        "title": "п-к, №2",
        "signals": {
            "temp": check_data_2(
                type_sensors="temp",
                number_sensors=2,
                data_sensors=get_redis_data(["[2:44]"])),

            "vibr": check_data_2(
                type_sensors="vibr",
                number_sensors=2,
                data_sensors=get_redis_data([
                    "[2:17]",
                    "[2:15]",
                    "[2:16]",
                    "[2:214]",
                    "[2:212]",
                    "[2:213]",
                    "[2:190]",
                    "[2:188]",
                    "[2:189]"
                ]))
        }
    }

    if sensor_2_2["signals"]["temp"] != 0 or sensor_2_2["signals"]["vibr"] != 0:
        warning_2.append(sensor_2_2)

    sensor_2_3: dict = {
        "title": "п-к, №3",
        "signals": {
            "temp": check_data_2(
                type_sensors="temp",
                number_sensors=3,
                data_sensors=get_redis_data(["[2:45]"])),
        }
    }

    if sensor_2_3["signals"]["temp"] != 0:
        warning_2.append(sensor_1_3)

    sensor_2_4: dict = {
        "title": "п-к, №4",
        "signals": {
            "temp": check_data_2(
                type_sensors="temp",
                number_sensors=4,
                data_sensors=get_redis_data(["[2:47]"])),
        }
    }

    if sensor_2_4["signals"]["temp"]:
        warning_2.append(sensor_2_4)

    sensor_2_5: dict = {
        "title": "п-к, №5",
        "signals": {
            "temp": check_data_2(
                type_sensors="temp",
                number_sensors=5,
                data_sensors=get_redis_data(["[2:48]"])),
        }
    }

    if sensor_2_5["signals"]["temp"] != 0:
        warning_2.append(sensor_2_5)

    sensor_2_6: dict = {
        "title": "п-к, №6",
        "signals": {
            "temp": check_data_2(
                type_sensors="temp",
                number_sensors=6,
                data_sensors=get_redis_data(["[2:49]"])),
        }
    }

    if sensor_2_6["signals"]["temp"]:
        warning_2.append(sensor_2_6)

    sensor_2_7: dict = {
        "title": "п-к, №7",
        "signals": {
            "temp": check_data_2(
                type_sensors="temp",
                number_sensors=7,
                data_sensors=get_redis_data(["[2:50]"])),

            "vibr": check_data_2(
                type_sensors="vibr",
                number_sensors=7,
                data_sensors=get_redis_data([
                    "[2:20]",
                    "[2:18]",
                    "[2:19]",
                    "[2:217]",
                    "[2:215]",
                    "[2:216]",
                    "[2:193]",
                    "[2:191]",
                    "[2:192]"
                ]))
        }
    }

    if sensor_2_7["signals"]["temp"] != 0 or sensor_2_7["signals"]["vibr"] != 0:
        warning_2.append(sensor_2_7)

    sensor_2_8: dict = {
        "title": "п-к, №8",
        "signals": {
            "temp": check_data_2(
                type_sensors="temp",
                number_sensors=8,
                data_sensors=get_redis_data(["[2:51]"])),

            "vibr": check_data_2(
                type_sensors="vibr",
                number_sensors=8,
                data_sensors=get_redis_data([
                    "[2:23]",
                    "[2:21]",
                    "[2:22]",
                    "[2:220]",
                    "[2:218]",
                    "[2:219]",
                    "[2:196]",
                    "[2:194]",
                    "[2:195]"
                ]))
        }
    }

    if sensor_2_8["signals"]["temp"] != 0 or sensor_2_8["signals"]["vibr"] != 0:
        warning_2.append(sensor_2_8)

    sensor_2_9: dict = {
        "title": "п-к, №9",
        "signals": {
            "temp": check_data_2(
                type_sensors="temp",
                number_sensors=9,
                data_sensors=get_redis_data(["[2:52]"])),
        }
    }

    if sensor_2_9["signals"]["temp"] != 0:
        warning_2.append(sensor_2_9)

    sensor_2_10: dict = {
        "title": "Уровень масла",
        "signals": {
            "oil_level": check_data_2(
                type_sensors="oil_level",
                number_sensors=10,
                data_sensors=get_redis_data(["[4:7]"])),
        }
    }

    if sensor_2_10["signals"]["oil_level"] != 0:
        warning_2.append(sensor_2_10)

    sensor_2_11: dict = {
        "title": "Давление масла",
        "signals": {
            "oil_pressure": check_data_2(
                type_sensors="oil_pressure",
                number_sensors=10,
                data_sensors=get_redis_data(["[4:8]"])),
        }
    }

    if sensor_2_11["signals"]["oil_pressure"] != 0:
        warning_2.append(sensor_2_11)

    sensors_2 = [
        sensor_2_1,
        sensor_2_2,
        sensor_2_3,
        sensor_2_4,
        sensor_2_5,
        sensor_2_6,
        sensor_2_7,
        sensor_2_8,
        sensor_2_9,
        sensor_2_10,
        sensor_2_11
    ]

    ######################
    ## Эксгаустер 3

    sensor_3_1: dict = {
        "title": "п-к, №1",
        "signals": {
            "temp": check_data_3(
                type_sensors="temp",
                number_sensors=1,
                data_sensors=get_redis_data(["[0:27]"])),

            "vibr": check_data_3(
                type_sensors="vibr",
                number_sensors=1,
                data_sensors=get_redis_data([
                    "[0:2]",
                    "[0:0]",
                    "[0:1]",
                    "[0:161]",
                    "[0:159]",
                    "[0:160]",
                    "[0:137]",
                    "[0:135]",
                    "[0:136]"
                ]))
        }
    }

    if sensor_3_1["signals"]["temp"] != 0 or sensor_3_1["signals"]["vibr"] != 0:
        warning_3.append(sensor_3_1)

    sensor_3_2: dict = {
        "title": "п-к, №2",
        "signals": {
            "temp": check_data_3(
                type_sensors="temp",
                number_sensors=2,
                data_sensors=get_redis_data(["[0:28]"])),

            "vibr": check_data_3(
                type_sensors="vibr",
                number_sensors=2,
                data_sensors=get_redis_data([
                    "[0:5]",
                    "[0:3]",
                    "[0:4]",
                    "[0:164]",
                    "[0:162]",
                    "[0:163]",
                    "[0:140]",
                    "[0:138]",
                    "[0:139]"
                ]))
        }
    }

    if sensor_3_2["signals"]["temp"] != 0 or sensor_3_2["signals"]["vibr"] != 0:
        warning_3.append(sensor_3_2)

    sensor_3_3: dict = {
        "title": "п-к, №3",
        "signals": {
            "temp": check_data_3(
                type_sensors="temp",
                number_sensors=3,
                data_sensors=get_redis_data(["[0:29]"])),
        }
    }

    if sensor_3_3["signals"]["temp"] != 0:
        warning_3.append(sensor_3_3)

    sensor_3_4: dict = {
        "title": "п-к, №4",
        "signals": {
            "temp": check_data_3(
                type_sensors="temp",
                number_sensors=4,
                data_sensors=get_redis_data(["[0:30]"])),
        }
    }

    if sensor_3_4["signals"]["temp"]:
        warning_3.append(sensor_3_4)

    sensor_3_5: dict = {
        "title": "п-к, №5",
        "signals": {
            "temp": check_data_3(
                type_sensors="temp",
                number_sensors=5,
                data_sensors=get_redis_data(["[0:31]"])),
        }
    }

    if sensor_3_5["signals"]["temp"] != 0:
        warning_3.append(sensor_3_5)

    sensor_3_6: dict = {
        "title": "п-к, №6",
        "signals": {
            "temp": check_data_3(
                type_sensors="temp",
                number_sensors=6,
                data_sensors=get_redis_data(["[0:32]"])),
        }
    }

    if sensor_3_6["signals"]["temp"]:
        warning_3.append(sensor_3_6)

    sensor_3_7: dict = {
        "title": "п-к, №7",
        "signals": {
            "temp": check_data_3(
                type_sensors="temp",
                number_sensors=7,
                data_sensors=get_redis_data(["[0:33]"])),

            "vibr": check_data_3(
                type_sensors="vibr",
                number_sensors=7,
                data_sensors=get_redis_data([
                    "[0:8]",
                    "[0:6]",
                    "[0:7]",
                    "[0:167]",
                    "[0:165]",
                    "[0:166]",
                    "[0:143]",
                    "[0:141]",
                    "[0:142]"
                ]))
        }
    }

    if sensor_3_7["signals"]["temp"] != 0 or sensor_3_7["signals"]["vibr"] != 0:
        warning_3.append(sensor_3_7)

    sensor_3_8: dict = {
        "title": "п-к, №8",
        "signals": {
            "temp": check_data_3(
                type_sensors="temp",
                number_sensors=8,
                data_sensors=get_redis_data(["[0:34]"])),

            "vibr": check_data_3(
                type_sensors="vibr",
                number_sensors=8,
                data_sensors=get_redis_data([
                    "[0:11]",
                    "[0:9]",
                    "[0:10]",
                    "[0:170]",
                    "[0:168]",
                    "[0:169]",
                    "[0:146]",
                    "[0:144]",
                    "[0:145]"
                ]))
        }
    }

    if sensor_3_8["signals"]["temp"] != 0 or sensor_3_8["signals"]["vibr"] != 0:
        warning_3.append(sensor_3_8)

    sensor_3_9: dict = {
        "title": "п-к, №9",
        "signals": {
            "temp": check_data_3(
                type_sensors="temp",
                number_sensors=9,
                data_sensors=get_redis_data(["[0:35]"])),
        }
    }

    if sensor_3_9["signals"]["temp"] != 0:
        warning_3.append(sensor_3_9)

    sensor_3_10: dict = {
        "title": "Уровень масла",
        "signals": {
            "oil_level": check_data_3(
                type_sensors="oil_level",
                number_sensors=10,
                data_sensors=get_redis_data(["[1:0]"])),
        }
    }

    if sensor_3_10["signals"]["oil_level"] != 0:
        warning_3.append(sensor_3_10)

    sensor_3_11: dict = {
        "title": "Давление масла",
        "signals": {
            "oil_pressure": check_data_3(
                type_sensors="oil_pressure",
                number_sensors=10,
                data_sensors=get_redis_data(["[1:1]"])),
        }
    }

    if sensor_3_11["signals"]["oil_pressure"] != 0:
        warning_3.append(sensor_3_11)

    sensors_3 = [
        sensor_3_1,
        sensor_3_2,
        sensor_3_3,
        sensor_3_4,
        sensor_3_5,
        sensor_3_6,
        sensor_3_7,
        sensor_3_8,
        sensor_3_9,
        sensor_3_10,
        sensor_3_11
    ]

    ######################
    ## Эксгаустер 4

    sensor_4_1: dict = {
        "title": "п-к, №1",
        "signals": {
            "temp": check_data_4(
                type_sensors="temp",
                number_sensors=1,
                data_sensors=get_redis_data(["[0:43]"])),

            "vibr": check_data_4(
                type_sensors="vibr",
                number_sensors=1,
                data_sensors=get_redis_data([
                    "[0:14]",
                    "[0:12]",
                    "[0:13]",
                    "[0:209]",
                    "[0:207]",
                    "[0:208]",
                    "[0:185]",
                    "[0:183]",
                    "[0:184]"
                ]))
        }
    }

    if sensor_4_1["signals"]["temp"] != 0 or sensor_4_1["signals"]["vibr"] != 0:
        warning_4.append(sensor_4_1)

    sensor_4_2: dict = {
        "title": "п-к, №2",
        "signals": {
            "temp": check_data_4(
                type_sensors="temp",
                number_sensors=2,
                data_sensors=get_redis_data(["[0:44]"])),

            "vibr": check_data_4(
                type_sensors="vibr",
                number_sensors=2,
                data_sensors=get_redis_data([
                    "[0:17]",
                    "[0:15]",
                    "[0:16]",
                    "[0:212]",
                    "[0:210]",
                    "[0:211]",
                    "[0:188]",
                    "[0:186]",
                    "[0:187]"
                ]))
        }
    }

    if sensor_4_2["signals"]["temp"] != 0 or sensor_4_2["signals"]["vibr"] != 0:
        warning_4.append(sensor_4_2)

    sensor_4_3: dict = {
        "title": "п-к, №3",
        "signals": {
            "temp": check_data_4(
                type_sensors="temp",
                number_sensors=3,
                data_sensors=get_redis_data(["[0:45]"])),
        }
    }

    if sensor_4_3["signals"]["temp"] != 0:
        warning_4.append(sensor_4_3)

    sensor_4_4: dict = {
        "title": "п-к, №4",
        "signals": {
            "temp": check_data_4(
                type_sensors="temp",
                number_sensors=4,
                data_sensors=get_redis_data(["[0:47]"])),
        }
    }

    if sensor_4_4["signals"]["temp"]:
        warning_4.append(sensor_4_4)

    sensor_4_5: dict = {
        "title": "п-к, №5",
        "signals": {
            "temp": check_data_4(
                type_sensors="temp",
                number_sensors=5,
                data_sensors=get_redis_data(["[0:48]"])),
        }
    }

    if sensor_4_5["signals"]["temp"] != 0:
        warning_4.append(sensor_4_5)

    sensor_4_6: dict = {
        "title": "п-к, №6",
        "signals": {
            "temp": check_data_4(
                type_sensors="temp",
                number_sensors=6,
                data_sensors=get_redis_data(["[0:49]"])),
        }
    }

    if sensor_4_6["signals"]["temp"]:
        warning_4.append(sensor_4_6)

    sensor_4_7: dict = {
        "title": "п-к, №7",
        "signals": {
            "temp": check_data_4(
                type_sensors="temp",
                number_sensors=7,
                data_sensors=get_redis_data(["[0:50]"])),

            "vibr": check_data_4(
                type_sensors="vibr",
                number_sensors=7,
                data_sensors=get_redis_data([
                    "[0:20]",
                    "[0:18]",
                    "[0:19]",
                    "[0:215]",
                    "[0:213]",
                    "[0:214]",
                    "[0:191]",
                    "[0:189]",
                    "[0:190]"
                ]))
        }
    }

    if sensor_4_7["signals"]["temp"] != 0 or sensor_4_7["signals"]["vibr"] != 0:
        warning_4.append(sensor_4_7)

    sensor_4_8: dict = {
        "title": "п-к, №8",
        "signals": {
            "temp": check_data_4(
                type_sensors="temp",
                number_sensors=8,
                data_sensors=get_redis_data(["[0:51]"])),

            "vibr": check_data_4(
                type_sensors="vibr",
                number_sensors=8,
                data_sensors=get_redis_data([
                    "[0:23]",
                    "[0:21]",
                    "[0:22]",
                    "[0:218]",
                    "[0:216]",
                    "[0:217]",
                    "[0:194]",
                    "[0:192]",
                    "[0:193]"
                ]))
        }
    }

    if sensor_4_8["signals"]["temp"] != 0 or sensor_4_8["signals"]["vibr"] != 0:
        warning_4.append(sensor_4_8)

    sensor_4_9: dict = {
        "title": "п-к, №9",
        "signals": {
            "temp": check_data_4(
                type_sensors="temp",
                number_sensors=9,
                data_sensors=get_redis_data(["[0:52]"])),
        }
    }

    if sensor_4_9["signals"]["temp"] != 0:
        warning_4.append(sensor_4_9)

    sensor_4_10: dict = {
        "title": "Уровень масла",
        "signals": {
            "oil_level": check_data_4(
                type_sensors="oil_level",
                number_sensors=10,
                data_sensors=get_redis_data(["[1:7]"])),
        }
    }

    if sensor_4_10["signals"]["oil_level"] != 0:
        warning_4.append(sensor_4_10)

    sensor_4_11: dict = {
        "title": "Давление масла",
        "signals": {
            "oil_pressure": check_data_4(
                type_sensors="oil_pressure",
                number_sensors=10,
                data_sensors=get_redis_data(["[1:8]"])),
        }
    }

    if sensor_4_11["signals"]["oil_pressure"] != 0:
        warning_4.append(sensor_4_11)

    sensors_4 = [
        sensor_4_1,
        sensor_4_2,
        sensor_4_3,
        sensor_4_4,
        sensor_4_5,
        sensor_4_6,
        sensor_4_7,
        sensor_4_8,
        sensor_4_9,
        sensor_4_10,
        sensor_4_11
    ]

    answer: dict = {
        "refresh_data": get_moment(),
        "sinter_machines": {
            "1": {
                "exhausters": {
                    "1": {
                        "name": "Эксгаустер У-171",
                        "rotor_name": "Ротор № 35",
                        "last_change": 1675902744,
                        "prediction": 1623424356,
                        "sensors": sensors_1,
                        "warnings": warning_1
                    },
                    "2": {
                        "name": "Эксгаустер У-172",
                        "rotor_name": "Ротор № 47",
                        "last_change": 1674068400,
                        "prediction": 1623424356,
                        "sensors": sensors_2,
                        "warnings": warning_2
                    },

                }
            },

            "2":{
            "exhausters" : {
             "1": {
                    "name": "Эксгаустер Ф-171",
                    "rotor_name": "Ротор № 37",
                    "last_change": 1675278000,
                    "prediction": 1623424356,
                    "sensors": sensors_3,
                    "warnings": warning_3
                },
                "2": {
                    "name": "Эксгаустер Ф-172",
                    "rotor_name": "Ротор № 27",
                    "last_change": 1676228400,
                    "prediction": 1623424356,
                    "sensors": sensors_4,
                    "warnings": warning_4
                }
            
            }
               

            },
            "3": {
            "exhausters":{
                "1": {
                    "name": "Эксгаустер Х-171",
                    "rotor_name": "Ротор № 39",
                    "last_change": 1675278000,
                    "prediction": 1623424356,
                    "sensors": sensors_3,
                    "warnings": warning_3
                },
                "2": {
                    "name": "Эксгаустер Х-172",
                    "rotor_name": "Ротор № 45",
                    "last_change": 1676228400,
                    "prediction": 1623424356,
                    "sensors": sensors_4,
                    "warnings": warning_4
                }

            }
            }
        }
    }

    return answer

