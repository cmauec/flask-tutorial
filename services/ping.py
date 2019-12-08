import json
from flask import Blueprint, jsonify

service_ping = Blueprint('service_ping', __name__)


@service_ping.route('/ping', methods=['GET'])
def ping():
    return jsonify(
        {
            'message': 'pong'
        }
    )
