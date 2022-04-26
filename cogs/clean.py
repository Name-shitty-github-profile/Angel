from nextcord.ext import commands
class Clean(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def clean(self, ctx, name = None):
    if not any(word in str(', '.join([str(p[0]).replace("_", " ").title() for p in ctx.author.guild_permissions if p[1]])).lower() for word in ['admin']): return await ctx.send("Tu ne peux pas faire cela !")
    if not name: return await ctx.send('Le nom du channel est obligatoire')
    channels = roles = 0
    for channel in ctx.guild.channels:
      if channel.name == name.lower():
        await channel.delete()
        channels += 1
    for role in ctx.guild.roles:
      if role.name == name.lower():
        await role.delete()
        roles += 1
    await ctx.send(f'Serveur clean !\nSalons cleans : {channels}\nRoles cleans : {roles}')

def setup(bot):
  bot.add_cog(Clean(bot))
