

class BuyerService():
    def __init__(self) -> None:
        db_file_obj = open("BuyerData.txt", "r+")
        self.db_file
        self.next_id = 1
        for _ in self.db_file:
            self.next_id += 1
    
    def check_id(self, id) -> bool:
        if self.next_id< id:
            True
        else:
            False

    def get_merchant_email(self, id):
        for line in self.db_file:
            if line[0]==id:
                return line[4] #If column 5 holds email information
                
    def new_buyer(self, name, email):
        id = self.next_id
        self.next_id += 1

    def get_buyer_info(self, id) -> str:
        for line in self.db_file:
            line_split = line.split(';')
            if int(line_split[0]) == id:
                return line
