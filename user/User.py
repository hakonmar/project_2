from sender import sender

class User():
    def __init__(self) -> None:
        self.sender = sender()
    def post_order(self, req_str):
        return sender.call(req_str, 'rpc_queue_post_order')

    def get_buyer_info(self, id):
        return sender.call((id, 'rpc_queue_post_order'))

    def get_merchant_info(self, id):
        return sender.call(id, 'rpc_queue_email_merch')

    def get_product_info(self, id):
        return sender.call(id, 'rpc_queue_prod_info') 

