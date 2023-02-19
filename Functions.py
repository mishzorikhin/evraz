# целевая переменная для каждого датчика подшипника
def target(a, a_w_min,a_w_max):
    if a >= a_w_min and a <= a_w_max: return


# функция которая переводит циклы в сутки, округляя их до целого числа
def cycle_to_day (count_cycle):
    days_before_change = count_cycle*1440
    return days_before_change

# функция которая сравнивает значения со всех датчиков и возвращает наименьшее число
def compare_and_return_min(list_days_before):
    min_el = min(list_days_before, key = lambda i: int(i))
    return min_el
# функция по замене '\\' на '.', чтобы название калонок читалось правильно.
def exchenge(list):
    x = []
    for i in list:
        k = i.replace('\\', '.')
        x.append(k)
    return x
# функция для определения смежных сигналов для определенного эксгаустера
def kafka_signal_column(df_signal_kafka, list_kafka_columns):
    kafka_signal_column = []
    for i in df_signal_kafka:
        for j in list_kafka_columns:
            if i == j:
                kafka_signal_column.append(i)
    return (kafka_signal_column)