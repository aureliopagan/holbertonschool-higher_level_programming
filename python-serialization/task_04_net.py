#!/usr/bin/env python3
"""Client-Server Application with Serialization."""

import socket
import json


def start_server():
    """
    Start a server that listens for incoming connections and processes data.
    
    The server:
    - Listens on localhost port 65432
    - Accepts one connection
    - Receives serialized JSON data
    - Deserializes and prints the dictionary
    - Closes the connection
    """
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to localhost and port 65432
    host = 'localhost'
    port = 65432
    
    try:
        # Enable socket reuse to avoid "Address already in use" error
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        
        # Listen for incoming connections (max 1 connection)
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")
        
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        
        if data:
            # Deserialize the JSON data
            received_dict = json.loads(data)
            print("Received Dictionary from Client:")
            print(received_dict)
        
        # Close the client connection
        client_socket.close()
        
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        # Close the server socket
        server_socket.close()


def send_data(dictionary):
    """
    Send a dictionary to the server using JSON serialization.
    
    Args:
        dictionary: Python dictionary to send to the server
    """
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Server connection details
    host = 'localhost'
    port = 65432
    
    try:
        # Connect to the server
        client_socket.connect((host, port))
        
        # Serialize the dictionary to JSON
        serialized_data = json.dumps(dictionary)
        
        # Send the serialized data to the server
        client_socket.send(serialized_data.encode('utf-8'))
        
    except ConnectionRefusedError:
        print("Error: Could not connect to server. Make sure server is running.")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        # Close the connection
        client_socket.close()
