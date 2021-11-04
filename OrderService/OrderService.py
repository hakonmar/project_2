from sender import sender


class OrderService():
    def __init__(self) -> None:
        self.sender = sender

    # Place a order:
    #Order validation
    def place_order(self, request: dict):
        id = self.order_validation(request)
        if id>=0:
            self.send_event(request, id)


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


    def send_event(self, request, order_id):
        pass


    def  save_order(self, request:dict) -> int:
        db_file = open("OrderData.txt", "a+")
        id = 1
        for _ in db_file:
            id+=1
        db_file.write("{},{},{},{},{},{},{},{},{}".format(id, request["productID"], request["merchantID"], request["buyerID"], request["creditCard"]["cardNumber"], request["creditCard"]["expirationMonth"], request["creditCard"]["expirationYear"], request["creditCard"]["cvc"], request["discount"]))
        db_file.close()
        return id


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

