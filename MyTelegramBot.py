import telebot
import random
bot = telebot.TeleBot('5362929766:AAGmueJb5UQySIq85R0YMzVsQ_bqJD7aHtE')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    baseRudeString = "Тадей – урод, каких поискать"
    messageUpper = message.text.upper()

    # Проверить упоминание Тадея
    tadeyNames = ['ТАДЕЙ', 'ТАДЕЯ', 'ТАДЕЮ', 'АЗАМ', 'АЗАМА', 'АЗАМУ', 'ТАДОЙ', 'ТЭДИ', 'ТЭДДИ', 'ТАДОЯ', 'АЗИМУТ', 'ДАРБИДОНТИ', 'УИЛСОН', 'ТАДОЮ', 'AZAMAT']
    for tadeyName in tadeyNames:
        if tadeyName in messageUpper:
            bot.send_message(message.chat.id, baseRudeString, reply_to_message_id=message.message_id)
            return

    # Проверить упоминание Длинного
    longNames = ['ДЛИННЫЙ', 'ДЛИННОГО', 'ДЛИННОМУ']
    for longName in longNames:
        if longName in messageUpper:
            bot.send_message(message.chat.id, "Кстати о длинных:\n" + baseRudeString, reply_to_message_id=message.message_id)
            return

    # Проверить упоминание Высокого
    tallNames = ['ВЫСОКИЙ', 'ВЫСОКОГО', 'ВЫСОКОМУ']
    for tallName in tallNames:
        if tallName in messageUpper:
            bot.send_message(message.chat.id, "Кстати о высоких:\n" + baseRudeString, reply_to_message_id=message.message_id)
            return

    # Проверить упоминание Дылды
    dildaNames = ['ДЫЛДА', 'ДЫЛДЕ', 'ДЫЛДУ']
    for dildaName in dildaNames:
        if dildaName in messageUpper:
            bot.send_message(message.chat.id, "Дылда у меня на аве)", reply_to_message_id=message.message_id)
            return


    isAuthorTadey = message.from_user.id == 443238354
    # Реакция на смех Тадея
    if isAuthorTadey:
        laughRudeMessages = ["Ржешь как конь!", "Че веселый такой? С психушки отпустили на денек?", "Тебе бы не смеяться, а плакать с таким ростом", "Хочу тоже вечно улыбаться!\nДля этого обязательно биться о дверной проем каждый день??", "Ты тут камеди клаб увидел? Шибзик!", "А этому лишь бы погыгыкать. Доктор! Хрэнов!"]
        laughWords = ['АХАХ', "ХАХА", '😂', '😄']
        randomIndexOfRudeMessage = random.randint(0, len(laughRudeMessages) - 1)
        randomLaughRudeMessage = laughRudeMessages[randomIndexOfRudeMessage]
        for laughWord in laughWords:
            if laughWord in messageUpper:
                bot.send_message(message.chat.id, randomLaughRudeMessage, reply_to_message_id=message.message_id)
                return

    # Реакция на ЫЫЫ Тадея
    if isAuthorTadey:
        iiiRudeMessages = ['Ыыыкать будешь в другом месте, Пилюлькин']
        iiiWords = ['ЫЫ']
        randomIndexOfRudeMessage = random.randint(0, len(iiiRudeMessages) - 1)
        randomIiiRudeMessage = iiiRudeMessages[randomIndexOfRudeMessage]
        for iiiWord in iiiWords:
            if iiiWord in messageUpper:
                bot.send_message(message.chat.id, randomIiiRudeMessage, reply_to_message_id=message.message_id)
                return


    # Команда 'Псевдоним для Тадея'
    tadeyPseudonims = ['Дылда', 'Дядя Стёпа', 'Долговязый хрен', 'Придурковатый великан', 'Дубина стоеросовая', 'Пробник человека', 'Пилюлькин', 'Дурилка картонная', 'Сутулая собака', 'Гомункул', 'Гермофродит', '40-летний лиственник', 'Крендель', 'Малый гигант большого секса', 'Дятел', 'Мерзавка', 'Лимузин', 'Мэлман', 'Писькин доктор']
    if messageUpper == '/PSEUDONIM' or messageUpper == '/PSEUDONIM@ZOOMERZBOT':
        randomIndexOfTadeyPseudonim = random.randint(0, len(tadeyPseudonims) - 1)
        randomTadeyPseudonim = tadeyPseudonims[randomIndexOfTadeyPseudonim]
        bot.send_message(message.chat.id, randomTadeyPseudonim)


    # Команда 'Какое-то фото'
    if messageUpper == '/RANDOMPHOTO' or messageUpper == '/RANDOMPHOTO@ZOOMERZBOT':
        import vk_api
        session = vk_api.VkApi(token='d2ae5ce95a8ac2cc021394b1e5d529dd0a2bbd074390c64c5f44d8ccc3f926ef1a799cd5fd6987aad9553')
        vk = session.get_api()
        owner_id = '77799357'
        album_id = '189050258'
        photosCount = vk.photos.get(owner_id=owner_id, album_id=album_id)['count']
        randomIndex = random.randint(0, photosCount - 1)
        allPhotosResponse = vk.photos.get(owner_id=owner_id, album_id=album_id, offset=randomIndex)
        allPhotos = allPhotosResponse['items']
        photoSizes = allPhotos[0]['sizes']
        photoUrl = photoSizes[-1]['url']
        bot.send_photo(message.chat.id, photoUrl)

    # Команда 'Озвучить сообщение'
    if messageUpper == '/AUDIOMESSAGE' or messageUpper == '/AUDIOMESSAGE@ZOOMERZBOT':
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.9)
        voices = engine.getProperty('voices')
        for voice in voices:
            if voice.languages == ['ru_RU']:
                engine.setProperty('voice', 'com.apple.speech.synthesis.voice.milena')
                engine.save_to_file('Привет, меня зовут Андрей', 'currentAudioMessage.mp3')
                print(voice)
        engine.runAndWait()



# Ответы на определенные стикеры
@bot.message_handler(content_types=['sticker'])
def get_sticker_messages(message):
    stickerId = message.sticker.file_unique_id
    if stickerId == 'AgADyhIAAjqOSEk':
        bot.send_message(message.chat.id, "Ну и клоун на стикере 🤡\nБездельник!!!", reply_to_message_id=message.message_id)
    elif stickerId == 'AgADnBEAAnMBOUo':
        bot.send_message(message.chat.id, "Тадей всегда отшучивается – че не спроси. Это я как уведомитель говорю!", reply_to_message_id=message.message_id)
    elif stickerId == 'AgADZxUAAt-AUUo':
        bot.send_message(message.chat.id, "Конечно не спорят, Тадей 💩 ест, и никто не спорит", reply_to_message_id=message.message_id)

bot.polling(none_stop=True, interval=0)
