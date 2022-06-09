from nonebot import on_regex
from nonebot.rule import to_me
from pathlib import Path


__zx_plugin_name__ = "关于"
__plugin_usage__ = """
usage：
    要更加了解灵梦吗
    指令：
        关于
""".strip()
__plugin_des__ = "要更加了解灵梦吗"
__plugin_cmd__ = ["关于"]
__plugin_version__ = 0.1
__plugin_type__ = ("其他",)
__plugin_author__ = "HibiKier"
__plugin_settings__ = {
    "level": 1,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["关于"],
}


about = on_regex("^关于$", priority=5, block=True, rule=to_me())


@about.handle()
async def _():
    ver_file = Path() / '__version__'
    version = None
    if ver_file.exists():
        with open(ver_file, 'r', encoding='utf8') as f:
            version = f.read().split(':')[-1].strip()
    msg = f"""
"灵梦 T-850"
版本：{version}
简介：基于 Nonebot2 与 go-cqhttp 开发;
版本: T-850;
模型: 灵梦;
项目地址： https://github.com/HibiKier/zhenxun_bot
    """.strip()
    await about.send(msg)
