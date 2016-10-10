# 15_midnighters

# Совы

Скрипт выводит список пользователей devman.org, кто отправлял задачи на проверку в ночное время, основываясь на предоставленных через [API](http://devman.org/api/challenges/solution_attempts/?page=1) данных.

**Запуск скрипта:**

`python seek_dev_nighters.py`


Для корректоной работы скрипта необходимо установить следующие модули:
* **requests** - для работы с HTTP,
* **pytz** - для работы с временными зонами.

Пакеты устанавливаются по команде `pip install -r requirements.txt`.
