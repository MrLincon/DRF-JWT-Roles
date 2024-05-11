
This is a DRF project. It only has authentication part. It has jwt authentication and custom user roles. The backend is configured with MySQL.

## Base URL: http://127.0.0.1:8000/auth/

Data Format: JSON

# Roles:
> `Admin - 1`

> `Manager - 2`

> `Employee - 3`

> `User - 4`

# Endpoints:


> `Register (POST /register)`

```json
{
    "email": "user@email.com",
    "password": "strong_password"
}
```

> `Register Admin (POST /register-admin): (Potentially Restricted)`

```json
{
    "email": "admin@email.com",
    "password": "strong_password"
}
```

> `Login (POST /login)`

```json
{
    "email": "user@email.com",
    "password": "user_password"
}
```

> `Change Password (POST /change-password): (Requires Authentication)`

```json
{
    "email": "user@email.com",
    "old_password": "current_password",
    "new_password": "new_strong_password"
}
```

> `Update Role (POST /update-role): (Requires Authentication)`

> Admin can chnage every role, Manager can change roles of Employee and User

```json
{
    "uid" : "efa691fef3b84a5c8e414275a439ce0b",
    "role": "3"
}
```
