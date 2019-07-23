import json
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
        self.wfile.write(response_json.encode('utf-8'))
        
        #ここにuniboを動かす関数を書く
        self.hello()
    #仮の関数
    def hello(self):
        print("hello")
        
def main():
    host = '0.0.0.0'
    port = 3333
    httpd = HTTPServer((host, port), MyHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    main()