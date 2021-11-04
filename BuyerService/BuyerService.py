

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

    def new_buyer(self, name, email):
        id = self.next_id
        self.next_id += 1
