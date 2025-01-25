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
