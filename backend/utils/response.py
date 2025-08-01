from flask import jsonify

def success_response(msg="success", data=None):
    return jsonify({
        "code": 0,
        "msg": msg,
        "data": data or {}
    })

def error_response(code, msg="error", data=None):
    return jsonify({
        "code": code,
        "msg": msg,
        "data": data or {}
    })
