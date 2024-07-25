
from flask import jsonify
from typing import Literal, Any, Union



def send_response(status:Literal[200, 201, 400, 401, 403, 404], message:str, data:Any=None):
    """
    Send a JSON response with the given status, message, and data.

    Args:
        status (Literal[200, 201, 400, 401, 403, 404]): The HTTP status code.
        message (str): The message to include in the response.
        data (Any, optional): Additional data to include in the response. Defaults to None.

    Returns:
        dict: A JSON response containing isSuccess, message, and data.

    Example:
        >>> send_response(200, "Operation successful", {"user_id": 123})
        {
            "isSuccess": True,
            "message": "Operation successful",
            "data": {"user_id": 123}
        }
    """
    match status:
        case 200:
            return jsonify({
                "isSuccess": True,
                "message": message if message else "Action Successful",
                "data": data
            })
        case 201:
            return jsonify({
                "isSuccess": True,
                "message": message if message else "Resource Created",
                "data": data
            })
        
        case 400:
            return jsonify({
                "isSuccess": False,
                "message": message if message else "Bad Request",
                "data": data
            });
        case 401:
            return jsonify({
                "isSuccess": False,
                "message": message if message else "Unauthorized",
                "data": data
            })
        case 403:
            return jsonify({
                "isSuccess": False,
                "message": message if message else "Forbidden",
                "data": data
            })
        case 404:
            return jsonify({
                "isSuccess": False,
                "message": message if message else "Resource Not Found",
                "data": data
            })
        
        case _:
            return jsonify({
                "isSuccess": False,
                "message": "An error occurred",
                "data": None
            })
        