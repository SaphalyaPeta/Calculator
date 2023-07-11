import http.server
import socketserver

# Set the port number for the server
PORT = 8000

# Create a request handler
Handler = http.server.SimpleHTTPRequestHandler

# Set the current directory as the root directory
Handler.extensions_map[".py"] = "text/plain"
http.server.SimpleHTTPRequestHandler.extensions_map[".js"] = "application/javascript"

# Start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server running at localhost:" + str(PORT))
    httpd.serve_forever()
