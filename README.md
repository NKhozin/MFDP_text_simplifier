## mfdp_text_simplifier - проект по созданию сервиса суммаризации текстов
###Модель: https://huggingface.co/nikitakhozin/t5_summarization
###Контейнер телеграмм бота: https://hub.docker.com/r/nkhozin/summarization_bot

### Описание файлов в архиве:
- data_prepare_main.ipynb - подготовка данных и разделение их на тренировочный, валидационный и тестовый наборы.
- rut5.ipynb - обучение модели Т5.
- rut5_optimize.ipynb - поиск оптимальных гиперпараметров модели Т5.
- rugpt3.ipynb - обучение модели RuGPT3.
- bart.ipynb - обучение модели BART.
- calculate_metrics.ipynb	- расчет метрик на тестовом наборе.
- tg_bot.ipynb - код для запуска телеграмм бота.
### Данные для обучения
![image](https://github.com/NKhozin/mfdp_text_simplifier/assets/92330362/1ffac000-cfa6-44f0-81dd-90534b2e536a)
### Метрики по данным для обучения в разбивке по корпусам
![image](https://github.com/NKhozin/mfdp_text_simplifier/assets/92330362/c071bc2f-f9fe-43c4-bbc7-1baf6851b6fe)
### Процесс поиска оптимальных гиперпараметров для rut5
batch_size=6, num_epochs=2    
![image](https://github.com/NKhozin/mfdp_text_simplifier/assets/92330362/f3fe0822-a459-4119-993a-b56c2ea66bc4)
### Метрики по моделям
![image](https://github.com/NKhozin/mfdp_text_simplifier/assets/92330362/0b02f3d0-acbe-401f-8bc8-35ebda85b3cd)
### Пример работы модели rut5_v7 в телеграмм боте
Примеры взяты из тестового набора.    
![image](https://github.com/NKhozin/mfdp_text_simplifier/assets/92330362/752c6f47-6bbb-41ec-abb9-8e3af867788e)

