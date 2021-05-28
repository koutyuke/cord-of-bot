from ssl import ALERT_DESCRIPTION_INSUFFICIENT_SECURITY, HAS_NEVER_CHECK_COMMON_NAME, PROTOCOL_TLSv1_1
from typing import List, Text
import discord
from bs4 import BeautifulSoup
from urllib import request
from discord import team
from discord import message
from discord.ext import tasks
from datetime import datetime, timedelta, timezone
import random
from time import sleep

intents = discord.Intents.default()
intents.members = True
# intents=discord.Intents.all()
client = discord.Client(intents=intents)


# TOKEN読み込み
TOKEN = "hoge hoge hoge"

#client = discord.Client()


@client.event
async def on_ready():
    print("logged in\n")

urls = "https://splatoon.caxdb.com/schedule2.cgi"


k1 = {1: "登録", 2: "登録", 3: "登録", 4: "登録", 5: "登録",6: "登録", 7: "登録", 8: "登録", "チーム分けメンバー": "あ"}
k2 = {1: "LYE", 2: "AYU", 3: "にこちゃん", 4: "せいな", 5: "ギン",6: "登録なし", 7: "ぱるる", 8: "社畜", 9: "なし", 10: "メンバー"}
k3 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}  # 基礎ポイント
k4 = {1:[0,0,0,0,0,0,0,0,0,0]}
k5 = {1: 5}  # 0

member_touroku = {1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3}
member_hozonn = {1: [0, 0, 0, 0, 0, 0, 0, 0]}
heikinwake = {1: ["登録なし", "登録なし", "登録なし", "登録なし", "登録なし", "登録なし", "登録なし", "登録なし"], 2: [0, 0, 0, 0, 0, 0, 0, 0], 3: [1, 2, 3, 4, 5, 6, 7, 8], 4: [1, 2, 3, 4, 5, 6, 7, 8], 5: [0, 0, 0, 0, 0, 0, 0, 0], 6: [1, 2, 3, 4, 5, 6, 7, 8]}  # 1メンバー 2ポイント　3ランダムの数　4ランダムのための数列　5基礎ポ　６うごく
channel_id = {1: 788349336735580171, 2: 792725056341409883, 3: 792725353532751892, 4: 123} #チャンネルID
messagee = {1: 12, 2: 123, 3: 123} #1:メッセージ設定
messaji = {1: 12, 2: 123, 3: 123}
move_member_id = {1: [0, 0, 0, 0, 0, 0, 0, 0]}
mooove = {1: 1, 2: []}
riaction_list = {1: ["🇦", "🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮", "🇯", "🇰", "🇱", "🇲", "🇳", "🇴", "🇵", "🇶", "🇷", "🇸", "🇹", "🇺", "🇻", "🇼", "🇽", "🇾", "🇿"], 2: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 3: ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣","7️⃣", "8️⃣","9⃣"], 4: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 5: ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"], 6: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
check1 = {1: 0, 2: 0, 3: 0, 4: 0}
list_number = {1: 0}


