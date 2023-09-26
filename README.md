# avg_crop_care_bot_2019
Прототип нейронной сети для детектирования болезней плодовых культур. В качестве рабочего интерфейса использовался Telegram-бот.
![AgACAgIAAxkBAAIjcF86NywnR0OqsKb398Gnl7H-YHcUAAKZrTEb2FPQSfcOXUWL9ATITOk-li4AAwEAAwIAA3gAA5DJAAIaBA](https://github.com/suuurfinbird/avg_crop_care_bot_2019/assets/145972187/1fa3548b-25e9-4cdf-8114-8b617f016115)

**Список файлов:**
1. global_config.conf - глобальные параметры(Telegram ID пользователей и админов, директории, классы болезней)
2. AvgustCare_cnn.json - параметры нейронной сети
3. AvgustCare_cnn.h5 - веса нейронной сети
4. Preprocessing.ipynb - блокнот с препроцессингом данных
5. AvgustCareBot.py - запуск Telegram бота и предсказание болезни
6. AvgustCarePredict.py - компиляция нейронной сети и выдача прогноза
7. predictAvgustCare.ipynb -блокнот с предсказанием по фотографии
