import io
import os
import discord

from errlog import log
from dotenv import load_dotenv
from discord import Intents, Client, Message, errors
from eventhandler import prompt_logic, info
from image import image_handler

load_dotenv()

token = os.getenv("token")
if not token:
    newtoken = input("enter your discord bot token: ")
    with open(".env", "w") as file:
        file.write(f"token={newtoken}")
        token = newtoken

intents: Intents = Intents.default()
bot: Client = Client(intents=intents)


async def send_message(message: Message, user_message: str) -> None:
    user_message = message.content
    response: str = await prompt_logic(prompt=user_message)





    try:
        if message.attachments:
            for attachment in message.attachments:
                if attachment.content_type and 'image' in attachment.content_type:
                    image_url = attachment.url
                    image_response = await image_handler(image_url)
                    await message.channel.send(str(image_response))
                elif attachment.filename.endswith(".txt"):
                    textfile = await attachment.read()
                    text = textfile.decode("utf-8")
                    print(text)
                    response = await prompt_logic(prompt=str(user_message + text))

    except Exception as AttachmentErr:
        log(f"Attachment Error: {AttachmentErr}")

    try:

        if response:
            if len(response) > info["clim"]:
                splitresponse = response.split(f"\n")
                for response in splitresponse:
                    if not response == "":
                        await message.author.send(response)

            elif response == "":
                return

            else:
                await message.author.send(response)
    except Exception as ResponseErr:
        log(f"Response Error: {ResponseErr}")
        text_file = io.BytesIO(response.encode('utf-8'))
        text_file.name = "response.txt"
        await message.author.send(file=discord.File(fp=text_file, filename=text_file.name))


@bot.event
async def on_ready() -> None:
    log(f"Logged in as {bot.user}")


@bot.event
async def on_message(message: Message) -> None:
    if message.author == bot.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    async with message.channel.typing():
        await send_message(message, user_message)
        return


def main() -> None:
    bot.run(token=token)


if __name__ == "__main__":
    main()
