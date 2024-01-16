## Проект по курсу My First Data Project 2 от ODS.ai: сервис по суммаризации текстов
### Краткое введение
### Контекст и проблематика
### Данные для обучения
Опишите данные, которые вы используете. Откуда они взяты? Какого они качества? Каков их объем?
![image](https://github.com/NKhozin/mfdp_text_simplifier/assets/92330362/39c02ca4-ca5b-4c18-baa0-7189e4d00810) <br />
По данным корпусам были рассчитаны 
![image](https://github.com/NKhozin/mfdp_text_simplifier/assets/92330362/60b1c333-1f5a-4ebf-9825-7010a587673b) <br />
***
## Методология
Какие методы или техники вы используете для решения задачи? Опишите свой подход подробно.
***
### Метрики
В таблице ниже можно увидеть значения метрик на тестовом наборе данных при различных комбинациях данных для обучения. 
![image](https://github.com/NKhozin/mfdp_text_simplifier/assets/92330362/ffec12d2-a7f3-4792-a502-740c80a3a47d)
***
### Пример работы модели rut5_v8 в телеграмм боте
Пример предсказания модели на данных, которых не было в обучающем наборе, из новостных каналов. 
![image](https://github.com/NKhozin/mfdp_text_simplifier/assets/92330362/9f6d55b5-16a3-488f-addd-f305e84f20e3)
***
### Описание файлов репозитория:
- calculate_metrics	- расчеты метрик на тестовом наборе.
- data_prepare_main - подготовка данных, разделение их на тренировочный, валидационный и тестовый наборы, очистка данных.
- fit_model - обучение моделей.
- inference_example - пример использования модели.
- ru_t5_optimize - оптимизация параметров модели T5.
- tg_bot - код для запуска телеграмм бота.
***
## Инструкция по использованию
### Модель: https://huggingface.co/nikitakhozin/t5_summarization
### Контейнер телеграмм бота: https://hub.docker.com/r/nkhozin/summarization_bot
### Контейнер с использованием моего телеграмм бота:
1) Скачать образ контейнера с телеграмм ботом: <br />
```docker pull nkhozin/summarization_bot```
2) Развернуть контейнер: <br />
```docker run nkhozin/summarization_bot```
3) Открыть в телеграмме бота - https://t.me/text_simplifier_bot
4) Подавать текст для суммаризации с префиксом:
"/simplify <your_text>"

### Использование модели в своем телеграмм боте:
1) Скачать mfdp_text_simplifier/tg_bot.
2) В main_bot.py подставить на место <YOUR_TG_BOT_TOKEN> свой токен от телеграмм бота.
3) Установить необходимые версии библиотек из файла requirements.txt: <br />
```pip install -r requirements.txt```
5) Запустить в main_bot.py: <br />
```bot.polling()```
5) Зайти в свой телеграмм бот. Подавать текст для суммаризации с префиксом:
"/simplify <your_text>"

### Использование модели в Python:
1) Скачать mfdp_text_simplifier/inference_example.
2) Установить необходимые версии библиотек из файла requirements.txt: <br />
```pip install -r requirements.txt```
4) Запустить функцию generate_t5(text) в rut5_inference.ipynb, где text - исходный текст для суммаризации.
***
Основной модуль приложения main_bot.py состоит из двух частей:
1) Функция генерации сокращенного варианта исходного текста - generate_t5.
2) Телеграмм бот с функциями отправки приветственного текста в начале взаимодействия с ним после команды "/start", а также обработкой команды "/simplify <text>", где text - исходный текст для суммаризации из сообщения.
