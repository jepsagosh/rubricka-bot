import vk_api
from admin_confgig import Admin
from vk_api.longpoll import VkLongPoll, VkEventType
from my_token import token_rubrick, token_test


session = vk_api.VkApi(token=token_rubrick)
list_of_users = [539106540]

print(list_of_users)
def send(user_id, message):
    session.method("messages.send",{
        "user_id": user_id,
        "message": message,
        "random_id": 0
    })

for event in VkLongPoll(session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id

        if text == 'привет':
            send(user_id, 'Начинаю рубрикацию бота!')
            list_of_users.append(user_id)
            print(list_of_users)

        if text == '/all' and user_id == 124888006:
            send(124888006, 'Введите сообщение')
            for event in VkLongPoll(session).listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    msg = event.text.lower()
                    for i in range(len(list_of_users)):
                        send(list_of_users[i], msg)
                    if user_id != 124888006:
                        send(user_id, 'отказано в доступе')




