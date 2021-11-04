from fanout import *

def paymentservice(order_id, credit_card_info):
    fanout = fanout()
    payment_result=payment_check(credit_card_info)
    string = f"{order_id};{payment_result}"
    fanout.call(string)

def payment_check(credit_card_info):
    credit_card_info = credit_card_info.split(";")
    if luhn_check(credit_card_info[0])==True:
        if month_check(credit_card_info[1])==True:
            if year_check(credit_card_info[2])==True:
                if cvc_check(credit_card_info[3])==True:
                    return True
    return False




def luhn_check(number):
    if number.isdigit():
        last_digit = int(str(number)[-1])
        reverse_sequence = list(int(d) for d in str(int(number[-2::-1])))

        for i in range(0, len(reverse_sequence), 2):
            reverse_sequence[i] *= 2

        for i in range(len(reverse_sequence)):
            if reverse_sequence[i] > 9:
                reverse_sequence[i] -= 9

        sum_of_digits = 0
        for i in range(len(reverse_sequence)):
            sum_of_digits += reverse_sequence[i]

        result = divmod(sum_of_digits, 10)

        if result != last_digit:
            return False
        return True

    return False

def month_check(number):
    if number<13 and number>0:
        return True
    return False

def year_check(number):
    if len(number)==4 and number.isdigit():
        return True
    return False

def cvc_check(number):
    if len(number)==3 and number.isdigit():
        return True
    return False

