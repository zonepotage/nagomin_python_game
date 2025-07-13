import sys

from lib.Settings import Settings
import logging


def _get_default_logger():
    """
    標準出力ロガー取得
    :return: loggerオブジェクト
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    log_handler_stdout = logging.StreamHandler(stream=sys.stdout)
    log_handler_stdout.setLevel(logging.DEBUG)
    log_handler_stdout.setFormatter(logging.Formatter('[%(levelname)s] %(message)s - %(asctime)s', datefmt='%Y/%m/%d %H:%M:%S'))
    logger.addHandler(log_handler_stdout)
    """
    log_handler_stderr = logging.StreamHandler(stream=sys.stderr)
    log_handler_stderr.setFormatter(logging.Formatter('[%(levelname)s] %(message)s - %(asctime)s', datefmt='%Y/%m/%d %H:%M:%S'))
    log_handler_stderr.setLevel(logging.WARN)
    logger.addHandler(log_handler_stderr)
    """
    logger.debug('Logger準備完了')
    return logger


class AbsClass:
    """
    基底クラス
    """

    def __init__(self, logger=None):
        """
        コンストラクタ
        @param logger: ロガー
        """
        self._settings = Settings()
        self._logger = logger or _get_default_logger()

    @property
    def settings(self):
        """
        設定オブジェクト
        @return 設定オブジェクト
        """
        return self._settings

    @property
    def logger(self):
        """
        ロガー取得
        @return: ロガー
        """
        return self._logger
