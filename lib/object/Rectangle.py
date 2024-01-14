import pyxel


class Rectangle:
    """
    矩形定義
    """
    def __init__(self, x, y, width, height, color=pyxel.COLOR_WHITE):
        """
        矩形作成
        @param x: 原点座標(x)
        @param y: 原点座標(y)
        @param width: 幅
        @param height: 高さ
        @param color: 色
        """
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._x2 = x + width
        self._y2 = y + height

    def __str__(self):
        return 'type:rectangle, x:%s, y:%s, x2:%s, y2:%s, width:%s, height:%s, color:%s' % (self.x, self.y, self._x2, self._y2, self.width, self.height, self.color)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def x2(self):
        return self._x2

    @property
    def y2(self):
        return self._y2

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def color(self):
        return self._color

    def draw(self):
        """
        描画
        @return: None
        """
        pyxel.rect(self.x, self.y, self.width, self.height, self.color)

    def move_relative(self, x, y):
        """
        移動(相対量)

        @param x: 移動量(x方向)
        @param y: 移動量(y方向)
        """
        self._x += x
        self._y += y
        self._x2 += x
        self._y2 += y

    def move_absolute(self, x, y):
        """
        移動(絶対座標)

        @param x: 移動先(x軸)
        @param y: 移動先(y軸)
        """
        self._x = x
        self._y = y
        self._x2 = x + self._width
        self._y2 = y + self._width

    def is_conflict(self, target):
        """
        衝突判定

        @param target: 判定対象の矩形オブジェクト
        @return: 判定結果
        """

        # 矩形同士の衝突判定
        if isinstance(target, Rectangle):
            # 矩形同士の衝突判定
            # 矩形Aおよび矩形Bについて、各辺の位置関係をみてあげればよい
            # (ゲーム内では、徐々に近づく&x方向にしか動かないので、ここまで厳密につくらなくてもよい気もする)
            return self.x <= target.x2 and self.x2 >= target.x and self.y <= target.y2 and self.y2 >= target.y
