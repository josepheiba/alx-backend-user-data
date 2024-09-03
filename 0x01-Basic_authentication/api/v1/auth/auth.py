#!/usr/bin/env python3
""" auth.py
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method that should implement the logic for checking if a path
            needs authentication
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        for expath in excluded_paths:
            if path == expath or path == expath + '/' or path + '/' == expath:
                return False
            elif expath[-1] == '*' and path.startswith(expath[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Method that should implement the logic for checking if a request
            is authorized
        """
        if request is None or request.headers.get('Authorization') is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method that should implement the logic for checking if a request
            is authorized
        """
        return None
