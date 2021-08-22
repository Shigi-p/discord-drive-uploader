# インストールした discord.py を読み込む
import discord
import requests
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from dotenv import load_dotenv
load_dotenv()

import os
BOT_TOKEN = os.getenv('BOT_TOKEN')

# 自分のBotのアクセストークンに置き換えてください
TOKEN = BOT_TOKEN

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(r.content)


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    # 「/pic」と発言した場合の処理
    if message.content.startswith('/pic'):
        print(f"message is {message}")
        print(f"message.attachments is {message.attachments}")

        filename = message.attachments[0].filename
        download_img(message.attachments[0].url, "image.png")

        # GoogleDrive接続
        gauth = GoogleAuth()
        gauth.CommandLineAuth()
        drive = GoogleDrive(gauth)
        f = drive.CreateFile({  'title': filename,
                                'mimeType': 'image/jepg'
        })
        f.SetContentFile('image.png')
        f.Upload()


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)