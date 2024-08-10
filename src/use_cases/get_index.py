from services.get import get_element


class IndexUseCase:
    def execute(self) -> str:
        try:
            return get_element("1")
        except Exception as e:
            raise e
