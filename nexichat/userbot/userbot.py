import asyncio
from os import getenv
from config import OWNER_ID
from dotenv import load_dotenv
from pyrogram import Client
import config


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="VIPAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=False,
            plugins=dict(root="nexichat.mplugin"),
        )
        

    async def start(self):
        print(f"Starting Assistants...")

        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("ammichatt")
                await self.one.join_chat("ammichatt")
                await self.one.join_chat("ammichatt")
                await self.one.join_chat("ammichatt")

            except:
                pass
            
            try:
                await self.one.send_message(config.OWNER_ID, "**ɪ'ᴍ sᴛᴀʀᴛᴇᴅ ʙᴀʙʏ !**")
                
            except Exception as e:
                print(f"{e}")

            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
     
            print(f"Id-Chatbot Started as {self.one.me.first_name}")

        

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Id-Chatbot...")
        try:
            if config.STRING1:
                await self.one.stop()
        except:
            pass
