# -*- coding: utf-8 -*
# Author: weijia shan
# Email: wjshan@goodoss.com
# Time: 2020-07-25 21:34
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

import attr


class ApiServer(object):
    name = attr.ib()
    interface_style = attr.ib(default='restful')
    version = attr.ib(default=1.0)
    host = attr.ib()
    port = attr.ib()
    swagger = attr.ib()
    client_id = attr.ib()


class RestfulRoute(object):
    source_name = attr.ib()
    method = attr.ib()
    swagger_rule = attr.ib(repr=False)
    description = attr.ib()  # 功能描述
    summary = attr.ib()  # 简介
    required_login = attr.ib()
    tags = attr.ib()


class RestfulResponse(object):
    code = attr.ib()
    body = attr.ib()
    description = attr.ib()
