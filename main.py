import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties  # ✅ Import DefaultBotProperties
from data_scraper import *
from Message_formatter import *

# TOKEN = "7577429699:AAFDna2WDWzLRhQehvVUyjVqIwyPd7-Ix7A"
TOKEN = "7649783739:AAEDScFMr9Xek8vM4u-VRc_eTq4ay8unyhg"

# ✅ Fix: Use DefaultBotProperties to set parse_mode
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="MarkdownV2"))
dp = Dispatcher()

category_links = {
    "android": "android",
    "angular": "angularjs",
    "bootstrap": "bootstrap",
    "c": "c",
    "cpp": "cpp",
    "csharp": "csharp",
    "css": "css",
    "dsa": "data-structure",
    "debug": "debug-test",
    "dev-tools": "development-tools",
    "django": "django",
    "drupal": "drupal",
    "ecom": "e-commerce",
    "hacking": "ethical-hacking",
    "gamedev": "game-development",
    "git": "git",
    "hardware": "hardware",
    "html": "html",
    "ios": "ios",
    "java": "java",
    "js": "javascript",
    "jquery": "jquery",
    "json": "json",
    "ml": "machine-learning",
    "matlab": "matlab",
    "mobile-dev": "mobile-development-other",
    "mysql": "mysql",
    "node": "nodejs",
    "nosql": "nosql",
    "php": "php",
    "other-prog": "programming-other",
    "python": "python",
    "r": "r-programming",
    "react": "react-redux",
    "robotics": "robotics",
    "ruby": "ruby",
    "seo": "seo",
    "software": "software",
    "sql": "sql",
    "sys-prog": "system-programming",
    "ux": "ux",
    "web-dev": "web-development-other",
    "wordpress": "wordpress",
    "vue": "vue",
    "modeling": "3d-model",
    "after-effects": "after-effects",
    "animation": "animation",
    "design": "graphic-design",
    "photo": "photography",
    "photoshop": "photoshop",
    "premiere": "premiere-pro",
    "video": "video-design",
    "aws": "aws",
    "hosting": "hosting",
    "linux": "linux",
    "mac": "mac",
    "security": "network-security",
    "windows": "windows",
    "win-server": "windows-server",
    "academic": "academic",
    "blockchain": "blockchain",
    "business": "business",
    "cert": "certification",
    "health": "health-fitness",
    "languages": "languages",
    "lifestyle": "lifestyle",
    "marketing": "marketing",
    "music": "music",
    "office": "office-productivity",
    "personal-dev": "personal-development",
    "social-media": "social-media",
}


@dp.message(Command("courses"))
async def send_courses(message: Message):
    count = 0
    query = message.text.replace("/courses", "").strip()
    if query == '':
        for link in links:
            print(f"sent {count} / {len(links)}")
            count += 1
            await message.answer(formated_message(link), parse_mode=None)
    else:
        course_count = int(query)
        if course_count > len(links):
            course_count = len(links)
        for link in links[:course_count]:
            count += 1
            print(f"sent {count} / {len(links[:course_count])}")

            await message.answer(formated_message(link), parse_mode=None)


@dp.message(Command("update"))
async def updater(message: Message):
    query = message.text.replace("/update", "").strip().lower()
    if query in category_links:
        udemy_links(f"https://www.discudemy.com/category/{category_links[query]}/")
    else:
        udemy_links("https://www.discudemy.com/all/")

    await message.answer("✅ *Links Update Done*")


@dp.message(Command("help"))
async def help_command(message: Message):
    help_text = "*Available Categories:*\n\n"
    help_text += "\n".join([f"`{key}`" for key in category_links.keys()])
    help_text += "\n\nUse `/update <category>` to fetch new links\nExample: `/update python`"

    await message.answer(help_text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
