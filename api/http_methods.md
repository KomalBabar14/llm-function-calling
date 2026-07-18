# HTTP Methods

HTTP methods (also called HTTP verbs) define the action that a client wants to perform on a resource.

| Method | Purpose | Example |
|---------|---------|---------|
| GET | Retrieve data | Get a user's profile |
| POST | Create a new resource | Create a new account |
| PUT | Replace an existing resource | Replace all user details |
| PATCH | Update part of a resource | Change only the email address |
| DELETE | Remove a resource | Delete a user account |

## Example

### GET Request

```http
GET /users/101
```

### POST Request

```http
POST /users
```

### PATCH Request

```http
PATCH /users/101
```

### DELETE Request

```http
DELETE /users/101
```

## Interview Tip

A common interview question is:

**Q:** What is the difference between PUT and PATCH?

**Answer:**
- **PUT** replaces the entire resource.
- **PATCH** updates only the specified fields.
