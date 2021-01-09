from ssl import ALERT_DESCRIPTION_INSUFFICIENT_SECURITY, HAS_NEVER_CHECK_COMMON_NAME
from typing import Text
import discord
from bs4 import BeautifulSoup
from urllib import request
from discord.ext import tasks
from datetime import datetime, timedelta, timezone
import random


#TOKEN読み込み
TOKEN = "hoge"

client = discord.Client()

@client.event
async def on_ready():
  print("logged in\n")

url="https://splatoon.caxdb.com/schedule2.cgi"
k = {"one":"登録なし","two":"登録なし","three":"登録なし","hour":"登録なし","five":"登録なし","six":"登録なし","seven":"登録なし","eight":"登録なし"}

def reload():
 #グローバル変数
  global inf1,inf2,inf3,inf4,inf5,inf6,inf7,inf8,inf9,inf10,inf11,inf12,inf13,inf14,inf15,inf16,inf17,inf18,inf19,inf20,inf21,inf22,inf23,inf24,inf25,inf26,inf27,inf28,buki1,face

  
 # サイトのurl
  response = request.urlopen(url)
  soup = BeautifulSoup(response)
  response.close()

 #スクレイピング
  #now
  inf1 = soup.find_all("ul")[1].text

  #next
  inf2 = soup.find_all("ul")[5].text

  #nextnext
  inf3 = soup.find_all("ul")[9].text

  #now の時間
  inf4 = soup.find_all("li")[0].text
  
  #next の時間
  inf5 = soup.find_all("li")[10].text
  
  #nextnext の時間
  inf6 = soup.find_all("li")[20].text
  
  #レギュラーマッチ(ルール)
  inf7 = soup.find_all("li")[1].text
  
 #ガチマッチ(ルール)
  #now
  inf8 = soup.find_all("li")[4].text

  #nowの用語変換
  if inf8 == "ガチマッチ(ガチホコバトル)": 
	  inf8 = "ガチホコバトル"
  elif inf8 == "ガチマッチ(ガチヤグラ)":
	  inf8 = "ガチヤグラ"
  elif inf8 == "ガチマッチ(ガチアサリ)":
	  inf8 = "ガチアサリ"
  elif inf8 == "ガチマッチ(ガチエリア)":
	  inf8 = "ガチエリア"

  #next
  inf9 = soup.find_all("li")[14].text

  #nextnextの用語変換
  if inf9 == "ガチマッチ(ガチホコバトル)": 
	  inf9 = "ガチホコバトル"
  elif inf9 == "ガチマッチ(ガチヤグラ)":
	  inf9 = "ガチヤグラ"
  elif inf9 == "ガチマッチ(ガチアサリ)":
	  inf9 = "ガチアサリ"
  elif inf9 == "ガチマッチ(ガチエリア)":
	  inf9 = "ガチエリア"

  #nextnext
  inf10 = soup.find_all("li")[24].text
  #nextnextの用語変換
  if inf10 == "ガチマッチ(ガチホコバトル)": 
	  inf10 = "ガチホコバトル"
  elif inf10 == "ガチマッチ(ガチヤグラ)":
	  inf10 = "ガチヤグラ"
  elif inf10 == "ガチマッチ(ガチアサリ)":
    inf10 = "ガチアサリ"
  elif inf10 == "ガチマッチ(ガチエリア)":
	  inf10 = "ガチエリア"

		  
 #リーグマッチ(ルール)
  # #now
  inf11 = soup.find_all("li")[7].text

  #nowの用語変換
  if inf11 == "リーグマッチ(ガチホコバトル)": 
    inf11 = "ガチホコバトル"
  elif inf11 == "リーグマッチ(ガチヤグラ)":
    inf11 = "ガチヤグラ"
  elif inf11 == "リーグマッチ(ガチアサリ)":
    inf11 = "ガチアサリ"
  elif inf11 == "リーグマッチ(ガチエリア)":
    inf11 = "ガチエリア"
      
  #next
  inf12 = soup.find_all("li")[17].text

  #nextの用語変換
  if inf12 == "リーグマッチ(ガチホコバトル)": 
	  inf12 = "ガチホコバトル"
  elif inf12 == "リーグマッチ(ガチヤグラ)":
	  inf12 = "ガチヤグラ"
  elif inf12 == "リーグマッチ(ガチアサリ)":
	  inf12 = "ガチアサリ"
  elif inf12 == "リーグマッチ(ガチエリア)":
	  inf12 = "ガチエリア"

  #nextnext
  inf13 = soup.find_all("li")[27].text

  #nextnextの用語変換
  if inf13 == "リーグマッチ(ガチホコバトル)": 
	  inf13 = "ガチホコバトル"
  elif inf13 == "リーグマッチ(ガチヤグラ)":
	  inf13 = "ガチヤグラ"
  elif inf13 == "リーグマッチ(ガチアサリ)":
	  inf13 = "ガチアサリ"
  elif inf13 == "リーグマッチ(ガチエリア)":
	  inf13 = "ガチエリア"


  #レギュラーマッチ(ステージ)
  inf14 = soup.find_all("ul")[2].text#now
  inf15 = soup.find_all("ul")[7].text#next
  inf16 = soup.find_all("ul")[12].text#nextnext

  #ガチマッチ(ステージ)
  inf17 = soup.find_all("ul")[3].text#now
  inf18 = soup.find_all("ul")[8].text#next
  inf19 = soup.find_all("ul")[11].text#nextnext

  #リーグマッチ(ステージ)
  inf20 = soup.find_all("ul")[4].text#now
  inf21 = soup.find_all("ul")[8].text#next
  inf22 = soup.find_all("ul")[12].text#nextnext

  #ランダム(武器)
  buki1 = ("スプラシューターコラボ",".52ガロン","わかばシューター",".96ガロンデコ","シャープマーカー","N-ZAP89","N-ZAP85","プライムシューター","シャープマーカーネオ","ボールドマーカー","ボールドマーカーネオ","プロモデラーRG","スプラシューター",".52ガロンデコ","L3リールガンD","ジェットスイーパーカスタム","プライムシューターコラボ","もみじシューター","プロモデラーMG","H3リールガンチェリー",".96ガロン","ボールドマーカー7","N-ZAP83","L3リールガン","ジェットスイーパー","H3リールガン","プロモデラーPG","H3リールガンD","ボトルガイザー","ボトルガイザーフォイル","スプラシューターベッチュー","プライムシューターベッチュー","おちばシューター","H3リールガンチェリー",".52ガロンベッチュー","デュアルスイーパー","デュアルスイーパーカスタム","スプラマニューバー","スプラマニューバーコラボ","スパッタリー","ケルビン525","スパッタリー・ヒュー","クアッドホッパーブラック","ケルビン525デコ","クアッドホッパーホワイト","スプラマニューバーベッチュー","ケルビン525ベッチュー","スパッタリークリア","スプラスコープ","スクイックリンα","スプラチャージャー","14式竹筒銃・甲","スクイックリンγ","14式竹筒銃・丙","スクイックリンβ","14式竹筒銃・乙","ソイチューバー","スプラチャージャー コラボ","スプラスコープ コラボ","リッター4K","4Kスコープ","リッター4kカスタム","4kスコープカスタム","ソイチューバーカスタム","スプラチャージャーベッチュー","スプラスコープベッチュー","ノヴァブラスターネオ","ロングブラスターカスタム","ホットブラスターカスタム","ノヴァブラスター","ラピッドブラスター","ロングブラスターネクロ","ホットブラスター","Rブラスターエリートデコ","Rブラスターエリート","ラピッドブラスターデコ","ロングブラスター","クラッシュブラスター","クラッシュブラスターネオ","ノヴァブラスターベッチュー","ラピッドブラスターベッチュー","ダイナモローラー","スプラローラーコラボ","カーボンローラー","ダイナモローラーテスラ","スプラローラー","カーボンローラーデコ","ヴァリアブルローラー","ヴァリアブルローラーフォイル","スプラローラーベッチュー","ダイナモローラーベッチュー","ホクサイ","パブロ","ホクサイ・ヒュー","パーマネント・パブロ","パブロ・ヒュー","ホクサイベッチュー","バケットスロッシャー","ヒッセン","スクリュースロッシャー","バケットスロッシャーデコ","バケットスロッシャーソーダ","ヒッセン・ヒュー","スクリュースロッシャーネオ","エクスプロッシャー","オーバーフロッシャー","スクリュースロッシャーベッチュー","エクスプロッシャーカスタム","オーバーフロッシャーデコ","スプラスピナーコラボ","バレルスピナーデコ","ハイドラントカスタム","バレルスピナー","バレルスピナーリミックス","ハイドラント","スプラスピナー","クーゲルシュライバー","ノーチラス47","クーゲルシュライバー・ヒュー","ノーチラス79","スプラスピナーベッチュー","パラシェルター","キャンピングシェルター","スパイガジェット","パラシェルターソレーラ","スパイガジェットソレーラ","キャンピングシェルターソレーラ","スパイガジェットベッチュー","キャンピングシェルターカーモ")
  
  #出力用語
  inf23 = "レギュラーマッチ\n" + "\n" + "now　("+ inf4 + ")\n" + inf14 +"\n" + "next　("+ inf5 + ")\n"  + inf15 +"\n" + "nextnext　(" + inf6 + ")\n" + inf16
  inf24 = "ガチマッチ\n" + "\n" + "now　("+ inf4 + ")\n\n" + inf8 +"\n" + inf17 +"\n" + "next　("+ inf5 + ")\n\n" + inf9 + "\n" + inf18 +"\n" + "nextnext　(" + inf6 + ")\n\n" + inf10 +"\n" + inf19
  inf25 = "リーグマッチ\n" + "\n" + "now　("+ inf4 + ")\n\n" + inf11 +"\n" + inf20 +"\n" + "next　("+ inf5 + ")\n\n" + inf12 + "\n" + inf21 +"\n" + "nextnext　(" + inf6 + ")\n\n" + inf13 +"\n" + inf22
  inf26 = "now　(" + inf4 + ")\n\n" + inf1
  inf27 = "next　(" + inf5 + ")\n\n" + inf2
  inf28 = "nextnext　(" + inf6 + ")\n\n" + inf3

  face = "変数"

