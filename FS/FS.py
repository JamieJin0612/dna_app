from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

# Store AS details
as_details = {}

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@app.route('/register', methods=['PUT'])
def register():
    data = request.json
    hostname = data.get('hostname')
    ip = data.get('ip')
    as_ip = data.get('as_ip')
    as_port = data.get('as_port')

    if not all([hostname, ip, as_ip, as_port]):
        return jsonify({"error": "Missing parameters"}), 400

    # Store AS details for later use
    as_details['as_ip'] = as_ip
    as_details['as_port'] = as_port

    # Register with AS using UDP
    dns_message = f"TYPE=A,NAME={hostname}\nVALUE=IP_ADDRESS={ip}TTL=10\n"
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        udp_socket.sendto(dns_message.encode(), (as_ip, int(as_port)))

    return "", 201

@app.route('/fibonacci')
def get_fibonacci():
    number = request.args.get('number')

    try:
        n = int(number)
        result = fibonacci(n)
        return jsonify({"fibonacci": result}), 200
    except ValueError:
        return jsonify({"error": "Bad format"}), 400

if __name__ == '__main__':
    app.run(port=9090)
