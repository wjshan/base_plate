# -*- coding: utf-8 -*
# Author: weijia shan
# Email: wjshan@goodoss.com
# Time: 2020-07-24 15:17
# Description: 
# //////////////////////////////////////////////////////////////////#
# /                          _ooOoo_                               /#
# /                         o8888888o                              /#
# /                         88" . "88                              /#
# /                         (| ^_^ |)                              /#
# /                         O\  =  /O                              /#
# /                      ____/`---'\____                           /#
# /                    .'  \\|     |//  `.                         /#
# /                   /  \\|||  :  |||//  \                        /#
# /                  /  _||||| -:- |||||-  \                       /#
# /                  |   | \\\  -  /// |   |                       /#
# /                  | \_|  ''\---/''  |   |                       /#
# /                  \  .-\__  `-`  ___/-. /                       /#
# /                ___`. .'  /--.--\  `. . ___                     /#
# /              ."" '<  `.___\_<|>_/___.'  >'"".                  /#
# /            | | :  `- \`.;`\ _ /`;.`/ - ` : | |                 /#
# /            \  \ `-.   \_ __\ /__ _/   .-` /  /                 /#
# /      ========`-.____`-.___\_____/___.-`____.-'========         /#
# /                           `=---='                              /#
# /      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        /#
# /            佛祖保佑       永不宕机     永无BUG                    /#
# //////////////////////////////////////////////////////////////////#
import asyncio
import uvloop
from sanic import Sanic
from sanic_cors import CORS
from ..api_schema import Register
import os
import uuid


def get_client_id():
    if os.path.exists('client_id'):
        with open('client_id', 'rb') as f:
            client_id = f.read().decode()
    else:
        client_id = str(uuid.uuid4())
        with open('client_id', 'wb') as f:
            f.write(client_id.encode())
    return client_id


def get_app(config):
    app = Sanic(getattr(config, 'name', None) or __name__)
    CORS(app, automatic_options=True)

    @app.middleware('request')
    async def request_hander(request):
        pass

    @app.middleware('response')
    async def prevent_xss(request, response):
        if response.status == 404:
            print('当前路由不在内容中，需要转接至其他服务')

    @app.listener('before_server_start')
    async def notify_server_started(app, loop):
        print('Server successfully already started!')

    @app.listener('before_server_stop')
    async def notify_server_stopping(app, loop):
        print('Server shutting down!')

    asyncio.set_event_loop(uvloop.new_event_loop())
    register = Register(app)
    return app, register
