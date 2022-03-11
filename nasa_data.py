import requests


def get_data_near_earth_objects(api_key, start_date='2016-09-07', end_date='2016-09-08', top=10):
    # Функция получает сведения из Api Nasa об объектах околоземной орбиты за заданный промежуток времени в днях.
    # Возвращает отсортированный результат и нужное количество объектов.

    try:
        urls_nasa_api = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}'
        get_info = requests.get(urls_nasa_api).json()
        date_earth_objects = get_info['near_earth_objects']
        data_near_earth_objects_dict = {}
        finish_data_near_earth_objects_dict = {}
        # Из ответа апи вынимаем и помещаем в словарь нужные нам данные
        for key in date_earth_objects.keys():
            for i in range(len(date_earth_objects[key])):
                absolute_magnitude_h = date_earth_objects[key][i]['absolute_magnitude_h']
                data_near_earth_objects_dict[absolute_magnitude_h] = dict(date=key,
                                                                          neo_reference_id=
                                                                          date_earth_objects[key][i][
                                                                              'neo_reference_id'],
                                                                          name=date_earth_objects[key][i]['name'],
                                                                          is_potentially_hazardous_asteroid=
                                                                          date_earth_objects[key][i][
                                                                              'is_potentially_hazardous_asteroid'])
        # Сортируем данные по убыванию по ключу absolute_magnitude_h.
        sorted_result = sorted(data_near_earth_objects_dict.items(), key=lambda x: x[0], reverse=True)
        # Обрабатываем отсортированный словарь к нужной нам форме для вывода.
        for y in sorted_result:
            finish_data_near_earth_objects_dict[f'{y[1]["date"]} {y[1]["neo_reference_id"]}'] = dict(name=y[1]["name"],
                                                                                                     absolute_magnitude_h=
                                                                                                     y[
                                                                                                         0],
                                                                                                     is_potentially_hazardous_asteroid=
                                                                                                     y[1][
                                                                                                       "is_potentially_hazardous_asteroid"])
        # Распечатываем заданное колличество объектов при запуске функции.
        top_count = top
        count = 1
        for key in finish_data_near_earth_objects_dict:

            if count <= top_count:
                print(f'{key}: {finish_data_near_earth_objects_dict[key]}')
                count += 1
            else:
                break

    except Exception as e:
        print(e)


def main():
    get_data_near_earth_objects()


if __name__ == '__main__':
    main()
