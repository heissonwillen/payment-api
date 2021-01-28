from credit_card_checker import CreditCardChecker
from datetime import datetime


def card_data_is_valid(card):
    print(card)

    card_number = card.get("CreditCardNumber")
    if (card_number is None) or (not CreditCardChecker(str(card_number)).valid()):
        print("Invalid card number")
        return False

    card_holder = card.get("CardHolder")
    if card_holder is None:
        print("Invalid card holder")
        return False

    expiration_date = card.get("ExpirationDate")
    if expiration_date is None:
        print("Invalid expiration date")
        return False
    else:
        try:
            if datetime.strptime(expiration_date, "%m-%Y") < datetime.now():
                print("Expiration date is in the past")
                return False
        except ValueError:
            print("Wrong expiration date format")
            return False

    security_code = card.get("SecurityCode")
    if (not security_code is None) and len(security_code) != 3:
        print("Invalid security code")
        return False

    amount = card.get("Amount")
    if amount is None:
        print("Invalid amount")
        return False
    else:
        try:
            if float(amount) < 0:
                print("Amount is negative")
                return False
        except ValueError:
            print("Amount could not be converted to a number")
            return False

    print("Valid credit card info")
    return True
