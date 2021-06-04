import discord
from discord.ext import commands


class Work(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_work(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game("these hoes"))

    # print('Bot is ready, loaded in Work Cog')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server, goodbye.')

    @commands.command()
    async def clear(self, ctx, amount=2):
        if amount == 0:
            pass
        else:
            await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'kicked {member.mention}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):

        await member.ban(reason=reason)
        await ctx.send(f'banned {member.mention}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'unbanned {user.mention}')
                return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def test(self, ctx):
        await ctx.send("Administrator only function successful")


def setup(client):
    client.add_cog(Work(client))
