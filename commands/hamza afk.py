import discord
from discord.ext import commands
from discord import app_commands
import config


global afkState
afkState = False

class afk(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="afk", description="Set afk status for support.")
    async def ping(self, interaction: discord.Interaction):
        try:
            if interaction.user.id != 496673945211240462:
                embed = discord.Embed(
                    color=discord.Colour.blurple(),
                    title='AFK Mode',
                    description='Only <@496673945211240462> can use this command.')
                embed.set_footer(text=f"HEO Systems Bot | version: {config.AVA_VERSION}", icon_url=config.FOOTER_ICON)
                await interaction.response.send_message(embed=embed)
                return
            global afkState
            if afkState == False:
                embed = discord.Embed(
                    color=discord.Colour.blurple(),
                    title='AFK Mode',
                    description='AFK mode is now enabled. When you are getting pinged we will let them know you are are not avaliable.')
                embed.set_footer(text=f"HEO Systems Bot | version: {config.AVA_VERSION}", icon_url=config.FOOTER_ICON)
                await interaction.response.send_message(embed=embed)
                afkState = True
                return
            else:
                embed = discord.Embed(
                    color=discord.Colour.blurple(),
                    title='AFK Mode',
                    description='AFK mode is now disabled. We wont let others know you are not avaliable anymore.')
                embed.set_footer(text=f"HEO Systems Bot | version: {config.AVA_VERSION}", icon_url=config.FOOTER_ICON)
                await interaction.response.send_message(embed=embed)
                afkState = False
                return
        except Exception as e:
            print(e)
            await interaction.followup.send(content='Error occured.')
    
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if afkState == False:
            return
        if message.mentions or message.role_mentions:
            user_id_to_check = 496673945211240462
            author_id_to_ignore = 1010270368814092400
            role_id_to_check = 1042142018740162680
            
            for user in message.mentions:
                if user.id == user_id_to_check and not message.mention_everyone:
                    if message.author.id == author_id_to_ignore:
                        return
                    embed = discord.Embed(
                        color=discord.Colour.blurple(),
                        title="Not Available.",
                        description="Hamza is currently unavailable. He will get back to you as soon as possible, likely because he is either asleep or busy."
                    )
                    embed.set_footer(text=f"HEO Systems Bot | version: {config.AVA_VERSION}", icon_url=config.FOOTER_ICON)
                    await message.reply(embed=embed)
                    return
            
            for role in message.role_mentions:
                if role.id == role_id_to_check and not message.mention_everyone:
                    embed = discord.Embed(
                        color=discord.Colour.blurple(),
                        title="Not Available.",
                        description="Hamza is currently unavailable. He will get back to you as soon as possible, likely because he is either asleep or busy."
                    )
                    embed.set_footer(text=f"HEO Systems Bot | version: {config.AVA_VERSION}", icon_url=config.FOOTER_ICON)
                    await message.reply(embed=embed)
                    return


async def setup(client:commands.Bot) -> None:
    await client.add_cog(afk(client))
