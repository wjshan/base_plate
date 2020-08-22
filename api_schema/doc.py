# -*- coding: utf-8 -*
# Author: weijia shan
# Email: wjshan@goodoss.com
# Time: 2020-07-25 23:12
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


class ModelMeta(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


class Model(metaclass=ModelMeta):
    pass


def register_model(model):
    def inner(func):
        func.argument = model
        return func

    return inner


class Register(object):
    def __init__(self, app):
        self.app = app

    def route(self, model,
              summary=None,
              description=None,
              consumes=None,
              produces=None,
              consumes_content_type=None,
              produces_content_type=None,
              exclude=None):
        def inner(func):
            func.meta = {'model': model}
            if summary is not None:
                func.meta['summary'] = summary
            if description is not None:
                func.meta['description'] = description
            if consumes is not None:
                func.meta['consumes'] = consumes
            if produces is not None:
                func.meta['produces'] = produces
            if consumes_content_type is not None:
                func.meta['consumes_content_type'] = consumes_content_type
            if produces_content_type is not None:
                func.meta['produces_content_type'] = produces_content_type
            if exclude is not None:
                func.meta['exclude'] = exclude
            return func

        return inner

    def response(self, model):
        pass
