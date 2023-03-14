import collections
import itertools
from operator import itemgetter


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


def generator_new_list(a: list) -> list:
    newList = []
    dictCards = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "J": 10, "Q": 11, "K": 12,
                 "A": 13}
    for i in a:
        rangCard = i[:-1]
        suitСard = i[-1]
        valueСard = dictCards.get(rangCard)
        cardWithValue = (rangCard, suitСard, valueСard)
        newList.append(cardWithValue)
    return newList


def check_combinations(a: list):
    cardsWithValues = generator_new_list(a)
    if not royal_flush(cardsWithValues):
        if not straight_flush(cardsWithValues):
            if not four_of_a_kind(cardsWithValues):
                if not full_house(cardsWithValues):
                    if not flash(cardsWithValues):
                        if not straight(cardsWithValues):
                            if not three_of_a_kind(cardsWithValues):
                                if not pair(cardsWithValues):
                                    high_card(cardsWithValues)


# card = (input("Введите карты, через пробел:\n")).split()
card = ['KH', '5S', 'QH', '2S', 'AH', 'JH', '10H']

check_combinations(card)
