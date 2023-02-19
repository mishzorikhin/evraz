from main_page import get_redis_data
from sensors_processing.exgaustr_from_2_page import check_data_for_exhauster


def get_exhauster_data() -> dict:
    answer: dict = {
        "refresh_data": 123134,
        "sinter_machines": {
            "1": {
                "exhausters": {
                    "1": {
                        "name": "Эксгаустер У-171",
                        "rotor_name": "Ротор № 35",
                        "last_change": 1623424356,
                        "prediction": 1623424356,
                        "sensors":
                            [
                                {
                                    "title": "п-к, №1",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=1,
                                        data_sensors=get_redis_data([
                                            "[2:27]",
                                            "[2:2]",
                                            "[2:0]",
                                            "[2:1]",
                                            "[2:162]",
                                            "[2:138]",
                                            "[2:161]",
                                            "[2:137]",
                                            "[2:163]",
                                            "[2:139]"
                                        ]))
                                },
                                {
                                    "title": "п-к, №2",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=2,
                                        data_sensors=get_redis_data([
                                            "[2:28]",
                                            "[2:4]",
                                            "[2:3]",
                                            "[2:5]",
                                            "[2:165]",
                                            "[2:141]",
                                            "[2:164]",
                                            "[2:140]",
                                            "[2:166]",
                                            "[2:142]"
                                        ]))
                                },
                                {
                                    "title": "п-к, №3",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=3,
                                        data_sensors=get_redis_data([
                                            "[2:29]"
                                        ]))
                                },
                                {
                                    "title": "п-к, №4",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=4,
                                        data_sensors=get_redis_data([
                                            "[2:30]"
                                        ]))
                                },
                                {
                                    "title": "п-к, №5",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=5,
                                        data_sensors=get_redis_data([
                                            "[2:31]"
                                        ]))
                                },
                                {
                                    "title": "п-к, №6",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=6,
                                        data_sensors=get_redis_data([
                                            "[2:32]"
                                        ]))
                                },
                                {
                                    "title": "п-к, №7",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=7,
                                        data_sensors=get_redis_data([
                                            "[2:33]",
                                            "[2:7]",
                                            "[2:6]",
                                            "[2:8]",
                                            "[2:168]",
                                            "[2:144]",
                                            "[2:167]",
                                            "[2:143]",
                                            "[2:169]",
                                            "[2:145]"
                                        ]))
                                },
                                {
                                    "title": "п-к, №8",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=8,
                                        data_sensors=get_redis_data([
                                            "[2:34]",
                                            "[2:10]",
                                            "[2:9]",
                                            "[2:11]",
                                            "[2:171]",
                                            "[2:147]",
                                            "[2:170]",
                                            "[2:146]",
                                            "[2:172]",
                                            "[2:148]"
                                        ]))
                                },

                                {
                                    "title": "п-к, №9",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=9,
                                        data_sensors=get_redis_data([
                                            "[2:35]"
                                        ]))
                                },

                                {
                                    "title": "П-к, №9",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=10,
                                        data_sensors=get_redis_data([
                                            "[4:0]"
                                        ]))
                                },

                                {
                                    "title": "Давление масла",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=11,
                                        data_sensors=get_redis_data([
                                            "[4:1]"
                                        ]))
                                },
                                {
                                    "title": "Главны привод Ток,А"
,
                                    "signals": check_data_for_exhauster(
                                        number_sensors=12,
                                        data_sensors=get_redis_data([
                                            "[4.2]"
                                        ]))
                                },
                                {
                                    "title": "Главный привод Ток двигателя, А",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=13,
                                        data_sensors=get_redis_data([
                                            "[4:3]"
                                        ]))
                                },
                                {
                                    "title": "Гл. привод, Ток статора эксгаустера №1",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=14,
                                        data_sensors=get_redis_data([
                                            "[4.4]"
                                        ]))
                                },
                                {
                                    "title": "Гл. привод. Напряжение статора эксгаустера №1",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=15,
                                        data_sensors=get_redis_data([
                                            "[4.5]"
                                        ]))
                                },
                                {
                                    "title": "Охладитель/ Масло",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=16,
                                        data_sensors=get_redis_data([
                                            "[2:36]"
                                        ]))
                                },
                                {
                                    "title": "-Охладитель/ Масло",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=17,
                                        data_sensors=get_redis_data([
                                            "[2:37]"
                                        ]))
                                },
                                {
                                    "title": "Охладитель/ Масло",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=18,
                                        data_sensors=get_redis_data([
                                            "[2:41]"
                                        ]))
                                },
                                {
                                    "title": "Охладитель/ Масло",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=19,
                                        data_sensors=get_redis_data([
                                            "[2:42]"
                                        ]))
                                },
                                {
                                    "title": "Температура перед эксгаустером №1",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=20,
                                        data_sensors=get_redis_data([
                                            "[2:24]"
                                        ]))
                                },
                                {
                                    "title": "Разрежение перед эксгаустером №1",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=21,
                                        data_sensors=get_redis_data([
                                            "[2:61]"
                                        ]))
                                },
                                {
                                    "title": "Положение задвижки газ эксгаустера №1",
                                    "signals": check_data_for_exhauster(
                                        number_sensors=22,
                                        data_sensors=get_redis_data([
                                            "[4.6]"
                                        ]))
                                },

                            ]
                    }
                }
            }
        }
    }

    return answer


print(get_exhauster_data())


