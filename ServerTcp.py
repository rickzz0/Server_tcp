import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

porta = int(input("Digite a porta que você deseja abrir:"))

try:

	server.bind(("127.0.0.1", porta))
	server.listen(5)
	print("Esperando conexão...")
	client, adress = server.accept()
	print("Mensagem recebida de: " + adress[0])

	while True:

		data = client.recv(2048).decode()
		print("\033[32m{}".format(data))
		
		enviar = input("\033[32mMensagem:")
		pacotes_enviados = client.send(enviar.encode())

		if enviar.lower().strip() == "sair":
			print("Conexão fechada!!!")
			break

		if data == "sair":
			print("Conexão fechada!!!")
			break
			
	server.close()

except Exception as error:
	print("Erro ao receber conexão")
	print(error)