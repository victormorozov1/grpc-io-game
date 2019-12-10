from game_server.server import Server


chat_server = Server(5000, '[::]')
chat_server.serve()
