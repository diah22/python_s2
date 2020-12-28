try:
    import socket

    hote = 'localhost'
    port = 12800
    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((hote, port))
    print('connexion etablie avec le serveur')
    message_a_envoyer = b"salut"
    while message_a_envoyer != b"fin":
        message_recu = connexion_avec_serveur.recv(1024)
        print(message_recu.decode())
        message_a_envoyer=input('Reponse: \n')
        connexion_avec_serveur.send(message_a_envoyer.encode())

    print('fermeture de la connexion')
    connexion_avec_serveur.close()
except:
    print("Svp, lancer le serveur")

