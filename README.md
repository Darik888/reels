# MyReelsHelperBot

Простой Telegram бот на Python с использованием aiogram 3.

## Запуск локально

1. Установить зависимости:

```
pip install -r requirements.txt
```

2. Установить переменную окружения с токеном бота:

- Linux/macOS:
```
export BOT_TOKEN=your_bot_token_here
```

- Windows (cmd):
```
set BOT_TOKEN=your_bot_token_here
```

3. Запустить бота:

```
python main.py
```

## Деплой на Render.com

1. Создайте репозиторий на GitHub с этим кодом (например, форкнув этот проект).  
2. Зайдите в Render и создайте новый Web Service, подключив репозиторий.  
3. В настройках сервиса добавьте переменную окружения `BOT_TOKEN` со значением вашего токена.  
4. В поле команды запуска укажите:  
```
python main.py
```  
5. Запустите сервис.

Бот будет доступен и отвечать на команду /start.