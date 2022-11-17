from flask import Flask
from flask import request
import redis
import random
app = Flask(__name__)
r = redis.from_url('rediss://red-cdqfg6sgqg47to27lk1g:ibY6E7A3nzWM4sLdrLwT8lIxuM47bfol@frankfurt-redis.render.com:6379')
r2 = redis.from_url('redis://red-cdqfg6sgqg47to27lk1g:6379')

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get')
def get():  
    args = dict(request.args)
    if args.get('internal') == 'true':
        return r2.get('key').decode('UTF-8')
    return r.get('key').decode('UTF-8')

@app.route('/set')
def set():
    args = dict(request.args)
    input = str(random.randint(0,20000))
    if args.get('internal') == 'true':
        return str(r2.set('key',str(input).encode('UTF-8')))
    return str(r.set('key',str(input).encode('UTF-8')))

if __name__ == "__main__":
    app.run(host='0.0.0.0')