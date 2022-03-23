import requests
from datetime import datetime

API_KEY = 'DEMO_KEY'


def get_data_near_earth_objects(api_key, start_date=datetime(2022, 9, 7).date(), end_date=datetime(2022, 9, 8).date(),
                                top=8):
    # Функция получает сведения из Api Nasa об объектах околоземной орбиты за заданный промежуток времени в днях.
    # Возвращает отсортированный результат и нужное количество объектов.
    # https://api.nasa.gov/neo/rest/v1/feed?start_date=2022-02-23&end_date=2022-02-23&api_key=DEMO_KEY

    url_nasa_api = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}'
    get_info = requests.get(url_nasa_api).json()
    data_earth_objects = get_info['near_earth_objects']
    search_values_dict = {}
    
    # Собираем данные из json в словарь для сортировки используя в качестве ключа словарь.
    
    for _date, value in data_earth_objects.items():
        for i in range(len(value)):
            final_search_dict = {}
            neo_reference_id = value[i]['neo_reference_id']
            name = value[i]['name']
            absolute_magnitude_h = value[i]['absolute_magnitude_h']
            is_potentially_hazardous_asteroid = value[i]['is_potentially_hazardous_asteroid']

            final_search_dict[neo_reference_id] = dict(name=name,
                                                       absolute_magnitude_h=absolute_magnitude_h,
                                                       is_potentially_hazardous_asteroid=
                                                       is_potentially_hazardous_asteroid)
            
    # Словарь для сортировки где ключ это строковое представление словоря, а значение нужные нам для сортировки данные.
    
            search_values_dict[f'{final_search_dict}'] = absolute_magnitude_h
      
    # Сортируем наш словарь.
    
        sorted_search_values_dict = sorted(search_values_dict.items(), key=lambda x: x[1], reverse=True)
      
    # Отрисовываем нужные данные в требуемом формате.
    
        print('\n', _date)
        count = 1
        top_count = top
        for search_dataframe in sorted_search_values_dict:
            d = eval(search_dataframe[0])  # Превращаем словарь в строковом представлении в обычный словарь.
            if count <= top_count:
                for k, v in d.items():
                    print(f'{count} {k}: {v}')
                    count += 1
            else:
                break


if __name__ == '__main__':
    try:
        get_data_near_earth_objects(API_KEY)
    except Exception as e:
        print(e)
