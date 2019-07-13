from aiohttp import web

async def handle(request):
    return web.json_response("pong")



app = web.Application()
app.router.add_route('GET', '/ping', handle)

web.run_app(app, port=8888)