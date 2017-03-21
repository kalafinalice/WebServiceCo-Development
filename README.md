# WebServiceCo-Development
For Engineering seminar "Try to co-development of web service"

## 開発にあたって
1. まず、wikiの以下のページを読んで、環境をなんとかしよう。
	- [はじめに](https://github.com/d-hisa/WebServiceCo-Development/wiki/%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB):githubでの開発の流れとか
	- [mariaDBについて](https://github.com/d-hisa/WebServiceCo-Development/wiki/mariaDB%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6):開発するのに必要なmariadbについて。Mysqlの方も見るとなおよい
1. [yasudanmpleの使い方](./yasudample/app/README.md)を読んでyasudampleの使い方を見よう
1. がんばって開発しよう

## 実装上の禁則事項
- IPアドレスをソースに含めない
	* 一応コミット時に差分ファイルにIP文字列が含まれているかのチェックをしています
- 特定されるような情報をコードに含めない
	* よく内部で使われているパスワードとか、個人を特定しやすい文字列などを含めないこと。
