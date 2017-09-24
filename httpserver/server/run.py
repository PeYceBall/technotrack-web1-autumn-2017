# -*- coding: utf-8 -*-
import socket
from os import walk

def getHttp(code, content):
    return "HTTP/1.1 " + code + "\n\n" + content

def get_response(request):
    if request != "":
        try:
            user_agent = ((request.split("User-Agent:"))[1].split('\n'))[0]
            url = (request.split('\n'))[0].split(' ')[1]
            request_type = (request.split('\n'))[0].split(' ')[0]
        except:
            return getHttp('400 Bad request', "Please send correct request!")
        if url == '/':
            return getHttp("200 OK", "Hello mister!\nYou are: " + user_agent)
        elif url == '/media/':
            files = []
            for(dirpath, dirnames, filenames) in walk("../files/"):
                files.extend(filenames)
            return getHttp("200 OK", ' '.join(files))
        elif url == '/test/':
            return getHttp('200 OK', request)
        elif url.split('/')[1] == 'media' and len(url) > 6: # /media is not allowed!
            filepath = "../files/" + url[(len("media") + 2) :]
            try:
                f = open(filepath)
                return getHttp('200 OK', f.read())
            except IOError:
                return getHttp('404 Not found', "File not found")
        else:
            return getHttp('404 Not found', "Page not found")

    
    return getHttp('400 Bad request', '')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #
server_socket.listen(0)  #

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  #
        request_string = client_socket.recv(2048)  #
        
        client_socket.send(get_response(request_string))  #
        client_socket.close()
    except KeyboardInterrupt:  #
        print 'Stopped'
        server_socket.close()  #
        exit()
