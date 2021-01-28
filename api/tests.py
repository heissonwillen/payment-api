import requests
import pytest
import json

from .config import FLASK_RUN_HOST, FLASK_RUN_PORT

url = "http://{}:{}".format(FLASK_RUN_HOST, FLASK_RUN_PORT)


requests.post(
    "http://127.0.0.1:5000/ProcessPayment",
    data={
        "CreditCardNumber": "CreditCardNumber",
        "CardHolder": "CardHolder",
        "ExpirationDate": "ExpirationDate",
        "SecurityCode": "SecurityCode",
        "Amount": "Amount",
    }
)


def test_invalid_request_type():
    pass


def test_invalid_payment_data():
    pass


def test_no_payment_data():
    pass


def test_valid_payment_data():
    pass


def test_invalid_expiration_date():
    pass


def test_security_code():
    pass
