import socket
connexion_principale=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind(('',12800))
connexion_principale.listen(10)
connexion_avec_client, info_connexion= connexion_principale.accept()
connexion_avec_client.send(b"je viens d'accepter votre requete")
print (info_connexion)
connexion_principale.close()