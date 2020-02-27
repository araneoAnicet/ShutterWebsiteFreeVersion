from flask import Blueprint, jsonify

mod = Blueprint('api', __name__)

@mod.route('/get_hello_world')
def get_hello_world():
    return jsonify(
        {
            'message': 'hello world!'
        }
    )