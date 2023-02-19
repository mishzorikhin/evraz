import joblib
import json
import pandas as pd

def main ():
    # читаем модель из файла
    model = joblib.load('a_pipe.pkl')

    # открываем наш json файл
    with open('example_kafka_for_1_ moment.json', 'r', encoding='utf-8') as fin:
        form = json.load(fin)
        # создаем из словаря датафрейм
        df = pd.DataFrame.from_dict([form])
        # вызываем предикт с датафреймом и выводим результат предсказания
        list_a = [] #все предсказанные значения для текущего датчика положим в список
        for a in range len(train):
            predictions = model_fit.predict(
            start=len(train), end=len(train) + len(test) - 1, dynamic=False)
            list_a.append(predictions)
        return list_a
    # добавим значения в колонку с уже имеющимися данными
    df_a = pd.DataFrame({'a': list_a})
    pd.merge(left = df, right = df_a, on = 'id', how = 'offset')
# мы получили предсказание возникновения предупреждения датчика, для одного момента времени считывания данных с датчика
# для каждого датчика вибрации подшипника создаем дополнитоельную колонку с указанием вышел ли он за рамки допустимых значений
df['target_a'] = target(a, a_w_min,a_w_max)

# посчитаем разницу в количестве индексов датасетов
len_df = df.count()
len_df_a = df_a.count()
y = len_df-len_df_a

# чтобы посчитать сколько дней займут эти циклы до прогназируемого выхода
# из строя ротора, применем следующую функцию
cycle_to_day (y)

# прогоняем так каждый датчик вибрации на подшипниках №7 и №8 для каждого эксгаустера и складываем в список
list_day = []

# применяем к списку функцию, которая сравнивает количество оставшихся дней до замены и выдает наименьший результат.
compare_and_return_min(list_day)

if __name__ == '__main__'


