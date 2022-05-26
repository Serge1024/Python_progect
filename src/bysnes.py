import base_constants as b


class Bysnes:
    def __init__(self, name, price, recept, is_potreb, main_product, cost_of_work):
        self.cost_of_work = cost_of_work
        self.rub_score = 0
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

    def add_rub(self, count_of_rub):
        self.rub_score += count_of_rub

    def add_worker(self):
        self.work_resurce += 1

    def normal(self):
        flag = True
        for i in LIST_OF_MATIRIAL:
            flag = flag and (self.sclad[i] >= self.recept.ingredient[i])
        return flag and (self.rub_score >= self.cost_of_work)

    def work(self):
        count_of_make_iteration = 0
        for i in range(self.work_resurce):
            if (self.normal()):
                count_of_make_iteration += 1
                for i in LIST_OF_MATIRIAL:
                    self.sclad[i] -= self.recept.ingredient[i]
                    self.sclad[i] += self.recept.result[i]
                self.rub_score -= self.cost_of_work
        self.work_resurce = count_of_make_iteration

    def get_offer(self, contract):
        self.offer.append(contract)

    def say_yes(self):
        if (self.sclad[self.offer[0].name] >= self.offer[0].count):
            self.sclad[self.offer[0].name] -= self.offer[0].count
            ans = self.offer[0]
            self.offer.pop(0)
            if(self.is_potreb and self.work_resurce > 0):
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

def from_offer_to_string(offer):
    ans = '0*' +str(offer.bysnes_id_to) + "*"+str(offer.bysnes_id_from) + "*" + offer.name + "*" + str(offer.count) + "*" + str(offer.cost)
    return ans
def from_ans_to_string(ans):
    ans = "1*" + str(ans.bysnes_id_to) + "*" + str(ans.money)+ "*" + ans.name + "*" + str(ans.count)
    return ans
def from_string_to_obgect(string):
    my_list = string.split("*")
    if (my_list[0] == '0'):
        return Contract(my_list[2], my_list[1],  my_list[3], my_list[4], my_list[5])
    else:
        return Answer(my_list[1], my_list[2],  my_list[3], my_list[4])
