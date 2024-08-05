#!/usr/bin/env python3
""" Auth model """
from flask import request
from typing import List, TypeVar


class Auth:
    """ template for all authentications """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ used to require authentication """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        p1, p2 = (path[:-1], path) if path[-1] == '/'else (path, path + '/')
        if p1 in excluded_paths or p2 in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ used to get the authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ used to get the current user """
        return None
