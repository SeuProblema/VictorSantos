from highrise import *
from highrise.models import *
import asyncio
from asyncio import Task

emote_list : list[tuple[str, str]] = [('smooch','emote-kissing-bound'),('fairyfloat','idle-floating'),('fairytwirl','emote-looping'),('kissing','emote-kissing-bound'),('tiktok11','dance-tiktok11'),('tiktok','dance-tiktok11'),('tik11','dance-tiktok11'),('gottago','idle-toilet'),('astronaut', 'emote-astronaut'),('wrong','dance-wrong'),('fashion','emote-fashionista'),('gravity','emote-gravity'),('icecream','dance-icecream'),('casual','idle-dance-casual'),('kiss','emote-kiss'),('no','emote-no'),('sad','emote-sad'),('yes','emote-yes'),('lau','emote-laughing'),('hello','emote-hello'),('wave','emote-wave'),('shy','emote-shy'),('tired','emote-tired'),('flirt','emote-lust'),('flirtywave','emote-lust'),('flirty','emote-lust'),('greedy','emote-greedy'),('model','emote-model'),('bow','emote-bow'),('curtsy','emote-curtsy'),('snowball','emote-snowball'),('hot','emote-hot'),('snowangel','emote-snowangel'),('charging','emote-charging'),('confused','emote-confused'),('telekinesis','emote-telekinesis'),('float','emote-float'),('teleport','emote-teleporting'),('maniac','emote-maniac'),('energyball','emote-energyball'),('snake','emote-snake'),('frog','emote-frog'),('superpose','emote-superpose'),('cute','emote-cute'),('pose7','emote-pose7'),('pose8','emote-pose8'),('pose1','emote-pose1'),('pose5','emote-pose5'),('pose3','emote-pose3'),('cutey','emote-cutey'),('tik10','dance-tiktok10'),('sing','idle_singing'),('singing','idle_singing'),('enthused','idle-enthusiastic'),('shop','dance-shoppingcart'),('russian','dance-russian'),('pennywise','dance-pennywise'),('tik2','dance-tiktok2'),('dontstartnow','dance-tiktok2'),('blackpink','dance-blackpink'),('kpop','dance-blackpink'),('celebrate','emoji-celebrate'),('gagging','emoji-gagging'),('flex','emoji-flex'),('cursing','emoji-cursing'),('thumbsup','emoji-thumbsup'),('angry','emoji-angry'),('punk','emote-punkguitar'),('zombie','emote-zombierun'),('sit','idle-loop-sitfloor'),('fight','emote-swordfight'),('ren','dance-macarena'),('wei','dance-weird'),('tik8','dance-tiktok8'),('savage','dance-tiktok8'),('tik9','dance-tiktok9'),('viral','dance-tiktok9'),('uwu','idle-uwu'),('tik4','idle-dance-tiktok4'),('sayso','idle-dance-tiktok4'),('star','emote-stargazer'),('pose9','emote-pose9'),('boxer','emote-boxer'),('guitar','idle-guitar'),('penguin','dance-pinguin'),('pinguin','dance-pinguin'),('zero','emote-astronaut'),('anime','dance-anime'),('saunter','dance-anime'),('creepy','dance-creepypuppet'),('watch','emote-creepycute'),('revelations','emote-headblowup'),('revelation','emote-headblowup'),('bashful','emote-shy2'),('arabesque','emote-pose10'),('pose10','emote-pose10'),('party','emote-celebrate'),('skating','emote-iceskating'),('scritchy','idle-wild'),('bitnervous','idle-nervous'),('nervous','idle-nervous'),('timejump','emote-timejump'),('jump','emote-timejump'),('jingle','dance-jinglebell'),('hyped','emote-hyped'),('sleigh','emote-sleigh'),('surprise','emote-pose6'),('repose','sit-relaxed'),('relaxed','sit-relaxed'),('kawaii','dance-kawai'),('kawai','dance-kawai'),('touch','dance-touch'),('gift','emote-gift'),('pushit','dance-employee'),('salute','emote-cutesalute'),('launch','emote-launch')]

async def loop(self: BaseBot, user: User, message: str) -> None:
    # Defining the loop_emote method locally so it cann't be accessed from the command handler.
    async def loop_emote(self: BaseBot, user: User, emote_name: str) -> None:
        emote_id = ""
        for emote in emote_list:
            if emote[0].lower() == emote_name.lower():
                emote_id = emote[1]
                break
        if emote_id == "":
          
            return
        user_position = None
        user_in_room = False
        room_users = (await self.highrise.get_room_users()).content
        for room_user, position in room_users:
            if room_user.id == user.id:
                user_position = position
                start_position = position
                user_in_room = True
                break
        if user_position == None:
            await self.highrise.send_whisper(user.id,f"🚫🔄 @{user.username} Para Parar o Loop Basta Apenas Andar🔄🚫")
            return
        await self.highrise.send_whisper(user.id,f"👯🏻‍♂️🔄 @{user.username} Você Está Em Loop : {emote_name} 👯🏻‍♂️🔄")
        while start_position == user_position:
            print(f"Loop {emote_name} - {user.username}")
            try:
                await self.highrise.send_emote(emote_id, user.id)
            except:
                await self.highrise.send_whisper(user.id,f"✅️{user.username} Siga <@Ashokk> Para Novas Novidades e Mande Ideias Na Nossa Hastag : #Ashokk ✅️")
                return
            await asyncio.sleep(10)
            room_users = (await self.highrise.get_room_users()).content
            user_in_room = False
            for room_user, position in room_users:
                if room_user.id == user.id:
                    user_position = position
                    user_in_room = True
                    break
            if user_in_room == False:
                break
    try:
        splited_message = message.split(" ")
        # The emote name is every string after the first one
        emote_name = " ".join(splited_message[1:])
        print(emote_name)
    except:
        await self.highrise.send_whisper(user.id,f"✅️ @{user.username} Siga <@Ashokk> Para Novas Novidades e Mande Ideias Na Nossa Hastag : #Ashokk ✅️")
        return
    else:   
        taskgroup = self.highrise.tg
        task_list : list[Task] = list(taskgroup._tasks)
        for task in task_list:
            if task.get_name() == user.username:
                # Removes the task from the task group
                task.cancel()
                
        taskgroup.create_task(coro=loop_emote(self, user, emote_name))

            
async def stop_loop(self: BaseBot, user: User, message: str) -> None:
        taskgroup = self.highrise.tg
        task_list : list[Task] = list(taskgroup._tasks)
        for task in task_list:
            if task.get_name() == user.username:
                task.cancel()
                await self.highrise.send_whisper(user.id,f"✅️ @{user.username} Siga <@Ashokk> Para Novas Novidades e Mande Ideias Na Nossa Hastag : #Ashokk ✅️")
                return
        await self.highrise.send_whisper(user.id,f"✅️ @{user.username} Siga <@Ashokk> Para Novas Novidades e Mande Ideias Na Nossa Hastag : #Ashokk ✅️")
        return