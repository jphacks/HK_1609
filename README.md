# Droneco
## 製品概要
### Droneco Tech

### 背景（製品開発のきっかけ、課題等）
####・ドローンの日常利用の提案
####・室内飼い猫の運動不足解消
####・遠隔地にいる飼い主の不安解消
### 製品説明（具体的な製品の説明）
####ドローンが猫とじゃれあい，猫の動画の撮影とYoutubeへの投稿をおこないます．
―

####・ドローンに付けられた猫じゃらしを揺らす
####・猫がじゃれると録画を開始する
####・記録した動画をYoutubeに投稿
####・動画の投稿をTwitterに通知
####・猫語を人語に翻訳しTwitterでつぶやく

### 特長
####1. 特長1
#####遠隔地から猫と遊べる
####2. 特長2
#####起動時にカメラの視野内に猫がいなくても探せる
####3. 特長3
#####遠隔地から猫の様子を観察できる(動画を投稿できる)

### 解決出来ること
####猫の運動不足解消，飼い主の不安解消
### 今後の展望
####1. ドローンの自動操縦
#####遠隔地の飼い主と自宅のネコとのインタラクションの促進, および, 安全な飛行によるネコへの配慮
####2. 
### 注力したこと（こだわり等）
*
*

## 開発技術
### 活用した外部技術
#### API・データ
#####1. YouTube Data API v3
######https://developers.google.com/youtube/v3/
######pythonによりYouTubeへ動画をアップロードする機能, および, その際のユーザデータアクセス認証に必要なOAuth 2.0 プロトコル
#####2. Twitter Application Management と TwitterOAuth
######pythonによりTwitterにツイートする機能, および, その際の認証プログラム

#### フレームワーク・ライブラリ・モジュール
#####1. カメラモジュール(Rasberry Pi)
######ドローン位置からの被写体(ネコ)撮影のため
#####2. LEDモジュール
######カメラモジュールの起動状態, および, 待機状態の確認するため

#### デバイス
#####1. Rasberry Pi
######ドローン位置からのカメラ制御, 動画データのYouTubeアップロード, および, Twitterでの動画リンクURLのツイート
#####2. (ドローン) : バッテリーの故障により, コンセプトとして...

### 独自技術
#### 期間中に開発した独自機能・技術
* 独自で開発したものの内容をこちらに記載してください
* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください（任意）

#### 研究内容（任意）
* もし、製品に研究内容を用いた場合は、研究内容の詳細及び具体的な活用法について、こちらに記載をしてください。
*
