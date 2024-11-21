from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the server address and port
host = "localhost"
port = 8000

# Create the HTTP server
server_address = (host, port)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print(f"Serving HTTP on {host} port {port} (http://{host}:{port}/) ...")
try:
    # Start the server
    httpd.serve_forever()
except KeyboardInterrupt:
    # Graceful shutdown
    print("\nShutting down server...")
    httpd.server_close()
