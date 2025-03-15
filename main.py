import discord
from discord.ext import commands

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix=".", intents=intents)

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def deny(ctx, *, reason="No Reason Provided"):
        if ctx.channel.type == discord.ChannelType.public_thread:
            thread = ctx.channel
            suggester = "Invalid"
            try:
                fetched = await thread.fetch_message(thread.id)
                starter_message = fetched.content
                suggester = fetched.author.id
            except discord.NotFound:
                starter_message = "Invalid Suggestion"
            except discord.HTTPException:
                starter_message = "Error Fetching Suggestion"
            embed_test = discord.Embed(title="Denied Suggestion", color=0xff0000)
            embed_test.add_field(name=ctx.channel.name, value=f"Suggested by <@{suggester}>", inline=False)
            embed_test.add_field(name="Suggestion", value=starter_message, inline=False)
            embed_test.add_field(name="Reason", value=reason, inline=False)
            embed_test.set_footer(text="elytra.minehut.gg")
            output_channel = bot.get_channel(1341894725359239260)
            if output_channel is None:
                output_channel = await bot.fetch_channel(1341894725359239260)
            if suggester != "Invalid":
                await output_channel.send(f"<@{suggester}>", embed=embed_test)
            else:
                await output_channel.send(embed=embed_test)
            await thread.delete()
        else:
            await ctx.send("This only works in **forum channels!**")

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def accept(ctx, *, reason="No Reason Provided"):
        if ctx.channel.type == discord.ChannelType.public_thread:
            thread = ctx.channel
            suggester = "Invalid"
            try:
                fetched = await thread.fetch_message(thread.id)
                starter_message = fetched.content
                suggester = fetched.author.id
            except discord.NotFound:
                starter_message = "Invalid Suggestion"
            except discord.HTTPException:
                starter_message = "Error Fetching Suggestion"
            embed_test = discord.Embed(title="Accepted Suggestion", color=0x00ff00)
            embed_test.add_field(name=ctx.channel.name, value=f"Suggested by <@{suggester}>", inline=False)
            embed_test.add_field(name="Suggestion", value=starter_message, inline=False)
            embed_test.add_field(name="Reason", value=reason, inline=False)
            embed_test.set_footer(text="elytra.minehut.gg")
            output_channel = bot.get_channel(1341894725359239260)
            if output_channel is None:
                output_channel = await bot.fetch_channel(1341894725359239260)
            if suggester != "Invalid":
                await output_channel.send(f"<@{suggester}>", embed=embed_test)
            else:
                await output_channel.send(embed=embed_test)
            await thread.delete()
        else:
            await ctx.send("This only works in **forum channels!**")

    bot.run('BOT_TOKEN')

if __name__ == "__main__":
    run()
