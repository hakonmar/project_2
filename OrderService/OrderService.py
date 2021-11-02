import rabbitmq

class OrderService():
    # Place a order:
    #Order validation
    def place_order(self, request: dict):
        if self.order_validation(request):
            pass






    def order_validation(self, request: dict):
        if self.merchant_checker(request["merchantID"]):
            if self.buyer_checker(request["buyerID"]):
                if self.product_checker(request["productID"]):
                    if self.sold_out_checker(request["productID"]):
                        if self.merchant_has_product_checker(request["productID"], request["merchantID"]):
                            if self.discount_checker(request["discount"]):
                                # return 201 status code with id
                                return True
                            else:
                                # return 400 HTTP Status Code with "Merchant does not allow discount"
                                return False
                        else:
                            #return 400 HTTP Status Code with "Product does not belong to merchant"
                            return False
                    else:
                        #Return  400 HTTP Status Code with "Product is sold out"
                        return False
                else:
                    #Return  400 HTTP Status Code with "Product does not exist"
                    return False
            else:
                #Return  400 HTTP Status Code with "Buyer does not exist"
                return False
        else:
            #Return  400 HTTP Status Code with "Merchant does not exist"
            return False



    def merchant_checker(self, id) -> bool:
        pass

    def buyer_checker(self, id) -> bool:
        pass

    def product_checker(self, id) -> bool:
        pass

    def sold_out_checker(self, id)  -> bool:
        pass

    def merchant_has_product_checker(self, prodid, merchid)  -> bool:
        pass

    def discount_checker(self, id) -> bool:
        pass

