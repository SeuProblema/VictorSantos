from highrise import *
from highrise.models import *
from highrise import BaseBot  ,User

async def fly(self: BaseBot, user: User, message: str)-> None:
    """
            Teleports the user to the specified user or coordinate
            Usage: /fly <x,y,z>
                                                            """
    #separates the message into parts
    #part 1 is the command "/teleport"
    #part 2 is the name of the user to teleport to (if it exists)
    #part 3 is the coordinates to teleport to (if it exists)
    try:
        command, coordinate = message.split(" ")
    except:
        
        return
    try:
        x, y, z = coordinate.split(",")
    except:
        
        return
    await self.highrise.teleport(user.id, dest = Position(float(x), float(y), float(z)))