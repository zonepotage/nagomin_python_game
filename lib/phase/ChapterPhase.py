from lib.phase.AbsPhase import AbsPhase
from lib.Pipe import Pipe
from lib.Player import Player
import pyxel


class ChapterPhase(AbsPhase):
    """
    本編画面用フェーズクラス
    (ゲーム中の画面はここ)
    """

    def __init__(self, game_object, logger=None):
        super().__init__(game_object, logger)
        self._player = None
        self._pipes = []
        self._score = 0
        self._counter_for_show_help = 0

    def prepare(self):
        self.logger.debug('Phase準備開始')
        super().prepare()
        pyxel.mouse(False)
        self._player = Player(self.game_object, self.logger)
        self._pipes = []
        self._pipes.append(Pipe(self.game_object, self.logger))
        self.game_object.is_playing = True
        self._score = 0
        self.game_object.last_game_score = 0
        self._counter_for_show_help = 0
        self.logger.debug('Phase準備完了')
        self.logger.info('ゲームを開始')

    def update(self):
        """
        フレーム更新
        """
        # フレーム更新頻度は設定に依存する
        if pyxel.frame_count % self.settings.move_frequency == 0:
            if self.game_object.is_playing is True:

                # 衝突していたらおわり
                if self.is_collision():
                    self.game_object.is_playing = False

                # プレイヤを動かす
                self._player.update()

                # パイプを一つずつ動かす
                for _pipe in self._pipes:
                    _pipe.update()

                leftest_pipe = self._pipes[0]
                # プレイヤが左端のパイプを通過したらばスコアを増やす
                if self._player.is_passed_pipe(leftest_pipe):
                    self.logger.debug('パイプ通過 現在スコア:%s' % self._score)
                    self._score += 1

                # パイプを増やせるのであれば増やす
                if self._pipes[-1].is_necessary_next_pipe():
                    self.logger.debug('パイプ追加')
                    self._pipes.append(Pipe(self.game_object, self.logger))

                # 左端のパイプについて不要であれば削除する
                if leftest_pipe.can_delete_pipe():
                    self.logger.debug('パイプ削除')
                    self._pipes.pop(0)

            # ゲームオーバ時
            else:
                # スコア保存
                self.game_object.last_game_score = self._score
                if self.game_object.high_score < self.game_object.last_game_score:
                    self.game_object.high_score = self._score
                # Phase切り替え
                self.game_object.current_phase = self.game_object.GAME_PHASE_EPILOGUE

    def draw(self):
        """
        描画
        @return: None
        """
        # 画面まっさら
        pyxel.cls(pyxel.COLOR_BLACK)

        # パイプを一つずつ描画
        for _pipe in self._pipes:
            _pipe.draw()

        # プレイヤを描画
        self._player.draw()

        # 10フレーム間はヘルプ表示をする
        if pyxel.frame_count % self.settings.move_frequency == 0:
            if self._counter_for_show_help < 10:
                self._counter_for_show_help += 1
                self.game_object.draw_text_center('Press SPACE to jump the player.', pyxel.COLOR_ORANGE, 5,
                                                  self.game_object.window_object.height - 10,
                                                  self.game_object.window_object.width - 10, 8)

    def is_collision(self):
        """
        ぶつかり判定
        @return: 判定結果
        """
        for _pipe in self._pipes:
            if self._player.is_collision_pipe(_pipe):
                return True

        return self._player.is_collision_window()

    @property
    def player_object(self):
        return self._player

    @property
    def score(self):
        return self._score
