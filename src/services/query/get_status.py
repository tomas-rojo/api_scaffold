from config.dependency import Dependency


def get_status() -> str:
    api_url: str = Dependency.get("api_url")
    return api_url
