from utils.message_builder import image
from configs.path_config import IMAGE_PATH
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.adapters.onebot.v11.permission import GROUP
from utils.utils import FreqLimiter
from configs.config import NICKNAME
import random
from nonebot import on_keyword
import os


__zx_plugin_name__ = "基本设置 [Hidden]"
__plugin_usage__ = "用法： 无"
__plugin_version__ = 0.1
__plugin_author__ = 'HibiKier'


_flmt = FreqLimiter(300)


self_introduction = on_command(
    "自我介绍", aliases={"你是谁"}, rule=to_me(), priority=5, block=True
)


@self_introduction.handle()
async def _():
    if NICKNAME.find('灵梦') != -1:
        result = (
            "我是灵梦\n"
            "你们可以叫我灵梦， 灵梦酱, 哪怕你们叫我十万巫女我也能接受！\n"
            + image("lym")
        )
        await self_introduction.finish(result)