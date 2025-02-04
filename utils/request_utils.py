

def translate_request(header: str) -> dict:
    
    lines = header.split("\r\n")
    request_line = lines[0]
    request = translate_request_line(request_line)
    # lines = lines[1:]
    # for line in lines:
    #     key, value = line.split(":")
    #     request[key.strip()] = value.strip()


    return request



def translate_request_line(request_line: str) -> dict:
    request = {}

    method, path, http_version = request_line.split(" ")
    request["method"] = method.strip()
    request["path"] = path.strip()
    request["http_version"] = http_version.strip()

    return request

    