def reload():
 # グローバル変数
    global inf1, inf2, inf3, inf4, inf5, inf6, inf7, inf8, inf9, inf10, inf11, inf12, inf13, inf14, inf15, inf16, inf17, inf18, inf19, inf20, inf21, inf22, inf23, inf24, inf25, inf26, inf27, inf28, buki1
 # サイトのurl
    response = request.urlopen(urls)
    soup = BeautifulSoup(response)
    response.close()
 # スクレイピング
    # now
    inf1 = soup.find_all("ul")[1].text

    # next
    inf2 = soup.find_all("ul")[5].text

    # nextnext
    inf3 = soup.find_all("ul")[9].text

    # now の時間
    inf4 = soup.find_all("li")[0].text

    # next の時間
    inf5 = soup.find_all("li")[10].text

    # nextnext の時間
    inf6 = soup.find_all("li")[20].text

    # レギュラーマッチ(ルール)
    inf7 = soup.find_all("li")[1].text

    # ガチマッチ(ルール)
    # now
    inf8 = soup.find_all("li")[4].text

    # nowの用語変換　歯よ関数化を
    if inf8 == "ガチマッチ(ガチホコバトル)":
        inf8 = "ガチホコバトル"
    elif inf8 == "ガチマッチ(ガチヤグラ)":
        inf8 = "ガチヤグラ"
    elif inf8 == "ガチマッチ(ガチアサリ)":
        inf8 = "ガチアサリ"
    elif inf8 == "ガチマッチ(ガチエリア)":
        inf8 = "ガチエリア"

    # next
    inf9 = soup.find_all("li")[14].text

    # nextnextの用語変換
    if inf9 == "ガチマッチ(ガチホコバトル)":
        inf9 = "ガチホコバトル"
    elif inf9 == "ガチマッチ(ガチヤグラ)":
        inf9 = "ガチヤグラ"
    elif inf9 == "ガチマッチ(ガチアサリ)":
        inf9 = "ガチアサリ"
    elif inf9 == "ガチマッチ(ガチエリア)":
        inf9 = "ガチエリア"

    # nextnext
    inf10 = soup.find_all("li")[24].text
    # nextnextの用語変換
    if inf10 == "ガチマッチ(ガチホコバトル)":
        inf10 = "ガチホコバトル"
    elif inf10 == "ガチマッチ(ガチヤグラ)":
        inf10 = "ガチヤグラ"
    elif inf10 == "ガチマッチ(ガチアサリ)":
        inf10 = "ガチアサリ"
    elif inf10 == "ガチマッチ(ガチエリア)":
        inf10 = "ガチエリア"

    # リーグマッチ(ルール)
    # #now
    inf11 = soup.find_all("li")[7].text

    # nowの用語変換
    if inf11 == "リーグマッチ(ガチホコバトル)":
        inf11 = "ガチホコバトル"
    elif inf11 == "リーグマッチ(ガチヤグラ)":
        inf11 = "ガチヤグラ"
    elif inf11 == "リーグマッチ(ガチアサリ)":
        inf11 = "ガチアサリ"
    elif inf11 == "リーグマッチ(ガチエリア)":
        inf11 = "ガチエリア"

    # next
    inf12 = soup.find_all("li")[17].text

    # nextの用語変換
    if inf12 == "リーグマッチ(ガチホコバトル)":
        inf12 = "ガチホコバトル"
    elif inf12 == "リーグマッチ(ガチヤグラ)":
        inf12 = "ガチヤグラ"
    elif inf12 == "リーグマッチ(ガチアサリ)":
        inf12 = "ガチアサリ"
    elif inf12 == "リーグマッチ(ガチエリア)":
        inf12 = "ガチエリア"

    # nextnext
    inf13 = soup.find_all("li")[27].text

    # nextnextの用語変換
    if inf13 == "リーグマッチ(ガチホコバトル)":
        inf13 = "ガチホコバトル"
    elif inf13 == "リーグマッチ(ガチヤグラ)":
        inf13 = "ガチヤグラ"
    elif inf13 == "リーグマッチ(ガチアサリ)":
        inf13 = "ガチアサリ"
    elif inf13 == "リーグマッチ(ガチエリア)":
        inf13 = "ガチエリア"

    # レギュラーマッチ(ステージ)
    inf14 = soup.find_all("ul")[2].text  # now
    inf15 = soup.find_all("ul")[7].text  # next
    inf16 = soup.find_all("ul")[12].text  # nextnext

    # ガチマッチ(ステージ)
    inf17 = soup.find_all("ul")[3].text  # now
    inf18 = soup.find_all("ul")[8].text  # next
    inf19 = soup.find_all("ul")[11].text  # nextnext

    # リーグマッチ(ステージ)
    inf20 = soup.find_all("ul")[4].text  # now
    inf21 = soup.find_all("ul")[8].text  # next
    inf22 = soup.find_all("ul")[12].text  # nextnext

    # ランダム(武器)
    buki1 = ("スプラシューターコラボ", ".52ガロン", "わかばシューター", ".96ガロンデコ", "シャープマーカー", "N-ZAP89", "N-ZAP85", "プライムシューター", "シャープマーカーネオ", "ボールドマーカー", "ボールドマーカーネオ", "プロモデラーRG", "スプラシューター", ".52ガロンデコ", "L3リールガンD", "ジェットスイーパーカスタム", "プライムシューターコラボ", "もみじシューター", "プロモデラーMG", "H3リールガンチェリー", ".96ガロン", "ボールドマーカー7", "N-ZAP83", "L3リールガン", "ジェットスイーパー", "H3リールガン", "プロモデラーPG", "H3リールガンD", "ボトルガイザー", "ボトルガイザーフォイル", "スプラシューターベッチュー", "プライムシューターベッチュー", "おちばシューター", "H3リールガンチェリー", ".52ガロンベッチュー", "デュアルスイーパー", "デュアルスイーパーカスタム", "スプラマニューバー", "スプラマニューバーコラボ", "スパッタリー", "ケルビン525", "スパッタリー・ヒュー", "クアッドホッパーブラック", "ケルビン525デコ", "クアッドホッパーホワイト", "スプラマニューバーベッチュー", "ケルビン525ベッチュー", "スパッタリークリア", "スプラスコープ", "スクイックリンα", "スプラチャージャー", "14式竹筒銃・甲", "スクイックリンγ", "14式竹筒銃・丙", "スクイックリンβ", "14式竹筒銃・乙", "ソイチューバー", "スプラチャージャー コラボ", "スプラスコープ コラボ", "リッター4K", "4Kスコープ", "リッター4kカスタム", "4kスコープカスタム", "ソイチューバーカスタム", "スプラチャージャーベッチュー", "スプラスコープベッチュー","ノヴァブラスターネオ", "ロングブラスターカスタム", "ホットブラスターカスタム", "ノヴァブラスター", "ラピッドブラスター", "ロングブラスターネクロ", "ホットブラスター", "Rブラスターエリートデコ", "Rブラスターエリート", "ラピッドブラスターデコ", "ロングブラスター", "クラッシュブラスター", "クラッシュブラスターネオ", "ノヴァブラスターベッチュー", "ラピッドブラスターベッチュー", "ダイナモローラー", "スプラローラーコラボ", "カーボンローラー", "ダイナモローラーテスラ", "スプラローラー", "カーボンローラーデコ", "ヴァリアブルローラー", "ヴァリアブルローラーフォイル", "スプラローラーベッチュー", "ダイナモローラーベッチュー", "ホクサイ", "パブロ", "ホクサイ・ヒュー", "パーマネント・パブロ", "パブロ・ヒュー", "ホクサイベッチュー", "バケットスロッシャー", "ヒッセン", "スクリュースロッシャー", "バケットスロッシャーデコ", "バケットスロッシャーソーダ", "ヒッセン・ヒュー", "スクリュースロッシャーネオ", "エクスプロッシャー", "オーバーフロッシャー", "スクリュースロッシャーベッチュー", "エクスプロッシャーカスタム", "オーバーフロッシャーデコ", "スプラスピナーコラボ", "バレルスピナーデコ", "ハイドラントカスタム", "バレルスピナー", "バレルスピナーリミックス", "ハイドラント", "スプラスピナー", "クーゲルシュライバー", "ノーチラス47", "クーゲルシュライバー・ヒュー", "ノーチラス79", "スプラスピナーベッチュー", "パラシェルター", "キャンピングシェルター", "スパイガジェット", "パラシェルターソレーラ", "スパイガジェットソレーラ", "キャンピングシェルターソレーラ", "スパイガジェットベッチュー", "キャンピングシェルターカーモ")

    # 出力用語  f文字列を知っていれば…

    inf23 = "レギュラーマッチ\n" + "\n" + "now　(" + inf4 + ")\n" + inf14 + "\n" + "next　(" + inf5 + ")\n" + inf15 + "\n" + "nextnext　(" + inf6 + ")\n" + inf16
    inf24 = "ガチマッチ\n" + "\n" + "now　(" + inf4 + ")\n\n" + inf8 + "\n" + inf17 + "\n" + "next　(" + inf5 + ")\n\n" + inf9 + "\n" + inf18 + "\n" + "nextnext　(" + inf6 + ")\n\n" + inf10 + "\n" + inf19
    inf25 = "リーグマッチ\n" + "\n" + "now　(" + inf4 + ")\n\n" + inf11 + "\n" + inf20 + "\n" + "next　(" +inf5 + ")\n\n" + inf12 + "\n" + inf21 + "\n" + "nextnext　(" + inf6 + ")\n\n" + inf13 + "\n" + inf22
    inf26 = "now　(" + inf4 + ")\n\n" + inf1
    inf27 = "next　(" + inf5 + ")\n\n" + inf2
    inf28 = "nextnext　(" + inf6 + ")\n\n" + inf3
    


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
async def on_raw_reaction_add(payload):

    role_list = ["1", "2", "3", "4", "5", "6", "7", "8"]
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
    member = payload.member

    if not str(payload.member) == "Splatoon stage bot v.3.11#9128":
        if mooove[1] == 1:
            for i in range(8):
                if str(payload.emoji.name) == riaction_list[3][i]:
                    role = guild.get_role(riaction_list[4][i])
                    await member.add_roles(role)

        elif mooove[1] == 2:
            for i in range(8):
                if str(payload.emoji.name) == riaction_list[3][i]:
                    print(payload.emoji.name)
                    role = guild.get_role(riaction_list[4][i])
                    h = [roles.name for roles in member.roles]
                    l = len(h)
                    for ii in range(l):
                        for b in range(8):
                            if str(h[ii]) == role_list[b]:
                                await messaji[1].remove_reaction(riaction_list[3][b], member)
                    await member.add_roles(role)
                    # await grant_move_role(payload = payload,role_point = role_number_kist[i],move_number=move_number[1],emoji_list=emoji_list[i])

        elif mooove[1] == 3:
            for g in range(26):
                if str(payload.emoji.name) == riaction_list[1][g]:
                    for h in range(len(riaction_list[2])):
                        if riaction_list[2][h] == 1:
                            await messagee[1].remove_reaction(str(riaction_list[1][h]), member)
                            riaction_list[2][h] = 0
                    riaction_list[2][g] = 1

                elif str(payload.emoji.name) == "✅":
                    for gh in range(26):
                        if riaction_list[2][gh] == 1:
                            check1[3] += 1

                    if check1[3] == 1:
                        for gg in range(26):
                            if riaction_list[2][gg] == 1:
                                check1[1] = 1
                                check1[2] = gg
                                await messagee[1].clear_reactions()
                                break
                        break
                    else:
                        await messagee[1].remove_reaction("✅", payload.member)
                        check1[4] = 1
                        break

                elif str(payload.emoji.name) == "☑":
                    check1[1] = 2
                    for re in range(len(riaction_list[6])):
                        riaction_list[6][re] = 0
                    await messagee[1].clear_reactions()
                    break

        elif mooove[1] == 4:
            for g in range(len(riaction_list[5])):

                if str(payload.emoji.name) == riaction_list[5][g]:
                    if riaction_list[6][9] == 1:
                        await messagee[1].remove_reaction("✔",member)
                    for h in range(8):
                        if riaction_list[6][h] == 1:
                            await messagee[1].remove_reaction(str(riaction_list[5][h]), member)
                            riaction_list[6][h] = 0
                    riaction_list[6][g] = 1
                    break

                elif str(payload.emoji.name) == "✅":
                    for gg in range(len(riaction_list[6])):
                        if riaction_list[6][gg] == 1:
                            check1[3] += 1

                    if check1[3] == 1:
                        for ggg in range(len(riaction_list[6])):
                            if riaction_list[6][ggg] == 1:
                                check1[1] = 1
                                check1[2] = ggg
                                await messagee[1].clear_reactions()
                        check1[4] = 1
                        break
                    else:
                        await messagee[1].remove_reaction("✅", payload.member)
                        check1[4] = 1
                        break

                elif str(payload.emoji.name) == "☑":
                    check1[1] = 2
                    for re in range(len(riaction_list[6])):
                        riaction_list[6][re] = 0
                    await messagee[1].clear_reactions()
                    break

                elif str(payload.emoji.name) == "✔":
                    for h in range(len(riaction_list[4])):
                        if riaction_list[6][h] == 1:
                            try:await messagee[1].remove_reaction(str(riaction_list[5][h]), member)
                            except:pass
                            riaction_list[6][h] = 0
                    riaction_list[6][9] = 1       
        
        elif mooove[1] == 5:
            emoji = payload.emoji.name
            if str(emoji) != "✅" and str(payload.emoji.name) != "☑" and str(payload.emoji.name) != "✔":
                if k4[1][9] == 1:
                    k4[1][9] = 0
                    await messagee[1].remove_reaction("✔",payload.member)
                for un in range(9):
                    if str(emoji) == str(riaction_list[3][un]):
                        k4[1][un] = 1
                        print(k4[1])

            elif str(emoji) == "✅":
                for j in range(len(k4[1])):
                    if k4[1][j] == 1:
                        check1[3] += 1
                if check1[3] != 0:
                    check1[1] = 1
                    await messagee[1].clear_reactions()
                else:
                    await messagee[1].remove_reaction("✅",payload.member)
                print(k4[1])

            elif str(emoji) == "☑":
                check1[1] = 2
                await messagee[1].clear_reactions()
                
            elif str(emoji) == "✔":
                for emo in range(8):
                    if k4[1][emo] == 1:
                        await messagee[1].remove_reaction(riaction_list[3][emo],payload.member)
                k4[1][9] = 1

