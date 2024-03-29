# Телеграм-бот “Менеджер мероприятий”

# Общая информация

Бот был создан в 2023 году в рамках заказа на фрилансе для самой крупной анимационной команды Челябинска. Компания занимается проведением различного рода мероприятий по типу тимбилдингов, корпоративов и детских праздников.

Бот является инструментом для менеджмента всех предстоящих событий. С его помощью можно добавлять в список новые предстоящие мероприятия и получать напоминания.

# Основной функционал

Взаимодействие с Telegram происходит асинхронно с помощью библиотеки aiogram. На момент написания проекта актуальной версией был aiogram2. При запуске бота можно авторизоваться как сотрудник и просматривать предстоящие события, либо как администратор (введя код администратора), чтобы добавлять, удалять, редактировать и архивировать события.

При добавлении мероприятия в базу данных собираются следующие данные:

- Название
- Стоимость
- Дата
- Время начала
- Время окончания
- Контакты организатора
- Местоположение
- Дополнительное описание

С помощью библиотек datetime и APScheduler за сутки и за трое суток до назначенного времени мероприятия всем администраторам высылается напоминание о предстоящем событии.

Любой параметр мероприятия можно изменить в любой момент. Также администраторы имеют право сделать рассылку на всех пользователей. Процесс создания мероприятия и рассылки реализован с помощью встроенной в aiogram state-машины.

Для запуска бота необходимо вставить токен собственного бота в файл config_info/config.py, который нужно получить в специальном [боте](https://t.me/BotFather).

# Архивация

Для архивации мероприятий к проекту подключены Google-таблицы. Мероприятие можно архивировать вручную в любой момент, однако каждый день в 23:55 бот автоматически проверяет, есть ли в базе данных мероприятия, датированные сегодняшним днём и архивирует их. Для подключения Google-таблиц при запуске необходимо воспользоваться этим [гайдом](https://habr.com/ru/articles/483302/).

# Стэк

- asyncio
- aiogram
- apscheduler
- gspread
- logging
- sqlite3
