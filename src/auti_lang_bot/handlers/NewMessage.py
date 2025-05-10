from telethon import events

async def init(client):
    @client.on(events.NewMessage)
    async def handler(event):
        await event.reply('test')
