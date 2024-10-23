class InvalidUserId(Exception):
    def __init__(self, id: str):
        super().__init__(f"User ID: {id!r} is invalid")
