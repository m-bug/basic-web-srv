import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# File to store the service states
DATA_FILE = 'data.json'

# Default state of services
DEFAULT_STATE = {
    "service_a": "on",
    "service_b": "off"
}

# Load or initialize the service states
def load_services():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            try:
                data = json.load(file)
                # Ensure the file contains valid JSON and has the required keys
                if not data or not isinstance(data, dict):
                    raise ValueError(f"Invalid configuration: {DATA_FILE} is empty or malformed.")
                return data
            except json.JSONDecodeError:
                raise ValueError(f"Invalid configuration: {DATA_FILE} contains invalid JSON.")
    else:
        raise FileNotFoundError(f"Configuration file {DATA_FILE} not found. Application cannot start.")


# Save the service states to the file
def save_services(services):
    with open(DATA_FILE, 'w') as file:
        json.dump(services, file, indent=2)

# Initialize service states
services = load_services()

# HTTP request handler class
class ServiceHandler(BaseHTTPRequestHandler):
    # HANDLE GET REQUESTS
    def do_GET(self):
        # Example: /api/service_a
        if self.path.startswith('/api/'):
            service_name = self.path.split('/api/')[-1]
            if service_name in services:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({service_name: services[service_name]}).encode('utf-8'))
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'Service not found')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    # HANDLE POST REQUESTS
    def do_POST(self):
        # Example: /api/service_a/on or /api/service_a/off
        if self.path.startswith('/api/'):
            parts = self.path.split('/api/')[-1].split('/')
            if len(parts) == 2:
                service_name, new_state = parts
                if service_name in services and new_state in ['on', 'off']:
                    services[service_name] = new_state
                    save_services(services)
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({service_name: new_state}).encode('utf-8'))
                else:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(b'Invalid service or state')
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Invalid URL format')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

# Start the server
def run():
    server_address = ('', 5000)  # Listen on port 5000
    httpd = HTTPServer(server_address, ServiceHandler)
    print("Server running on port 5000...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
