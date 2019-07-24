import json
import UniboArm
import UniboFace
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        #受け取った値を取得
        content_len=int(self.headers.get('content-length'))
        request_body = json.loads(self.rfile.read(content_len).decode('utf-8'))

        #クライアント側に値を返す
        response = {"test": 1}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response_json = json.dumps(response)
        print(request_body["face"])
        self.wfile.write(response_json.encode('utf-8'))
        
        #ここにuniboを動かす関数を書く
        #UniboArm.Arm().move_arm()
        UniboFace.DotMatrixLED().loop_face(request_body["face"])
    #仮の関数
class Server:
    def main(self):
        host = '0.0.0.0'
        port = 3334
        httpd = HTTPServer((host, port), MyHandler)
        httpd.serve_forever()
a = Server()
a.main()
