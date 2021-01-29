class BasePaymentGateway:
	def __init__(self):
		self.gateway = None
		
	def __repr__(self):
		return self.gateway
	
	def connect(self):
		return True
	
	def pay(self, amount, gateway=None):
		if gateway is None:
			gateway = self.gateway

		if not self.connect():
			return False

		return True

class PremiumPaymentGateway(BasePaymentGateway):
	def __init__(self):
		self.gateway = "PremiumBasePaymentGateway"
	
class ExpensivePaymentGateway(BasePaymentGateway):
	def __init__(self):
		self.gateway = "ExpensiveBasePaymentGateway"
	
class CheapPaymentGateway(BasePaymentGateway):
	def __init__(self):
		self.gateway = "CheapBasePaymentGateway"
	
class ExternalPayment:
	def __init__(self, amount, card_details=None):
		self.amount = amount
		self.card_details = card_details
	
	def make_payment(self):
		payment_succefully = False

		if self.amount < 20:
			gateway = CheapPaymentGateway()
			payment_succefully = gateway.pay()
		elif 21 <= self.amount < 500:
			gateway = ExpensivePaymentGateway()
			payment_succefully = gateway.pay()
			if not payment_succefully:
				gateway = CheapPaymentGateway()
				payment_succefully = gateway.pay()
		elif self.amount > 500:
			gateway = PremiumPaymentGateway()
			for _ in range(3):
				payment_succefully = gateway.pay()
				if payment_succefully:
					return True

		if not payment_succefully:
			raise Exception("Payment not processed")
		
		return True