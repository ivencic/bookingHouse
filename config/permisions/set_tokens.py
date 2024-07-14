import datetime

from django.utils.deprecation import MiddlewareMixin
from rest_framework.request import Request
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import AccessToken


class JWTAuthenticationsMiddleware(MiddlewareMixin):

    def process_request(self, request: Request, **kwargs):
        access_token = request.COOKIES.get('access_token')
        refresh_token = request.COOKIES.get('refresh_token')

        if access_token:
            try:
                token = AccessToken(access_token)
                if datetime.fromtimestamp(token['exp']) < datetime.now():
                    raise TokenError('Token is expired')
                request.META['HTTP_AUTHORIZATION'] = f'JWT {access_token}'

            except TokenError:
                new_access_token = self.refresh_access_token(refresh_token)
