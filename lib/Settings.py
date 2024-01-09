import configparser


class Settings:
    """
    Settingsクラス

    DIの実装が面倒なので、シングルトンにしておく

    TODO:エラーチェックをちゃんと実装する
    """

    _object = None
    _is_initialized = False

    def __init__(self):
        if self._is_initialized:
            return

        config = configparser.ConfigParser()
        config.read('settings.ini', encoding='utf-8')

        self._game_ini = config['GAME']
        self._title = self._game_ini.get('title')
        self._fps = self._game_ini.getint('fps')
        self._gravity = self._game_ini.getint('gravity')
        self._jump_speed = self._game_ini.getint('jump_speed')
        self._move_frequency = self._game_ini.getint('move_frequency')
        self._pipe_width = self._game_ini.getint('pipe_width')
        self._slit_height = self._game_ini.getint('slit_height')
        self._pipe_interval_min = self._game_ini.getint('pipe_interval_min')
        self._pipe_interval_max = self._game_ini.getint('pipe_interval_max')

        self._logger_ini = config['LOGGER']
        self._loglevel = self._logger_ini.getint('loglevel')
        self._log_file_name = self._logger_ini.get('logFileName')
        self._is_initialized = True

    def __new__(cls, *args, **kwargs):
        if cls._object is None:
            cls._object = super().__new__(cls)
        return cls._object

    @property
    def loglevel(self):
        """
        ログレベル返却
        :return: ログレベル
        """
        return self._loglevel

    @property
    def log_file_name(self):
        """
        ログファイル名返却
        :return: ログファイル名
        """
        return self._log_file_name

    @property
    def game_title(self):
        """
        ゲームタイトル返却
        :return: タイトル文言
        """
        return self._title

    @property
    def game_fps(self):
        return self._fps

    @property
    def gravity(self):
        return self._gravity

    @property
    def jump_speed(self):
        return self._jump_speed

    @property
    def move_frequency(self):
        return self._move_frequency

    @property
    def pipe_width(self):
        return self._pipe_width

    @property
    def slit_height(self):
        return self._slit_height

    @property
    def pipe_interval_min(self):
        return self._pipe_interval_min

    @property
    def pipe_interval_max(self):
        return self._pipe_interval_max
