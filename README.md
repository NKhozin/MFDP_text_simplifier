## Проект по курсу My First Data Project 2 от ODS.ai: сервис по суммаризации текстов
### Введение
В современном информационном мире мы сталкиваемся с непрерывным потоком текстовых данных, которые требуют быстрой и эффективной обработки. Редакторы, журналисты и специалисты по социальным медиа сталкиваются с постоянной необходимостью кратко и емко представить информацию, сохранив при этом исходный смысл. Однако, обработка больших объемов текста и поиск наиболее значимых сведений может быть утомительной и времязатратной задачей. Исходя из этой проблемы появилась идея создания сервиса по автоматическому упрощению текстовых данных.
***
### Цель
Создание сервиса для автоматической суммаризации текста
***
### Задачи
- поиск подходящих корпусов параллельных текстов и их обработка
- выбор и обучение модели, подбор гиперпараметров
- создание интерфейса для взаимодействия с пользователями
***
### Данные
Для решения задачи использовались следующие наборы данных:
- [gazeta](https://github.com/IlyaGusev/gazeta)
- [para_phraser](https://huggingface.co/datasets/cointegrated/ru-paraphrase-NMT-Leipzig)
- [ru_adapt](https://github.com/Digital-Pushkin-Lab/RuAdapt)
- [ru_simp](https://huggingface.co/datasets/IlyaGusev/headline_cause)
- [ru_xlsum](https://huggingface.co/datasets/csebuetnlp/xlsum)
  
Данные были предварительно очищены. Для всех корпусов оставлены только те пары:
- где целевой текст больше по количеству токенов, чем исходный
- где в исходном тексте 10 и более токенов, а в целевом не менее 5
- где целевой текст не является подстрокой исходного
- для корпуса перефразирования уберем тексты, где в целевом содержится менее 20 и более 80 процентов от исходного текста

Информация по датасетам после очистки:
| Название датасета | Количество | Макс. длина исходного предложения (токенов) | Средняя длина исходного предложения (токенов) | Средняя длина целевого предложения (токенов)
|-------|-------|-------|-------|-------|
| gazeta | 63434 | 2841 | 1353 | 91 |
| para_phraser | 1143158 | 5663 | 23 | 16 |
| ru_adapt | 41563 | 8180 | 68 | 37 |
| ru_simp | 6432 | 168 | 42 | 26 |
| ru_xlsum | 66669 | 37904 | 1173 | 54 |

По данным корпусам были рассчитаны различные метрики сходства предложений внутри корпусов: 
- sim - косинусная близость пар. Чем она выше, тем парафразы ближе по смыслу друг к другу
- sim_random - косинусная близость случайным образом перемешанных пар. Чем она выше, тем корпус однообразнее
- bleu - BLEU пары парафраз, усреднённое по обоим направлениям
- char_ngram_overlap - доля общих символьных n-грамм
- perp - средняя перплексия всех предложений в корпусе

| Название датасета | sim | sim_random | bleu_1 | bleu_2 | bleu_ | char_ngram_overlap | perp_1 | perp_2 | perp_mean |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| [gazeta](https://github.com/IlyaGusev/gazeta) | 0.68 | 0.26 | 0.0002 | 0.07 | 0.04 | 0.09 | 2.99 | 3.13 | 1.61 |
| [para_phraser](https://huggingface.co/datasets/cointegrated/ru-paraphrase-NMT-Leipzig) | 0.66 | 0.32 | 0.32 | 0.34 | 0.27 | 4.65 | 4.09 | 3.52 | 1.65 |
| [ru_adapt](https://github.com/Digital-Pushkin-Lab/RuAdapt) | 0.74 | 0.22 | 0.52 | 0.58 | 0.55 | 0.52 | 4.05 | 3.70 | 3.07 |
| [ru_simp](https://huggingface.co/datasets/IlyaGusev/headline_cause) | 0.77 | 0.27 | 0.36 | 0.42 | 0.39 | 0.34 | 4.23 | 4.12 | 3.34 |
| [ru_xlsum](https://huggingface.co/datasets/csebuetnlp/xlsum) | 0.54 | 0.27 | 0.01 | 0.08 | 0.05 | 0.08 | 3.03 | 3.06 | 1.65 |

***
## Методология
В качестве моделей, которые будут дообучаться на задачу суммаризации текста, будут использоваться:
- ruT5
- GPT-3
- BART

Метрики:
- ROUGE(1,2,L)
- SARI
***
### Метрики
В таблице ниже можно увидеть значения метрик на тестовом наборе данных при различных комбинациях: датасетов, длинны исходных текстов.
| Этап | Модель | Данные / количество эпох | SARI | rouge1 | rouge2 | rougeL | time_predict | avg_time_predict |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| **baseline** | **ruT5** | **all_small / 3** | **33.4** | **6.1** | **1.5** | **6.1** | **485.3** | **0.19** |
| baseline | BART | all_small / 3 | 33.5 | 5.3 | 1.3 | 5.3 | 2048 | 0.8 |
| fine_tuning 1.0 | ruT5 | ru_adapt_small / 3 | 33.4 | 6.7 | 1.9 | 6.6 | 721.3 | 0.28 |
| fine_tuning 1.1.0 | ruT5 | ru_xlsum_small / 3 | 33.6 | 4.6 | 1.1 | 4.6 | 523.6 | 0.2 |
| fine_tuning 1.2 | ruT5 | mix_medium / 3 | 33.6 | 6.1 | 1.5 | 5.4 | 630.9 | 0.24 |
| fine_tuning 1.3 | ruT5 | mix_large / 3 | 33.7 | 3.7 | 0.6 | 3.6 | 668.9 | 0.26 |
| fine_tuning 1.4 | ruT5 | para_phraser_small / 1 | 33.6 | 2.4 | 0.2 | 2.4 | 386.9 | 0.15 |
| **fine_tuning 1.1.1** | **ruT5** | **all_small+medium / 1** | **33.4** | **7.2** | **2.2** | **7.2** | **657.3** | **0.26** |
| fine_tuning 3.0 | ruT5 | all_clean_small+medium / 1 | 33.4 | 7.1 | 2.0 | 7.0 | 729.2 | 0.28 |

По метрикам видно, что в какой-то момент модель переобучается: особенно метрики ухудшаются от версии 1.2 к 1.3 и от 1.3 к 1.4. Особенно переобучение заметно при попытках предсказать сокращенный текст для текстовой выборки. В предсказании появляются слова, не относящиеся к контексту исходного предложения. Думаю, это связано с неправильными параметрами обучения.
По этой причине в итерации 1.1.1 берутся базовые гиперпараметры модели. <br />
В fine_tuning 3.0 корпус текстов для обучения был очищен более подробно: были отброшены примеры с менее чем двумя леммами на пересечении между лемматизированным источником и целевым предложением.
***
### Пример работы модели rut5_v8 в телеграмм боте
Пример предсказания модели на данных, которых не было в обучающем наборе, из новостных каналов. 
![image](https://github.com/NKhozin/mfdp_text_simplifier/assets/92330362/9f6d55b5-16a3-488f-addd-f305e84f20e3)
***
### Описание файлов репозитория:
- data_prepare_main - подготовка данных, разделение их на тренировочный, валидационный и тестовый наборы, очистка данных
- fit_model - обучение моделей
- calculate_metrics	- расчеты метрик на тестовом наборе
- inference_example - пример использования модели
- ru_t5_optimize - оптимизация параметров модели T5
- tg_bot - код для запуска телеграмм бота
***
## Инструкция по использованию
#### Ссылка на скачивание модели на huggingface: [t5_summarization](https://huggingface.co/nikitakhozin/t5_summarization)
#### Ссылка на скачивание docker контейнера: [t5_summarization](https://hub.docker.com/r/nkhozin/summarization_bot)
#### Шаг 1
Скачать образ контейнера с телеграмм ботом:
```python
docker pull nkhozin/summarization_bot
```
#### Шаг 2
Развернуть контейнер:
```python
docker run nkhozin/summarization_bot
```
#### Шаг 3
Открыть в телеграмме бота - [text_simplifier_bot](https://t.me/text_simplifier_bot)
#### Шаг 4
Подавать текст для суммаризации с префиксом:
"/simplify <your_text>"

### Использование модели в Python:
#### Шаг 1
Склонируйте репозиторий командой:
```python
git clone https://github.com/NKhozin/MFDP_text_simplifier
```
#### Шаг 2
Перейдите в папку MFDP_text_simplifier:
```python
```
cd mfdp-emotion-detection
#### Шаг 3
Установить необходимые версии библиотек из файла requirements.txt:
```python
pip install -r requirements.txt
```
#### Шаг 3
Запустить функцию generate_t5(text) в rut5_inference.ipynb, где text - исходный текст для суммаризации.
***
Основной модуль приложения main_bot.py состоит из двух частей:
1) Функция генерации сокращенного варианта исходного текста - generate_t5.
2) Телеграмм бот с функциями отправки приветственного текста в начале взаимодействия с ним после команды "/start", а также обработкой команды "/simplify <text>", где text - исходный текст для суммаризации из сообщения.
