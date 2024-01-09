from lib.GameApp import GameApp
from lib.Settings import Settings
import logging


def get_logger():
    """
    ロガー取得
    :return: ロガーオブジェクト
    """
    settings = Settings()
    logger_obj = logging.getLogger(__name__)
    logger_obj.setLevel(settings.loglevel)
    logger_obj.propagate = False
    log_handler = logging.FileHandler(settings.log_file_name)
    log_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s - %(asctime)s', datefmt='%Y/%m/%d %H:%M:%S'))
    log_handler.setLevel(settings.loglevel)
    logger_obj.addHandler(log_handler)
    return logger_obj


# アプリケーションエントリポイント
if __name__ == '__main__':
    logger = get_logger()
    logger.info('アプリケーションを起動')
    gameApp = GameApp()
