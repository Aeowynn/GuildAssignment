
# ASYNC Chat
# Accepts multiple incoming connections
# Places them in a chat with each other
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from flask import Flask

app = Flask(__name__)

from app import routes