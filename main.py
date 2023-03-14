import collections
import itertools
from operator import itemgetter
from random import choice

def cards(a, b: tuple) -> dict:  # функция генерации колды со значениями карт
    cards = {}
    amount = len(a)
    for i in range(0, amount):
        for j in b:
            cards.update({(a[i] + j): (a[i], j, (i + 1))})
    return cards


def card_in_hands(a: dict) -> (list):  # Список карт на руках + сообщение на экран
    cardInHands = []
    message = ''
    for i in range(2):
        cardRandom = choice(list(a.keys()))  # Ключ случ карты
        message += str(cardRandom) + " "
        card = a[cardRandom]  # Значение случ карты
        cardInHands.append(card)
        a.pop(cardRandom)  # Удаляем карту из колоды
    print("На руках у вас: " + message)
    return cardInHands


def card_in_table(a: dict, n: int) -> (list, dict):  # Список карт на столе и колоду без них + сообщение на экран
    cardInTable = []
    message = ''
    for i in range(n):
        cardRandom = choice(list(a.keys()))  # Ключ случ карты
        message += str(cardRandom) + " "
        card = a[cardRandom]  # Значение случ карты
        cardInTable.append(card)
        a.pop(cardRandom)  # Удаляем карту из колоды
    print("На стол выпали карты: " + message)
    return cardInTable, a


def all_cards(CardOnTable: int) -> list:  # создание колоды, раздача карт)
    a = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    b = ("D", "H", "C", "S")
    cardDeck = cards(a, b)  # создание колоды
    cardOnTableAndCardDeck = card_in_table(cardDeck, CardOnTable)  # получаем карты на столе и оставш.колоду
    cardInTable = cardOnTableAndCardDeck[0]  # переменая карт на столе
    Card_decK = cardOnTableAndCardDeck[1]  # переменая оставшиеся колоды
    cardInHands = card_in_hands(Card_decK)  # получаем карты на руках
    allCards = cardInTable + cardInHands  # переменая всех открытых карт (номинал карты + масть + знчение)
    return allCards


def combinations(a: list, n: int) -> list:  # функция генерирует камбинации
    return list(itertools.combinations(a, n))


def message_of_card(a: list) -> str:
    sortCards = (sorted(a, key=itemgetter(2)))
    strFihish = ''
    for i in sortCards:
        strFihish += str(i[0]) + str(i[1]) + ' '
    return strFihish


def max_value(a: list) -> list:
    allCardWithSumValeus = []
    for i in a:
        sum = 0
        for j in i:
            sum += j[2]
        allValesCard = (sum, i)
        allCardWithSumValeus.append(allValesCard)
    maxCardValues = ((sorted(allCardWithSumValeus))[-1])[1]
    return maxCardValues


def max_valeu_straight(a: list) -> list:  # для нахождения большего стрита (отдельная функция так как A.2.3.4.5 - мин.)
    listStrit = []
    for i in a:
        sortCards = (sorted(i, key=itemgetter(2)))
        if sortCards[0][2] == 1 and sortCards[4][2] == 13:
            continue
        else:
            listStrit.append(sortCards)
    if len(listStrit) == 0:
        for i in a:
            sortCards = (sorted(i, key=itemgetter(2)))
            if sortCards[0][2] == 1 and sortCards[4][2] == 13:
                listStrit.append(sortCards)
    if len(listStrit) == 1:
        return listStrit[0]
    else:
        return max_value(listStrit)  # тут уже можем запустить обычную проверку на нахождения макс. комбинации


def check_four_of_a_kind(a: list) -> bool:
    if a[0][2] == a[1][2] == a[2][2] == a[3][2]:
        return True
    return False


def check_strit(a: list) -> bool:  # функция проверки комбинации на стрит (отправляем сюда 1 комбинацию из 5 карт)
    sortCards = (sorted(a, key=itemgetter(2)))  # cортируем пол карты по значению
    valeuStrit = []  # список только со значениями полученных карт
    for i in sortCards:
        valeuStrit.append(i[2])
    valueChek = []  # создаем список для проверки, берем 1 знач у полученых карт, и шагами +1
    valueChek.append(valeuStrit[0])
    for j in range(0, 4):
        valueChek.append(valueChek[j] + 1)
    if collections.Counter(valeuStrit) == collections.Counter(valueChek):  # если равны, то комбинация стрит
        return True
    valueChekSpecStrit = [13, 1, 2, 3, 4]
    if collections.Counter(valeuStrit) == collections.Counter(
            valueChekSpecStrit):  # сравниваем равны ли они, так находим стрит
        return True
    return False


