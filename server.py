from simplews import SimpleWSServer

server = SimpleWSServer(port=8765)
clients = set()
@server.on_connect
async def on_connect(client):
    clients.add(client)

@server.on_close
async def on_close(client):
    clients.remove(client)

@server.on_message
async def on_message(client, message):
    server.broadcast(clients, message)

server.serve()
