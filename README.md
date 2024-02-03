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

## Session example

To take a look at a sample session that is sent as a cookie from the Starlette SessionMiddleware
Add the session string from the browser into the `decode_session.py`
Run the `decode_session.py`

```
poetry run python decode_sesion.py
```

### Example session output

```json
{
    "user": {
        "given_name": "First",
        "family_name": "Last",
        "nickname": "firstlast",
        "name": "First Last",
        "picture": "",
        "locale": "en",
        "updated_at": "2000-02-03T18:07:58.686Z",
        "email": "first.last@email.com",
        "email_verified": true,
        "iss": "https://tenant.us.auth0.com/",
        "aud": "clientIdofauth0app",
        "iat": 1706983679,
        "exp": 1707019679,
        "sub": "userId",
        "sid": "sessionId",
        "nonce": "anonce"
    }
}
```