def check_flush(a: list) -> bool:  # функция проверки комбинации на флеш
    if a[0][1] == a[1][1] == a[2][1] == a[3][1] == a[4][1]:
        return True
    return False


def check_flash_roial(a: list) -> bool:  # Проверяет стрит флеш на флеш рояль (если да - возвращет true
    valeuStrit = []  # список только со значениями полученных карт
    for i in a:
        valeuStrit.append(i[2])
    flashRoialList = [9, 10, 11, 12, 13]
    if collections.Counter(valeuStrit) == collections.Counter(flashRoialList):  # сравниваем значения
        return True


def check_full_house(a: list) -> bool:
    a = (sorted(a, key=itemgetter(2)))
    if (a[0][2]) == (a[1][2]) == (a[2][2]) and (a[3][2]) == (a[4][2]) or (a[4][2]) == (a[3][2]) == (a[2][2]) and (
            a[1][2]) == (a[0][2]):
        return True
    return False


def check_three_of_a_Kind(a: list) -> (bool):
    if a[0][2] == a[1][2] == a[2][2]:
        return True
    return False


def checkPair(a: list) -> (bool):
    if a[0][2] == a[1][2]:
        return True
    return False


def royal_flush(a: list) -> (str, bool):
    if len(a) < 5:
        return False
    listCombinations = combinations(a, 5)
    for i in listCombinations:  # перебираем список всех комбинаций
        if check_flush(i):  # На флеш
            if check_flash_roial(i):  # На флеш роял, только флеш
                print('У вас Royal Flush: ' + message_of_card(i))
                return True
    return False


def straight_flush(a: list) -> (str, bool):
    if len(a) < 5:
        return False
    listCombinations = combinations(a, 5)
    listStraightFlush = []
    for i in listCombinations:  # перебираем список всех комбинаций
        if check_flush(i):  # На флеш
            if check_strit(i):  # На стрит
                listStraightFlush.append(i)  # Добавляем найденные значения в список
    if len(listStraightFlush) == 0:
        return False
    else:
        maxStraightFlush = max_valeu_straight(listStraightFlush)
        print('У вас Straight Flush: ' + message_of_card(maxStraightFlush))
        return True


def four_of_a_kind(a: list) -> (str, bool):
    if len(a) < 4:
        return False
    listCombinations = combinations(a, 4)
    for i in listCombinations:
        if check_four_of_a_kind(i):
            print('У вас Four of a Kind: ' + message_of_card(i))
            return True
    return False


def full_house(a: list) -> (str, bool):
    if len(a) < 5:
        return False
    listFullHouse = []
    listCombinations = combinations(a, 5)
    for i in listCombinations:
        if check_full_house(i):
            listFullHouse.append(i)
    if len(listFullHouse) == 0:
        return False
    else:
        maxFullHouse = max_value(listFullHouse)
        print('У вас Full House: ' + message_of_card(maxFullHouse))
        return True


def flash(a: list) -> (str, bool):
    if len(a) < 5:
        return False
    listFullFlash = []
    listCombinations = combinations(a, 5)
    for i in listCombinations:
        if check_flush(i):
            listFullFlash.append(i)
    if len(listFullFlash) == 0:
        return False
    else:
        maxFullFlash = max_value(listFullFlash)
        print('У вас Flash: ' + message_of_card(maxFullFlash))
        return True


def straight(a: list) -> (str, bool):
    if len(a) < 5:
        return False
    listFullStraight = []
    listCombinations = combinations(a, 5)
    for i in listCombinations:
        if check_strit(i):
            listFullStraight.append(i)
    if len(listFullStraight) == 0:
        return False
    else:
        maxFullSraight = max_valeu_straight(listFullStraight)
        print('У вас Straight: ' + message_of_card(maxFullSraight))
        return True


def three_of_a_kind(a: list) -> (str, bool):
    if len(a) < 3:
        return False
    listCombinations = combinations(a, 3)
    for i in listCombinations:
        if check_three_of_a_Kind(i):
            print('У вас Three of a Kind: ' + message_of_card(i))
            return True
    return False


