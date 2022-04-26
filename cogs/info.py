from nextcord import Embed, Member; from nextcord.ext import commands
class Info(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def serverinfo(self, ctx):
    bots = 0
    for member in ctx.guild.members:
      if member.bot: bots += 1
    embed = Embed(title=f'Information sur le serveur {ctx.guild.name}', description=f"Toutes les informations possible d'avoir sur le serveur {ctx.guild.name}", color = 0x99aab5).add_field(name='Salon', value=f"Nombres de categories : {len(ctx.guild.categories)}\nNombres de salons textuels : {len(ctx.guild.text_channels)}\nNombres de vocaux : {len(ctx.guild.voice_channels)}").add_field(name="Date", value = f"Creation du serveur : {ctx.guild.created_at.__format__('%A, %d. %B %Y %H:%M:%S')}\nCreation du compte du owner ({ctx.guild.owner.name}) : {ctx.guild.owner.created_at.__format__('%A, %d. %B %Y %H:%M:%S')}").add_field(name="Id", value = f"Id du serveur : {ctx.guild.id}\nId du owner : {ctx.guild.owner.id}").set_thumbnail(url=ctx.guild.icon.url).add_field(name="Membres", value=f"Membres totaux : {len(ctx.guild.members)}\nBots : {bots}\nHumain : {int(len(ctx.guild.members))  - bots}").add_field(name='Roles', value = f"{len(ctx.guild.roles)}"); emojistr = ""
    if len(ctx.guild.emojis) != 0:
      for emoji in ctx.guild.emojis: emojistr = f"{emojistr}, {str(emoji)}"
      embed.add_field(name='Emojis', value=emojistr)
    await ctx.send(embed=embed)

  @commands.command()
  async def userinfo(self, ctx, member: Member = None):
    member = ctx.author if not member else print('\n')
    roles = ''
    for role in ctx.author.roles: roles = f"{roles}\n{role.mention}"
    embed = Embed(title=f'information de {member.name}', description=f'Toutes les informations possible sur {member.name}', color = 0x99aab5).add_field(name='Roles', value=f"{roles}").add_field(name="Creation du compte", value = f"{ctx.author.created_at.__format__('%A, %d. %B %Y %H:%M:%S')}").add_field(name='Id', value = f'{ctx.author.id}').set_thumbnail(url=ctx.author.avatar.url)
    await ctx.send(embed=embed)
    
    
def setup(bot):
  bot.add_cog(Info(bot))
