from enum import Enum
from lib.AbsClass import AbsClass
from lib.object.Rectangle import Rectangle
from lib.phase.ChapterPhase import ChapterPhase
from lib.phase.EpiloguePhase import EpiloguePhase
from lib.phase.ProloguePhase import ProloguePhase
from lib.Window import Window
import pyxel


class GameApp(AbsClass):
    """
    Game機能クラス
    """

    """
    Phase番号
    """
    GAME_PHASE_PROLOGUE = 0
    GAME_PHASE_CHAPTER = 1
    GAME_PHASE_EPILOGUE = 2

    def __init__(self, logger=None):
        """
        コンストラクタ
        @param logger ロガー
        """
        super().__init__(logger)
        self.logger.debug('GameApp初期化開始')

        # 画面の定義
        self._window = Window(self.logger)

        # Phase(画面)の定義
        self.logger.debug('Phase定義準備開始')
        self._phase_list = {
            self.GAME_PHASE_PROLOGUE: ProloguePhase(self, self.logger),
            self.GAME_PHASE_CHAPTER: ChapterPhase(self, self.logger),
            self.GAME_PHASE_EPILOGUE: EpiloguePhase(self, self.logger),
        }

        self._phase_name_list = {
            None: '(None)',
            self.GAME_PHASE_PROLOGUE: 'GAME_PHASE_PROLOGUE',
            self.GAME_PHASE_CHAPTER: 'GAME_PHASE_CHAPTER',
            self.GAME_PHASE_EPILOGUE: 'GAME_PHASE_EPILOGUE',
        }

        # 現在Phaseの設定
        self._current_phase = None
        self.current_phase = self.GAME_PHASE_PROLOGUE  # 最初はプロローグ画面

        # プレイ中フラグの設定
        self._is_playing = False

        # 最終ゲームスコア
        self._last_game_score = 0
        self._high_score = 0

        # アセットオープン
        pyxel.load('../resource.pyxres')

        # pyxel開始
        pyxel.run(self.update, self.draw)

    def update(self):
        """
        フレーム更新
        """
        self._phase_list[self.current_phase].update()

    def draw(self):
        """
        画面描画
        """
        self._phase_list[self.current_phase].draw()

    @property
    def current_phase(self):
        return self._current_phase

    @current_phase.setter
    def current_phase(self, phase):
        """
        Phase変更
        @param phase: 変更先のPhase番号 (GAME_PHASE_*)
        @return: None
        """

        # 変更する必要がある場合のみ変更する
        if self.current_phase is not phase:
            self.logger.debug('現在Phase設定更新: %s -> %s' % (self._phase_name_list[self.current_phase], self._phase_name_list[phase]))
            if self.current_phase is not None:
                self._phase_list[self.current_phase].clearn()
            self._current_phase = phase
            self._phase_list[self.current_phase].prepare()

    @property
    def is_playing(self):
        return self._is_playing

    @is_playing.setter
    def is_playing(self, val):
        self._is_playing = val

    @property
    def window_object(self):
        return self._window

    @property
    def last_game_score(self):
        return self._last_game_score

    @last_game_score.setter
    def last_game_score(self, val):
        self._last_game_score = val

    @property
    def high_score(self):
        return self._high_score

    @high_score.setter
    def high_score(self, val):
        self._high_score = val

    def draw_text_center(self, text, color=pyxel.COLOR_WHITE, x=0, y=0, width=None, height=None):
        """
        センタリングテキスト

        @param text: 文言
        @param color: 色
        @param x: 描画領域開始座標(x)
        @param y: 描画領域開始座標(y)
        @param width: 描画領域幅
        @param height: 描画領域高さ

        @return: None
        """

        if width is None:
            width = self.window_object.width

        if height is None:
            height = self.window_object.height

        # 1文字は4ドットなのでこれでよい
        _x = (width / 2) - (len(text) * 4 / 2)
        _y = (height / 2) - 2

        pyxel.text(x + _x, y + _y, text, color)

    def is_clicked_object(self, obj):
        """
        オブジェクトクリックチェック

        オブジェクトの重なりは考慮せず、あくまで座標ベースのベリファイです。

        @param obj: 対象オブジェクト
        @return: チェック結果
        """

        mouse_x = pyxel.mouse_x
        mouse_y = pyxel.mouse_y

        if isinstance(obj, Rectangle):  # 矩形
            return (obj.x <= mouse_x <= (obj.x + obj.width)) and (obj.y <= mouse_y <= (obj.y + obj.height))

        return False
