import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from my_token import token_rubrick

session = vk_api.VkApi(token=token_rubrick)

class Admin():
    def __init__(self,user_id,list_of_users):
        self.user_id = user_id
        self.list_of_users = list_of_users

    def send(user_id, message):
        session.method("messages.send", {
            "user_id": user_id,
            "message": message,
            "random_id": 0
        })

    def mass_spam(self):
        for event in VkLongPoll(session).listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                txt = event.text.low()
                if txt == '/all':
                    Admin.send(self.user_id,'Введите сообщение')
                    msg = event.text.low()
                    for i in range(len(self.list_of_users)):
                        Admin.send(self.list_of_users[i],msg)
