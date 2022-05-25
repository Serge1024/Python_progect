from base_constants import *
class Bysnes:
    def __init__(self, name, price, recept):
        self.name = name
        self.price = price
        self.recept = recept
        self.sclad = dict()
        for i in LIST_OF_MATIRIAL:
            self.sclad[i] = 0
        self.work_resurce = 1
        self.bysnes_id = 0
        self.offer = list()

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
            ans = self.offer[0].cost
            self.offer.pop(0)
            return ans
        return 0
    def say_no(self):
        self.offer.pop(0)


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
