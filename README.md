# Fastapi Regular Web app sample
This application is a simple web server using auth0 regular web application setup

## To Run
1. Add an `.env` file at the root with contents
    ```
    AUTH0_CLIENT_ID=
    AUTH0_CLIENT_SECRET=
    AUTH0_DOMAIN=
    APP_SECRET_KEY=
    ```
2. Install dependencies
    ```
    poetry install
    ```
3. Run the application
    ```
    poetry run python app.py
    ```


