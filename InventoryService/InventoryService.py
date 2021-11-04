


from io import SEEK_CUR


class InventoryService():
    def __init__(self) -> None:
        db_file_obj = open("InverntoryData.txt", "r+")
        self.db_file = db_file_obj.readlines()
        db_file_obj.close()
        self.next_id = 1
        for _ in self.db_file:
            self.next_id += 1
    
    def check_id(self, id:int) -> bool:
        if self.next_id< id & id>=0:
            True
        else:
            False
    
    def check_sold_out(self, id:int) -> bool:
        for line in self.db_file:
            line_split = line.split(';')
            if int(line_split[0]) == id:
                amount =int( line_split[1])
                if amount>0:
                    return True
                else:
                    return False
    
    def check_merchant(self, id:int, merchid:int) -> bool:
        for line in self.db_file:
            line_split = line.split(';')
            if int(line_split[0]) == id:
                if line_split[2] == merchid:
                    return True
                else:
                    return False
    
    def get_prod_info(self, id:int) -> str:
        for line in self.db_file:
            line_split = line.split(';')
            if int(line_split[0]) == id:
                return line

    def restock(self, id, amount):
        """Add the amount to the current stock of the product with the id"""
        line = self.db_file[id-1]
        line_split = line.split(';')
        new_amount = int(line_split[1]) + int(amount)
        line_split[1] = new_amount
        line = ';'.join(line_split)
        self.db_file[id-1] = line
        db_file_obj = open('InventoryData.txt', 'w')
        db_file_obj.writelines(self.db_file)
        self.db_file = db_file_obj.readline()
        db_file_obj.close()

    def new_prod(self, id, amount, merchantid, reserved_amount):
        self.db_file.append('\n{};{};{};{};{}'.format(id, amount, merchantid, reserved_amount))
        db_file_obj = open('InventoryData.txt', 'w')
        db_file_obj.writelines(self.db_file)
        self.db_file = db_file_obj.readline()
        db_file_obj.close()

    def reserve_product(self, id):
        pass



