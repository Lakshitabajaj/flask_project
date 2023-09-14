from flask import Flask, request, render_template
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store_data', methods=['POST'])
def store_data():
    key = request.form['key']
    value = request.form['value']
    redis_client.set(key, value)
    return 'Data stored successfully!'

@app.route('/get_data/<key>', methods=['GET'])
def get_data(key):
    value = redis_client.get(key)
    if value:
        value = value.decode('utf-8')
    else:
        value = "Key not found in Redis."

    return render_template('index.html', key=key, value=value)

if __name__ == '__main__':
    app.run(debug=True)
