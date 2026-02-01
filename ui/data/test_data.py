from random import choices
from string import ascii_letters, ascii_lowercase, digits, punctuation


class RegistrationData:
    def __init__(
            self,
            name_length=10,
            email_suffix='@mail.com',
            password_length=15,
    ):
        punct = punctuation.replace('\\', '').replace('"', '').replace("'", '')
        self.name = ''.join(choices(ascii_lowercase, k=1) + choices(
            ascii_lowercase + digits, k=name_length))
        self.email = self.name + email_suffix
        self.password = ''.join(choices(
            ascii_letters + digits + punct, k=password_length))


class Burger:
    bun = [
        {'name': 'Флюоресцентная булка R2-D3', 'price': 988},
        {'name': 'Краторная булка N-200i', 'price': 1255}
    ]
    sauce = [
        {'name': 'Соус Spicy-X', 'price': 90},
        {'name': 'Соус фирменный Space Sauce', 'price': 80},
        {'name': 'Соус традиционный галактический', 'price': 15},
        {'name': 'Соус с шипами Антарианского плоскоходца', 'price': 88}
    ]
    filling = [
        {'name': 'Мясо бессмертных моллюсков Protostomia', 'price': 1337},
        {'name': 'Говяжий метеорит (отбивная)', 'price': 3000},
        {'name': 'Биокотлета из марсианской Магнолии', 'price': 424},
        {'name': 'Филе Люминесцентного тетраодонтимформа', 'price': 988},
        {'name': 'Хрустящие минеральные кольца', 'price': 300},
        {'name': 'Плоды Фалленианского дерева', 'price': 874},
        {'name': 'Кристаллы марсианских альфа-сахаридов', 'price': 762},
        {'name': 'Мини-салат Экзо-Плантаго', 'price': 4400},
        {'name': 'Сыр с астероидной плесенью', 'price': 4142}
    ]


class TestData:
    burger = [
        Burger.bun[1]['name'],
        Burger.sauce[2]['name'],
        Burger.filling[2]['name']
    ]
