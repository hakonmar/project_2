


class MerchantService():
    def __init__(self) -> None:
        db_file_obj = open("MerchantData.txt", "r+")
        self.db_file = db_file_obj.readlines()
        db_file_obj.close()
        self.next_id = 1
        for _ in self.db_file:
            self.next_id += 1
    
    def check_id(self, id) -> bool:
        if self.next_id< id:
            True
        else:
            False

    def check_discount(self, id:int, discount:float):
        for line in self.db_file:
            line_split = line.split(';')
            if line_split[0] == id:
                if float(line_split[1]) >= discount:
                    return True
                else:
                    return False
    
    def get_merch_info(self, id):
        for line in self.db_file:
            line_split = line.split(';')
            if int(line_split[0]) == id:
                return line