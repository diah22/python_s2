import socket
hote=''
port=12800
connexion_principale=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote,port))
connexion_principale.listen(5)
print('en ecoute...')
connexion_avec_client, info_connexion= connexion_principale.accept()
message_recu=b""
while message_recu != b"fin":
    message=input('Votre message: \n')
    connexion_avec_client.send(message.encode())
    message_recu=connexion_avec_client.recv(1024)
    print(message_recu.decode())

print('Fermeture de connexion')
connexion_avec_client.close()
connexion_principale.close()