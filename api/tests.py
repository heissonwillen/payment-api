import requests
import pytest
import json

from config import FLASK_RUN_HOST, FLASK_RUN_PORT

URL = f"http://{FLASK_RUN_HOST}:{FLASK_RUN_PORT}/ProcessPayment"

# requests.post(
#     "http://127.0.0.1:5000/ProcessPayment",
#     data={
#         "CreditCardNumber": "CreditCardNumber",
#         "CardHolder": "CardHolder",
#         "ExpirationDate": "ExpirationDate",
#         "SecurityCode": "SecurityCode",
#         "Amount": "Amount",
#     }
# )


def test_invalid_request_type():
    response = requests.get(URL)
    assert 400 <= response.status_code < 500


def test_invalid_payment_data():
    response_1 = requests.post(URL,    
        data={
            "CreditCardNumber": "401333306731172993",
            "CardHolder": "Celedor Chimaobim",
            "ExpirationDate": "08;2023",
            "SecurityCode": "209",
            "Amount": "600",
        })

    response_2 = requests.post(URL,    
        data={
            "CreditCardNumber": "4016098843694561",
            "CardHolder": "Davide Maciejewski",
            "ExpirationDate": "04-2029",
            "SecurityCode": "4987",
            "Amount": -200,
        })

    assert response_1.status_code == 400
    assert response_2.status_code == 400


def test_blank_payment_data():
    response = requests.post(URL, data={})
    assert response.status_code == 400


def test_valid_payment_data():
    response_1 = requests.post(URL,    
        data={
            "CreditCardNumber": "4013306731172993",
            "CardHolder": "Celedor Chimaobim",
            "ExpirationDate": "08-2023",
            "SecurityCode": "209",
            "Amount": "600",
        })

    response_2 = requests.post(URL,    
        data={
            "CreditCardNumber": "4016098843694561",
            "CardHolder": "Davide Maciejewski",
            "ExpirationDate": "04-2029",
            "SecurityCode": "487",
            "Amount": "877",
        })

    assert response_1.status_code == 200
    assert response_2.status_code == 200


def test_invalid_expiration_date():
    response_1 = requests.post(URL,    
        data={
            "CreditCardNumber": "4013306731172993",
            "CardHolder": "Celedor Chimaobim",
            "ExpirationDate": "08-2020",
            "SecurityCode": "209",
            "Amount": "600",
        })

    response_2 = requests.post(URL,    
        data={
            "CreditCardNumber": "4016098843694561",
            "CardHolder": "Davide Maciejewski",
            "ExpirationDate": "04/2029",
            "SecurityCode": "487",
            "Amount": "877",
        })

    assert response_1.status_code == 400
    assert response_2.status_code == 400


def test_security_code():
    pass


test_invalid_request_type()
test_invalid_payment_data()
test_blank_payment_data()
test_valid_payment_data()
test_invalid_expiration_date()
test_security_code()