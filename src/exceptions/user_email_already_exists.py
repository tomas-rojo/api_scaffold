class EmailAlreadyExists(Exception):
    def __init__(self, email: str):
        super().__init__(f"User email {email!r} already exists")
