from highrise import BaseBot
from highrise.models import SessionMetadata, User

class Bot(BaseBot):
    
    DANCES = {
        "1": "emote-hello",
        "2": "dance-macarena",
        "3": "emote-dance",
        "4": "dance-tiktok",
        "5": "dance-breakdance",
        "6": "dance-russian",
        "7": "dance-shuffle",
        "8": "dance-twist",
        "9": "dance-samba",
        "10": "dance-silly",
        "11": "dance-floss",
        "12": "dance-gangnam",
        "13": "emote-laugh",
        "14": "emote-kiss",
        "15": "emote-wave",
        "16": "emote-sit",
        "17": "emote-clap",
        "18": "emote-bow",
        "19": "emote-flirt",
        "20": "emote-cheer",
        "21": "emote-kissblow",
        "22": "emote-curtsy",
        "23": "emote-salute",
        "24": "emote-flex",
        "25": "emote-dab",
        "26": "emote-angry",
        "27": "emote-sad",
        "28": "emote-shy",
        "29": "emote-tired",
        "30": "emote-yes",
    }

    async def on_start(self, session_metadata: SessionMetadata):
        print("✅ البوت شغال!")
        await self.highrise.chat("🎵 بوت الرقصات شغال! اكتب رقم من 1-30 باش ترقصني!")

    async def on_user_join(self, user: User):
        welcome_msg = f"مرحبا بيك عندنا {user.username} 🎉"
        await self.highrise.chat(welcome_msg)
        print(f"👋 شخص دخل: {user.username}")

    async def on_chat(self, user: User, message: str):
        print(f"💬 {user.username}: {message}")
        msg = message.strip()
        if msg in self.DANCES:
            emote_id = self.DANCES[msg]
            try:
                await self.highrise.send_emote(emote_id)
                print(f"🎵 رقصت: {emote_id}")
            except Exception as e:
                print(f"❌ خطأ: {e}")
                await self.highrise.chat(f"ما قدرتش نرقص هاذي يا {user.username} 😅")
        elif msg.lower() in ["رقصات", "list", "help", "مساعدة"]:
            dances_list = "🎵 **قائمة الرقصات:**\n"
            for num, emote in self.DANCES.items():
                dances_list += f"{num}. {emote}\n"
            await self.highrise.chat(dances_list[:500])
