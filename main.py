from nextcord.ext import commands; from os import system, environ, listdir; from nextcord import Intents; bot = commands.Bot(command_prefix=['Angel.', 'angel.', 'A.', 'a.'], intents=Intents.all(), help_command=None)
@bot.command()
async def reloadcogs(ctx):
  if ctx.author.id not in [884220029867003916, 551134188695191563]: return await ctx.send('Tu peux pas ahah')
  for fn in listdir("./cogs"): bot.unload_extension(f'cogs.{fn[: -3]}') if fn.endswith('.py') else print('no file')
  for fn in listdir("./cogs"): bot.load_extension(f'cogs.{fn[: -3]}') if fn.endswith('.py') else print('no file')
  await ctx.send('Reloaded')
for fn in listdir("./cogs"): bot.load_extension(f'cogs.{fn[: -3]}') if fn.endswith('.py') else print('no file')
bot.run(environ['token'])
