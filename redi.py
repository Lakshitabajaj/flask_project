from flask import Flask, render_template, request, redirect, url_for
import redis

app = Flask(__name__)
# Connect to the Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/')
def index():
    return render_template('get.html')

@app.route('/set', methods=['POST'])
def set_key():
    key = request.form['key']
    value = request.form['value']
    # Store the key-value pair in Redis
    redis_client.set(key, value)
    return redirect(url_for('index'))

@app.route('/get', methods=['POST'])
def get_key():
    key = request.form['key']
    # Retrieve the value from Redis
    value = redis_client.get(key)
    if value:
        value = value.decode('utf-8')
    else:
        value = "Key not found in Redis."

    return render_template('get.html', key=key, value=value)
 
if __name__ == '__main__':
    app.run(debug=True)

