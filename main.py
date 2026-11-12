"""Loca Nova - Simple local command server."""

import hmac
import json
import os
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer

# 1. Load the secret APP_KEY from the local .env file
env_file = Path(__file__).with_name(".env")

if env_file.exists():
    for line in env_file.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("APP_KEY="):
            os.environ["APP_KEY"] = line.strip().split("=", 1)[1]
            break

APP_KEY = os.getenv("APP_KEY", "")

# Bind strictly to localhost (127.0.0.1) so the server is only accessible locally
HOST = "127.0.0.1"
PORT = 8080


class Handler(BaseHTTPRequestHandler):

    # Helper method to send standardized JSON responses
    def send_json(self, status, data):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    # 2. Health-check endpoint (GET /) to verify that the local Core is running
    def do_GET(self):
        if self.path == "/":
            self.send_json(200, {
                "application": "Loca Nova",
                "status": "ENGINE_ACTIVE",
                "hardware_control_enabled": False
            })
        else:
            self.send_json(404, {"error": "NOT_FOUND"})

    # 3. Command endpoint (POST /command) to receive and validate JSON payloads
    def do_POST(self):
        if self.path != "/command":
            self.send_json(404, {"error": "NOT_FOUND"})
            return

        if not APP_KEY:
            self.send_json(500, {"error": "APP_KEY_NOT_CONFIGURED"})
            return

        # Parse and validate incoming JSON size and structure
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 4096:
                raise ValueError

            data = json.loads(self.rfile.read(length).decode("utf-8"))

            if not isinstance(data, dict):
                raise ValueError

        except (ValueError, UnicodeDecodeError):
            self.send_json(400, {"error": "INVALID_REQUEST"})
            return

        password = data.get("password")
        command = data.get("command")

        # Verify authorization using timing-safe comparison
        if not isinstance(password, str) or not hmac.compare_digest(password, APP_KEY):
            self.send_json(401, {"error": "INVALID_PASSWORD"})
            return

        # Validate that the command is supported (currently ON or OFF)
        if not isinstance(command, str) or command.upper() not in ("ON", "OFF"):
            self.send_json(400, {"error": "INVALID_COMMAND"})
            return

        command = command.upper()

        # TODO: Connect actual device driver here to control physical hardware (e.g., smart lamp)
        self.send_json(200, {
            "status": "AUTHORIZED",
            "command": command,
            "device_action_performed": False
        })


# 4. Start the local server if APP_KEY is properly configured
if __name__ == "__main__":
    if not APP_KEY:
        print("ERROR: APP_KEY is missing from .env")
    else:
        server = HTTPServer((HOST, PORT), Handler)
        print(f"Loca Nova prototype running at http://{HOST}:{PORT}/")

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
        finally:
            server.server_close()
