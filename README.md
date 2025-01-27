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

# :dart: API Documentation

## Endpoints

| **HTTP Method** | **Endpoint**               | **Description**                                                   | **Request Example**                       | **Response**                                                                 |
|-----------------|----------------------------|-------------------------------------------------------------------|-------------------------------------------|-------------------------------------------------------------------------------|
| **GET**         | `/api/<service_name>`     | Fetch the state of a specific service.                           | `curl http://localhost:6666/api/service_a` | **Status Code**: `200 OK` <br> **JSON**: `{"service_a": "on"}`                |
| **POST**        | `/api/<service_name>/<state>` | Update the state of a specific service to `on` or `off`.         | `curl -X POST http://localhost:6666/api/service_a/off` | **Status Code**: `200 OK` <br> **JSON**: `{"message": "Service updated successfully", "service_a": "off"}` |
| **GET**         | Invalid Service Name      | Attempt to fetch state for a non-existent service.               | `curl http://localhost:6666/api/invalid_service` | **Status Code**: `404 Not Found` <br> **JSON**: `{"error": "Service not found"}` |
| **POST**        | Invalid State Value       | Attempt to update a service with an invalid state (not `on/off`).| `curl -X POST http://localhost:6666/api/service_a/invalid_state` | **Status Code**: `400 Bad Request` <br> **JSON**: `{"error": "Invalid state. Must be 'on' or 'off'."}` |

---

## Notes

- Replace `<service_name>` with the name of the service (`service_a`, `service_b`, etc.).
- Replace `<state>` with `on` or `off` when using the POST endpoint.
- The API returns meaningful error messages for invalid inputs or non-existent services.
