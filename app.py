from flask import Flask, jsonify, request
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['GET'])
def hello_world():
  environment = os.getenv("ENVIRONMENT")
  message     = "Hello, Flask!!"
  json        = {
    "environment": environment,
    "message": message
  }
  
  return jsonify(json)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000)
