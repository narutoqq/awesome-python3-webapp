import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from aiohttp import web
from datetime import datetime

def index(request):
	return web.Response(body=b'<h1>Awesome</h1>',headers={'content-type':'text/html'})

def init():
	app = web.Application()
	app.add_routes([web.get('/', index)])
	logging.info('server started ...')
	web.run_app(app, host='0.0.0.0', port=9000)

init()
