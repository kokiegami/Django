# Django Voting App

Djangoを使用した投票アプリです。

## 機能
- 質問と選択肢を表示
- ユーザーが選択肢に投票
- 投票結果を表示
- 管理者画面で質問と選択肢の管理

## 必要条件
- Python 3.x
- Django 3.x以上
- データベース（SQLiteを使用）

## セットアップ手順

以下の手順でローカル開発環境をセットアップできます。

### 1. 仮想環境のセットアップ
python -m venv myenv
source myenv/bin/activate

### 2. 必要なライブラリのインストール
pip install django

### 3.プロジェクト設定
cd /path/to/your/django-project
python manage.py migrate

### 4.管理者ユーザーの作成
python manage.py createsuperuser

### 5.サーバー起動
python manage.py runserver

サーバーが立ち上がったら、以下のURLにアクセスしてアプリケーションを確認できます。
管理者画面: http://127.0.0.1:8000/admin/
管理者画面にログインして、質問（Question）と選択肢（Choice）を管理画面から追加します。

ユーザー用ページ: http://127.0.0.1:8000/polls/
管理者画面で追加した質問とその選択肢が表示されます。
選択肢を選んで「投票」ボタンをクリックすると、投票結果が反映されます。

以上となります。
