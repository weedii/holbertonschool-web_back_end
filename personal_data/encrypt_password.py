#!/usr/bin/env python3
"""Encrypting passwords Check & valid password"""


import bcrypt


def hash_password(password: str) -> str:
    """hash_password function that  returns a salted, hashed password"""
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash
