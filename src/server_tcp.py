import socket
import random

server_port = input("Enter preferred port: ")

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", int(server_port))) # Bind to all interfaces on specified port
server_socket.listen(1)  # Listen for 1 incoming connection

print("Waiting for client to connect...")

try:
    # Here we wait for the client to connect
    client_socket, client_address = server_socket.accept()
    print(f"Client connected from {client_address[0]}")

    # Initializing the game
    secret_number = random.randint(1, 100)  # Secret number between 1 and 100
    attempts = 0
    game_over = False

    # Start the game loop
    while not game_over:
        # Receive the client's guess
        guess_data = client_socket.recv(1024).decode()
        if not guess_data:
            break

        # Convert guess to an integer
        try:
            guess = int(guess_data)
        except ValueError:
            # If the client didn't send a valid number, continue the loop
            client_socket.send("Please send a valid number.".encode())
            continue

        # Count the attempts
        attempts += 1

        # Check if the guess is correct
        if guess < secret_number:
            client_socket.send("Too low! Try again.".encode())
        elif guess > secret_number:
            client_socket.send("Too high! Try again.".encode())
        else:
            client_socket.send(f"Correct! You guessed the number in {attempts} attempts.".encode())

            # End the game and disconnect if the guess is correct
            game_over = True
            client_socket.close()

finally:
    # Close the server socket
    server_socket.close()
