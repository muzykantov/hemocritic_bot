# 🧪 Hemocritic Bot - умный анализ результатов крови в Telegram

Hemocritic - это Telegram-бот для автоматического анализа результатов клинических исследований крови. Бот мгновенно обрабатывает загруженные анализы и предоставляет понятные рекомендации.

## ✨ Возможности

- Быстрый анализ результатов (около 30 секунд)
- Поддержка PDF-файлов и фотографий бланков
- Работа с результатами из всех основных лабораторий
- Персонализированные рекомендации с учетом пола, возраста и других параметров
- Понятные объяснения отклонений от нормы
- Защищенная обработка медицинских данных

## 🚀 Как использовать

1. Найдите бота в Telegram: [@Hemocritic_bot](https://t.me/Hemocritic_bot)
2. Отправьте фото или PDF-файл с результатами анализа
3. При необходимости укажите дополнительные данные (возраст, пол, вес, рост)
4. Получите подробный анализ и рекомендации

## 📋 Поддерживаемые форматы данных

- PDF-файлы с результатами анализов
- Фотографии бланков
- Текстовые данные в структурированном формате

## 🛠 Технические требования

Для запуска собственной копии бота необходимо:

1. Python 3.8 или выше
2. Docker и Docker Compose
3. Токен Telegram Bot API
4. Токен OpenAI API

## ⚙️ Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/muzykantov/hemocritic_bot.git
cd hemocritic_bot
```

2. Создайте конфигурационные файлы:
```bash
cp config/config.example.yml config/config.yml
cp config/config.example.env config/config.env
```

3. Отредактируйте `config/config.yml` и `config/config.env`, указав ваши токены

4. Запустите бота через Docker Compose:
```bash
docker-compose --env-file config/config.env up --build
```

## 🔒 Безопасность

- Бот не хранит результаты анализов и персональные данные
- Все данные обрабатываются в оперативной памяти и удаляются после анализа
- Взаимодействие с ботом происходит через защищенный протокол Telegram

## 📝 Команды бота

- `/start` - Начать работу с ботом
- `/help` - Получить справку по использованию
- `/new` - Начать новый анализ
- `/cancel` - Отменить текущий анализ

## 👥 Команда проекта

- [Ольга Шварева](https://t.me/OlgaShvareva)
- [Лиана Гайсина](https://t.me/Liana_Gg)
- [Дарья Курочкина](https://t.me/Smile_Week)
- [Зилия Чайка](https://t.me/alivamira)
- [Евгений Захарцев](https://t.me/DjoniZZZZ)
- [Геннадий Музыкантов](https://t.me/muzykantov)

## 🤝 Вклад в проект

Мы приветствуем вклад в развитие проекта! Если вы хотите помочь:

1. Создайте форк репозитория
2. Внесите изменения
3. Создайте Pull Request

## 📜 Лицензия

MIT License. Подробности в файле [LICENSE](LICENSE)

## ✉️ Контакты

По всем вопросам обращайтесь:
- Telegram: [@Liana_Gg](https://t.me/Liana_Gg)