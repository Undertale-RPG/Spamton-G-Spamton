class ConsoleColors:
    HEADER  = '\033[95m'
    BLUE    = '\033[94m'
    CYAN    = '\033[96m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[1;33m'
    LRED    = '\033[1;31m'
    WARNING = '\033[93m'
    FAIL    = '\033[91m'
    ENDC    = '\033[0m'
    BOLD    = '\033[1m'
    UNDER   = '\033[4m'

async def create_guild(inter, mem):
    dat = await inter.bot.players.find_one({"_id": mem.id})
    if dat is None:
        new_account = {
            # unique idx
            "_id": inter.guild.id,

            #channel id's
            "logs_chan": None,
            "join_chan": None,
            "leave_chan": None,

            #role id's
            "admin_role": None,
            "mod_role": None
        }

        await inter.bot.players.insert_one(new_account)
    else:
        return