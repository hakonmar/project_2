


class InventoryService():
    def __init__(self) -> None:
        self.db_file = open("InverntoryData.txt", "r+")
        self.next_id = 1
        for _ in self.db_file:
            self.next_id += 1
    
    def check_id(self, id) -> bool:
        if self.next_id< id & id>=0:
            True
        else:
            False
    
    def check_sold_out(self, id) -> bool:
        self.db_file = open('InventoryData.txt', 'r+')
        for line in self.db_file:
            line_split = line.split(';')
            if line_split[0] == id:
                amount =int( line_split[1])
                if amount>0:
                    return True
                else:
                    return False



