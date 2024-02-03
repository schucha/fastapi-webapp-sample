# This example is based on this authlib tutorial:
# https://github.com/authlib/demo-oauth-client/blob/master/fastapi-google-login/app.py

import json
from fastapi import FastAPI
from starlette.config import Config
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, RedirectResponse
from authlib.integrations.starlette_client import OAuth, OAuthError
from os import environ as env
from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=env.get("APP_SECRET_KEY"))

# config = Config('.env') # TODO: get config to work
config = Config()
oauth = OAuth(config)


CONF_URL = server_metadata_url = (
    f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)
oauth.register(
    name="auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    server_metadata_url=CONF_URL,
    client_kwargs={"scope": "openid email profile"},
)


@app.get("/")
async def homepage(request: Request):
    user = request.session.get("user")
    if user:
        data = json.dumps(user)
        html = f"<pre>{data}</pre>" '<a href="/logout">logout</a>'
        return HTMLResponse(html)
    # return HTMLResponse('<a href="/login">login</a>')
    redirect_uri = request.url_for("auth")
    return await oauth.auth0.authorize_redirect(request, redirect_uri)


@app.get("/login")
async def login(request: Request):
    redirect_uri = request.url_for("auth")
    return await oauth.auth0.authorize_redirect(request, redirect_uri)


@app.get("/auth")
async def auth(request: Request):
    try:
        token = await oauth.auth0.authorize_access_token(request)
    except OAuthError as error:
        return HTMLResponse(f"<h1>{error.error}</h1>")
    user = token.get("userinfo")
    if user:
        request.session["user"] = dict(user)
    return RedirectResponse(url="/")


@app.get("/logout")
async def logout(request: Request):
    request.session.pop("user", None)
    # return RedirectResponse(url="/")
    return HTMLResponse('<h1>You have been logged out</h1><a href="/login">login</a>')


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
