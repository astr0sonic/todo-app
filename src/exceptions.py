from fastapi import HTTPException, status


class AlreadyRegisteredException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="This username is already taken!",
        )


class UserNotRegisteredException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="This username does not exist!",
        )


class InvalidPasswordException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid password!",
        )


# already_registered_exception = HTTPException(
#     status_code=409,
#     detail="This username is already taken!",
# )
