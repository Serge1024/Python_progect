from clicker import *
user_name = "Serge"
class Server():
    def __init__(self):
        self.data_base = dict()
    def put_contract(self, contract):
        game.my_bysnes[self.data_base[contract.bysnes_id_to][1]].get_offer(contract)
server = Server()
