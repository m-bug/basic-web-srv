# :rocket: Basic web server

Helpful tool to manage the state of simple key-value pairs using web requests.

## :wrench: Installation

Use the Dockerfile to build an image.

```bash
docker build -t simple-python-server .
```

## :runner: Run

Run a container using the image.

```python
docker run -p 5000:5000 simple-python-server
```

## :dart: API

### Endpoints


| Method   | URL                                      | Description                              |
| -------- | ---------------------------------------- | ---------------------------------------- |
| `GET`    | `/api/{service_name}`                    | Retrieve informations about a service    |
| `POST`   | `/api/{service_name}/{on|off}`           | Change state of service                  |

