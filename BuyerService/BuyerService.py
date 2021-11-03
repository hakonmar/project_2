

class BuyerService():
    def __init__(self) -> None:
        self.db_file = open("BuyerData.txt", "r+")
        self.next_id = 1
        for _ in self.db_file:
            self.next_id += 1
    
    def check_id(self, id) -> bool:
        if self.next_id< id:
            True
        else:
            False