#!/usr/bin/env python3
"""manage the API authentication"""

from flask import request
from typing import List, TypeVar


class Auth():
    """Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth method"""
        if path:
            path = path.rstrip('/')
        if path is None or excluded_paths is None:
            return True
        if len(excluded_paths) == 0 or path not in excluded_paths:
            return True
        if path in excluded_paths:
            return False

    def authorization_header(self, request=request) -> str:
        """authorization_header method"""
        return None

    def current_user(self, request=request) -> TypeVar('User'):
        """current_user method"""
        return None
