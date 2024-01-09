from lib.AbsClass import AbsClass
from lib.object.Rectangle import Rectangle
import pyxel
import random


class Pipe(AbsClass):
    """
    パイプクラス

    主にパイプについての動作を定義する。
    (本クラスはパイプの集合体ではなく、パイプひとつひとつの定義)
    """

    def __init__(self, game_object, logger=None):
        super().__init__(logger)
        self.logger.debug('パイプ初期化開始')
        self._game_object = game_object
        
        # パイプの座標
        self._pipe_left_x = self._game_object.window_object.width
        self._pipe_right_x = self._pipe_left_x + self.settings.pipe_width
        self._pipe_height = self._game_object.window_object.height

        # プレイヤが通ることのできるパイプの隙間
        if self.settings.slit_height > 0:
            self._slit_height = self.settings.slit_height
        else:
            self._slit_height = self.settings.jump_speed * 6 + random.randint(0, self.settings.jump_speed // 2)

        self._slit_top_y = random.randint(0, (self._pipe_height - self._slit_height))
        self._slit_bottom_y = self._slit_top_y + self._slit_height

        # 描画&判定用に、パイプを矩形で表現&パイプの隙間はその上にあらためて矩形を重ねる
        self._pipe_rectangle = Rectangle(self.pipe_left_x, 0, self.settings.pipe_width, self._pipe_height, pyxel.COLOR_LIME)
        self._slit_rectangle = Rectangle(self.pipe_left_x, self._slit_top_y, self.settings.pipe_width, self._slit_height, pyxel.COLOR_BLACK)

        # 通過判定用
        self._is_passed_player = False

        self.logger.debug('パイプ初期化完了')

    @property
    def pipe_left_x(self):
        """
        パイプX座標(左端)
        """
        return self._pipe_left_x

    @property
    def pipe_right_x(self):
        """
        パイプX座標(右端)
        """
        return self._pipe_right_x

    @property
    def slit_top_y(self):
        """
        隙間Y座標(上部)
        """
        return self._slit_top_y
    
    @property
    def slit_bottom_y(self):
        """
        隙間Y座標(下部)
        """
        return self._slit_bottom_y
    
    @property
    def slit_height(self):
        """
        隙間の高さ
        """
        return self._slit_height
    
    @property
    def pipe_rectangle(self):
        """
        パイプ矩形
        """
        return self._pipe_rectangle

    @property
    def slit_rectangle(self):
        """
        隙間矩形
        """
        return self._slit_rectangle

    @property
    def is_passed_player(self):
        return self._is_passed_player

    @is_passed_player.setter
    def is_passed_player(self, value):
        self._is_passed_player = value

    def update(self):
        """
        オブジェクト更新
        """
        self._pipe_rectangle.move_relative(-1, 0)
        self._slit_rectangle.move_relative(-1, 0)
        self._pipe_left_x -= 1
        self._pipe_right_x -= 1

    def draw(self):
        """
        オブジェクト描画
        """
        self._pipe_rectangle.draw()
        self._slit_rectangle.draw()

    def is_necessary_next_pipe(self):
        """
        新たなパイプ生成の必要性

        このメンバ関数はパイプが右端にある場合に使用する。

        @return: 必要性
        """

        # パイプの右側にある余白がパイプ間隔の最小値を切っていたら、作る事はない
        if self.pipe_right_x + self.settings.pipe_interval_min >= self._game_object.window_object.width:
            return False

        # パイプの右側にある余白がパイプ間隔の最大値を超えていたら、かならず作る必要がある
        if self.pipe_right_x + self.settings.pipe_width + self.settings.pipe_interval_max <= self._game_object.window_object.width:
            return True

        # ここまで来たときは、作っても作らなくてもよい
        if random.randint(0, 9) > 8:
            return random.choice([True, False])

    def can_delete_pipe(self):
        """
        パイプ削除の可能性

        @return: 可能性        
        """
        # パイプの右端が画面外に出ていたら、そのパイプはもういらない
        return (self.pipe_right_x + self.settings.pipe_width) < 0
