from lib.AbsClass import AbsClass


class AbsPhase(AbsClass):
    """
    ゲームフェーズ基底クラス

    各ゲームフェーズクラスはこれを継承する。
    ライフサイクルとしては、
        1. コンストラクタ(__init__)
        2. フェーズ準備(prepare)
        3. フレーム更新(update)
        4. 画面描画(draw)
        (その後、3と4を繰り返し)
        5. フェーズ終了(clearn)
    となる。
    """

    def __init__(self, game_object, logger=None):
        self._game_object = game_object
        super().__init__(logger)

    def prepare(self):
        """
        フェーズ準備
        @return: None
        """
        pass

    def update(self):
        """
        フレーム更新

        ここにフレーム更新の処理を記述する。
        @return: None
        """
        pass

    def draw(self):
        """
        画面描画

        ここに画面描画の処理を記述する。
        @return:
        """
        pass

    def clearn(self):
        """
        フェーズ終了

        ここにフェーズ終了の処理を記述する。
        @return:
        """

        self.logger.debug('Phase終了開始')
        self.logger.debug('Phase終了完了')

    @property
    def game_object(self):
        return self._game_object

