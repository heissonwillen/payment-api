import requests

requests.post(
    "http://127.0.0.1:5000/ProcessPayment",
    data = {
        "CreditCardNumber": "CreditCardNumber",
        "CardHolder": "CardHolder",
        "ExpirationDate": "ExpirationDate",
        "SecurityCode": "SecurityCode",
        "Amount": "Amount",
    }
)
