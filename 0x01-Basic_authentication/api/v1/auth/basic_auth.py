#!/usr/bin/env python3
""" basic_auth.py
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ BasicAuth class
    """
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """ Method that should implement the logic for checking if a request
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ Method that should implement the logic for checking if a request
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            header = base64_authorization_header.encode('utf-8')
            header = header.decode('base64')
            return header.decode('utf-8')
        except Exception:
            return None
