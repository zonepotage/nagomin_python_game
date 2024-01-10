# ふらっぴーばーどらしきもの

## 環境
* Python 3.8 (or Higher)

## 依存パッケージ
* configparser
* pyxel

## プロジェクト準備
### PyCharmを使用する場合 (Recommended)
1. フォルダごとプロジェクトファイルとして開く
2. 設定画面を開く (PyCharm -> Settings の順に開く)
3. プロジェクト -> Pythonインタープリター の順に開く
4. "インタープリターの追加"を押下
5. "ローカルインタープリターの追加"を押下
6. "Virtualenv 環境"が選択されていることを確認して"OK"を押下
7. パッケージ一覧上部の"+"を押下し、"configparser"と"pyxel"をそれぞれインストール
8. 設定画面を閉じる
9. 画面右上の"現在のファイル"を押下
10. "実行構成の編集"を押下
11. 左ペインの"新規追加" -> "Python" の順に押下
12. "プロジェクトファイルとして保存"にチェックを入れる
13. scriptの右側にあるテキストボックスに"main.py"を入力
14. "OK"を押して保存する

### その他の場合
1. 以下、コマンドを実行する。(依存パッケージのインストール) 
    ```sh
    pip3 install configparser
    pip3 install pyxel
    ```

## 起動
1. settings.iniを修正する。
2. main.pyを起動する
### PyCharmを使う場合
1. "実行" -> "'main'の実行" の順に押下する ("'main'のデバッグ"を選ぶと、変数の状態などもみられる)
### その他の場合
1. 以下、コマンドを実行する。
    ```sh
    python main.py
    ```

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