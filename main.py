import vk_api
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def loh_detector(group):
    return group[random.randint(0, 18)]


def main():
    vk_session = vk_api.VkApi(
        token='e16cf68317bcf5092112a4672cd17b6642e4635eb7ba7b06106c7d661141546f4c42ec4f9fbf8cadbae37')

    longpoll = VkBotLongPoll(vk_session, '205367481')

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()

            if event.obj.message['text'].lower().startswith('кто дежурный'):
                if event.from_user:
                    vk.messages.send(user_id=event.obj['message']['from_id'],
                                     message=f"Сегодняшний дежурный - {loh_detector(group_lst)}",
                                     random_id=random.randint(0, 2 ** 64))
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     message=f"Сегодняшний дежурный - {loh_detector(group_lst)}",
                                     random_id=random.randint(0, 2 ** 64))
            elif event.obj.message['text'].lower().startswith('кого в бан'):
                if event.from_user:
                    vk.messages.send(user_id=event.obj['message']['from_id'],
                                     message=f"Я думаю, что в бан полетит Слава Миленко",
                                     random_id=random.randint(0, 2 ** 64))
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     message=f"Я думаю, что в бан полетит Слава Миленко",
                                     random_id=random.randint(0, 2 ** 64))

group_lst = ["Слава Милый", "Руся Казачок", "Витюша", "Егорик Безмамный", "Серёжа Буйный", "Димочка-Душнилочка",
             "Даня Лолер", "Даша, которой надо перекраситься", "Даша Первая", "Дарья Яблочная Собака", "Яша Лава",
             "Родя Клоун", "Оляяяяяя", "Карина Лес Ив", "Маша, но вряд ли она пришла", "Тёмыч", "Слава Бездельник",
             "Саша пальцем в небо - в корабелку", "Илья просто работяга"]

if __name__ == '__main__':
    main()


