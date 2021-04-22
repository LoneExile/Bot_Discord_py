import discord
import requests
import D_TOKEN
import json


client = discord.Client()


def get_quotes():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    for quote_give in json_data:
        quote = f"{quote_give['q']}\n by {quote_give['a']}"
        # print(type(json_data))
        # print(json_data[0]["q"])
    return quote


#  get_quotes()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    #  don't respond to ourselves
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        quote = get_quotes()
        await message.channel.send(f"{quote} ")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print("Message from {0.author}: {0.content}".format(message))
    #  lock user channel to command bot

    channel_lock = "bot"

    if str(message.channel) == channel_lock:
        await message.channel.send("!play here")
    elif "{0.content}".format(message) == "!play":
        await message.delete()


client.run(D_TOKEN.TOKEN)
