from sender import sender
from fanout import *

class OrderService():
    def __init__(self) -> None:
        self.sender = sender

    # Place a order:
    #Order validation
    def place_order(self, request: dict):
        id = self.order_validation(request)

        string = []
        string.append(str(id))
        string.append(request["productID"])
        string.append(request["merchantID"])
        string.append(request["buyerID"])
        string.append(request["creditCard"]["cardNumber"])
        string.append(request["creditCard"]["expirationMonth"])
        string.append(request["creditCard"]["expirationYear"])
        string.append(request["creditCard"]["cvc"])
        string.append(request["discount"])

        prod_info = get_prod_info(request["productID"])
        prod_info.split(";")
        prod_price = prod_info[4]
        prod_name = prod_info[5]
        string.append(prod_name)
        total_price = float(prod_price)*float(request["discount"])
        total_price=str(total_price)
        string.append(total_price)

        buyer_email = get_email_buyer
        string.append(buyer_email)

        merchant_email = get_email_merchant
        string.append(merchant_email)

        string.join(";")
        if id>=0:
            self.send_event(string)


    def order_validation(self, request: dict):
        if self.merchant_checker(request["merchantID"]):
            if self.buyer_checker(request["buyerID"]):
                if self.product_checker(request["productID"]):
                    if self.sold_out_checker(request["productID"]):
                        if self.merchant_has_product_checker(request["productID"], request["merchantID"]):
                            if self.discount_checker(request["merchantID"], request["discount"]):
                                # add order to txt file
                                order_id = self.save_order(request)
                                # return 201 status code with id
                                return order_id
                            else:
                                # return 400 HTTP Status Code with "Merchant does not allow discount"
                                
                                return -1
                        else:
                            #return 400 HTTP Status Code with "Product does not belong to merchant"
                            return -1
                    else:
                        #Return  400 HTTP Status Code with "Product is sold out"
                        return -1
                else:
                    #Return  400 HTTP Status Code with "Product does not exist"
                    return -1
            else:
                #Return  400 HTTP Status Code with "Buyer does not exist"
                return -1
        else:
            #Return  400 HTTP Status Code with "Merchant does not exist"
            return -1


    def send_event(self, string):
        fanout = fanout()
        fanout.call(string)


    def  save_order(self, request:dict) -> int:
        db_file = open("OrderData.txt", "a+")
        id = 1
        for _ in db_file:
            id+=1
        db_file.write("{};{};{};{};{};{};{};{};{}".format(id, request["productID"], request["merchantID"], request["buyerID"], request["creditCard"]["cardNumber"], request["creditCard"]["expirationMonth"], request["creditCard"]["expirationYear"], request["creditCard"]["cvc"], request["discount"]))
        db_file.close()
        return id


    def get_email_buyer(self, id) -> str:
        return sender.call(id, 'rpc_queue_email_buy').split(';')

    def get_email_merchant(self, id) -> str:
        return sender.call(id, 'rpc_queue_email_merch').split(';')

    def get_prod_info(self, id) -> list:
        return sender.call(id, 'rpc_queue_prod_info').split(';')


    def merchant_checker(self, id) -> bool:
        return bool(sender.call(id, 'rpc_queue_merch_check'))

    def buyer_checker(self, id) -> bool:
        return bool(sender.call(id, 'rpc_queue_buyer_check'))

    def product_checker(self, id) -> bool:
        return bool(sender.call(id, 'rpc_queue_product_check'))

    def sold_out_checker(self, id)  -> bool:
        return bool(sender.call(id, 'rpc_queue_sold_out_check'))

    def merchant_has_product_checker(self, prodid, merchid)  -> bool:
        check_str = str(prodid) + ';' + str(merchid)
        return bool(sender.call(check_str, 'rpc_queue_merch_prod_check'))

    def discount_checker(self, id, discount) -> bool:
        id_n_discount = str(id) + ';' + str(discount)
        return bool(sender.call(id_n_discount, 'rpc_queue_discount_check'))

