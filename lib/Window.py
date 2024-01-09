from lib.AbsClass import AbsClass
import pyxel
import logging


class Window(AbsClass):
    """
    Windowオブジェクト

    たいしたことはやっていなく、ただ単にを作るのみ。
    (細かいことは、Phase側で行う)
    """

    def __init__(self, logger=None):
        """
        コンストラクタ
        """
        super().__init__(logger)
        self.logger.debug('Windowオブジェクト初期化開始')
        pyxel.init(width=self.width, height=self.height, fps=self.fps, title=self.title)
        self.logger.debug('Windowオブジェクト初期化完了')

    @property
    def title(self):
        return self.settings.game_title

    @property
    def fps(self):
        return self.settings.game_fps

    @property
    def width(self):
        return 150

    @property
    def height(self):
        return 96
