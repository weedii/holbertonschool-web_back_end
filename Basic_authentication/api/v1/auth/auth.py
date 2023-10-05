#!/usr/bin/env python3
"""0"""

from flask import request
from typing import List, TypeVar


class Auth():
    """Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth method"""
        return False

    def authorization_header(self, request=request) -> str:
        """authorization_header method"""
        return None

    def current_user(self, request=request) -> TypeVar('User'):
        """current_user method"""
        return None
