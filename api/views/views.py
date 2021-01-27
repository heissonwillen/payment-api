from flask import Blueprint, request, abort, jsonify

blueprint = Blueprint("views", __name__, url_prefix="/")

@blueprint.route("ProcessPayment", methods=["POST"])
def process_payment():
	print("processing")
	abort(404)