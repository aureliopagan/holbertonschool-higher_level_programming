# RESTful API

## Introduction

RESTful APIs are fundamental to modern software development, enabling efficient data exchange between systems. This project explores REST (Representational State Transfer), an architectural style that promotes scalable, stateless, and cacheable communication. RESTful APIs simplify integration, making web services accessible to diverse applications.

## Learning Objectives

- **HTTP/HTTPS Basics:** Understand the core web protocols, their methods, and the distinction between secure and non-secure communication.
- **API Consumption with Command Line:** Practice interacting with APIs using command-line tools.
- **API Consumption with Python:** Use Python to fetch and process data from APIs.
- **API Development with `http.server`:** Learn to build basic APIs using Python’s built-in modules.
- **API Development with Flask:** Develop more advanced APIs with Flask, focusing on routing, data handling, and scalability.
- **API Security & Authentication:** Explore methods to secure APIs and manage authorized access.
- **API Standards & Documentation with OpenAPI:** Learn the importance of standardized API documentation for usability and maintenance.

## Importance

RESTful APIs are crucial for connecting systems in today’s digital landscape. They act as intermediaries, translating requests, fetching data, and triggering actions. From social media integrations to industrial automation, APIs are everywhere.

Mastering API consumption, development, security, and documentation provides essential skills for building robust and efficient digital solutions.

## REST API Conceptual Diagram

```
+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   ----->  |       |  -------> |         |  Modify   |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
    Client            Web Server           API Server           Database
```

### Components

- **Client:** Initiates requests (e.g., browser or app).
- **Web Server:** Receives requests and forwards them to the API server.
- **API Server:** Processes requests and determines required actions.
- **Database:** Stores and provides data as needed.

### Flow

1. The client sends an HTTP/HTTPS request to the web server.
2. The web server forwards the request to the API server.
3. The API server processes the request and interacts with the database if necessary.
4. The API server returns a response to the web server.
5. The web server sends the final response to the client.

> In simpler setups, the web server and API server may be combined. This separation illustrates the layers in more complex environments.