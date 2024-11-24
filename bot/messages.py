START_MESSAGE = """🧪 Привет! Я Hemocritic - ваш умный помощник в расшифровке медицинских анализов

Что я умею:
- Мгновенный анализ результатов
- Понятные объяснения показателей
- Персональные рекомендации

🔬 Чтобы начать:
1. Сфотографируйте анализ или сохраните PDF
2. Отправьте файл мне
3. Получите расшифровку через 30 секунд

Поддерживаю анализы из всех основных лабораторий
🚀 Начнем? Отправьте свой анализ!

"""

HELP_MESSAGE = """🧪 Команды бота:
⚪ /retry – Повторно проанализировать последние результаты
⚪ /new – Начать анализ новых результатов
⚪ /settings – Настройить параметры анализа
⚪ /help – Показать справку

📋 Поддерживаемые форматы:
- PDF-файлы с результатами анализов
- Фотографии бланков
- Текстовые данные в структурированном формате
"""

HELP_GROUP_CHAT_MESSAGE = """Вы можете добавить Hemocritic в <b>групповой чат</b> вашей клиники или медицинского центра!

Инструкция (смотрите <b>видео</b> ниже):
1. Добавьте бота в групповой чат
2. Сделайте его <b>администратором</b>, чтобы он мог видеть сообщения (остальные права можно ограничить)
3. Готово!

Чтобы получить анализ результатов в чате – @ <b>отметьте</b> бота или <b>ответьте</b> на его сообщение.
Например: "{bot_username} проанализируй результаты анализов"
"""

MESSAGES = {
    "wait_for_answer": "⏳ Пожалуйста, <b>подождите</b>, идет анализ предыдущих результатов\nИли используйте /cancel чтобы отменить",
    "nothing_to_cancel": "<i>Нет активных анализов для отмены</i>",
    "canceled": "✅ Анализ отменен",
    "new_dialog": "Готов к анализу новых результатов ✅",
    "empty_message": "🥲 Вы отправили <b>пустое сообщение</b>. Пожалуйста, отправьте результаты анализов!",
    "no_retry_message": "Нет результатов для повторного анализа 🤷‍♂️",
    "editing_not_supported": "🥲 К сожалению, <b>редактирование</b> отправленных результатов не поддерживается",
    "error_handler": "Произошла ошибка при анализе результатов",
    "file_not_supported": "Я умею работать только с изображениями, PDF-файлами и текстом. Пожалуйста, отправьте результаты в поддерживаемом формате.",
    "voice_transcribed": "🎤: <i>{text}</i>",
    "context_length_exceeded_one": "✍️ <i>Примечание:</i> Текущая сессия содержит слишком много данных, поэтому ваши <b>первые результаты</b> были удалены из анализа.\nОтправьте команду /new чтобы начать новый анализ",
    "context_length_exceeded_many": "✍️ <i>Примечание:</i> Текущая сессия содержит слишком много данных, поэтому <b>{n} первых результатов</b> были удалены из анализа.\nОтправьте команду /new чтобы начать новый анализ",
    "timeout_new_dialog": "Начинаю новый анализ из-за длительного периода неактивности ✅",
    "start_message": START_MESSAGE,  # Ссылка на константу START_MESSAGE
    "need_basic_info": "Для более точного анализа, пожалуйста, укажите:",
    "need_age": "Укажите, пожалуйста, ваш возраст",
    "need_gender": "Укажите, пожалуйста, ваш пол (М/Ж)",
    "need_weight": "Укажите, пожалуйста, ваш вес в килограммах",
    "need_height": "Укажите, пожалуйста, ваш рост в сантиметрах",
    "confirm_data": "Подтвердите, пожалуйста, ваши данные:\nВозраст: {age} лет\nПол: {gender}\nВес: {weight} кг\nРост: {height} см",
    "processing_results": "🔬 Анализирую результаты...",
    "unsupported_file_type": "К сожалению, я не могу обработать этот тип файла. Пожалуйста, отправьте результаты анализов в виде PDF, фото или текста.",
}

MENU_MESSAGES = {
    "settings_model_select": "Выберите <b>режим анализа</b>:",
    "model_changed": "Режим анализа изменен на {model_name} ✅",
}

BALANCE_MESSAGES = {
    "balance_header": "Статистика использования:\nПроанализировано результатов: <b>{total_tokens}</b>\n\n",
    "balance_details": "🏷️ Детали:\n",
    "balance_model": "- Тип анализа {model}: <b>{tokens} результатов</b>\n",
}

BOT_COMMANDS = [
    ("new", "Начать анализ новых результатов"),
    ("retry", "Повторить анализ последних результатов"),
    ("settings", "Настройки анализа"),
    ("help", "Показать справку"),
]
