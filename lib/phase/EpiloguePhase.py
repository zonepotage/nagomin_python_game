from lib.phase.AbsPhase import AbsPhase
import pyxel


class EpiloguePhase(AbsPhase):
    """
    エピローグ画面用フェーズクラス
    """
    can_skip_draw = False

    def prepare(self):
        self.logger.debug('Phase準備開始')
        super().prepare()
        self.can_skip_draw = False
        self.logger.debug('Phase準備完了')
        self.logger.info('結果画面を表示')

    def update(self):

        # Nキーを押下したら、またゲームを行う
        if pyxel.btn(pyxel.KEY_N):
            self.logger.info('再プレイを開始')
            self.game_object.current_phase = self.game_object.GAME_PHASE_CHAPTER

        if pyxel.btn(pyxel.KEY_Q):
            self.logger.info('アプリケーションを終了')
            pyxel.quit()

    def draw(self):
        if self.can_skip_draw:
            return
        self.game_object.draw_text_center('Game Over!!!', pyxel.COLOR_RED, 0, 0, None, self.game_object.window_object.height / 2)
        self.game_object.draw_text_center(format('Score: %d' % self.game_object.last_game_score), pyxel.COLOR_RED, 0, self.game_object.window_object.height / 2, None, self.game_object.window_object.height / 2)
        self.game_object.draw_text_center('N: New Game / Q: Quit', pyxel.COLOR_ORANGE, 5, self.game_object.window_object.height - 10, self.game_object.window_object.width - 10, 8)
        self.can_skip_draw = True
