from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()

import argparse
from server.main import runserver


args_parser = argparse.ArgumentParser()
args_parser.add_argument("port")


def parse_port(port):
    try:
        port = int(port)
        assert (port >0) and (port <= 65535)
        return port
    except Exception:
        return None


def main():
    args = args_parser.parse_args()
    port = parse_port(args.port)
    if port is None:
        msg = "error: port is not in PORT format : %s"
        return
    runserver(port)


if __name__ == "__main__":
    main()