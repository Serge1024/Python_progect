from base_constants import *


class Bysnes:
    def __init__(self, name, price, recept, is_potreb, main_product):
        self.name = name
        self.price = price
        self.recept = recept
        self.is_potreb = is_potreb
        self.main_product = main_product
        self.sclad = dict()
        for i in LIST_OF_MATIRIAL:
            self.sclad[i] = 0
        self.work_resurce = 1
        self.bysnes_id = 0
        self.offer = list()
        if (is_potreb):
            self.offer.append(Contract(0, self.bysnes_id, self.main_product, self.work_resurce * 10, self.work_resurce * 10 * DICT_OF_COST_OF_MATERIAL[self.main_product]))


    def normal(self):
        flag = True
        for i in LIST_OF_MATIRIAL:
            flag = flag and (self.sclad[i] >= self.recept.ingredient[i])
        return flag

    def work(self):
        for i in range(self.work_resurce):
            if (self.normal()):
                for i in LIST_OF_MATIRIAL:
                    self.sclad[i] -= self.recept.ingredient[i]
                    self.sclad[i] += self.recept.result[i]

    def get_offer(self, contract):
        self.offer.append(contract)

    def say_yes(self):
        if (self.sclad[self.offer[0].name] >= self.offer[0].count):
            self.sclad[self.offer[0].name] -= self.offer[0].count
            ans = self.offer[0]
            self.offer.pop(0)
            if(self.is_potreb):
                self.offer.append(Contract(0, self.bysnes_id, self.main_product, self.work_resurce * 10, self.work_resurce * 10 * DICT_OF_COST_OF_MATERIAL[self.main_product]))
            return ans.cost, Answer(ans.bysnes_id_from, 0, ans.name, ans.count)
        return 0, 0
    def say_no(self):
        ans = self.offer[0]
        self.offer.pop(0)
        return Answer(ans.bysnes_id_from, ans.cost, ans.name, 0)


class Recept:
    def __init__(self, ingredient, result):
        self.ingredient = ingredient
        self.result = result

class Contract:
    def __init__(self, bysnes_id_from, bysnes_id_to, name, count, cost):
        self.bysnes_id_from = bysnes_id_from
        self.bysnes_id_to = bysnes_id_to
        self.name = name
        self.count = count
        self.cost = cost
class Answer:
    def __init__(self, bysnes_id_to, money, name, count):
        self.bysnes_id_to = bysnes_id_to
        self.money = money
        self.name = name
        self.count = count
