# HTTP Status Codes

HTTP status codes indicate the result of a client's request to a server.

## Successful Responses (2xx)

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | The request was successful. |
| 201 | Created | A new resource was successfully created. |
| 204 | No Content | Request succeeded but there is no content to return. |

---

## Client Errors (4xx)

| Code | Meaning | Description |
|------|---------|-------------|
| 400 | Bad Request | The request contains invalid data or syntax. |
| 401 | Unauthorized | Authentication is required. |
| 403 | Forbidden | The client is authenticated but lacks permission. |
| 404 | Not Found | The requested resource does not exist. |
| 409 | Conflict | The request conflicts with existing data. |
| 429 | Too Many Requests | Too many requests were sent in a short period. |

---

## Server Errors (5xx)

| Code | Meaning | Description |
|------|---------|-------------|
| 500 | Internal Server Error | An unexpected server error occurred. |
| 503 | Service Unavailable | The server is temporarily unavailable. |

---

# Example

## Successful Login

```http
POST /login
```

Response:

```http
200 OK
```

---

## Creating a New User

```http
POST /users
```

Response:

```http
201 Created
```

---

## Requesting a Missing Resource

```http
GET /users/999
```

Response:

```http
404 Not Found
```

---

## Interview Tips

### 401 vs 403

- **401 Unauthorized** → You need to log in.
- **403 Forbidden** → You are logged in but do not have permission.

### 400 vs 409

- **400 Bad Request** → Invalid request data.
- **409 Conflict** → The request conflicts with existing data (for example, an email address that already exists).

### 500 vs 503

- **500 Internal Server Error** → The server encountered an unexpected problem.
- **503 Service Unavailable** → The server is temporarily unavailable, often due to maintenance or overload.
