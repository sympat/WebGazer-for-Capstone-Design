import http.server 
import ssl

PORT_NUMBER = 8080
HOST = '0.0.0.0'

try:
    httpd = http.server.HTTPServer((HOST, PORT_NUMBER), http.server.SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile='newcert.pem', keyfile='newkey.pem') 

    print('Started httpserver on port ' , PORT_NUMBER)
    httpd.serve_forever()
except KeyboardInterrupt:
    print ('^C received, shutting down the web server')
    httpd.socket.close()