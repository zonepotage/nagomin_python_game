# ふらっぴーばーどらしきもの

## 環境
* Python 3.8

## 利用パッケージ
* configparser
* logging
* pyxel

## ディレクトリ構成
```
.
├── lib ライブラリ格納フォルダ
│    ├─ object オブジェクトクラス格納フォルダ
│    │   ├─ Circle.py 円形オブジェクトクラスファイル
│    │   └─ Rectangle.py 矩形オブジェクトクラスファイル
│    │
│    ├─ phase フェーズクラス格納フォルダ
│    │   ├─ AbsPhase.py フェーズ基底クラスファイル
│    │   ├─ ChapterPhase.py 本編フェーズクラスファイル
│    │   ├─ EpiloguePhase.py エピローグフェーズクラスファイル
│    │   └─ ProloguePhase.py プロローグフェーズクラスファイル
│    │
│    ├─ AbsClass.py 基底クラス
│    ├─ GameApp.py ゲームクラス
│    ├─ Pipe.py パイプクラス
│    ├─ Player.py プレイヤクラス
│    ├─ Settings.py 設定ファイルローダクラス
│    └─ Window.py ウインドウクラス
│
├── app.log アプリケーションログファイル
├── main.py アプリケーションエントリポイント
└── settings.ini 設定ファイル
```

## プロジェクト準備
1. 以下、コマンドを実行する。 
    ```sh
    pip3 install configparser
    pip3 install loggig
    pip3 install pyxel
    ```

## 起動
1. settings.iniを修正する。
2. 以下、コマンドを実行する。
    ```sh
    python main.py
    ```