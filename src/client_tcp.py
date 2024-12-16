import socket

# Here we provide the server's IP
server_ip = input("Enter the server IP: ")
server_port = input("Enter the server port: ")

# Creating the socket object and connecting
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, int(server_port)))

print("Connected to the server. Let's start the guessing game!")

try:
    while True:
        # Prompt the user to input their guess
        guess = input("Enter your guess (between 1 and 100): ")

        # Send the guess to the server
        client_socket.send(guess.encode())

        # Receive the server's response
        response = client_socket.recv(1024).decode()

        # Print the server's response to the client
        print(f"Server: {response}")

        # If the guess is correct, we exit the game
        if "Correct!" in response:
            break

finally:
    # Close the socket when done
    client_socket.close()
