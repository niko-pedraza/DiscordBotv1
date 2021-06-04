import discord
import random
from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_fun(self):
        print('Bot is ready, loaded in Fun Cog')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined a server, welcome.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server, goodbye.')

    @commands.command()
    async def clear(self, ctx, amount=2):
        if amount == 0:
            pass
        else:
            await ctx.channel.purge(limit=amount)

    @commands.command(aliases=["give me a job"])
    async def give_me_a_job(self, ctx, *, redacted):
        responses = [f"Thank you for your interest in joining the {redacted} team. While we were impressed with "
                     "your background and experience, we have concluded that another candidate’s qualifications "
                     "more closely match the requirements of this position. We will keep your resume in our files "
                     "to review for future openings, and in the event an "
                     "appropriate position is available, we will not hesitate "
                     f"to contact you.Again, thank you for your interest in {redacted}, and you have our best "
                     "wishes in your search."
            , f'Thank you for taking the time to apply to {redacted}. We appreciate your interest in joining '
              f'{redacted}. When you submit your application to us, we look for certain minimum requirements essential '
              f'for the role. Though your achievements are impressive, they didn’t exactly line up with what we’re '
              f'looking for in this particular job. For example, you may not have met the required years of '
              f'experience, education or other minimum requirements.We understand that being rejected is always '
              f'disappointing no matter how far along you’ve made it in the process. But, don’t let it hold you back. '
              f'Your relationship with {redacted} doesn’t end here and there are some things you can do to open '
              f'yourself up to other possibilities'
            , f'We wanted to notify you that {redacted} and all associated postings have been closed. This will not '
              f'affect your application status on other open requisitions.We appreciate your interest in {redacted}, '
              f'and encourage you to visit {redacted} Jobs for the most current opportunities.'
            , f'Thank you for the interest you have expressed in the {redacted} position and in employment with '
              f'{redacted}.We have reviewed your resume and have carefully considered your qualifications. While your '
              f'skills are certainly impressive, we have decided to pursue other candidates for this position. Please '
              f'be assured that your application was given full consideration.If you have applied for other positions, '
              f'please note that this message is only in reference to the {redacted} position. We encourage you to '
              f'visit our website at {redacted} in the future for positions with our company that you may find of '
              f'interest.']
        await ctx.send(random.choice(responses))

    @give_me_a_job.error
    async def job_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please write a Company after command :)")

    @commands.command(aliases=["Francisco", "Frank", "francisco", "frankie"])
    async def Frankie(self, ctx):
        await ctx.send('https://youtu.be/X1u93x1oGdE\nhttps://youtu.be/Zd8vzIRQLLM')

    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question):
        answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
                   "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
                   "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
                   "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                   "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
        await ctx.send(f'Question:{question}\nAnswer: {random.choice(answers)}')

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please write a question after command :)")

    @commands.command(aliases=["kelsey"])
    async def Kelsey(self, ctx):
        await ctx.send('Makes bomb ass Birria <3!!')


def setup(client):
    client.add_cog(Fun(client))
