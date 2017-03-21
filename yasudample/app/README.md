# yasudample
## 概要
サンプルというか作るアプリの骨組みです。
## 使い方
wikiの **mariadbについて** を読み、既にmariadbの初期設定を完了している前提。
## 構成
```
app
│  manage.py
│  
├─app
│  │  settings.py: 設定
│  │  urls.py: ルーティング
│  │  wsgi.py: 本番環境で動かすときはこっち
│  │  __init__.py
│  │  
│  └─__pycache__
│          
├─enzemi: アプリケーション
│  │  admin.py: adminサイト用設定
│  │  apps.py
│  │  forms.py: formの設定
│  │  tests.py
│  │  urls.py: アプリケーションのルーティング
│  │  __init__.py
│  │  
│  ├─migrations: マイグレーションファイルが入る
│  │  │  ・・・
│  │  │  
│  │  └─__pycache__
│  │          ・・・
│  │          
│  ├─models: モデル置き場（テーブルとファイルを1:1にしてみた）
│  │  │  employee_list.py
│  │  │  goal_master.py
│  │  │  holiday_master.py
│  │  │  major_classification_master.py
│  │  │  morning_comment_master.py
│  │  │  morning_task_master.py
│  │  │  night_comment_master.py
│  │  │  night_task_master.py
│  │  │  review_master.py
│  │  │  small_classification_master.py
│  │  │  team_inter.py
│  │  │  team_list.py
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          ・・・
│  │          
│  ├─static: 静的ファイル置き場
│  │  ├─css
│  │  ├─img
│  │  ├─js
│  │  └─plugins
│  │              
│  ├─templates: テンプレート置き場
│  │  ├─enzemi
│  │  │      head.html: ヘッダ
│  │  │      layout.html: レイアウト
│  │  │      login.html: ログインページ
│  │  │      select_date.html: 日付選択
│  │  │      settings.html: 個人設定
│  │  │      
│  │  ├─individual: 個人分析
│  │  │      analysis.html
│  │  │      
│  │  ├─task: タスク
│  │  │      edit.html: タスク編集
│  │  │      new.html: タスク新規作成
│  │  │      show.html: タスク確認
│  │  │      
│  │  └─team: チーム分析
│  │          analysis.html
│  │          
│  ├─views: コントローラ置き場
│  │  │  individual.py
│  │  │  task.py
│  │  │  team.py
│  │  │  views.py
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          ・・・
│  │          
│  └─__pycache__
│             ・・・
│          
└─fixtures
        default.json: テスト用データ
 ```     

### リポジトリ準備準備
1. リポジトリをクローンする  
`git clone https://github.com/d-hisa/WebServiceCo-Development.git`
1. ディレクトリ移動  
`cd WebServiceCo-Development/yasudample/app`
1. GoogleDriveから`secret_settings.py`をDLし、`manage.py`と同じディレクトリに配置  
`GoogleDrive/06.開発用ファイル/secret_settings.py`
1. `secret_settings.py`の中身を必要に応じて書き換え  
特にDB_PW。これは自分の環境でmariadbのrootユーザに指定したパスワードを書く。

### mariadbセッティング
#### maridbを起動
```bash
[Mac]
$ mysql.server start
[Windows]
???
[CentOS]
$ systemctl start mysqld
```
#### mariadbへログイン
```bash
[Mac / CentOS]
$ mysql -uroot
[Windows]
???
```
#### DBを作成
```sql
> create database enzemi
```

### sampleセッティング
> **注意**  
> 仮想環境のactivateを忘れないこと。

下記コマンドを実行
```bash
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py loaddata fixtures/default.json
```
### 動かす
```bash
$ python manage.py runserver
```

### model変更後のmigrate
下記コマンドを実行
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

## 現状
- [朝夜メール画面]
	* 新規登録とタスクの表示（生JSON）
- [個人設定]
	* 個人設定の１つめのユーザの情報更新ができる（id=1をハードコーディングしている）
