# til

## これは何？

- Today I Learned
- 航海日誌型知識ベース
    - 事実ベースの学びと考察を記述して残す
    - アイデアの種をまとめておく
- 思考の整理学のメタノートのアイデアを参考にする

## フォルダ構成

```
til/
├── logbook/                  # 日々の学び
│   ├── yyyy-MM-dd.md
│   └── ...
├── tips/                     # 技術・知識系
│   ├── programming/
│   ├── system-design/
│   ├── db/
│   └── ...
├── ideas/                    # 普遍的な学び・思考メモ
│   ├── learning/
│   ├── philosophy/
│   └── ...
└── scripts/                  # 自動処理用Pythonスクリプト
```

## 運用方法

- 基本方針
    - logbookに毎日の記録を書く
    - 特に残したい内容はtips(技術関連)、ideas(技術以外の学びや思考)に移す
- フォーマット
    - 冒頭に日付とtagリストを付与する
    - ##(見出し2)ごとにタグ付けをする(#idea等)
        - 現在のタグはtag_index.jsonを参照
- スクリプトの実行
    - `uvx nox -s check`: タグが設定されているかチェックする
    - `uvx nox -s index`: タグインデックスの整理
- TODO: タグ一覧スクリプト、タグの階層化整理(rはprogrammingに入れる等)
