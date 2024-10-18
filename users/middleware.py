from dj_rest_auth.app_settings import api_settings as settings

"""
Middleware for handling JWT tokens in cookies for Django Rest Framework JWT endpoints.
Classes:
    MoveJWTCookieIntoTheBody(MiddlewareMixin):
        Middleware to move JWT token from cookies to the body for the "/auth/token/verify/" endpoint.
        Methods:
            __init__(self, get_response):
                Initializes the middleware with the given response handler.
            __call__(self, request):
                Processes the request and returns the response.
            process_view(self, request, view_func, *view_args, **view_kwargs):
                Checks if the request path is "/auth/token/verify/" and if the JWT token is in the cookies.
                If so, adds the token to the body payload.
    MoveJWTRefreshCookieIntoTheBody(MiddlewareMixin):
        Middleware to move JWT refresh token from cookies to the body for the "/auth/logout/" and "/auth/token/refresh" endpoints.
        Methods:
            __init__(self, get_response):
                Initializes the middleware with the given response handler.
            __call__(self, request):
                Processes the request and returns the response.
            process_view(self, request, view_func, *view_args, **view_kwargs):
                Checks if the request path is "/auth/logout/" or "/auth/token/refresh" and if the JWT refresh token is in the cookies.
                If so, adds the refresh token to the body payload.
"""
from django.utils.deprecation import MiddlewareMixin
import json


class MoveJWTCookieIntoTheBody(MiddlewareMixin):
    """
    for Django Rest Framework JWT's POST "/token-refresh" endpoint --- check for a 'token' in the request.COOKIES
    and if, add it to the body payload.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        if (
            request.path == "/auth/token/verify/"
            and settings.JWT_AUTH_COOKIE in request.COOKIES
        ):
            if request.body != b"":
                data = json.loads(request.body)
                data["token"] = request.COOKIES[settings.JWT_AUTH_COOKIE]
                request._body = json.dumps(data).encode("utf-8")
            else:
                # I cannot create a body if it is not passed so the client must send '{}'
                pass

        return None


class MoveJWTRefreshCookieIntoTheBody(MiddlewareMixin):
    """
    for Django Rest Framework JWT's POST "/token-refresh" endpoint --- check for a 'token' in the request.COOKIES
    and if, add it to the body payload.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        if (
            request.path in ("/auth/logout/", "/auth/token/refresh")
            and settings.JWT_AUTH_REFRESH_COOKIE in request.COOKIES
        ):
            if request.body != b"":
                print("moviedsdlfkjdsalkfjdslakjfldaksfjdslifhadiughkdjfnoi refresh")
                data = json.loads(request.body)
                data["refresh"] = request.COOKIES[settings.JWT_AUTH_REFRESH_COOKIE]
                request._body = json.dumps(data).encode("utf-8")
            else:
                # I cannot create a body if it is not passed so the client must send '{}'
                pass

        return None


