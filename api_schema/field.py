# -*- coding: utf-8 -*
# Author: weijia shan
# Email: wjshan@goodoss.com
# Time: 2020-07-25 23:28
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


@attr.s
class Argument(object):
    name = attr.ib(default=None, type=str)  # argument key
    nullable = attr.ib(default=False, type=bool)  # 允许为空
    required = attr.ib(default=True, type=bool)  # 必填
    description = attr.ib(default='', type=str)  # 描述信息
    default = attr.ib(default='', type=object)  # 默认值


@attr.s
class Number(Argument):
    minimum = attr.ib(default=None, type=int)  # 用于约束取值范围，表示取值范围应该大于或等于minimum
    maximum = attr.ib(default=None, type=int)  # 用于约束取值范围，表示取值范围应该小于或等于maximum
    exclusive_minimum = attr.ib(default=None, type=bool)  # 当设置为true时 value必须大于minimum
    exclusive_maximum = attr.ib(default=None, type=bool)  # 如果maximum和exclusiveMaximum同时存在，且exclusiveMaximum的值为true，则表示取值范围只能小于maximum
    multiple_of = attr.ib(default=None, type=float)  # 如果设置 则取值必须被设置值整除
    format = attr.ib(default=None, type=str)  # 数据格式 int32 int64 float
    type = 'number'


@attr.s
class String(Argument):
    pattern = attr.ib(default=None, type=str)  # 使用正则表达式约束字符串类型数据
    min_length = attr.ib(default=None, type=int)  # 字符串类型数据的最大长度
    max_length = attr.ib(default=None, type=int)  # 字符串类型数据的最小长度
    format = attr.ib(default=None, type=str)  # email phone
    enum = attr.ib(default=None, type=list)  # 数据枚举 如果设置取值必须与枚举值中的一个相同
    type = 'string'


@attr.s
class Array(Argument):
    items = attr.ib(default=None, type=list)
    one_of = attr.ib(default=None, type=list)
    min_items = attr.ib(default=None, type=int)
    max_items = attr.ib(default=None, type=int)
    unique_items = attr.ib(default=None, type=bool)
    type = 'array'


class Object(Argument):
    min_properties = attr.ib(default=None, type=int)
    max_properties = attr.ib(default=None, type=int)
    type = 'object'
