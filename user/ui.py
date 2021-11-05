from User import User
def main():
    user = User()
    print('Options:\n1 post new order\n2 Get Product info\n3 Get Buyer info\n4 Get Merchant info\n5 Get Order info')
    choice = input('What do you want to do? (1,2,3,4): ')
    if choice == '1':
        request_str = get_request(['product id (int)', 'merchant id (int)', 'buyer id (int)', 'card number (XXXX XXXX XXXX XXXX)', 'expiration month (0<int<=12)', 'expiration year (XXXX)', 'cvc (XXX)', 'discount (0<=float<=1)'])
        id = user.post_order(request_str)
        print(id)
    elif choice == '2':
        id = input('Enter id: ')
        print(user.get_product_info(id))
    elif choice == '3':
        id = input('Enter id: ')
        print(user.get_buyer_info(id))
    elif choice == '4':
        id = input('Enter id: ')
        print(user.get_merchant_info(id))


def get_request(header_list):
    return_string = ''
    for header in header_list:
        value = input('Enter your {} please: '.format(header))
        return_string+=value+';'
    return_string = return_string[:-1]
    return return_string




if __name__ == '__main__':
    main()