@client.event
async def on_raw_reaction_remove(payload):
    emoji_list = riaction_list[3]
    role_number_kist = riaction_list[4]
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

    member = guild.get_member(payload.user_id)
    if not str(payload.member) == "Splatoon stage bot v.3.11#9128":
        if mooove[1] == 1 or mooove[1] == 2:
            for i in range(8):
                if str(payload.emoji.name) == emoji_list[i]:
                    role = guild.get_role(role_number_kist[i])
                    await member.remove_roles(role)

        elif mooove[1] == 3:
            if str(payload.emoji.name) == "✔":
                riaction_list[2][27] = 0
            for i in range(len(riaction_list[1])):
                if str(payload.emoji.name) == riaction_list[1][i]:
                    riaction_list[2][i] = 0
        elif mooove[1] == 4:
            for i in range(len(riaction_list[5])):
                if str(payload.emoji.name) == riaction_list[1][i]:
                    riaction_list[6][i] = 0
        elif mooove[1] == 5:
            if str(payload.emoji.name) == "✔":
                k4[1][9] = 0
                print(k4[1])
            else:
                for e in range(9):
                    if str(riaction_list[3][e]) == str(payload.emoji.name):
                        k4[1][e] = 0
                        print(k4[1])
                        break


@client.event
async def on_message(message):

    if message.author.bot:
        return

    def check(msg):
        return msg.author == message.author

    def team_choise(g):
        for e in range(1, g):
            for ee in range(1, 9):
                if 1 == member_touroku[ee]:
                    k1[e] = k2[ee]
                    member_touroku[ee] = 0
                    break

    def team_member():
        for i in range(1, 9):
            if not k2[i] == "登録なし":
                member_touroku[i] = 1
            else:
                member_touroku[i] = 0

    def team_choise_count(p, q):
        k1["チーム分けメンバー"] = "チーム分けでのチーム編成は…\n\n"
        x = [k1[1], k1[2], k1[3], k1[4], k1[5], k1[6], k1[7], k1[8]]
        c = ""
        d = ""
        s = 8 - p
        for ss in range(s):
            z = 7-ss
            print(z)
            del x[z]
        l = p // 2
        if p == 0:
            c = [k1[1]]
            d = ["なし"]
        elif p == 1:
            c = [k1[1]]
            d = [k1[2]]
        else:
            if q == 1:
                x = random.sample(x, p)
                c = x[l:]
                d = x[:l]
            else:
                w = q - 1
                x = random.sample(x, p)
                c = x[w:]
                d = x[:w]

        k1["チーム分けメンバー"] += "Aチーム  "
        for k in range(len(c)):
            k1["チーム分けメンバー"] += "[" + str(c[k]) + "]"
        k1["チーム分けメンバー"] += "\nBチーム  "
        for kk in range(len(d)):
            k1["チーム分けメンバー"] += "[" + str(d[kk]) + "]"
        k1["チーム分けメンバー"] += "\n\nだ‼"

    def team_heikinwake_sikibetu():
        for j in range(8):
            jj = j + 1
            heikinwake[1][j] = k2[jj]

        k = 0
        for h in range(8):
            if heikinwake[1][k] == "登録なし":
                del heikinwake[1][k]
                del heikinwake[6][k]
            else:
                k += 1

        h = len(heikinwake[1])
        hh = 8 - h

        for _ in range(hh):
            del heikinwake[4][h]

    def reaction_check(reaction, user):
        aaa = (str(reaction.emoji) == "✅" or str(reaction.emoji) == '☑')
        return aaa and user == message.author

    if message.content == "!ping":
        await message.channel.send("pong!")

    if message.content == "メンバー登録":
        check1[1] = 0
        check1[2] = 0
        check1[3] = 0
        k4[1] = [0,0,0,0,0,0,0,0,0,0,0]
        count = 0
        mooove[1] = 5
        riaction_text = ""

        for mem in range(1,9):
            riaction_text_yxt = str(riaction_list[3][mem -1]) +"：" + str(mem) + "人目　[" + str(k2[mem]) + "]\n" 
            riaction_text += riaction_text_yxt

        m1 = await message.channel.send("メンバーを登録するぞ‼\n登録したいメンバーのに対応する数字のリアクションを付けてくれ‼(複数選択可)\n" + riaction_text)
        messagee[1] = m1
        for nen in range(1,9):
            await messagee[1].add_reaction(riaction_list[3][nen-1])
        await m1.add_reaction("✔")
        await m1.add_reaction("✅")
        await m1.add_reaction("☑")

        while True:
            reaction, user = await client.wait_for('reaction_add', check=reaction_check)               
            if check1[1] == 1 or check1[1] == 2:
                break

        if check1[1] == 1:
            if k4[1][9] != 1:
                mm = "<メンバー一覧>\n"
                m = ""
                for gr in range(len(k4[1])):
                    if k4[1][gr] == 1:
                        gg = gr+ 1
                        m = await message.channel.send(str(gg) + "人目に登録したいメンバーの名前を送ってくれ‼")
                        t = await client.wait_for("message", check=check)
                        k2[gr + 1] = t.content
                        await m.delete()
                for mk in range(8):
                    u = mk +1
                    mm = mm + str(u) + "人目 [" + k2[u] + "]\n"
                await m1.delete()
                await message.channel.send(mm)
            else:
                mm = "<メンバー一覧>\n"

                for g in range(8):
                    gg = g+ 1
                    m = await message.channel.send(str(gg) + "人目に登録したいメンバーの名前を送ってくれ‼")
                    t = await client.wait_for("message", check=check)
                    k2[g + 1] = t.content
                    await m.delete()

                for mk in range(8):
                    u = mk +1
                    mm = mm + str(u) + "人目 [" + k2[u] + "]\n"
                await m1.delete()
                await message.channel.send(mm)
    
    elif message.content == "チームメンバー":
        await message.channel.send("１人目　「" + k2[1] + "」\n２人目　「" + k2[2] + "」\n３人目　「" + k2[3] + "」\n４人目　「" + k2[4] + "」\n５人目　「" + k2[5] + "」\n６人目　「" + k2[6] + "」\n７人目　「" + k2[7] + "」\n８人目　「" + k2[8] + "」\n")

    elif message.content == "メンバーリセット":
        check1[1] = 0
        check1[2] = 0
        check1[3] = 0
        k4[1] = [0,0,0,0,0,0,0,0,0,0,0]
        riaction_text = ""
        count = 0
        mooove[1] = 5

        for mem in range(1,9):
            if k2[mem] != "登録なし":
                count += 1
                riaction_text_yxt = str(riaction_list[3][mem -1]) +"：" + str(mem) + "人目　[" + str(k2[mem]) + "]\n" 
                riaction_text += riaction_text_yxt
        if count != 0:
            m1 = await message.channel.send("メンバーをリセットするぞ‼\nリセットしたいメンバーのに対応する数字のリアクションを付けてくれ(複数選択可)‼\n" + riaction_text)
            messagee[1] = m1
            for nen in range(1,9):
                if k2[nen] != "登録なし":
                    await messagee[1].add_reaction(riaction_list[3][nen-1])
            await m1.add_reaction("✔")
            await m1.add_reaction("✅")
            await m1.add_reaction("☑")


            while True:
                reaction, user = await client.wait_for('reaction_add', check=reaction_check)               
                if check1[1] == 1 or check1[1] == 2:
                    break

            if check1[1] == 1:

                if k4[1][9] != 1:
                    mm = "<メンバー一覧>\n"
                    for gr in range(len(k4[1])):
                        if k4[1][gr] == 1:
                            k2[gr + 1] = "登録なし"
                    for mk in range(8):
                        u = mk +1
                        mm = mm + str(u) + "人目 [" + k2[u] + "]\n"
                    await m1.delete()
                    await message.channel.send(mm)
                else:
                    mm = "<メンバー一覧>\n"

                    for g in range(1, 9):
                        k2[g] = "登録なし"

                    for mk in range(8):
                        u = mk +1
                        mm = mm + str(u) + "人目 [" + k2[u] + "]\n"
                    await m1.delete()
                    await message.channel.send(mm)
            
            
        else:
            await message.channel.send("メンバーが一人も登録されていないぞ‼")

    elif message.content == "いま":
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

        await message.channel.send("おすすめの武器は…\n\n「" + random.choice(buki1) + "」\n\nだ!!")

    elif message.content == "チーム分け":

        team_member()
        i = member_touroku[1] + member_touroku[2] + member_touroku[3] + member_touroku[4] + member_touroku[5] + member_touroku[6] + member_touroku[7] + member_touroku[8]

        if k5[1] == 1:
            if i == 0:
                await message.channel.send("\nメンバーを登録してないぞ‼")

            elif i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8:
                for r in range(1, 9):
                    d = r + 1

                    if i == r:
                        team_choise(d)
                        team_choise_count(r, 1)
                        await message.channel.send("登録した名前でチームを分けるぞ‼")
                        await message.channel.send(k1["チーム分けメンバー"])
                        break

            else:
                await message.channel.send("エラー:c1 botの製作者に言ってくれ‼")

        elif k5[1] == 2:
            if i == 0 or i == 1:
                await message.channel.send("人数が足りないぞ‼　　2人以上5人以下にしてくれ")

            elif i == 2 or i == 3 or i == 4 or i == 5:
                await message.channel.send("１vs〇でのチーム分けをするぞ‼")
                for l in range(2, 6):
                    if i == l:
                        ll = l + 1
                        team_choise(ll)
                        team_choise_count(l, 2)
                        await message.channel.send(k1["チーム分けメンバー"])

            elif i == 6 or i == 7 or i == 8:
                await message.channel.send("登録してあるメンバーの人数が多すぎるぞ‼")

        elif k5[1] == 3:
            if i == 0 or i == 1 or i == 2:
                await message.channel.send("人数が足りないぞ‼　　3人以上6人以下にしてくれ")

            elif i == 3 or i == 4 or i == 5 or i == 6:
                await message.channel.send("２vs〇でのチーム分けをするぞ‼")
                for l in range(3, 7):
                    if i == l:
                        ll = l + 1
                        team_choise(ll)
                        team_choise_count(l, 3)
                        await message.channel.send(k1["チーム分けメンバー"])

            elif i == 7 or i == 8:
                await message.channel.send("登録してあるメンバーの人数が多すぎるぞ‼")

        elif k5[1] == 4:
            if i == 0 or i == 1 or i == 2 or i == 3:
                await message.channel.send("人数が足りないぞ‼　　4人以上7人以下にしてくれ")

            elif i == 4 or i == 5 or i == 6 or i == 7:
                await message.channel.send("３vs〇でのチーム分けをするぞ‼")
                for l in range(4, 8):
                    if i == l:
                        ll = l + 1
                        team_choise(ll)
                        team_choise_count(l, 4)
                        await message.channel.send(k1["チーム分けメンバー"])

            elif i == 8:
                await message.channel.send("登録してあるメンバーの人数が多すぎるぞ‼")

        elif k5[1] == 5:
            riaction_list[2] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0]
            heikinwake[1] = ["登録なし", "登録なし", "登録なし","登録なし", "登録なし", "登録なし", "登録なし", "登録なし"]
            heikinwake[2] = [0, 0, 0, 0, 0, 0, 0, 0]
            heikinwake[3] = [1, 2, 3, 4, 5, 6, 7, 8]
            heikinwake[4] = [1, 2, 3, 4, 5, 6, 7, 8]
            heikinwake[5] = [0, 0, 0, 0, 0, 0, 0, 0]
            heikinwake[6] = [1, 2, 3, 4, 5, 6, 7, 8]
            wwwww = 0

            m1 = 1
            m2 = 1
            m3 = 1
            m4 = 1
            m5 = 1
            m6 = 1
            m7 = 1
            m8 = 1
            m9 = 1
            m10 = 1

            team_heikinwake_sikibetu()
            poinntosa = 0
            t = len(heikinwake[1])
            discord_member = []

            if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8:
            
             #ロール付与
                tt = t + 1
                g = 0
                ww = 0
                chn_list = []
                chch_list = ["1️⃣", "2️⃣", "3️⃣"]
                qp = ""

                for h in range(1, tt):
                    k3[h] = 0

                for q in range(t):
                    if not heikinwake[1][q] == "登録なし":
                        qp += str(riaction_list[5][q]) + "：[" + str(heikinwake[1][q]) + "]　　" + str(heikinwake[2][q]) + "ポイント\n"
                        chn_list.append(riaction_list[3][q])

                m = await message.channel.send("勝敗ポイントが同じになるチーム分けをするぞ‼\nボイスチャンネル移動を行うかどうかをリアクションを付けてくれ‼")
                messagee[1] = m
                m1 = m

                mooove[1] = 4

                for hg in range(2):
                    await m1.add_reaction(riaction_list[5][hg])
                await m1.add_reaction("✅")

                while True:
                    reaction, user = await client.wait_for('reaction_add', check=reaction_check)
                    if check1[1] == 1 or check1[1] == 2:
                        break

                if riaction_list[6][0] == 1:
                    wwwww = 1
                    await m1.delete()
                    m2 = await message.channel.send("ボイスチャンネル移動を行うことを確認したぞ‼\n移動のためにロールを付与するぞ‼\n")

                    while True:

                        move_number = 3
                        abc = "<チームメンバー>\n"
                        for vbb in range(1, 9):
                            if k2[vbb] != "登録なし":
                                abc += riaction_list[3][vbb-1] + "：" + str(vbb) + "人目[" + str(k2[vbb]) + "]\n"
                        abc += "\n"

                        deg = "<discordメンバー>\n"



                        wq = 0
                        for mm in message.guild.voice_channels:
                            for nn in mm.members:
                                deg += str(riaction_list[1][wq]) + "：" + str(nn) + "　"
                                discord_member.append(nn)

                                nb = [nk.name for nk in nn.roles]
                                for hg in range(1, 9):
                                    for gh in nb:
                                        if str(gh) == str(hg):
                                            deg += "[" + str(gh) + "]"
                                            break
                                deg += "\n"
                                wq += 1
                        """
                        wq = 0
                        for nm in range(1,9):
                            deg += "<" + str(nm) + ">：" 
                            for mm in message.guild.voice_channels:
                                for nn in mm.members:
                                    o = 0
                                    for ee in discord_member:
                                        if str(ee.name) == str(nn.name):
                                            o = 1
                                    if o == 0:
                                        for oo in nn.roles:
                                            if str(oo) == str(nm):
                                                deg += "[" + str(nn.name) + "]"
                                                discord_member.append(nn)
                                                break
                            deg += "\n"
                        """






                        m3 = await message.channel.send(abc + deg)
                        messagee[1] = m3

                        mooove[1] = 5
                        riaction_list[2] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0]
                        k4[1] = [0,0,0,0,0,0,0,0,0,0]
                        check1[1] = 0
                        check1[2] = 0
                        check1[3] = 0
                        check1[4] = 0
                        kaisuu = 0

                        m4 = await message.channel.send("\n登録したメンバーとdiscordユーザーを連結させます。\n何人目のチームメンバーを連結させるかリアクションを付けてくれ‼")
                        messagee[1] = m4

                        for ji in range(1, 9):
                            if k2[ji] != "登録なし":
                                await m4.add_reaction(riaction_list[3][ji-1])
                        await m4.add_reaction("✔")
                        await m4.add_reaction("✅")
                        await m4.add_reaction("☑")

                        while True:
                            reaction, user = await client.wait_for('reaction_add', check=reaction_check)
                            if check1[1] == 1 or check1[1] == 2:
                                break

                        if check1[1] == 1:
                            await m4.delete()
                            for yt in range(8):
                                if k4[1][yt] == 1:
                                    if kaisuu !=0:
                                        m3 = await message.channel.send(abc + deg)
                                        messagee[1] = m3

                                    m5 = await message.channel.send(str(yt + 1) + "人目(" + str(k2[yt + 1]) + ")を確認しました。\n次にdiscordメンバーを選択してください。")
                                    messagee[1] = m5

                                    mooove[1] = 3
                                    riaction_list[2] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0]
                                    check1[1] = 0
                                    check1[2] = 0
                                    check1[3] = 0
                                    check1[4] = 0

                                    for fj in range(wq):
                                        await m5.add_reaction(riaction_list[1][fj])
                                    await m5.add_reaction("✅")
                                    await m5.add_reaction("☑")

                                    while True:
                                        reaction, user = await client.wait_for('reaction_add', check=reaction_check)
                                        if check1[1] == 1 or check1[1] == 2:
                                            break

                                    akb = 0

                                    if check1[1] == 1:
                                        for ew in range(26):
                                            if riaction_list[2][ew] == 1:
                                                for ch in message.guild.voice_channels:
                                                    for mem in ch.members:
                                                        if str(mem) == str(discord_member[ew]):
                                                            rn = [roruna.name for roruna in message.guild.roles]
                                                            ri = [roruid.id for roruid in message.guild.roles]

                                                            for rere in range(len(rn)):
                                                                for yy in range(1, 9):
                                                                    if str(rn[rere]) == str(yy):
                                                                        try:
                                                                            await mem.remove_roles(message.guild.get_role(ri[rere]))
                                                                        except:
                                                                            pass
                                                                        break

                                                            for rona in range(len(rn)):
                                                                if str(rn[rona]) == str(yt + 1):
                                                                    role = message.guild.get_role(
                                                                        ri[rona])

                                                                    await mem.add_roles(role)
                                                                    await m5.delete()
                                                                    await m3.delete()
                                                                    akb = 1
                                                                    break
                                                            break
                                                    if akb == 1:
                                                        break
                                            if akb == 1:
                                                break

                                        kaisuu = 1
                                        abc = "<チームメンバー>\n"
                                        for vbb in range(1, 9):
                                            if k2[vbb] != "登録なし":
                                                abc += riaction_list[3][vbb-1] + "：" + str(vbb) + "人目[" + str(k2[vbb]) + "]\n"
                                        abc += "\n"
                                        deg = "<discordメンバー>\n"
                                        wq = 0
                                        for mm in message.guild.voice_channels:
                                            for nn in mm.members:
                                                deg += str(riaction_list[1][wq]) + "：" + str(nn) + "　"
                                                discord_member.append(nn)
                                                nb = [nk.name for nk in nn.roles]
                                                for hg in range(1, 9):
                                                    for gh in nb:
                                                        if str(gh) == str(hg):
                                                            deg += "[" + str(gh) + "]"
                                                            break
                                                deg += "\n"
                                                wq += 1
                                            
                                    elif check1[1] == 2:
                                        await m3.delete()
                                        await m5.delete() 

                        elif check1[1] == 2:
                            break
             #基礎ポイント
                delete_list = [m1, m2, m3,m4,m5]
                for jf in delete_list:
                    try:await jf.delete()
                    except:pass

                m6 = await message.channel.send("\n基礎ポイントを上げるぞ‼\n上げたいメンバーの番号をうってくれ‼")
                messagee[1] = m6
                while True:

                    m7 = await message.channel.send("<メンバーとポイント>\n" + qp )
                    messagee[1] = m7

                    riaction_list[6] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    check1[1] = 0
                    check1[2] = 0
                    check1[3] = 0
                    check1[4] = 0
                    mooove[1] = 5
                    rr = 0
                    kk = 0



                    for h in range(3):
                        await m7.add_reaction(chch_list[h])
                    await m7.add_reaction("✔")
                    await m7.add_reaction("✅")

                    await m7.add_reaction("☑")
                    while True:
                        reaction, user = await client.wait_for('reaction_add', check=reaction_check)
                        if check1[1] == 1 or check1[1] == 2:
                            break

                    if check1[1] == 1:
                        hantei = k4[1]

                        if riaction_list[6][9] == 1:
                            for time in range(3):
                                ti = time +1
                                if time != 0:
                                    m7 = await message.channel.send("<メンバーとポイント>\n" + qp )
                                m8 = await message.channel.send("[" + str(ti) + "]ポイントを確認しました。次に付与するメンバーのリアクションを押してください。")
                                messagee[1] = m8
                                mooove[1] = 5
                                check1[1] = 0
                                check1[2] = 0
                                check1[3] = 0
                                k4[1] = [0,0,0,0,0,0,0,0,0,0]

                                for h in chn_list:
                                    await m8.add_reaction(h)
                                await m8.add_reaction("✅")
                                await m8.add_reaction("☑")

                                while True:
                                    reaction, user = await client.wait_for('reaction_add', check=reaction_check)
                                    if check1[1] == 1 or check1[1] == 2:
                                        break
                                if  check1[1] == 1:
                                    for l in range(len(k4[1])):
                                        if k4[1][l] == 1:
                                            heikinwake[2][l] = ti
                                    qp = ""
                                    for q in range(t):
                                        if not heikinwake[1][q] == "登録なし":
                                            qp += str(riaction_list[5][q]) + "：[" + str(heikinwake[1][q]) + "]　　" + str(heikinwake[2][q]) + "ポイント\n"
                                    await m7.delete()
                                    await m8.delete()
                                elif check1[1] == 2:
                                    await m7.delete()
                                    await m8.delete()

                        else:
                            for r in range(3):
                                if hantei[r] == 1:
                                    rr = r + 1
                                    if kk != 0:
                                        m7 = await message.channel.send("<メンバーとポイント>\n" + qp )
                                    m8 = await message.channel.send("[" + str(rr) + "]ポイントを確認しました。次に付与するメンバーのリアクションを押してください。")
                                    messagee[1] = m8
                                    mooove[1] = 5
                                    check1[1] = 0
                                    check1[2] = 0
                                    check1[3] = 0
                                    k4[1] = [0,0,0,0,0,0,0,0,0,0]

                                    for h in chn_list:
                                        await m8.add_reaction(h)
                                    await m8.add_reaction("✅")
                                    await m8.add_reaction("☑")
                                    while True:
                                        reaction, user = await client.wait_for('reaction_add', check=reaction_check)
                                        if check1[1] == 1 or check1[1] == 2:
                                            break
                                    if  check1[1] == 1:
                                        for l in range(8):
                                            if k4[1][l] == 1:
                                                heikinwake[2][l] = rr
                                        qp = ""
                                        for q in range(t):
                                            if not heikinwake[1][q] == "登録なし":
                                                qp += str(riaction_list[5][q]) + "：[" + str(heikinwake[1][q]) + "]　　" + str(heikinwake[2][q]) + "ポイント\n"
                                        js = [m7, m8]
                                        for me in js:
                                            try:await me.delete()
                                            except:pass
                                    elif check1[1] == 2:
                                        await m7.delete()
                                        await m8.delete()
                                    kk += 1
                                    
                    elif check1[1] == 2:
                        js = [m6, m7, m8]
                        for me in js:
                            try:
                                await me.delete()
                            except:
                                pass
                        break           
             #ランダムチーム分け
                while True:
                    check1[1] = 0
                    check1[2] = 0
                    check1[3] = 0
                    poinntosa = 0
                    riaction_list[2] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0]
                    if ww == 0:
                        for d in range(0, 10000):
                            for s in range(1, 40000):
                                k = t
                                c0 = random.sample(heikinwake[4], k)
                                for w in range(k):
                                    heikinwake[3][w] = c0[w]
                                p = k // 2  # B
                                pp = k - p  # A

                                g1 = 0
                                g2 = 0

                                for gg in range(pp):
                                    g1 += heikinwake[2][heikinwake[3][gg]-1]

                                for gg in range(p):
                                    ab = pp + gg
                                    g2 += heikinwake[2][heikinwake[3][ab]-1]

                                if g1 > g2:
                                    g = g1 - g2
                                elif g2 > g1:
                                    g = g2 - g1
                                elif g1 == g2:
                                    g = 0

                                team1 = ["登録なし", "登録なし", "登録なし", "登録なし"]
                                team2 = ["登録なし", "登録なし", "登録なし", "登録なし"]
                                team1ch = [10, 10, 10, 10]
                                team2ch = [10, 10, 10, 10]
                                if d == g:
                                    for v in range(pp):
                                        team1[v] = heikinwake[1][heikinwake[3][v]-1]
                                        team1ch[v] = heikinwake[6][heikinwake[3][v]-1]

                                    for v in range(p):
                                        ab = pp + v
                                        team2[v] = heikinwake[1][heikinwake[3][ab]-1]
                                        team2ch[v] = heikinwake[6][heikinwake[3][ab]-1]

                                    vv = 0
                                    vvv = 0
                                    for v in range(4):
                                        if team1[vv] == "登録なし":
                                            del team1[vv]
                                            del team1ch[vv]
                                        else:
                                            vv += 1
                                        if team2[vvv] == "登録なし":
                                            del team2[vvv]
                                            del team2ch[vvv]

                                        else:
                                            vvv += 1

                                    a = ""
                                    b = ""

                                    team1_count = len(team1)
                                    team2_count = len(team2)

                                    for A in range(team1_count):
                                        a = a + "[" + str(team1[A]) + "]"
                                    for B in range(team2_count):
                                        b = b + "[" + str(team2[B]) + "]"
                                    c = ""
                                    for cs in range(t):
                                        c = c + "[" + heikinwake[1][cs] + "]　　" + str(heikinwake[2][cs]) + "ポイント\n"

                                    aa = str(a)
                                    bb = str(b)
                                    cc = str(c)
                                    gg = str(g)
                                    m = await message.channel.send("チーム分けでのチーム編成は…\n\nAチーム　" + aa + "\n\nBチーム　" + bb + "\nチームの点差は　" + gg + "だ‼\n\n<各ポイント>\n" + cc + "<リアクション>\n🇦：　Aチームが勝った時\n🇧：Bチームが勝った時\n🇨：チーム分けのチャンネルに移動\n🇩：ロビーに移動")
                                    messagee[1] = m
                                    pl = 0
                                    while True:
                                        riaction_list[2] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0]
                                        check1[1] = 0
                                        check1[2] = 0
                                        check1[3] = 0
                                        mooove[1] = 3
                                        for h in range(2):
                                            await messagee[1].add_reaction(riaction_list[1][h])
                                        if wwwww == 1:
                                            await messagee[1].add_reaction(riaction_list[1][2])
                                            await messagee[1].add_reaction(riaction_list[1][3])
                                        await messagee[1].add_reaction("✅")
                                        await messagee[1].add_reaction("☑")
                                        while True:
                                            reaction, user = await client.wait_for('reaction_add', check=reaction_check)
                                            if check1[1] == 1 or check1[1] == 2:
                                                break

                                        if check1[1] == 1:
                                            for yy in range(4):
                                                if riaction_list[2][yy] == 1:
                                                    if yy == 0:
                                                        for gg in range(pp):
                                                            heikinwake[2][heikinwake[3][gg] - 1] += 1

                                                        try:await m10.delete()
                                                        except:pass

                                                        m10 = await message.channel.send("Aチームの勝利‼")
                                                        check1[3] = 0
                                                        await messagee[1].delete()
                                                        pl = 1

                                                    elif yy == 1:
                                                        for gg in range(p):
                                                            s = pp + gg
                                                            heikinwake[2][heikinwake[3][s] - 1] += 1

                                                        try:await m10.delete()
                                                        except:pass

                                                        m10 = await message.channel.send("Bチームの勝利！")
                                                        check1[3] = 0
                                                        await messagee[1].delete()
                                                        pl = 1

                                                    elif yy == 2:
                                                        for ewre in team1ch:
                                                            for bn in message.guild.voice_channels:
                                                                for nnb in bn.members:
                                                                    hg = [go.name for go in nnb.roles]
                                                                    for fd in hg:
                                                                        if str(fd) == str(ewre):
                                                                            await nnb.move_to(client.get_channel(channel_id[2]))
                                                                            break
                                                        for ewwre in team2ch:
                                                            for bn in message.guild.voice_channels:
                                                                for nnbb in bn.members:
                                                                    hg = [go.name for go in nnbb.roles]
                                                                    for fdd in hg:
                                                                        if str(fdd) == str(ewwre):
                                                                            await nnbb.move_to(client.get_channel(channel_id[3]))
                                                                            break
                                                    elif yy == 3:
                                                        for lo in message.guild.voice_channels:
                                                            for bbn in lo.members:
                                                                await bbn.move_to(client.get_channel(channel_id[1]))

                                        elif check1[1] == 2:
                                            ww = 1
                                            await message.channel.send("チーム分けを終了したぞ‼")
                                            
                                            break
                                        poinntosa = 1
                                        if pl == 1:
                                            break           

                                if ww == 1:
                                    break
                                if poinntosa == 1:
                                    break
                            if ww == 1:
                                break
                            if poinntosa == 1:
                                break
                    if ww == 1:
                        break
            else:
                await message.channel.send("メンバーが登録されていないぞ‼")
        
        else:
            await message.channel.send("チーム分けの設定が行われていないぞ‼「チーム分け設定」で設定してくれ‼")

    elif message.content == "ルール":
        x = ["ガチアサリ", "ガチホコ", "ガチヤグラ", "ガチエリア"]
        x = random.choice(x)
        await message.channel.send("ルールは…　" + x + "　だ‼")

    elif message.content == "チーム分け設定":

        m1 = await message.channel.send("チーム分けの設定をするぞ‼\nチーム分けの人数を確認して次にコマンドを送ってくれ!\n1⃣：登録した人数が均等になるチーム分け\n2⃣：登録した人数を１vs〇でのチーム分け\n3⃣：登録した人数を２vs〇でのチーム分け\n4⃣：登録した人数を３vs〇でのチーム分け\n5⃣：４vs４でのチーム分けでメンバー全員の勝率ポイントが同じになるようなチーム分け\n☑：設定をキャンセルする")
        messagee[1] = m1
        mooove[1] = 4
        riaction_list[6] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        check1[1] = 0
        check1[2] = 0
        check1[3] = 0
        check1[4] = 0

        for ji in range(5):
            await m1.add_reaction(riaction_list[3][ji])
        await m1.add_reaction("✅")
        await m1.add_reaction("☑")

        while True:
            reaction, user = await client.wait_for('reaction_add', check=reaction_check)
            if check1[1] == 1 or check1[1] == 2:
                break
        
        if check1[1] == 1:
            for e in range(5):
                if riaction_list[6][e] == 1:
                    k5[1] = e + 1
                    if e == 0:
                        await message.channel.send("登録した人数を均等になるチーム分けするように設定したぞ‼")
                    elif e == 1:
                        await message.channel.send("登録した人数を１vs〇でのチーム分けをするように設定したぞ‼")
                    elif e == 2:
                        await message.channel.send("登録した人数を２vs〇でのチーム分けをするように設定したぞ‼")
                    elif e == 3:
                        await message.channel.send("登録した人数を３vs〇でのチーム分けをするように設定したぞ‼")
                    elif e == 4:
                        await message.channel.send("チームの勝率ポイントが同じになるチーム分けにするように設定したぞ‼")

                    break
        if check1[1] == 2:
            await message.channel.send("チーム分けをキャンセルしたぞ!!")

    elif message.content == "コマンド情報":
        await message.channel.send("「いま」　今の各ルールでのステージ情報\n「つぎ」　次の各ルールでのステージ情報\n「つぎつぎ」　次の次の各ルールでのステージ情報\n「れぎ」　レギュラーマッチの今、次、次の次ステージ情報\n「がち」　ガチマッチの今、次、次の次ステージ情報\n「りぐ」　リーグマッチの今、次、次の次ステージ情報\n「ぶき」 ランダム武器選択\n「チーム」　数字でのチーム分け\n「チーム分け」　登録した名前でのチーム分け\n「メンバー登録」　一斉にメンバー登録\n「ち」＋「数字」　数字と同じ番号のメンバー登録を変更\n「リセット」　登録した名前のリセット\n「チームメンバー」 登録した名前一覧")
        # 8人でリーグマッチをやるときは「チーム」と打ってみよう!!チームをランダムで編成するぞ!!\n8人そろって誰がやるかが分かっていたら「チーム分け」と打ってみよう!!

    elif message.content == "チャンネル設定":

        if message.author.voice is None:
            await message.channel.send("ボイスチャンネルに接続して(入って)いないぞ‼\n接続してからやり直してくれ‼")
        else:
            arara = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            chn = ""
            chn_list = []

            k = [channel.name for channel in message.guild.voice_channels]

            talk_channel_id = message.author.voice.channel.id

            channel1 = client.get_channel(talk_channel_id)

            for ch in range(len(channel1.guild.voice_channels)):

                chn = chn + str(riaction_list[1][ch])
                chn = chn + " : [" + str(k[ch]) + "]\n"
                chn_list.append(riaction_list[1][ch])
            channel_id_number = 0
            mooove[1] = 3
            mooove[2] = []

            messagee[2] = await message.channel.send("移動先のボイスチャンネルを設定します。\n\n<チャンネル一覧>\n" + chn)
            channel_name = ["「ロビー」", "「Aチーム」", "「Bチーム」"]
            for i in channel_name:
                riaction_list[2] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                check1[1] = 0
                check1[2] = 0
                check1[3] = 0
                check1[4] = 0

                m = await message.channel.send(i + "にするチャンネルの名前に割り振られたリアクションを付けてくれ‼\n決まったら✅を押してね。")
                messagee[1] = m

                for h in range(len(chn_list)):
                    await messagee[1].add_reaction(chn_list[h])
                for ppo in range(len(riaction_list[2])):
                    if arara[ppo] == 1:
                        await messagee[1].clear_reaction(riaction_list[1][ppo])
                await messagee[1].add_reaction("✅")

                while True:
                    reaction, user = await client.wait_for('reaction_add', check=reaction_check)
                    if check1[1] == 1 or check1[1] == 2:
                        break

                if check1[1] == 1:
                    jk = 0
                    await messagee[1].delete()
                    if messagee[3] != 123:
                        await messagee[3].delete()
                    for bbd in range(len(riaction_list[2])):
                        if riaction_list[2][bbd] == 1:
                            jk = bbd
                            arara[jk] = 1
                    k = [channel.name for channel in message.guild.voice_channels]
                    c = [channel.id for channel in message.guild.voice_channels]
                    p = len(k)
                    channel_id_number += 1
                    channel_id[channel_id_number] = c[jk]

                    messagee[3] = await message.channel.send(i + "にするチャンネルは「" + str(k[jk]) + "]")
            await messagee[3].delete()
            m = await message.channel.send("\n<チャンネル確認>\n「ロビー」→「" + str(client.get_channel(channel_id[1])) + "」\n「Aチーム」→「" + str(client.get_channel(channel_id[2])) + "」\n「Bチーム」→「" + str(client.get_channel(channel_id[3])) + "」")

    elif message.content == "join":
        if message.author.voice is None:
            await message.channel.send("ボイスチャンネルに接続していないぞ‼")
            return

        elif message.guild.voice_client is None:
            print(message.guild.voice_client)
            await message.author.voice.channel.connect()
            await message.channel.send("入室‼")

        elif message.author.voice.channel.members is not None and not message.guild.me in message.author.voice.channel.members:
            print(1)
            print()
            await message.guild.me.move_to(message.author.voice.channel)
            await message.channel.send("移動‼")

        else:
            await message.channel.send("既に同じチャンネルにいるぞ‼")
            print(2)

    elif message.content == "leave":
        await message.guild.me.move_to(None)
        await message.channel.send("退室‼")
        return



if __name__ == "__main__":
    reload()
    loop.start()
    client.run(TOKEN)
