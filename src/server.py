import base_constants 
user_name = "Serge"
class Server():
    def __init__(self):
        self.data_base = dict()
    def put_contract(self, contract):
        import clicker
        clicker.game.my_bysnes[self.data_base[contract.bysnes_id_to][1]].get_offer(contract)
    def send_ans(self, ans):
        if (ans.bysnes_id_to == 0):
            return
        import clicker
        clicker.game.my_bysnes[self.data_base[ans.bysnes_id_to][1]].sclad[ans.name] += ans.count
        clicker.game.dollar_score += ans.money
global server
server = Server()
