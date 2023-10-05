#!/usr/bin/env python3
"""manage the API authentication"""

from flask import request
from typing import List, TypeVar


class Auth():
    """Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth method"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        for i in range(len(excluded_paths)):
            if excluded_paths[i].rstrip('/') == path:
                return False
            else:
                return True

    def authorization_header(self, request=request) -> str:
        """authorization_header method"""
        return None

    def current_user(self, request=request) -> TypeVar('User'):
        """current_user method"""
        return None
