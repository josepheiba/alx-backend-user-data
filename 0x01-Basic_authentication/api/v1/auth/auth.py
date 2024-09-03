#!/usr/bin/env python3
""" auth.py
"""
from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method that should implement the logic for checking if a path
            needs authentication
        """
        return False


    def authorization_header(self, request=None) -> str:
        """ Method that should implement the logic for checking if a request
            is authorized
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ Method that should implement the logic for checking if a request
            is authorized
        """
        return None
