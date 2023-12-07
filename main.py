import image_generator
import bot

if __name__ == "__main__":
    image_generator.access_key = "Unsplash API Key"
    TOKEN = "Discord Bot Token"
    bot.run_discord_bot(TOKEN)