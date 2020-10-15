
# ASYNC Chat
# Accepts multiple incoming connections
# Places them in a chat with each other
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# Setup processing for an inbound connection
def processing_inbound_connection():
	"""METHOD INFORMATION"""
	client, client_address = SERVER_SOCKET.accept()
	print("%s:%s connection accepted." % client_address)
	client.send(bytes("You are now connected!", "utf8")) #utf8?
	addresses[client] = client_address
	Thread(target=handle_single_connection, args=(client,)).start()

def handle_single_connection(client):
	""" yup """
	name = client.recv(BUFSIZ).decode("utf8")
	print(">>>>> NAME : %s " % name)
	instructions = "If you want to leave, type [EXIT] to exit. Otherwise, you can view messages by sender with [SENT] or all messages with [MESSAGES]. Type [HELP] to recieve these instructions again."
	client.send(bytes(instructions, "utf8"))
	clients[client] = name

# Setup
clients = {}
addresses = {}
# Given more time, the messages would be stored in a database
messages = {}

HOST = '127.0.0.1'
PORT = 65432
BUFSIZ = 1024
ADDRESS = (HOST, PORT)

SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)
SERVER_SOCKET.bind(ADDRESS)

print("Hello?")

if __name__ == "__main__":
    SERVER_SOCKET.listen()
    print("Accepting incoming connections")
    INCOMING_CONNECTION_THREAD = Thread(target=processing_inbound_connection)
    INCOMING_CONNECTION_THREAD.start()
    INCOMING_CONNECTION_THREAD.join()
    SERVER_SOCKET.close()