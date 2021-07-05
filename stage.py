import cv2
import discord
 
stage_name_list = ["バッテラストリート","フジツボスポーツクラブ","ガンガゼ野外音楽堂","コンブトラック","海女美術大学","チョウザメ造船","タチウオパーキング","ホッケふ頭","マンタマリア号","モズク農園","エンガワ河川敷","Ｂバスパーク","ザトウマーケット","ハコフグ倉庫","デボン海洋博物館","アロワナモール","アジフライスタジアム","ショッツル鉱山","モンガラキャンプ場","スメーシーワールド","ホテルニューオートロ","アンチョビットゲームズ","ムツゴ楼"]
stage_url_list = ["battera","hujitubo","gangase","konbu","amami","tyouzame","tatiuo","hokke","mannta","mozuku","engawa","bbasu","zatou","hakohugu","debon","arowana","ajihurai","syotturu","mongara","sumesi","ootoro","antyobi","mutugo"]
stage_name = None
stage_url = None

#web: python stage.py
def rule(inf_rule):
    rule_name = ""
    big_rule_list = ["ガチマッチ","リーグマッチ"]
    rule_list = ["ガチホコバトル","ガチヤグラ","ガチアサリ","ガチエリア"]
    for big in big_rule_list:
        for i in rule_list:
            if inf_rule == f"{big}({i})":
                rule_name = i
                break
    return rule_name

def stage_image(inf_stage1,inf_stage2,file_name):
    path = [inf_stage1,inf_stage2]
    for number_path in range(len(path)):
        for i in range(len(stage_name_list)):
            if path[number_path] == stage_name_list[i]:
                path[number_path] = f"splatoon_stage_image/stage_image/{stage_url_list[i]}.jpg"
                break
    #print(path)
    img1 = cv2.imread(path[0])
    img2 = cv2.imread(path[1])

    after_image = cv2.hconcat([img1,img2]) 
    cv2.imwrite(f"splatoon_stage_image/after_image/{file_name}.jpg",after_image)

def embed(title,rule,description,fname):
    colour = None
    if rule == "regu":
        colour = discord.Colour.from_rgb(0,255,0)
    elif rule == "gati":
        colour = discord.Colour.from_rgb(255,165,0)
    elif rule == "rigu":
        colour = discord.Colour.from_rgb(255,20,147)

    embed = discord.Embed(
        title = title,
        color = colour,
        description = description
        )

    file_name=f"{fname}.jpg" 
    file = discord.File(fp=f"splatoon_stage_image/after_image/{fname}.jpg",filename = file_name,spoiler=False)
    
    embed.set_image(url=f"attachment://{file_name}")
    return [embed,file]
