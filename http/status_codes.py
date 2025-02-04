
OK = 200
CREATED = 201
ACCEPTED = 202
BAD_REQUEST = 400
UNAUTHORIZED = 401
FORBIDDEN = 403
NOT_FOUND = 404
METHED_NOT_ALLOWED = 405
INTERNAL_SERVER_ERROR = 500
BAD_GATEWAY = 502

def format_status_code(code: int) -> str:
    match code:
        case 200:
            return "200 OK"
        case 201:
            return "201 Created"
        case 202:
            return "202 Accepted"
        case 400:
            return "400 Bad Request"
        case 401:
            return "401 Unauthorized"
        case 403:
            return "403 Forbidden"
        case 404:
            return "404 Not Found"
        case 405:
            return "405 Method Not Allowed"
        case 500:
            return "500 Internal Server Error"
        case 502:
            return "502 Bad Gateway"