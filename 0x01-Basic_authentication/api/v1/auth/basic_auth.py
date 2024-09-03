#!/usr/bin/env python3
""" basic_auth.py
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class
    """
    def extract_base64_authorization_header(
        """ Method that should implement the logic for checking if a request
        """
        self, authorization_header: str
    ) -> str:
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header[6:]
