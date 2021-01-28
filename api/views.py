from flask import Blueprint, request, abort, jsonify
from flask.views import MethodView

from .utils import card_data_is_valid

blueprint = Blueprint("views", __name__, url_prefix="/")


class ProcessPaymentView(MethodView):
    def post(self):
        card_data = request.form
        if card_data_is_valid(card_data):
            try:    
                print("Payment processed")
                return {"Status code": "200"}, 200
                # Make payment
            except:
                # Internal server error
                abort(500)
        else:
            abort(400)


process_payment = ProcessPaymentView.as_view('process_payment')
blueprint.add_url_rule("ProcessPayment", view_func=process_payment, methods=['POST'])
