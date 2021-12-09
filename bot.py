# bot.py
import os
import random
from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER

from discord.ext import commands
from dotenv import load_dotenv

from keepalive import keepalive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='draft')
async def draft(ctx, name1, name2, name3, name4, name5):
    response = ''

    x = PrettyTable()
    x.set_style(DOUBLE_BORDER)

    players = [name1, name2, name3, name4, name5]
    roles = ['Top', 'Jungle', 'Mid', 'ADC', 'Sup']

    topchamps = ['Akshan','Aatrox','Akali','Camille','Cho\'Gath','Darius','Dr. Mundo','Fiora','Gangplank','Garen','Gnar','Gwen','Gragas','Graves','Heimerdinger','Illaoi','Irelia','Jax','Jayce','Karma','Kayle','Kennen','Kled','Malphite','Maokai','Mordekaiser','Nasus','Ornn','Pantheon','Poppy','Quinn','Renekton','Rengar','Riven','Rumble','Ryze','Sett','Shen','Singed','Sion','Sylas','Tahm Kench','Teemo','Trundle','Tryndamere','Urgot','Vayne','Viktor','Viego','Vladimir','Volibear','Warwick','Wukong','Yasuo','Yone','Yorick','Zed']
    jngchamps = ['Amumu','Brand','Diana','Ekko','Elise','Evelynn','Fiddlesticks','Gragas','Graves','Hecarim','Ivern','Jarvan IV','Karthus','Kayn','Kha\'Zix','Kindred','Lee Sin','Lillia','Malphite','Master Yi','Nidalee','Nocturne','Nunu and Willump','Olaf','Poppy','Qiyana','Rammus','Rek\'Sai','Rengar','Sejuani','Shaco','Shyvana','Skarner','Taliyah','Talon','Trundle','Udyr','Vi','Volibear','Warwick','Xin Zhao','Zac','Viego','Zed']
    midchamps = ['Akshan', 'Ahri','Akali','Anivia','Annie','Aurelion Sol','Azir','Brand','Cassiopeia','Cho\'Gath','Corki','Diana','Ekko','Fizz','Galio','Gangplank','Heimerdinger','Irelia','Karthus','Kassadin','Katarina','Kayle','LeBlanc','Lissandra','Lucian','Lux','Malphite','Malzahar','Morgana','Neeko','Orianna','Pantheon','Qiyana','Rumble','Ryze','Seraphine','Sylas','Syndra','Taliyah','Talon','Tristana','Twisted Fate','Veigar','Vel\'Koz','Vex','Viego','Viktor','Vladimir','Xerath','Yasuo','Yone','Zed','Ziggs','Zilean','Zoe','Zyra']
    adcchamps = ['Akshan','Aphelios','Ashe','Caitlyn','Draven','Ezreal','Heimerdinger','Jhin','Jinx','Kai\'Sa','Kalista','Kog\'Maw','Lucian','Miss Fortune','Samira','Senna','Seraphine','Syndra','Tristana','Twitch','Varus','Vayne','Veigar','Vex','Xayah','Yasuo','Ziggs']
    supchamps = ['Alistar','Ashe','Bard','Blitzcrank','Brand','Braum','Galio','Gragas','Janna','Jarvan IV','Karma','Leona','Lulu','Lux','Malphite','Morgana','Nami','Nautilus','Neeko','Poppy','Pyke','Rakan','Rell','Senna','Seraphine','Sett','Shaco','Shen','Sona','Soraka','Swain','Tahm Kench','Taric','Thresh','Trundle','Veigar','Vel\'Koz','Vex','Xerath','Yuumi','Zilean','Zyra']
    rolechamps = [topchamps, jngchamps, midchamps, adcchamps, supchamps]

    draft = []

    for i in range(5):
        l = random.randrange(5-i)
        positionchamps = []
        for p in range(3):
            y = random.randrange(len(rolechamps[i]))
            positionchamps.append(rolechamps[i][y])
            rolechamps[i].remove(rolechamps[i][y])
        positon = [players[l], roles[i], positionchamps]
        draft.append(positon)
        players.remove(players[l])

    x.field_names = ["Role", "Player", "Champions"]

    for player in draft:
        champstring = ''

        for p in range(2):
            champstring = champstring + player[2][p] + ', '
        champstring = champstring + player[2][2]

        x.add_row([player[1],  player[0], champstring])

    x.align = "l"
    response = '```\n' + x.get_string() + '```'
    await ctx.send(response)

keepalive()
bot.run(TOKEN)