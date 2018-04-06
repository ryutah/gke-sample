import sys

from logging import DEBUG
from logging import getLogger, StreamHandler

from flask import Flask

from glog_formatter import GlogFormatter


app = Flask(__name__)


handler = StreamHandler(sys.stdout)
handler.setFormatter(GlogFormatter())
logger = getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(DEBUG)


@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/log")
def log_example():
    logger.debug("This is debug")
    logger.info("This is info")
    logger.warn("This is warn")
    logger.error("This is error")
    logger.critical("This is critical")
    return "gatche"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
