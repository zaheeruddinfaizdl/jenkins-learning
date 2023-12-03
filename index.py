from http.server import BaseHTTPRequestHandler, HTTPServer

# Create a custom request handler by subclassing BaseHTTPRequestHandler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Send the message content as a response
        message = "Hello, this is your HTTP server from the Jenkins build!"
        self.wfile.write(message.encode())

# Set the host and port for the server
host = 'localhost'
port = 8088

# Create an instance of HTTPServer with the custom request handler
httpd = HTTPServer((host, port), SimpleHTTPRequestHandler)

# Print a message indicating the server has started
print(f"Server started on http://{host}:{port}")

# Start the server
httpd.serve_forever()
