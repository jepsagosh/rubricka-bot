import vk_api
from admin_confgig import Admin
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import keyboard
from vk_api.keyboard import VkKeyboardColor, VkKeyboard
from my_token import token_rubrick, token_test


session = vk_api.VkApi(token=token_test)
list_of_users = []
list_of_commands = ['/info','привет','/profile','/add_brands','/pay']

print(list_of_users)
def send(user_id, message, keyboard = None):
    post = {
        "user_id": user_id,
        "message": message,
        "random_id": 0
    }
    if keyboard != None:
        post['keyboard'] = keyboard.get_keyboard()
    else:
        post = post

    session.method("messages.send", post)

for event in VkLongPoll(session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id

        if text == 'привет':
            keyboard = VkKeyboard()
            keyboard.add_button('/info', VkKeyboardColor.PRIMARY)
            keyboard.add_button('/profile', VkKeyboardColor.NEGATIVE)
            keyboard.add_button('/add_brands',VkKeyboardColor.POSITIVE)
            send(user_id, 'Начинаю рубрикацию бота!')
            send(user_id,'Доступные команды:')
            send(user_id,'/info - инфо о боте 🎲'
                         '\n/profile - просмотр вашего профиля!👤'
                         '\n/add_brands - добавить бренды 👕👖👟',keyboard)
            if user_id not in list_of_users:
                list_of_users.append(user_id)
                print(list_of_users)

        if text =='/info':
            keyboard = VkKeyboard()
            keyboard.add_button('/pay',VkKeyboardColor.PRIMARY)
            send(user_id, 'Добро пожаловать в бота сообщества РУБРИКА. Данный бот нужен для отслеживания дропа вещей. Конечно все в этом мире не бесплатно, но цена на нашего бота всего 349 рублей в месяц. Ждем твою подписку!')
            send(user_id, 'Для оплаты бота нажмите на кнопку',keyboard)
        if text not in list_of_commands:
            send(user_id,'Такой команды не существует.')


