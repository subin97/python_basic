# 위치 파라미터

def connect(server, port):
    url = f'http://{server}:{port}'
    return url


print(connect('localhost', '8000'))
