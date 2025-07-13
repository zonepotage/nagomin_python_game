from lib.phase.AbsPhase import AbsPhase
from lib.object.Rectangle import Rectangle
import pyxel


class ProloguePhase(AbsPhase):
    """
    プロローグ画面用フェーズクラス
    (タイトル画面)
    """

    def __init__(self, game_object, logger=None):
        super().__init__(game_object, logger)

        # スタートボタンの位置定義
        self._start_button = Rectangle(5, self.game_object.window_object.height - 10, self.game_object.window_object.width - 10, 8)

    def prepare(self):
        self.logger.debug('Phase準備開始')
        super().prepare()
        pyxel.mouse(True)
        self.logger.debug('Phase準備完了')

    def update(self):
        # スタートボタンを押下したら、現在PhaseをChapterPhaseに切り換える
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.game_object.is_clicked_object(self._start_button):
            self.game_object.current_phase = self.game_object.GAME_PHASE_CHAPTER

    def draw(self):
        # 画面初期化&オブジェクト描画
        pyxel.cls(pyxel.COLOR_BLACK)
        self.game_object.draw_text_center('Flappy Bird.')
        self._start_button.draw()
        self.game_object.draw_text_center('Click to Start!!!', pyxel.COLOR_RED, 5,
                                          self.game_object.window_object.height - 10,
                                          self.game_object.window_object.width - 10, 8)
