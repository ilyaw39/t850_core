from io import BytesIO
from typing import Union

from nonebot.params import Depends
from nonebot.matcher import Matcher
from nonebot.typing import T_Handler
from nonebot import on_command, require, on_message
from nonebot.adapters.onebot.v11 import MessageSegment
from configs.path_config import IMAGE_PATH
require("nonebot_plugin_imageutils")

from .data_source import commands
from .depends import split_msg, regex
from .utils import Command, help_image

__zx_plugin_name__ = "头像表情包"
__plugin_usage__ = """
usage：
    触发方式：指令 + @user/qq/自己/图片
    发送“头像表情包”查看支持的指令
    指令：
        摸 @任何人
        摸 qq号
        摸 自己
        摸 [图片]
""".strip()
__plugin_des__ = "生成各种表情"
__plugin_type__ = ("群内小游戏",)
__plugin_cmd__ = ["头像表情包", "头像相关表情包", "头像相关表情制作"]
__plugin_version__ = 0.4
__plugin_author__ = "MeetWq"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    'cmd': __plugin_cmd__
}
__plugin_resources__ = {
    "images": IMAGE_PATH / "petpet", }

help_cmd = on_command("头像表情包", aliases={"头像相关表情包", "头像相关表情制作"}, block=True, priority=5)


@help_cmd.handle()
async def _():
    img = await help_image(commands)
    if img:
        await help_cmd.finish(MessageSegment.image(img))


def create_matchers():
    def handler(command: Command) -> T_Handler:
        async def handle(
            matcher: Matcher, res: Union[str, BytesIO] = Depends(command.func)
        ):
            if isinstance(res, str):
                await matcher.finish(res)
            await matcher.finish(MessageSegment.image(res))

        return handle

    for command in commands:
        on_message(
            regex(command.pattern),
            block=True,
            priority=5,
        ).append_handler(handler(command), parameterless=[split_msg()])


create_matchers()
