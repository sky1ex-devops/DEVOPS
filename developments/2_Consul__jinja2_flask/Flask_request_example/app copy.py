# Code Implementation
from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(filename='request_logs.log', level=logging.INFO)

@app.route('/endpoint', methods=['POST'])
def log_request_body():
    request_body = request.get_data(as_text=True)
    request_method = request.method
    app.logger.info(f"{request_method} request body: {request_body}")
    return 'Request body logged with request method successfully!'

if __name__ == '__main__':
    app.run()