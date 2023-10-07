#!/usr/bin/env python3
"""Basic Auth"""

from api.v1.auth.auth import Auth
import re
import base64
from typing import TypeVar
from models.user import User


class BasicAuth (Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract_base64_authorization_header that returns the Base64 part
        of the Authorization header for a Basic Authentication"""

        if authorization_header is None or (type(authorization_header) != str):
            return None
        if authorization_header.startswith("Basic ") is False:
            return None
        Base64 = re.split(' ', authorization_header)
        return Base64[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode_base64_authorization_header that returns the
        decoded value of a Base64 string base64_authorization_header"""

        if (base64_authorization_header is None or
                (type(base64_authorization_header) != str)):
            return None
        try:
            decodeBytes = base64.b64decode(base64_authorization_header)
            decodedStr = decodeBytes.decode("utf-8")
            return decodedStr
        except ValueError:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """extract_user_credentials method that returns
        the user email and password from the Base64 decoded value"""

        if (decoded_base64_authorization_header is None
                or type(decoded_base64_authorization_header) != str):
            return None, None
        if (re.search(':', decoded_base64_authorization_header)):
            res = re.split(':', decoded_base64_authorization_header)
            return res[0], res[1]
        else:
            return None, None

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """user_object_from_credentials method that
        returns the User instance based on his email and password"""

        if type(user_email) != str or user_email is None:
            return None
        if type(user_pwd) != str or user_pwd is None:
            return None
        user = User.search({"email": user_email})
        print("----")
        for i in user:
            print(i)
        print("----")
        print(user_email)
        if user:
            if User.is_valid_password(user_pwd):
                return user
        return None
