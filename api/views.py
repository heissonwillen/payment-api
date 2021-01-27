from flask import Blueprint, request, abort, jsonify
from flask.views import MethodView


blueprint = Blueprint("views", __name__, url_prefix="/")


class ProcessPaymentView(MethodView):
    def post(self):
        print("Processing payment")
        print(request.form["CreditCardNumber"])
        abort(404)


process_payment = ProcessPaymentView.as_view('process_payment')
blueprint.add_url_rule("ProcessPayment", view_func=process_payment, methods=['POST'])
