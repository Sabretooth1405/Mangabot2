
import discord
import asyncio
import reddit_scrape_manga
#from keep_alive import keep_alive
#mport requests
client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #channel=client.get_channel(989101760335458344)
    # time.sleep(15)
    #await channel.send("$update")

  
    
@client.event
async def on_message(message):

    if message.content.startswith('$update'):
      
      print('SENDING....')
      
     
      
       # await message.channel.send(reddit_scrape_manga.update())
      send_list = reddit_scrape_manga.update()
      for manga in send_list:
          await message.channel.send(str(manga))
      await asyncio.sleep(900)
      await message.channel.send('$update')

#client.run("OTg5NDM2NTMzNjMzMzQzNTA4.G1NoLT.jFU7Z7PtWMYECKc-ldGxp7o9RdnNtaisEn678k")

#keep_alive()
#req = requests.get("https://discord.com/api/path/to/the/endpoint")

#print(req.headers["X-RateLimit-Remaining"])
          
def run():
  client.run(
	    "OTg5NDM2NTMzNjMzMzQzNTA4.G1NoLT.jFU7Z7PtWMYECKc-ldGxp7o9RdnNtaisEn678k")
