import  socket
connexion_avec_serveur= socket.socket(socket.AF_NET, socket.SOCK_STREAM)
connexion_avec_serveur.connect(('localhost',12800))
message=connexion_avec_serveur.recv(1024)
print(message)
connexion_avec_serveur.close()