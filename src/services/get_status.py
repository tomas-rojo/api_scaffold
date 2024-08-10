from config.container import container


def get_status() -> str:
    return container.api_url
