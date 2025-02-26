import re
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/../../model')
import userManagement

async def playBlackJack(self, message, db, command):
    moneyStrings = re.findall(f"^玩 21点 ([0-9]+\.?[0-9]*) \<\@\![0-9]+\>$", command)
    money = int(float(moneyStrings[0]) * 100)
    if len(message.mentions) == 0:
        await message.channel.send("不知道你要跟谁玩")
        return
    alphaPlayerInfo = userManagement.getUser(db, message.author.id)
    betaPlayerInfo = userManagement.getUser(db, message.mentions)
    if alphaPlayerInfo[1] < money:
        await message.channel.send("你不够钱")
        return
    if betaPlayerInfo[1] < money:
        await message.channel.send("他（她）不够钱")
        return

