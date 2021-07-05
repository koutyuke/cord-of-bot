from ssl import ALERT_DESCRIPTION_INSUFFICIENT_SECURITY, HAS_NEVER_CHECK_COMMON_NAME, PROTOCOL_TLSv1_1
from typing import List, Text
import discord
from bs4 import BeautifulSoup
from urllib import request
from discord import team
from discord import message
from discord.colour import Colour
from discord.ext import tasks
from datetime import datetime, timedelta, timezone
import random
from time import sleep
import stage
import mojimoji

intents = discord.Intents.default()
intents.members = True
# intents=discord.Intents.all()
client = discord.Client(intents=intents)


# TOKEN読み込み
TOKEN = "hoge-hoge-hoge"

#client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name = "Splatoon",type = 1))
    print("logged in\n")

urls = "https://splatoon.caxdb.com/schedule2.cgi"

k1 = {1: "登録", 2: "登録", 3: "登録", 4: "登録", 5: "登録",6: "登録", 7: "登録", 8: "登録", "チーム分けメンバー": "あ"}
team_wake_settei = {1: 5}
member_touroku = {1:["登録なし","AYU","にこちゃん","登録なし","登録なし","登録なし","登録なし","登録なし"],2:[3,3,3,3,3,3,3,3]}



ri_list = {
    "eng": ["🇦", "🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮", "🇯", "🇰", "🇱", "🇲", "🇳", "🇴", "🇵", "🇶", "🇷", "🇸", "🇹", "🇺", "🇻", "🇼", "🇽", "🇾", "🇿"], #riaction_list[1]
    "num":["1⃣", "2⃣", "3⃣", "4️⃣", "5️⃣", "6️⃣","7️⃣", "8️⃣","9⃣","🔟"], #riaction_list[3][5]
    "che":{"gr_em":"✅","bl_em":"☑","br_em":"✔"},
    "val":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#riaction_list[2,4,6]
    "chv":{"ge_em":0,"bl_em":0,"br_em":0},
    "check":{1: 0, 2: 0, 3: 0, 4: 0},#check1
    "multi":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
mooove = {1:0}#チャンネル移動用
members = {
    "member":["a", "b", "c", "d", "e", "f", "g", "h", "i", "登録なし"]
}
channel_id = {
    1: 788349336735580171, 
    2: 792725056341409883, 
    3: 792725353532751892, 
}
heikin = {
    "setting":4,
    "point":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "members":[],
}
messagee = {1: 12, 2: 123, 3: 123}
message_tyouhuku_kaihi = {1,0}

def reload():
 # グローバル変数
    global now_time, next_time, nextnext_time,now_gati_rule, next_gati_rule, nextnext_gati_rule, now_rigu_rule, next_rigu_rule, nextnext_rigu_rule
    global buki,embed,file,rigu_now1,rigu_now2,rigu_next1,rigu_next2,rigu_nextnext1,rigu_nextnext2,gati_now1,gati_now2,gati_next1,gati_next2,gati_nextnext1,gati_nextnext2,regu_now1,regu_now2,regu_next1,regu_next2,regu_nextnext1,regu_nextnext2
 # サイトのurl
    response = request.urlopen(urls)
    soup = BeautifulSoup(response)
    response.close()
 # スクレイピング
    
    # now の時間
    now_time = soup.find_all("li")[0].text
    # next の時間
    next_time = soup.find_all("li")[10].text
    # nextnext の時間
    nextnext_time = soup.find_all("li")[20].text

    # ガチマッチ(ルール)
    # now
    now_gati_rule= stage.rule(soup.find_all("li")[4].text)
    # next
    next_gati_rule = stage.rule(soup.find_all("li")[14].text)
    # nextnext
    nextnext_gati_rule = stage.rule(soup.find_all("li")[24].text)

    # リーグマッチ(ルール)
    # #now
    now_rigu_rule = stage.rule(soup.find_all("li")[7].text)
    # next
    next_rigu_rule = stage.rule(soup.find_all("li")[17].text)
    # nextnext
    nextnext_rigu_rule = stage.rule(soup.find_all("li")[27].text)


    # レギュラーマッチ(ステージ)
    regu_now1 = soup.find_all("li")[2].text
    regu_now2 = soup.find_all("li")[3].text

    regu_next1 = soup.find_all("li")[12].text
    regu_next2= soup.find_all("li")[13].text

    regu_nextnext1 = soup.find_all("li")[22].text
    regu_nextnext2 = soup.find_all("li")[23].text


    # ガチマッチ(ステージ)
    gati_now1 = soup.find_all("li")[5].text
    gati_now2 = soup.find_all("li")[6].text

    gati_next1 = soup.find_all("li")[15].text
    gati_next2 = soup.find_all("li")[16].text

    gati_nextnext1 = soup.find_all("li")[25].text
    gati_nextnext2 = soup.find_all("li")[26].text
    

    # リーグマッチ(ステージ)
    rigu_now1 = soup.find_all("li")[8].text
    rigu_now2 = soup.find_all("li")[9].text

    rigu_next1 = soup.find_all("li")[18].text
    rigu_next2 = soup.find_all("li")[19].text

    rigu_nextnext1 = soup.find_all("li")[28].text
    rigu_nextnext2 = soup.find_all("li")[29].text

    # ランダム(武器)
    buki = ("スプラシューターコラボ", ".52ガロン", "わかばシューター", ".96ガロンデコ", "シャープマーカー", "N-ZAP89", "N-ZAP85", "プライムシューター", "シャープマーカーネオ", "ボールドマーカー", "ボールドマーカーネオ", "プロモデラーRG", "スプラシューター", ".52ガロンデコ", "L3リールガンD", "ジェットスイーパーカスタム", "プライムシューターコラボ", "もみじシューター", "プロモデラーMG", "H3リールガンチェリー", ".96ガロン", "ボールドマーカー7", "N-ZAP83", "L3リールガン", "ジェットスイーパー", "H3リールガン", "プロモデラーPG", "H3リールガンD", "ボトルガイザー", "ボトルガイザーフォイル", "スプラシューターベッチュー", "プライムシューターベッチュー", "おちばシューター", "H3リールガンチェリー", ".52ガロンベッチュー", "デュアルスイーパー", "デュアルスイーパーカスタム", "スプラマニューバー", "スプラマニューバーコラボ", "スパッタリー", "ケルビン525", "スパッタリー・ヒュー", "クアッドホッパーブラック", "ケルビン525デコ", "クアッドホッパーホワイト", "スプラマニューバーベッチュー", "ケルビン525ベッチュー", "スパッタリークリア", "スプラスコープ", "スクイックリンα", "スプラチャージャー", "14式竹筒銃・甲", "スクイックリンγ", "14式竹筒銃・丙", "スクイックリンβ", "14式竹筒銃・乙", "ソイチューバー", "スプラチャージャー コラボ", "スプラスコープ コラボ", "リッター4K", "4Kスコープ", "リッター4kカスタム", "4kスコープカスタム", "ソイチューバーカスタム", "スプラチャージャーベッチュー", "スプラスコープベッチュー","ノヴァブラスターネオ", "ロングブラスターカスタム", "ホットブラスターカスタム", "ノヴァブラスター", "ラピッドブラスター", "ロングブラスターネクロ", "ホットブラスター", "Rブラスターエリートデコ", "Rブラスターエリート", "ラピッドブラスターデコ", "ロングブラスター", "クラッシュブラスター", "クラッシュブラスターネオ", "ノヴァブラスターベッチュー", "ラピッドブラスターベッチュー", "ダイナモローラー", "スプラローラーコラボ", "カーボンローラー", "ダイナモローラーテスラ", "スプラローラー", "カーボンローラーデコ", "ヴァリアブルローラー", "ヴァリアブルローラーフォイル", "スプラローラーベッチュー", "ダイナモローラーベッチュー", "ホクサイ", "パブロ", "ホクサイ・ヒュー", "パーマネント・パブロ", "パブロ・ヒュー", "ホクサイベッチュー", "バケットスロッシャー", "ヒッセン", "スクリュースロッシャー", "バケットスロッシャーデコ", "バケットスロッシャーソーダ", "ヒッセン・ヒュー", "スクリュースロッシャーネオ", "エクスプロッシャー", "オーバーフロッシャー", "スクリュースロッシャーベッチュー", "エクスプロッシャーカスタム", "オーバーフロッシャーデコ", "スプラスピナーコラボ", "バレルスピナーデコ", "ハイドラントカスタム", "バレルスピナー", "バレルスピナーリミックス", "ハイドラント", "スプラスピナー", "クーゲルシュライバー", "ノーチラス47", "クーゲルシュライバー・ヒュー", "ノーチラス79", "スプラスピナーベッチュー", "パラシェルター", "キャンピングシェルター", "スパイガジェット", "パラシェルターソレーラ", "スパイガジェットソレーラ", "キャンピングシェルターソレーラ", "スパイガジェットベッチュー", "キャンピングシェルターカーモ")

    #レギュラーマッチ画像
    stage.stage_image(regu_now1,regu_now2,"regu_now")#now
    stage.stage_image(regu_next1,regu_next2,"regu_next")#next
    stage.stage_image(regu_nextnext1,regu_nextnext2,"regu_nextnext")#nextnext
    #ガチマッチ画像
    stage.stage_image(gati_now1,gati_now2,"gati_now")#now
    stage.stage_image(gati_next1,gati_next2,"gati_next")#next
    stage.stage_image(gati_nextnext1,gati_nextnext2,"gati_nextnext")#nextnext
    #リーグマッチ画像
    stage.stage_image(rigu_now1,rigu_now2,"rigu_now")#now
    stage.stage_image(rigu_next1,rigu_next2,"rigu_next")#next
    stage.stage_image(rigu_nextnext1,rigu_nextnext2,"rigu_nextnext")#nextnext

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

    member = payload.member
    if not member.bot:

        if mooove[1] == 1 or mooove[1] == 2:#1:英語の絵文字重複無し 2:数字の絵文字重複無し

            if mooove[1] == 1:
                key = "eng"
            elif mooove[1] == 2:
                key = "num"

            if str(payload.emoji.name) in ri_list[key]:
                
                if ri_list["chv"]["br_em"] == 1:
                    await messagee[1].remove_reaction("✔",member)

                eng_match = ri_list[key].index(str(payload.emoji.name))

                val_mach = [i for i,x in enumerate(ri_list["val"]) if x == 1]
                for q in val_mach:   
                    await messagee[1].remove_reaction(ri_list[key][q], member)
                    ri_list["val"][q] = 0
                ri_list["val"][eng_match] = 1

            elif str(payload.emoji.name) == "✅":
                eng_match = [i for i,x in enumerate(ri_list["val"]) if x == 1]
                s = len(eng_match)
                if s == 1:
                    ri_list["check"][1] = s
                    ri_list["check"][2] = s
                    await messagee[1].clear_reactions()
                else:await messagee[1].remove_reaction("✅", payload.member)

            elif str(payload.emoji.name) == "☑":
                ri_list["check"][1] = 2
                eng_match = [i for i,x in enumerate(ri_list["val"]) if x == 1]
                for i in eng_match:
                    ri_list["val"][i] = 0
                await messagee[1].clear_reactions()

            elif str(payload.emoji.name) == "✔":
                eng_match = [i for i,x in enumerate(ri_list["val"]) if x == 1]
                for i in eng_match:
                    try:await messagee[1].remove_reaction(ri_list[key][i], member)
                    except:pass
                    ri_list["val"][i] = 0
                ri_list["chv"]["br_em"] = 1
        
        elif mooove[1] == 3 or mooove[1] == 4:#3数字の絵文字重複有り 4:英語の絵文字重複有り

            if mooove[1] == 3:
                key = "num"
            elif mooove[1] == 4:
                key = "eng"
                
            emoji = payload.emoji.name
            try:eng_match = ri_list[key].index(emoji)
            except:pass

            if str(emoji) in ri_list[key]:
                if ri_list["chv"]["br_em"] == 1:
                    await messagee[1].remove_reaction("✔",member)
                ri_list["multi"][eng_match] = 1
                print(ri_list["multi"])
            
            elif str(emoji) == "✅":
                a = len([i for i,x in enumerate(ri_list["multi"]) if x == 1])
                if a != 0 or ri_list["chv"]["br_em"] == 1:
                    ri_list["check"][1] = 1
                    await messagee[1].clear_reactions()
                else:
                    await messagee[1].remove_reaction("✅",member)
                print(ri_list["multi"])

            elif str(emoji) == "☑":
                ri_list["check"][1] = 2
                await messagee[1].clear_reactions()
                
            elif str(emoji) == "✔":
                e = [i for i,x in enumerate(ri_list["multi"]) if x == 1]
                for em in e:
                    try:await messagee[1].remove_reaction(ri_list[key][em],member)
                    except: pass
                for r in e:
                    ri_list["multi"][r] = 0
                ri_list["chv"]["br_em"] = 1        
        
@client.event
async def on_raw_reaction_remove(payload):
    val_mach = [i for i,x in enumerate(ri_list["val"]) if x == 1]
    emoji = payload.emoji.name

    if mooove[1] == 1:#アルファベット
        if emoji in ri_list["eng"] and not payload.member is None:
            for i in val_mach:
                ri_list["val"][i] = 0
        if emoji == "✔":
            ri_list["chv"]["br_em"] = 0
        
    elif mooove[1] == 2:#数字
        if emoji in ri_list["num"] and not payload.member is None:
            for i in val_mach:
                ri_list["val"][i] = 0
        if emoji == "✔":
            ri_list["chv"]["br_em"] = 0
    elif mooove[1] == 3:#複数
        if emoji == "✔":
            ri_list["chv"]["br_em"] = 0
        if emoji in ri_list["num"]:
            a = ri_list["num"].index(emoji)
            ri_list["multi"][a] = 0
    elif mooove[1] == 4:#複数
        if emoji == "✔":
            ri_list["chv"]["br_em"] = 0
        if emoji in ri_list["num"]:
            a = ri_list["eng"].index(emoji)
            ri_list["multi"][a] = 0


@client.event
async def on_message(message):

    if message.author.bot:
        return

    def check(msg):
        return msg.author == message.author

    def team_choise(g):
        for e in range(1, g):
            for ee in range(8):
                if 1 == member_touroku[2][ee]:
                    k1[e + 1] = member_touroku[1][ee]
                    member_touroku[2][ee] = 0
                    break

    def team_member():
        for i in range(8):
            if not member_touroku[1][i] == "登録なし":
                member_touroku[2][i] = 1
            else:
                member_touroku[2][i] = 0

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

    def reaction_check(reaction, user):
        aaa = (str(reaction.emoji) == "✅" or str(reaction.emoji) == '☑')
        return aaa and user == message.author

    def reset():
        ri_list["val"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ri_list["multi"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ri_list["chv"] = {"ge_em":0,"bl_em":0,"br_em":0}
        ri_list["check"] = {1: 0, 2: 0, 3: 0, 4: 0}    

    if message.content == "!ping":
        await message.channel.send("pong!")

    if message.content == "メンバー登録":
        if message_tyouhuku_kaihi == 1:
            return

        def team_member():
            riaction_text = "<メンバー一覧>\n"
            for mem in range(10):
                ments = members["member"][mem]
                emoji = ri_list["num"][mem]

                if mem + 1 < 10:
                    su = mojimoji.han_to_zen(str(mem + 1))
                else:
                    su = mem + 1

                if ments == "登録なし":
                    riaction_text += f"{emoji}：{su}：未登録\n"
                else:
                    riaction_text += f"{emoji}：{su}：[{ments}]\n"
            return riaction_text
        reset()
        check_list = ["✔","✅","☑"]
        mooove[1] = 3
        riaction_text = ""
        
        u = team_member()
        m1 = messagee[1] = await message.channel.send(f"メンバーを登録するぞ‼\n登録したいメンバーのに対応する数字のリアクションを付けてくれ‼(複数選択可)\n{u}")
        
        for nen in range(10):
            await messagee[1].add_reaction(ri_list["num"][nen])
        for emo in check_list:
            await m1.add_reaction(emo)

        while True:
            reaction, user = await client.wait_for('reaction_add', check=reaction_check)               
            if ri_list["check"][1] == 1 or ri_list["check"][1] == 2:
                break

        if ri_list["check"][1] == 1:
            if ri_list["chv"]["br_em"] != 1:
                henkou = [i for i,x in enumerate(ri_list["multi"]) if x == 1]
            else:
                henkou = range(10)

            for he in henkou:
                await m1.delete()
                m1 = messagee[1] = await message.channel.send(team_member())
                gg = he +1
                m = messagee[1] = await message.channel.send(f"{gg} に登録したいメンバーの名前を送ってくれ‼\n(※登録したくないときには「登録なし」と送っていください。)")
                t = await client.wait_for("message", check = check)
                members["member"][he] = t.content
                await m.delete()

            us = [x for x in members["member"] if not x == "登録なし" ]
            l = 10 - len(us)
            for _ in range(l):
                us.append("登録なし")
            members["member"] = us

            await m1.delete()
            await message.channel.send(f"{team_member()}\n完了‼")
        elif ri_list["check"][1] == 2:
            await message.channel.send("メンバー登録をキャンセルしたぞ‼")

    elif message.content == "チームメンバー":
        await message.channel.send("１人目　「" + members["member"][0] + "」\n２人目　「" + members["member"][1] + "」\n３人目　「" + members["member"][2] + "」\n４人目　「" + members["member"][3] + "」\n５人目　「" + members["member"][4] + "」\n６人目　「" + members["member"][5] + "」\n７人目　「" + members["member"][6] + "」\n８人目　「" + members["member"][7] + "」\n")

    elif message.content == "メンバーリセット":
        if message_tyouhuku_kaihi == 1:
            return


        check_list = ["✔","✅","☑"]
        reset()
        mooove[1] = 3

        def reset_member():
            p = [i for i,x in enumerate(members["member"]) if not x == "登録なし" ]
            print(p)
            riaction_text = "<メンバーリスト>\n"
            for mem in p:
                ments = members["member"][mem]
                emoji = ri_list["num"][mem]

                if mem + 1 < 10:
                    su = mojimoji.han_to_zen(str(mem + 1))
                else:
                    su = mem + 1

                riaction_text += f"{emoji}：{su}：[{ments}]\n"
            return riaction_text
        
        def team_member():
            riaction_text = "<メンバーリスト>\n"
            for mem in range(10):
                ments = members["member"][mem]

                if mem + 1 < 10:
                    su = mojimoji.han_to_zen(str(mem + 1))
                else:
                    su = mem + 1

                if ments == "登録なし":
                    riaction_text += f"{su}：未登録\n"
                else:
                    riaction_text += f"{su}：[{ments}]\n"
            return riaction_text

        r = [i for i,x in enumerate(members["member"]) if x == "登録なし"]

        if not len(r) == 10 :
            m1 = messagee[1] = await message.channel.send("メンバーをリセットするぞ‼\nリセットしたいメンバーのに対応する数字のリアクションを付けてくれ(複数選択可)‼\n" + reset_member())

            for nen in range(10):
                if members["member"][nen] != "登録なし":
                    await messagee[1].add_reaction(ri_list["num"][nen])
            for emo in check_list:
                await m1.add_reaction(emo)

            while True:
                reaction, user = await client.wait_for('reaction_add', check=reaction_check)               
                if ri_list["check"][1] == 1 or ri_list["check"][1] == 2:
                    break

            if ri_list["check"][1] == 1:
                if ri_list["chv"]["br_em"] != 1:
                    num = [i for i,x in enumerate(ri_list["multi"]) if x == 1]
                    for i in num:
                        members["member"][i] = "登録なし"

                    us = [x for x in members["member"] if not x == "登録なし" ]
                    l = 10 - len(us)
                    for _ in range(l):
                        us.append("登録なし")
                    members["member"] = us

                    await m1.delete()
                    await message.channel.send(team_member())
                else:
                    members["member"] = ["登録なし", "登録なし", "登録なし", "登録なし", "登録なし", "登録なし", "登録なし", "登録なし", "登録なし", "登録なし"]
                    await m1.delete()
                    await message.channel.send(team_member())
            
            
        else:
            await message.channel.send("メンバーが一人も登録されていないぞ‼")

    elif message.content == "いま":
        m =  await message.channel.send("変換中…")
        hensuu1 = [regu_now1,gati_now1,rigu_now1]
        hensuu2 = [regu_now2,gati_now2,rigu_now2]
        files = ["regu_now","gati_now","rigu_now"]
        yougo = ["now","now","now"]
        time = [now_time,now_time,now_time]
        rules = ["regu","gati","rigu"]
        rule_rules = ["",f"({now_gati_rule})",f"({now_rigu_rule})"]
        titles = ["レギュラーマッチ","ガチマッチ","リーグマッチ"]

        for i in range(3):
            title = f"{titles[i]}{rule_rules[i]}\nTime:[{yougo[i]}]({time[i]})"
            rule = rules[i]
            descriptoin = f"{hensuu1[i]}\n{hensuu2[i]}"
            fname = files[i]
            emb = stage.embed(title=title,rule = rule,description=descriptoin,fname=fname)
            await message.channel.send(embed = emb[0],file = emb[1])
        await m.delete()

    elif message.content == "つぎ":
        m =  await message.channel.send("変換中…")
        hensuu1 = [regu_next1,gati_next1,rigu_next1]
        hensuu2 = [regu_next2,gati_next2,rigu_next2]
        files = ["regu_next","gati_next","rigu_next"]
        yougo = ["next","next","next"]
        time = [next_time,next_time,next_time]
        rules = ["regu","gati","rigu"]
        rule_rules = ["",f"({next_gati_rule})",f"({next_rigu_rule})"]
        titles = ["レギュラーマッチ","ガチマッチ","リーグマッチ"]

        for i in range(3):

            title = f"{titles[i]}{rule_rules[i]}\nTime:[{yougo[i]}]({time[i]})"
            rule = rules[i]
            descriptoin = f"{hensuu1[i]}\n{hensuu2[i]}"
            fname = files[i]
            emb = stage.embed(title=title,rule = rule,description=descriptoin,fname=fname)
            await message.channel.send(embed = emb[0],file = emb[1])
        await m.delete()

    elif message.content == "つぎつぎ":
        m =  await message.channel.send("変換中…")
        hensuu1 = [regu_nextnext1,gati_nextnext1,rigu_nextnext1]
        hensuu2 = [regu_nextnext2,gati_nextnext2,rigu_nextnext2]
        files = ["regu_nextnext","gati_nextnext","rigu_nextnext"]
        yougo = ["nextnext","nextnext","nextnext"]
        time = [nextnext_time,nextnext_time,nextnext_time]
        rules = ["regu","gati","rigu"]
        rule_rules = ["",f"({nextnext_gati_rule})",f"({nextnext_rigu_rule})"]
        titles = ["レギュラーマッチ","ガチマッチ","リーグマッチ"]

        for i in range(3):

            title = f"{titles[i]}{rule_rules[i]}\nTime:[{yougo[i]}]({time[i]})"
            rule = rules[i]
            descriptoin = f"{hensuu1[i]}\n{hensuu2[i]}"
            fname = files[i]
            emb = stage.embed(title=title,rule = rule,description=descriptoin,fname=fname)
            await message.channel.send(embed = emb[0],file = emb[1])
        await m.delete()

    elif message.content == "れぎ":
        m =  await message.channel.send("変換中…")
        hensuu1 = [regu_now1,regu_next1,regu_nextnext1]
        hensuu2 = [regu_now2,regu_next2,regu_nextnext2]
        files = ["regu_now","regu_next","regu_nextnext"]
        yougo = ["now","next","nextnext"]
        time = [now_time,next_time,nextnext_time]
        rule_rules = ["","",""]

        for i in range(3):

            title = f"レギュラーマッチ{rule_rules[i]}\nTime:[{yougo[i]}]({time[i]})"
            rule = "regu"
            descriptoin = f"{hensuu1[i]}\n{hensuu2[i]}"
            fname = files[i]
            emb = stage.embed(title=title,rule = rule,description=descriptoin,fname=fname)
            await message.channel.send(embed = emb[0],file = emb[1])
        await m.delete()

    elif message.content == "がち":
        m =  await message.channel.send("変換中…")
        hensuu1 = [gati_now1,gati_next1,gati_nextnext1]
        hensuu2 = [gati_now2,gati_next2,gati_nextnext2]
        files = ["gati_now","gati_next","gati_nextnext"]
        yougo = ["now","next","nextnext"]
        time = [now_time,next_time,nextnext_time]
        rule_rules = [f"({now_gati_rule})",f"({next_gati_rule})",f"({nextnext_gati_rule})"]
        
        for i in range(3):

            title = f"ガチマッチ{rule_rules[i]}\nTime:[{yougo[i]}]({time[i]})"
            rule = "gati"
            descriptoin = f"{hensuu1[i]}\n{hensuu2[i]}"
            fname = files[i]
            emb = stage.embed(title=title,rule = rule,description=descriptoin,fname=fname)
            await message.channel.send(embed = emb[0],file = emb[1])
        await m.delete()

    elif message.content == "りぐ":
        m =  await message.channel.send("変換中…")
        hensuu1 = [rigu_now1,rigu_next1,rigu_nextnext1]
        hensuu2 = [rigu_now2,rigu_next2,rigu_nextnext2]
        files = ["rigu_now","rigu_next","rigu_nextnext"]
        yougo = ["now","next","nextnext"]
        time = [now_time,next_time,nextnext_time]
        rule_rules = [f"({now_rigu_rule})",f"({next_rigu_rule})",f"({nextnext_rigu_rule})"]
        
        for i in range(3):

            title = f"リーグマッチ{rule_rules[i]}\nTime:[{yougo[i]}]({time[i]})"
            rule = "rigu"
            descriptoin = f"{hensuu1[i]}\n{hensuu2[i]}"
            fname = files[i]
            emb = stage.embed(title=title,rule = rule,description=descriptoin,fname=fname)
            await message.channel.send(embed = emb[0],file = emb[1])
        await m.delete()

    elif message.content == "ぶき":

        await message.channel.send("おすすめの武器は…\n\n「" + random.choice(buki) + "」\n\nだ!!")

    elif message.content == "チーム分け":

        if message_tyouhuku_kaihi == 1:
            return
        

        team_member()

        i = len([i for i,x in enumerate(members["member"]) if not x == "登録なし" ])

        """
        if team_wake_settei[1] == 1:
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

        elif team_wake_settei[1] == 2:
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

        elif team_wake_settei[1] == 3:
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

        elif team_wake_settei[1] == 4:
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
        """
        if team_wake_settei[1] == 5:
            reset()
            moving = 0
            poinntosa = 0
            discord_member = []
            kansenn_list = []
            chn_list = []
            dassyutu = 0

            m1 = m2 = m3 = m4 = m5 = m6 = m7 = m8 = m9 = 1
            
            if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9 or i == 10:
            
             #ロール付与
                g = 0
                ww = 0
                m1 = messagee[1] = await message.channel.send("勝敗ポイントが同じになるチーム分けをするぞ‼\nボイスチャンネル移動を行うかどうかをリアクションを付けてくれ‼")

                mooove[1] = 1

                #移動するかどうか
                for hg in range(2):
                    await m1.add_reaction(ri_list["eng"][hg])
                await m1.add_reaction("✅")

                while True:
                    reaction, user = await client.wait_for('reaction_add', check=reaction_check)
                    if ri_list["check"][1] == 1 or ri_list["check"][1] == 2:
                        break
                
                #移動します。
                if ri_list["val"][0] == 1:
                    moving = 1
                    await m1.delete()
                    m2 = await message.channel.send("ボイスチャンネル移動を行うことを確認したぞ‼\n移動のためにロールを付与するぞ‼\n")

                    while True:
                        discord_member = []
                        abc = "<チームメンバー>\n"
                        j = len([i for i,x in enumerate(members["member"]) if not x == "登録なし"])
                        for r in range(j):
                            f = r +1
                            if f + 1 <= 10:
                                f = mojimoji.han_to_zen(str(f))
                            abc += f"{ri_list['num'][r]}：{f}：[{members['member'][r]}]\n"

                        deg = "<discordメンバー>\n"
                        wq = 0

                        for hg  in range(1,11):
                            print(hg)
                            for mm in message.guild.voice_channels:
                                for nn in mm.members:
                                    nb = [nk.name for nk in nn.roles]
                                    dd = [f.name for f in discord_member]
                                    if str(hg) in nb and not nn.name in dd:
                                        deg += f"{ri_list['eng'][wq]}："
                                        if hg< 10:
                                            g = mojimoji.han_to_zen(str(hg))
                                        else:
                                            g = hg
                                            
                                        deg += f"[{g}]：{nn.name}\n"
                                        discord_member.append(nn) 
                                        wq += 1

                        m3 = messagee[1] = await message.channel.send(abc + deg)

                        mooove[1] = 3
                        reset()
                        kaisuu = 0

                        m4 = messagee[1] =  await message.channel.send("\n登録したメンバーとdiscordユーザーを連結させます。\nまずチームメンバーを選択してください")

                        o = [i for i,x in enumerate(members["member"]) if not x == "登録なし"]
                        for ji in o:
                            await m4.add_reaction(ri_list["num"][ji])
                        await m4.add_reaction("✔")
                        await m4.add_reaction("✅")
                        await m4.add_reaction("☑")

                        while True:
                            reaction, user = await client.wait_for('reaction_add', check=reaction_check)
                            if ri_list["check"][1] == 1 or ri_list["check"][1] == 2:
                                break

                        if ri_list["check"][1] == 1:
                            await m4.delete()
                            if not ri_list["chv"]["br_em"] == 1:
                                z = [i for i,x in enumerate(ri_list["multi"]) if x == 1]
                                
                            else:
                                sa = [i for i,x in enumerate(members["member"]) if not x == "登録なし"]
                                z = range(len(sa))

                            for yt in z:
                                print(123)
                                print(yt)
                                
                                if kaisuu != 0:
                                    m3 = messagee[1] = await message.channel.send(abc + deg)

                                m5 = messagee[1] = await message.channel.send(f"{yt+1}：[{members['member'][yt]}]を確認しました。\n次にDiscordメンバーを選択してください")
                                mooove[1] = 1
                                reset()

                                for fj in range(wq):
                                    await m5.add_reaction(ri_list["eng"][fj])
                                await m5.add_reaction("✅")
                                await m5.add_reaction("☑")

                                while True:
                                    reaction, user = await client.wait_for('reaction_add', check=reaction_check)
                                    if ri_list["check"][1] == 1 or ri_list["check"][1] == 2:
                                        break
     
                                if ri_list["check"][1] == 1:
                                    ew = ri_list["val"].index(1)

                                    if not discord_member.index(discord_member[ew]) is None:
                                        rn = [roruna.name for roruna in message.guild.roles]
                                        ri = [roruid.id for roruid in message.guild.roles]
                                        bb = ["1","2","3","4","5","6","7","8","9","10"]
                                        b = [g.name for g in discord_member[ew].roles]
                                        sd = list(set(b) & set(bb))
                                        r_m = []
                                        for rr in sd:
                                            try:
                                                a = rn.index(rr)
                                                r_m.append(a)
                                            except:pass
                                        for ee in r_m:
                                            try:await discord_member[ew].remove_roles(message.guild.get_role(ri[ee]))
                                            except:pass
                                        await discord_member[ew].add_roles(message.guild.get_role(ri[rn.index(str(yt + 1))]))
                                        await m5.delete()
                                        await m3.delete()
                                    
                                    kaisuu = 1
                                    discord_member = []
                                    deg = "<discordメンバー>\n"
                                    wq = 0

                                    for hg  in range(1,11):
                                        for mm in message.guild.voice_channels:
                                            for nn in mm.members:
                                            
                                                nb = [nk.name for nk in nn.roles]
                                                dd = [f.name for f in discord_member]

                                                if str(hg) in nb and not nn.name in dd:
                                                    deg += f"{ri_list['eng'][wq]}："
                                                    if hg< 10:
                                                        g = mojimoji.han_to_zen(str(hg))
                                                    deg += f"[{g}]：{nn.name}\n"
                                                    discord_member.append(nn) 
                                                    wq += 1
                                else:
                                    await m3.delete()
                                    await m5.delete()

                        else:
                            break                        

             #基礎ポイント
                delete_list = [m1, m2, m3,m4,m5]
                for jf in delete_list:
                    try:await jf.delete()
                    except:pass
                mem = len([i for i,x in enumerate(members["member"]) if not x == "登録なし"])
                m6 = messagee[1] = await message.channel.send("\n基礎ポイントを上げるぞ‼\n<付与ポイント>\n1⃣：１ポイント\n2⃣：２ポイント\n3⃣：３ポイント\n")

                qp = ""
                wq = 0
                add_member = []
                for pp in range(4):
                    for q in range(mem):
                        if heikin["point"][q] == pp:
                            f = mojimoji.han_to_zen(str(heikin["point"][q]))
                            qp += f"{ri_list['eng'][wq]}：{f}P：[{members['member'][q]}]\n"
                            add_member.append(members["member"][q])
                            wq += 1

                while True:

                    m7 = messagee[1] = await message.channel.send("<メンバーとポイント>\n" + qp )
                    hanntei = 0
                    reset()
                    mooove[1] = 3
                    rr = 0
                    kk = 0

                    for h in range(3):
                        await m7.add_reaction(ri_list["num"][h])
                    await m7.add_reaction("✔")
                    await m7.add_reaction("✅")
                    await m7.add_reaction("☑")

                    while True:
                        reaction, user = await client.wait_for('reaction_add', check=reaction_check)
                        if ri_list["check"][1] == 1 or ri_list["check"][1] == 2:
                            break

                    if ri_list["check"][1] == 1:
                        if ri_list["chv"]["br_em"] == 1:
                            point_num = [1,2,3]
                        else:
                            point_num = [i+1 for i,x in enumerate(ri_list["multi"]) if x == 1 ]

                        for point in point_num:

                            if not hanntei == 0:
                                m7 = await message.channel.send(f"<メンバーとポイント>\n{qp}")
                            m8 = messagee[1]= await message.channel.send(f"[{point}]ポイントを確認しました。次に付与するメンバーのリアクションを押してください。")
                            reset()
                            mooove[1] = 4
                            
                            for h in range(mem):
                                await m8.add_reaction(ri_list["eng"][h])
                            await m8.add_reaction("✅")
                            await m8.add_reaction("☑")

                            while True:
                                reaction, user = await client.wait_for('reaction_add', check=reaction_check)
                                if ri_list["check"][1] == 1 or ri_list["check"][1] == 2:
                                    break

                            if ri_list["check"][1] == 1:
                                k = [i for i,x in enumerate(ri_list["multi"]) if x == 1]
                                for kk in k:
                                    m = members["member"].index(add_member[kk])
                                    heikin["point"][m] = point

                                qp = ""
                                wq = 0
                                add_member = []
                                for pp in range(4):
                                    for q in range(mem):
                                        if heikin["point"][q] == pp:
                                            f = mojimoji.han_to_zen(str(heikin["point"][q]))
                                            qp += f"{ri_list['eng'][wq]}：{f}P：[{members['member'][q]}]\n"
                                            add_member.append(members["member"][q])
                                            wq += 1

                                await m7.delete()
                                await m8.delete()
                            elif ri_list["check"][1] == 2:
                                await m7.delete()
                                await m8.delete()
                            
                            hanntei = 1
                                    
                    elif ri_list["check"][1] == 2:
                        js = [m6, m7, m8]
                        for me in js:
                            try:await me.delete()
                            except:pass
                        break           
             #ランダムチーム分け
                t = i
                ii = [i for i,x in enumerate(members["member"]) if not x == "登録なし" ]
                for fd in ii:
                    heikin["members"].append(members["member"][fd])
                while True:
                    reset()
                    poinntosa = 0
                    dassyutu = 0
                    kansenn = 0
                    if ww == 0:
                        for d in range(100):
                            for _ in range(1, 10000):
                                
                                c0 = random.sample(list(range(t)), t)


                                if t >= 9:
                                    a = 4
                                    b = [4,8]
                                    #print(kansenn)
                                    #
                                    kansenn = [heikin["members"][c0[i]] for i in range(8,t)]#ランダムでの観戦メンバー
                                    re = list( set(kansenn) & set(kansenn_list))
                                    if not len(re) == 0:
                                        continue

                                else:                                    
                                    b = t // 2  # B
                                    a = t - b  # A
                                    b = [a,t]
                                g1 = 0
                                g2 = 0

                                #A_team
                                for gg in range(a):
                                    g1 += heikin["point"][c0[gg]]
                                #B_team
                                for gg in range(b[0],b[1]):
                                    g2 += heikin["point"][c0[gg]]

                                if g1 > g2:
                                    poinntosa = g1 - g2
                                elif g2 > g1:
                                    poinntosa = g2 - g1
                                elif g1 == g2:
                                    poinntosa = 0

                                team1 = []
                                team2 = []
                                
                                if d == poinntosa:
                                    for v1 in range(a):
                                        team1.append(heikin["members"][c0[v1]])

                                    for v2 in range(b[0],b[1]):
                                        team2.append(heikin["members"][c0[v2]])

                                    aa = ""
                                    bb = ""
                                    cc = ""

                                    for A in range(len(team1)):
                                        aa += f"[{str(team1[A])}]"
                                    for B in range(len(team2)):
                                        bb += f"[{str(team2[B])}]"

                                    for po in range(max(heikin["point"])+1):
                                        cs = [i for i,x in enumerate(heikin["point"]) if x == po]
                                        if cs:
                                            cc += f"[{po}ポイント]\n｜"
                                            for css in cs:
                                                cc += f"[{heikin['members'][css]}]"
                                            cc += "\n"

                                    if t >= 9:
                                        bb +="\n\n< 観　戦 >　"
                                        if t == 9:
                                            kansenn_list.append(heikin['members'][c0[8]])
                                            bb += f"[{heikin['members'][c0[8]]}]"

                                        elif t == 10:
                                            kansenn_list.append(heikin['members'][c0[8]])
                                            kansenn_list.append(heikin['members'][c0[9]])
                                            bb += f"[{heikin['members'][c0[8]]}][{heikin['members'][c0[9]]}]"
                                        
                                        if len(kansenn_list) == t:
                                            kansenn_list = []
                                        

                                    messagee[1] = await message.channel.send(f"チーム分けでのチーム編成は…\n\n<Aチーム>　{aa}\n\n<Bチーム>　{bb}\n\nチームの点差は　{poinntosa}だ‼\n\n<各ポイント>\n{cc}\n<リアクション>\n🇦：Aチームが勝った時\n🇧：Bチームが勝った時\n🇨：チーム分けのチャンネルに移動\n🇩：ロビーに移動")
                                    #移動やらなんやら
                                    while True:
                                        reset()
                                        mooove[1] = 1

                                        for h in range(2):
                                            await messagee[1].add_reaction(ri_list["eng"][h])
                                        if moving == 1:
                                            await messagee[1].add_reaction(ri_list["eng"][2])
                                            await messagee[1].add_reaction(ri_list["eng"][3])
                                        await messagee[1].add_reaction("✅")
                                        await messagee[1].add_reaction("☑")

                                        while True:
                                            reaction, user = await client.wait_for('reaction_add', check=reaction_check)
                                            if ri_list["check"][1] == 1 or ri_list["check"][1] == 2:
                                                break

                                        if ri_list["check"][1] == 1:

                                            yy = ri_list["val"].index(1)
                                            if yy == 0:
                                                for gg in range(a):
                                                    heikin["point"][c0[gg]] += 1
                                                try:await m9.delete()
                                                except:pass
                                                m9 = await message.channel.send("Aチームの勝利‼")
                                                await messagee[1].delete()
                                                dassyutu = 1
                                            
                                            elif yy == 1:
                                                for gg in range(b[0],b[1]):
                                                    heikin["point"][c0[gg]] += 1
                                                try:await m9.delete()
                                                except:pass
                                                m9 = await message.channel.send("Bチームの勝利！")
                                                await messagee[1].delete()
                                                dassyutu = 1

                                            elif yy == 2:
                                                for ll in range(a):
                                                    for bn in message.guild.voice_channels:
                                                        for nnb in bn.members:
                                                            hg = [go.name for go in nnb.roles]
                                                            if str(c0[ll] + 1) in hg :
                                                                await nnb.move_to(client.get_channel(channel_id[2]))
                                                for ll in range(b[0],b[1]):
                                                    for bn in message.guild.voice_channels:
                                                        for nnb in bn.members:
                                                            hg = [go.name for go in nnb.roles]
                                                            if str(c0[ll] + 1) in hg :
                                                                await nnb.move_to(client.get_channel(channel_id[3]))
                                            
                                            elif yy == 3:
                                                for lo in message.guild.voice_channels:
                                                    for bbn in lo.members:
                                                        await bbn.move_to(client.get_channel(channel_id[1]))

                                        elif ri_list["check"][1] == 2:
                                            ww = 1
                                            await message.channel.send("チーム分けを終了したぞ‼")
                                            break
                                        if dassyutu == 1:
                                            break
                                if dassyutu == 1 or ww == 1:
                                    break
                            if dassyutu == 1 or ww == 1:
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

        if message_tyouhuku_kaihi == 1:
            return

        reset()
        m1  = messagee[1] = await message.channel.send("チーム分けの設定をするぞ‼\nチーム分けの人数を確認して次にコマンドを送ってくれ!\n1⃣：登録した人数が均等になるチーム分け\n2⃣：登録した人数を１vs〇でのチーム分け\n3⃣：登録した人数を２vs〇でのチーム分け\n4⃣：登録した人数を３vs〇でのチーム分け\n5⃣：４vs４でのチーム分けでメンバー全員の勝率ポイントが同じになるようなチーム分け\n☑：設定をキャンセルする")
        mooove[1] = 2#数字重複無し

        for ji in range(5):
            await m1.add_reaction(ri_list["num"][ji])
        await m1.add_reaction("✅")
        await m1.add_reaction("☑")

        while True:
            reaction, user = await client.wait_for('reaction_add', check=reaction_check)
            if ri_list["check"][1] == 1 or ri_list["check"][1] == 2:
                break
        
        if ri_list["check"][1] == 1:

            e = ri_list["val"].index(1)
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
            heikin["setting"] = e

        if ri_list["check"][1] == 2:
            await message.channel.send("チーム分けをキャンセルしたぞ!!")

    elif message.content == "コマンド情報":
        #await message.channel.send("「いま」　今の各ルールでのステージ情報\n「つぎ」　次の各ルールでのステージ情報\n「つぎつぎ」　次の次の各ルールでのステージ情報\n「れぎ」　レギュラーマッチの今、次、次の次ステージ情報\n「がち」　ガチマッチの今、次、次の次ステージ情報\n「りぐ」　リーグマッチの今、次、次の次ステージ情報\n「ぶき」 ランダム武器選択\n「チーム」　数字でのチーム分け\n「チーム分け」　登録した名前でのチーム分け\n「メンバー登録」　一斉にメンバー登録\n「ち」＋「数字」　数字と同じ番号のメンバー登録を変更\n「リセット」　登録した名前のリセット\n「チームメンバー」 登録した名前一覧")
        # 8人でリーグマッチをやるときは「チーム」と打ってみよう!!チームをランダムで編成するぞ!!\n8人そろって誰がやるかが分かっていたら「チーム分け」と打ってみよう!!
        embed = discord.Embed(
            title = "コマンド一覧",
            descriptoin = "コマンドの名称と処理を記述します",
            color=discord.Colour.red()
        )

        embed.add_field(name="いま",value= " | 今のレギュラーマッチ・ガチマッチ・リーグマッチのルールとステージを表示します。",inline= False)
        embed.add_field(name="つぎ",value=" | 次のレギュラーマッチ・ガチマッチ・リーグマッチのルールとステージを表示します。",inline= False)
        embed.add_field(name="つぎつぎ",value=" | 次の次のレギュラーマッチ・ガチマッチ・リーグマッチのルールとステージを表示します。",inline= False)
        embed.add_field(name="れぎ",value=" | 今・次・次の次のレギュラーマッチのステージを表示します。",inline= False)
        embed.add_field(name="がち",value=" | 今・次・次の次のガチマッチのルールとステージを表示します。",inline= False)
        embed.add_field(name="りぐ",value=" | 今・次・次の次のリーグマッチのルールとステージを表示します。",inline= False)
        embed.add_field(name="チームメンバー",value=" | 現在登録しているメンバー一覧を表示します。",inline= False)
        embed.add_field(name="メンバー登録",value=" | チーム分けに必要なメンバーを登録します。",inline= False)
        embed.add_field(name="メンバーリセット",value=" | 現在登録してあるメンバーを選択式でリセットします。",inline= False)
        embed.add_field(name="チャンネル設定",value=" | チーム分けの「平均分け」の時に使用する、移動のために必要なボイスチャンネルを3つ設定します。",inline= False)
        embed.add_field(name="チーム分け設定",value=" | チーム分けの設定を行います。",inline= False)
        embed.add_field(name="チーム分け",value=" | チーム分け設定で設定されている方法で登録してあるメンバーをランダムで選択し表示します。",inline= False)

        await message.channel.send(embed = embed)

    elif message.content == "チャンネル設定":

        if message_tyouhuku_kaihi == 1:
            return

        if message.author.voice is None:
            await message.channel.send("ボイスチャンネルに接続して(入って)いないぞ‼\n接続してからやり直してくれ‼")
        else:
            reset()
            chn = ""
            m1 = m2 = m3 = ""
            channel = [channel.name for channel in message.guild.voice_channels]
            check_list = ["✔","✅","☑"]
            channel_malti = []
            chn_list = []
            
            for ch in range(len(channel)):
                voice = ri_list["eng"][ch]
                chn += f"{voice} : [{channel[ch]}]\n"
                chn_list.append(ri_list["eng"][ch])

            channel_id_number = 0

            mooove[1] = 1#eng
            mooove[2] = []

            m1 = await message.channel.send(f"移動先のボイスチャンネルを設定します。\n\n<チャンネル一覧>\n{chn}")
            channel_name = ["「ロビー」", "「Aチーム」", "「Bチーム」"]
            for i in channel_name:

                reset()
                m2 = messagee[1]= await message.channel.send(f"{i}にするチャンネルの名前に割り振られたリアクションを付けてくれ‼")

                #リアクション付加
                for h in range(len(chn_list)):
                    await messagee[1].add_reaction(chn_list[h])

                #重複削除
                if channel_malti:
                    for g in channel_malti:
                        await messagee[1].clear_reaction(ri_list["eng"][g])
                await messagee[1].add_reaction("✅")

                while True:
                    reaction, user = await client.wait_for('reaction_add', check=reaction_check)
                    if ri_list["check"][1] == 1 or ri_list["check"][1] == 2:
                        break

                if ri_list["check"][1] == 1:
                    await m2.delete()
                    if m3:
                        await m3.delete()
                    
                    jk = ri_list["val"].index(1)

                    channel_malti.append(jk)
                    k = [channel.name for channel in message.guild.voice_channels]
                    c = [channel.id for channel in message.guild.voice_channels]

                    channel_id_number += 1
                    channel_id[channel_id_number] = c[jk]
                    if not channel_id_number == 3:
                        m3 = await message.channel.send(f"{i}にするチャンネルは「{str(k[jk])}]")
            try:await m3.delete()
            except:pass
            await message.channel.send(f"\n<チャンネル確認>\n「ロビー」→「{str(client.get_channel(channel_id[1]))}」\n「Aチーム」→「{str(client.get_channel(channel_id[2]))}」\n「Bチーム」→「{str(client.get_channel(channel_id[3]))}」")

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
