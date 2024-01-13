from lib.AbsClass import AbsClass
from lib.object.Circle import Circle
import pyxel


class Player(AbsClass):
    """
    プレイヤクラス

    主にプレイヤについての動作を定義する。
    """

    CIRCLE_SIZE = 8
    CIRCLE_RADIUS = 4

    def __init__(self, game_object, logger=None):
        super().__init__(logger)
        self.logger.debug('プレイヤ初期化開始')
        self._game_object = game_object
        self._circle = Circle(self.CIRCLE_SIZE, self.CIRCLE_SIZE, self.CIRCLE_RADIUS, pyxel.COLOR_RED)
        self._gravity = self.settings.gravity
        self.logger.debug('プレイヤ初期化完了')

    def update(self):
        """
        オブジェクト更新
        """
        # スペースキーが押下されたら、上方向にジャンプさせる
        if pyxel.btn(pyxel.KEY_SPACE):
            self._gravity = self.settings.jump_speed * -1

        self._circle.move_relative(0, self._gravity)
        self._gravity += self.settings.gravity

    def draw(self):
        """
        オブジェクト描画
        """
        pyxel.blt(self._circle.x - self.CIRCLE_RADIUS, self._circle.y - self.CIRCLE_RADIUS, 0, 0, 0, self.CIRCLE_SIZE, self.CIRCLE_SIZE, pyxel.COLOR_WHITE)

    def is_collision_window(self):
        """
        衝突チェック(ウインドウ枠)

        ・プレイヤが地上に墜落していないか
        ・プレイヤが天井にぶつかっていないか

        @return チェック結果
        """

        # 墜落
        if self._circle.y + self._circle.r >= self._game_object.window_object.height - 1:
            self.logger.debug('地上墜落検知')
            self._circle.move_absolute(self._circle.x, self._game_object.window_object.height - self._circle.r - 1)
            pyxel.blt(self._circle.x - self.CIRCLE_RADIUS,  self._game_object.window_object.height - (self._circle.r * 2) - 1, 0, 0, 0, self.CIRCLE_SIZE, self.CIRCLE_SIZE, pyxel.COLOR_WHITE)
            return True

        # 天井衝突
        elif self._circle.y - self._circle.r <= 0:
            self.logger.debug('天井衝突検知')
            self._circle.move_absolute(self._circle.x, self._circle.r)
            pyxel.blt(self._circle.x - self.CIRCLE_RADIUS, 0, 0, 0, 0, self.CIRCLE_SIZE, self.CIRCLE_SIZE, pyxel.COLOR_WHITE)
            return True

        return False

    def is_collision_pipe(self, pipe):
        """
        衝突チェック(パイプ)

        @param pipe パイプ
        @return チェック結果
        """
        if self._circle.is_conflict(pipe.pipe_rectangle) and not self._circle.is_conflict(pipe.slit_rectangle):
            self.logger.debug('衝突検知 player::: %s / slit::: %s / pipe::: %s' % (self._circle, pipe.slit_rectangle, pipe.pipe_rectangle))
            return True

        return False

    def is_passed_pipe(self, pipe):
        """
        パイプ通過チェック
        @param pipe パイプ
        @return チェック結果
        """

        if pipe.pipe_left_x < (self._circle.x - self._circle.r) and not pipe.is_passed_player:
            pipe.is_passed_player = True
            return True

        return False
