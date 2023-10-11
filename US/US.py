from flask import Flask, request, jsonify

app = Flask(__name__)

# @app.route('/fibonacci', methods=['GET'])
@app.route('/', methods=['GET'])
def fibonacci():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    if not all([hostname, fs_port, number, as_ip, as_port]):
        return "Missing parameters", 400

    # Query the Authoritative Server (AS) to get IP address for the given hostname
    # For this example, I'll simulate this with a placeholder IP
    resolved_ip = "127.0.0.1"  # This should come from AS

    # Now, with the resolved IP, query the Fibonacci Server (FS)
    # This step is also simulated for this example
    fibonacci_number = int(number) * 10  # Placeholder logic
    return jsonify(re="ok"), 200

if __name__ == '__main__':
    app.run(port=8080)
