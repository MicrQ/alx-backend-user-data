#!/usr/bin/env python3
""" Auth model """
from flask import request
from typing import List, TypeVar


class Auth:
    """ template for all authentications """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ used to require authentication """
        return False

    def authorization_header(self, request=None) -> str:
        """ used to get the authorization header """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """ used to get the current user """
        return None