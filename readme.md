Base URL: http://127.0.0.1:8000/auth/

Data Format: JSON

Endpoints:

    Register User (POST /register):

        Request Body: 

    ```json
    { "email": "user@email.com", "password": "strong_password" }
    ```

    Register Admin User (POST /register-admin): (Potentially Restricted)

        Request Body: { "email": "admin@email.com", "password": "strong_password" }


    Login (POST /login):

        Request Body: { "email": "user@email.com", "password": "user_password" }


    Change Password (POST /change-password): (Requires Authentication)

        Request Body: { "email": "user@email.com", "old_password": "current_password", "new_password": "new_strong_password" }