def pair(a: list) -> (str, bool):
    if len(a) < 2:
        return False
    listFullPair = []
    listCombinations = combinations(a, 2)
    for i in listCombinations:
        if checkPair(i):
            listFullPair.append(i)
    if len(listFullPair) == 0:
        return False
    elif len(listFullPair) == 1:
        print('У вас Pair : ' + message_of_card(listFullPair[0]))
        return True
    else:
        maxPara = (sorted(listFullPair, key=itemgetter(0)))
        maxPara = maxPara[-2], maxPara[-1]
        strFihish = 'У вас Two Pair: '
        for i in maxPara:
            strFihish += str(i[0][0]) + str(i[0][1]) + ' ' + str(i[1][0]) + str(i[1][1]) + ' '
        print(strFihish)
        return True


def high_card(a: list):
    a = (sorted(a, key=itemgetter(2)))
    maxCard = a[-1]
    print('У вас Кикер: ' + str(maxCard[0]) + str(maxCard[1]))


def check_combinations(a: list):
    if not royal_flush(a):
        if not straight_flush(a):
            if not four_of_a_kind(a):
                if not full_house(a):
                    if not flash(a):
                        if not straight(a):
                            if not three_of_a_kind(a):
                                if not pair(a):
                                    high_card(a)

"""
Для тестирования закомитить генерацию колоды и выпадения карт - allCards = all_cards(5)
В функцию передать список имеющий вид:
    allCards = [('2', 'D', 1), ('3', 'D', 2), ('4', 'D', 3), ('5', 'D', 4), ('6', 'D', 5), ('7', 'D', 6), ('8', 'D', 7)] 
ОБОЗНАЧЕНИЯ ('2', 'D', 1) <- 2 -обозначение карты , D - масть карты, 1 - значение (2-1.....A-13)

В Кикере передается большая карта из всех!

Масти: D - Diamonds / H- Hearts / C -Clubs / S Spades
"""

# test = [[('2', 'D', 1), ('3', 'D', 2), ('4', 'D', 3), ('5', 'D', 4), ('6', 'D', 5), ('7', 'D', 6), ('8', 'D', 7)], #Стрит Флеш 8-4 (тут 3 стрит флеша)
#         [('2', 'H', 1), ('A', 'H', 13), ('2', 'D', 1), ('3', 'H', 2), ('4', 'K', 3), ('5', 'D', 4), ('K', 'C', 12)], #Cтрит где туз первый
#         [('10', 'S', 9), ('10', 'C', 9), ('10', 'D', 9), ('J', 'D', 10), ('Q', 'D', 11), ('K', 'D', 12), ('A', 'D', 13)], #флеш рояль (тут еще тройка 10)
#         [('2', 'D', 1), ('K', 'D', 12), ('4', 'D', 3), ('J', 'D', 10), ('6', 'D', 5), ('7', 'D', 6), ('2', 'S', 1)], #Флеш от 4 (есть еще один от 2)
#         [('2', 'D', 1), ('8', 'D', 7), ('4', 'H', 3), ('2', 'C', 1), ('6', 'S', 5), ('7', 'H', 6), ('J', 'D', 10)], #Пара двоек
#         [('10', 'S', 9), ('10', 'C', 9), ('10', 'D', 9), ('J', 'D', 10), ('J', 'H', 10), ('J', 'S', 10), ('A', 'D', 13)], #фул хаус 1010jjj (сть еще 3-10 2-j)
#         [('J', 'D', 10), ('J', 'H', 10), ('J', 'S', 10), ('J', 'C', 10), ('6', 'D', 5), ('7', 'D', 6), ('8', 'D', 7)],   #Каре на вальтах
#         [('J', 'D', 10), ('J', 'H', 10), ('J', 'S', 10), ('3', 'C', 2), ('7', 'D', 6), ('2', 'H', 1), ('8', 'D', 7)],   #Тролька вальтов
#         [('J', 'D', 10), ('J', 'H', 10), ('A', 'S', 13), ('A', 'C', 13), ('2', 'D', 1), ('2', 'H', 1), ('8', 'D', 7)], #2 ары AJ (есть еще комбинация 2х пар)
#         [('4', 'D', 3), ('3', 'H', 2), ('7', 'S', 6), ('J', 'C', 10), ('2', 'D', 1), ('Q', 'H', 12), ('8', 'D', 7)]] #rикер Q
#
# for i in test:
#     check_combinations(i)

allCards = all_cards(5)  # Колличество карт на столе, 2 карты на руках будут всегда
check_combinations(allCards)

