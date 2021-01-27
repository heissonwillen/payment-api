from flask import Blueprint, request, abort, jsonify

blueprint = Blueprint("views", __name__, url_prefix="/")
