from lib.AbsClass import AbsClass
from lib.object.Rectangle import Rectangle

import math
import pyxel


class Circle:
    """
    円形定義
    """
    def __init__(self, x, y, r, color=pyxel.COLOR_WHITE):
        """
        円形作成
        @param x: 中心座標(x)
        @param y: 中心座標(y)
        @param r: 半径
        @param color: 色
        """
        self._x = x
        self._y = y
        self._r = r
        self._color = color

        # 衝突判定する時のために、円に内接する矩形もつくっておく
        self._rectangle = Rectangle(x - r, y - r, r * 2, r * 2)

    def __str__(self):
        return 'type:circle, x:%s, y:%s, radius:%s, color:%s, rectangled_x:%s, rectangled_y:%s, rectangled_width:%s, rectangled_height:%s, ' % (self.x, self.y, self.r, self.color, self._rectangle.x, self._rectangle.y, self._rectangle.width, self._rectangle.height)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def r(self):
        return self._r

    @property
    def rectangle(self):
        return self._rectangle

    @property
    def color(self):
        return self._color

    def draw(self):
        """
        描画
        @return: None
        """
        pyxel.circ(self.x, self.y, self.r, self.color)

    def move_relative(self, x, y):
        """
        移動(相対量)

        @param x: 移動量(x方向)
        @param y: 移動量(y方向)
        """
        self._x += x
        self._y += y
        self._rectangle = Rectangle(self._x - self.r, self._y - self.r, self.r * 2, self.r * 2)

    def move_absolute(self, x, y):
        """
        移動(絶対座標)

        @param x: 移動先(x軸)
        @param y: 移動先(y軸)
        """
        self._x = x
        self._y = y
        self._rectangle = Rectangle(self._x - self.r, self._y - self.r, self.r * 2, self.r * 2)

    def is_conflict(self, target):
        """
        衝突判定
        @param target: 判定対象の円形ないし矩形オブジェクト
        @return: 判定結果
        """
        # 矩形との衝突判定
        if isinstance(target, Rectangle):
            # ひとまず、自分のことを円に内接する矩形だと思い込ませて確認する
            if not target.is_conflict(self.rectangle):
                # この場合はぶつかりようがない
                return False
            # TODO: 処理速度が気になる場合は、方法を考える
            return (target.x < self.x < target.x2 and (target.y - self.r) < self.y < (target.y2 + self.r)) or \
                ((target.x - self.r) < self.x < (target.x2 + self.r) and target.y < self.y < target.y2) or \
                ((target.x - self.x) ** 2 + (target.y - self.y) ** 2) < self.r ** 2 or \
                ((target.x2 - self.x) ** 2 + (target.y - self.y) ** 2) < self.r ** 2 or \
                ((target.x - self.x) ** 2 + (target.y2 - self.y) ** 2) < self.r ** 2 or \
                ((target.x2 - self.x) ** 2 + (target.y2 - self.y) ** 2) < self.r ** 2

        # 円形との衝突判定
        if isinstance(target, Circle):
            # 円の中心座標間の距離を計算し、半径の和よりも大きければぶつからない
            distance = math.sqrt(abs(self.x - target.x) ** 2 + abs(self.y - target.y) ** 2)
            return distance <= (self.r + target.r)

        return False
