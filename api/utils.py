from credit_card_checker import CreditCardChecker
from datetime import datetime


def card_data_is_valid(card):
    card_number = card.get("CreditCardNumber")
    if (card_number is None) or (not CreditCardChecker(str(card_number)).valid()):
        return False

    card_holder = card.get("CardHolder")
    if card_holder is None:
        return False

    expiration_date = card.get("ExpirationDate")
    if expiration_date is None:
        return False
    else:
        try:
            if datetime.strptime(expiration_date, "%Y-%m-%d") < datetime.now():
                return False
        except ValueError:
            return False

    security_code = card.get("SecurityCode")
    if (not security_code is None) and len(security_code) == 3:
        return False

    amount = card.get("Amount")
    if amount is None:
        return False
    else:
        try:
            if int(amount) < 0:
                return False
        except ValueError:
            return False

    return True
