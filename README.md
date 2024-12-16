# PyGuesser
Tiny Python networking demonstration for school. Using the [socket](https://docs.python.org/3/library/socket.html) module from Python's standard library.

## Dependencies
To run this program, you'll have to install the following dependencies:
- Python 3.13+ (Built and tested on, probably works with older releases too)

## Running the server
First an foremost, you'll have to start the server, this can be done by executing the `server_tcp.py` file.

```sh
python src/server_tcp.py
```

## Connecting to the server
Once the server is up and running, you'll have to establish a connection between client and server, the relevant functionality is provided by the `client_tcp.py` file.

```sh
python src/client_tcp.py

Enter the server IP:
> 127.0.0.1

Enter the server port:
> 4200
```


## Conclusion
That's it, happy guessing <3
