import nonebot
from nonebot import logger
import os
from pathlib import Path
from pydantic import BaseModel, ValidationError
try:
    import ujson as json
except ModuleNotFoundError:
    import json

class PluginConfig(BaseModel):
    fortune_path: str = os.path.join(os.path.dirname(__file__), "resource")
    '''
        各主题抽签开关, 仅在random抽签中生效
        请确保不全是False
    '''
    amazing_grace: bool = False
    arknights_flag: bool = False
    asoul_flag: bool = False
    azure_flag: bool = False
    genshin_flag:  bool = False
    onmyoji_flag: bool = False
    pcr_flag: bool = False
    touhou_flag: bool = True
    touhou_lostword_flag: bool = False
    touhou_olg_flag: bool = False
    hololive_flag: bool = False
    granblue_fantasy_flag: bool = False
    punishing_flag: bool = False
    pretty_derby_flag: bool = False
    dc4_flag: bool = False
    einstein_flag: bool = False
    sweet_illusion_flag: bool = False
    liqingge_flag: bool = False
    hoshizora_flag: bool = False
    sakura_flag: bool = False 
    summer_pockets: bool = False

driver = nonebot.get_driver()
global_config = driver.config
config: PluginConfig = PluginConfig.parse_obj(global_config.dict())
FORTUNE_PATH: str = config.fortune_path
CONFIG_PATH: Path = Path(FORTUNE_PATH) / "fortune_config.json"

'''
    Reserved for next version
'''
@driver.on_startup
async def check_config():
    if not CONFIG_PATH.exists():
        logger.warning("配置文件不存在, 已重新生成配置文件……")
        config = PluginConfig()
    else:
        with CONFIG_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
        try:
            config = PluginConfig.parse_obj({**global_config.dict(), **data})
        except ValidationError:
            config = PluginConfig()
            logger.warning("配置文件格式错误, 已重新生成配置文件……")
        
    with CONFIG_PATH.open("w", encoding="utf-8") as f:
        json.dump(config.dict(), f, ensure_ascii=False, indent=4)