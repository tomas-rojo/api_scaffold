class ItemNotFound(Exception):
    def __init__(self, id: str):
        super().__init__(f"No item found with ID: {id!r}")
