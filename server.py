from flask import Flask, render_template
import socket

app = Flask(__name__)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_host = "localhost"
udp_port = 8000

# List of commands
commands = [
    "Command 1",
    "Command 2",
    "Command 3",
    "Command 4",
]

# commands.reverse()


@app.route("/")
def index():
    return render_template("index.html", commands=commands)


@app.route("/send-command/<command>")
def send_command(command):
    udp_socket.sendto(command.encode(), (udp_host, udp_port))
    return ""


if __name__ == "__main__":
    app.run(debug=True)
