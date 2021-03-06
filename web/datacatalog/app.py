from aiohttp import web

from datacatalog import systemhealth, index, action_api


def get_app():
    """
        Construct the the application
    """
    app = web.Application()

    app.router.add_get('/', index.handle)
    app.router.add_get('/system/health', systemhealth.handle)

    app.router.add_get('/datacatalog/api/3/action/{action}', action_api.handle)

    return app