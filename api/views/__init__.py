from flask import Blueprint, request, abort, Response
from flask.views import MethodView

from api.utils import card_data_is_valid
from api.services import ExternalPayment

blueprint = Blueprint("views", __name__, url_prefix="/")


class ProcessPaymentView(MethodView):
    def post(self):
        card_data = request.form
        if card_data_is_valid(card_data):
            try:    
                amount = float(card_data["Amount"])
                payment = ExternalPayment(amount)
                payment.make_payment()
                return Response({"Payment status": "Succefully processed"}, status=200)
            except:
                abort(500)
        else:
            abort(400)


process_payment = ProcessPaymentView.as_view('process_payment')
blueprint.add_url_rule("ProcessPayment", view_func=process_payment, methods=['POST'])
