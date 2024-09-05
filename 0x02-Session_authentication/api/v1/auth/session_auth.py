#!/usr/bin/env python3
""" session_auth module
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User
import os


class SessionAuth(Auth):
    """ SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Method that should implement the logic for checking if a request
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Method that should implement the logic for checking if a request
        """
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def destroy_session(self, request=None) -> bool:
        """ Method that should implement the logic for checking if a request
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True

    def current_user(self, request=None) -> User:
        """Retrieves the user associated with the request.
        """
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)
