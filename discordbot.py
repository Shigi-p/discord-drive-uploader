# インストールした discord.py を読み込む
import discord
import requests
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from dotenv import load_dotenv
import random
import re
import csv
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import pprint

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CLIENT_SECRET_JSON = os.getenv('CLIENT_SECRET_JSON')
GENERAL = os.getenv('GENERAL')
TEST_DISCORD_BOT = os.getenv('TEST_DISCORD_BOT')

pprint.pprint([GENERAL, TEST_DISCORD_BOT])

SCOPES = [
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive.install",
]

# 環境変数の中身をjsonにパースしてから利用する
# secret = json.loads(os.getenv("CLIENT_SECRET_JSON"))
# oath_obj = InstalledAppFlow.from_client_config(secret, SCOPES)

TOKEN = BOT_TOKEN

selifs = []

with open('selif.csv') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i == 0:
            continue
        selifs.append(row)

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')


def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(r.content)


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    pick = random.choice(selifs)
    pick_selif = f'{pick[2]} | {pick[0]}:{pick[1]}'

    if message.author.bot:
        return
    if message.content == '/selif':
        await message.channel.send(pick_selif)
    elif message.content and message.channel.id in [int(GENERAL), int(TEST_DISCORD_BOT)]:
        if int(random.uniform(0, 100)) <= 30:
            await message.channel.send(pick_selif)
    # if message.content.startswith('/pic'):
    #     filename = message.attachments[0].filename
    #     download_img(message.attachments[0].url, "image.png")

    #     # GoogleDrive接続
    #     gauth = GoogleAuth()
    #     print(f"gauth = {gauth}")
    #     gauth.CommandLineAuth()
    #     drive = GoogleDrive(gauth)
    #     f = drive.CreateFile({  'title': filename,
    #                             'mimeType': 'image/jepg'
    #     })
    #     f.SetContentFile('image.png')
    #     f.Upload()


client.run(TOKEN)