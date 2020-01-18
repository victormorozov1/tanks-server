from game_server.server import Server


game_server = Server(5000, '[::]')
game_server.serve()
