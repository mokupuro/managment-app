# managment-app
帝京大学の単位管理アプリ（ハッカソン用）

## git clonで環境をローカルにコピーする
- このレポジトリから```git clone```をする
- venvで作った仮想環境がactivateになっている状態にする
- その状態で```pip install -r requirements.txt```を実行する

## 新しく追加したパッケージを共有したい場合
- ```pip freeze > requirements.txt```

## ファイル構成

<pre>
.
├── coursemanagement
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py（ウェブアプリケーションの設定)
│   ├── urls.py(URLとビューを結びつけるためのファイル)
│   └── wsgi.py(デプロイするときに使う)
└── manage.py(管理コマンド,開発サーバーを起動したり、データベースのマイグレーションなどを行う)
└── managementapp
    ├── __init__.py
    ├── admin.py(Djanogの管理サイトにこのアプリケーションを登録するときに使う)
    ├── apps.py(アプリケーションの設定を行う)
    ├── migrations
    │   └── __init__.py
    ├── models.py(このアプリケーションのモデル,データを保存したり、データベースとやり取りする)
    ├── tests.py(テストを記述する)
    └── views.py(URLにリクエストが来たときに対応する処理を記述する,いわゆるコントローラーにあたる)
</pre>