JST = timezone(timedelta(hours=+9), "JST")

@tasks.loop(seconds=60)
async def loop():
  now = datetime.now(JST).strftime("%H:%M")
  if now == "01:06":
    reload()
  if now == "03:06":
    reload()
  if now == "05:06":
    reload()
  if now == "07:06":
    reload()
  if now == "09:06":
    reload()
  if now == "11:06":
    reload()
  if now == "13:06":
    reload()
  if now == "15:06":
    reload()
  if now == "17:06":
    reload()
  if now == "19:06":
    reload()
  if now == "21:06":
    reload()
  if now == "23:06":
    reload()
  


@client.event

async def on_ready():

	print("logged in\n")


@client.event

async def on_message(message):

  team1 = "a"
  team2 = "a"
  team3 = "a"
  team4 = "a"
  team5 = "a"
  team6 = "a"
  team7 = "a"
  team8 = "a"

  if message.author.bot:
    return

  def check(msg):
    return msg.author == message.author

  if message.content == "!ping":
    await message.channel.send("pong!")

  if message.content == "ち１":

    await message.channel.send("チーム分けの１人目を登録するぞ!!\n名前を次に送ってね!!")
    await message.channel.send(k["one"])
    k["one"] = await client.wait_for("message", check=check)
    await message.channel.send("１人目に登録した名前の確認「 " + k["one"].content + " 」")
    #face = team1.content
    
  elif message.content == "ち２":
    await message.channel.send("チーム分けの2人目を登録するぞ!!\n名前を次に送ってね!!")
    team2 = await client.wait_for("message", check=check)
    await message.channel.send("２人目に登録した名前の確認「 " + team2.content + " 」")

  elif message.content == "ち３":
    await message.channel.send("チーム分けの3人目を登録するぞ!!\n名前を次に送ってね!!")
    team3 = await client.wait_for("message", check=check)
    await message.channel.send("３人目に登録した名前の確認「 " + team3.content + " 」")

  elif message.content == "ち４":
    await message.channel.send("チーム分けの4人目を登録するぞ!!\n名前を次に送ってね!!")
    team4 = await client.wait_for("message", check=check)
    await message.channel.send("４人目に登録した名前の確認「 " + team4.content + " 」")

  elif message.content == "ち５":
    await message.channel.send("チーム分けの5人目を登録するぞ!!\n名前を次に送ってね!!")
    team5 = await client.wait_for("message", check=check)
    await message.channel.send("５人目に登録した名前の確認「 " + team5.content + " 」")

  elif message.content == "ち６":
    await message.channel.send("チーム分けの6人目を登録するぞ!!\n名前を次に送ってね!!")
    team6 = await client.wait_for("message", check=check)
    await message.channel.send("６人目に登録した名前の確認「 " + team6.content + " 」")

  elif message.content == "ち７":
    await message.channel.send("チーム分けの7人目を登録するぞ!!\n名前を次に送ってね!!")
    team7 = await client.wait_for("message", check=check)
    await message.channel.send("７人目に登録した名前の確認「 " + team7.content + " 」")

  elif message.content == "ち８":
    await message.channel.send("チーム分けの8人目を登録するぞ!!\n名前を次に送ってね!!")
    team8 = await client.wait_for("message", check=check)
    await message.channel.send("８人目に登録した名前の確認「 " + team8.content + " 」")

  elif message.content == "チームメンバー":
    await message.channel.send("１人目　「" + face + "」\n２人目　「" + team2 + "」\n３人目　「" + team3 + "」\n４人目　「" + team4 + "」\n５人目　「" + team5 + "」\n６人目　「" + team6 + "」\n７人目　「" + team7 + "」\n８人目　「" + team8 + "」\n")

  elif message.content == "メンバーリセット":
    team1 = "登録なし"
    team2 = "登録なし"
    team3 = "登録なし"
    team4 = "登録なし"
    team5 = "登録なし"
    team6 = "登録なし"
    team7 = "登録なし"
    team8 = "登録なし"

    await message.channel.send("メンバーをリセットしたぞ!!")
  if message.content == "いま":
    await message.channel.send(inf26)

  elif message.content == "つぎ":
    await message.channel.send(inf27)

  elif message.content == "つぎつぎ":
    await message.channel.send(inf28)

  elif message.content == "れぎ":
    await message.channel.send(inf23)
	
  elif message.content == "がち":
    await message.channel.send(inf24)

  elif message.content == "りぐ":
    await message.channel.send(inf25)

  elif message.content == "ぶき":

    await message.channel.send("おすすめの武器は…\n\n「" + random.choice(buki1) + "」\n\nだ!!" )
    
  elif message.content == "チーム":

    ing=[ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ,]
    ing = random.sample(ing, 8)
    a = str(ing[:4])
    b = str(ing[4:])
    await message.channel.send("チーム分けでのチーム編成は…\n\n" + "Aチーム　" + a + "\n\n" + "Bチーム　" + b +"\n\n" + "だ!!")

  elif message.content == "チーム分け":

    x = [team1.content,team2.comtent,team3.content,team4.content]
    s = [team5.content,team6.content,team7.content,team8.content]
    x = random.sample(x, 4)
    s = random.sample(s, 4)
    c = str(x[:2])
    d = str(x[2:])
    e = str(s[:2])
    f = str(s[2:])

    g = ("レギュラーマッチ","ガチホコバト","ガチヤグラ","ガチアサリ","ガチエリア")


    await message.channel.send("チーム分けでのチーム編成は…\n\n" + "Aチーム　" + c + f +  "\n\n" + "Bチーム　" + d + e + "\n\n" + "だ!!\n\nルールは…　　「" + random.choice(g) + "」　だ!!")

  elif message.content == "目次":
    await message.channel.send("「いま」と打つと今のステージ情報が、「つぎ」を打つと次のステージ情報が、「つぎつぎ」と打つと次の次のステージ情報がでるぞ!!\nまた、「れぎ」と打つとレギュラーマッチの、「がち」と打つとガチマッチの「りぐ」と打つとリーグマッチの今、次、次の次のステージ情報とルールが出るぞ!!\nどうしても使いたい武器がない場合には「ぶき」と打ってみよう!!おすすめの武器を選ぶぞ!!\n８人でチーム分けをするやり方は「チーム分け説明」で見れるぞ!!")
    #8人でリーグマッチをやるときは「チーム」と打ってみよう!!チームをランダムで編成するぞ!!\n8人そろって誰がやるかが分かっていたら「チーム分け」と打ってみよう!!
	
  elif message.contenr == "チーム分け説明":
    await message.content.send("")

if __name__ == "__main__":
  reload()
  loop.start()
  client.run(TOKEN)