import discord

### REFERENCES ###
# https://realpython.com/how-to-make-a-discord-bot-python/
# https://discordpy.readthedocs.io/en/stable/api.html
# https://github.com/Rapptz/discord.py/tree/master/examples
# https://gist.github.com/makupi/c508c9d33bb01dcc04e57d1a93c23ae1
# https://github.com/Arthurdw/Reaction-Role

#TODO: Move to .env file
GUILD_ID = 791115181325287464
ROLES_CHANNEL_ID = 984886829415268453

guild = discord.Client.get_guild(GUILD_ID)
## Initialization and Role Assignment ##




# Create the roles for the different events if they don't already exist
# Ancient Arena, Ancient Nightmare, Battlegrounds, Demon Gates, Haunted Carriage
# Shadow Assembly, Shadow Lottery, Vaults
roles = ["Ancient Arena", "Ancient Nightmare", "Battlegrounds", "Demon Gates", "Haunted Carriage", "Shadow Assembly", "Shadow Lottery", "Vaults"]
for role in roles:
    discord.Guild.create_role(name = role)

# Create a post, "React here to receive pings for specific events! If you want to stop receiving these pings, click the button a second time"

# Add reactions to the post for each of the different events

# When a reaction is clicked on, toggle the role on the member (add it if they don't have it, remove it if they do)

###################################################################

## 10 minutes prior to each event, send out a reminder message @theAppropriateRole(s) ##

