import random
import os
import importlib.util
from highrise import*
from highrise import BaseBot,Position
from highrise.models import SessionMetadata

louca = ["🤪Seu Livel De Loucura é de : 100%","🤪Seu Livel De Loucura é de : 99%","🤪Seu Livel De Loucura é de : 50%","🤪Seu Livel De Loucura é de : 0%","🤪Seu Livel De Loucura é de : 1%","🤪Seu Livel De Loucura é de : 2%","🤪Seu Livel De Loucura é de : 64%","🤪Seu Livel De Loucura é de : 22%","🤪Seu Livel De Loucura é de : 19%","🤪Seu Livel De Loucura é de : 88%","🤪Seu Livel De Loucura é de : 39%","🤪Seu Livel De Loucura é de : 40%","🤪Seu Livel De Loucura é de : 92%","🤪Seu Livel De Loucura é de : 74%","🤪Seu Livel De Loucura é de : 10%","🤪Seu Livel De Loucura é de : 9%","🤪Seu Livel De Loucura é de : 77%","🤪Seu Livel De Loucura é de : 82%","🤪Seu Livel De Loucura é de : 66%","🤪Seu Livel De Loucura é de : 11%","🤪Seu Livel De Loucura é de : 15%"]
        
casa = ["Eu Caso Com Você 💍","Claro Que sim 💍❤️","Não Quero 💍💔","Claro Que Não 💍💔","Eu Te Amo Claro Que Eu Caso Com Você 💍"]


curativo = ["🔴Você Usou o Curativo Sua Vida Está em : 100%🔴","🔴Você Usou o Curativo Sua Vida Está em : 50%🔴","🔴Você Usou o Curativo Sua Vida Está em : 60%🔴","🔴Você Usou o Curativo Sua Vida Está em : 75%🔴","🔴Você Usou o Curativo Sua Vida Está em : 85%🔴","🔴Você Usou o Curativo Sua Vida Está em : 80%🔴","🔴Você Usou o Curativo Sua Vida Está em : 90%🔴","🔴Você Usou o Curativo Sua Vida Está em : 95%🔴","🔴Você Usou o Curativo Sua Vida Está em : 99%🔴","🔴Você Usou o Curativo Sua Vida Está em : 91%🔴"]
         
bomba = ["💣🧟‍♂️ Você Jogou Uma Bomba em 1x Boss Zombie 🧟‍♀️💣","💣🧟 Você Jogou Uma Bomba em 3x Boss Zombie 🧟💣","💣🧟‍♂️ Você Jogou Uma Bomba em 2x Boss Zombie 💣🧟‍♀️","💣🧟‍♂️ Você Jogou Uma Bomba em 7x Boss Zombie 💣🧟‍♂️","💣🧟 Você Jogou Uma Bomba em 4x Boss Zombie 🧟💣"]

facada = ["🧟🔪 Você Esfaqueou 1x Zombie 🔪🧟","🧟🔪 Você Esfaqueou 6x Zombie 🔪🧟","🧟🔪 Você Esfaqueou 7x Zombie 🔪🧟","🧟‍♂️🔪🧟‍♂️ Você Esfaqueou  8x Zombie 🔪🧟‍♂️","🧟🔪 Você Esfaqueou  10x Zombie 🔪🧟","🧟🔪 Você Esfaqueou  9x Zombie 🔪🧟","🧟‍♀️🔪🧟‍♂️ Você Esfaqueou  3x Zombie 🧟‍♂️🔪🧟‍♀️"]

atirar = ["🧟Você Atirou em 5x Zombie🧟","🧟Você Atirou em 1x Zombie🧟","🧟Você Atirou em 8x Zombie🧟","🧟Você Atirou em 3x Zombie🧟","🧟‍♂️Você Atirou em 5x Zombie🧟‍♂️","🧟‍♀️Você Atirou em 10x Zombie🧟‍♀️","🧟🧟‍♀️Você Atirou em 9x Zombie🧟🧟‍♀️"]

play = ["🔴Sua Vida Está em 50% use : /curativo","🔴Sua Vida Está em 20% use : /curativo","🔴Sua Vida Está em 40% use : /curativo","🧟Os Zombies Estão Vindo Use : /facada ou /atirar","🧟🧟‍♂️ Tem Muitos Zombies 🧟‍♀️🧟 🛡 Use : /escudo 🛡","🧟O Zombie Boss Esta  Vindo Use : /bomba ","🧟Os Zombies Estão Vindo Use : /facada ou /atirar","🧟🧟‍♂️ Tem Muitos Zombies 🧟‍♀️🧟 🛡 Use : /escudo 🛡","🔴Sua Vida Está em 60% use : /curativo","🔴Sua Vida Está em 10% use : /curativo","🧟Os Zombies Estão Vindo Use : /facada ou /atirar"
      ,"🧟Os Zombies Estão Vindo Use : /facada ou /atirar","🧟Os Zombies Estão Vindo Use : /facada ou /atirar","🧟Os Zombies Estão Vindo Use : /facada ou /atirar","🧟Os Zombies Estão Vindo Use : /facada ou /atirar","🧟Os Zombies Estão Vindo Use : /facada ou /atirar"]

pescar = ["🥈VOCÊ GANHOU A MEDALHA : PESCADOR PRATA🥈","🥉VOCÊ GANHOU A MEDALHA : PESCADOR BRONZE🥉","🥉VOCÊ GANHOU A MEDALHA : PESCADOR BRONZE🥉","🥉VOCÊ GANHOU A MEDALHA : PESCADOR BRONZE🥉","🥉VOCÊ GANHOU A MEDALHA : PESCADOR BRONZE🥉","🟡Evento :  /carpa 🟡","⚫️Você Pescou 3x Lua Da Noite⚫️(+150 PONTOS)","⚫️Você Pescou 2x Lua Da Noite⚫️(+100 PONTOS)","⚫️Você Pescou 1x Lua Da Noite⚫️(+50 PONTOS)","🟡Você Pescou 1x Camarão Dourado 🟡 (MULTIPLO PONTO)","🟡Você Pescou 1x Linguado Dourado🟡 (MULTIPLO PONTO)","🪼🌈Você Pescou 1x Polvo Arco-iris🪼🌈 (EXTRA PONTOS)","🐢Você Pescou 3x  Tartaruga 🐢 (PERDA DE PONTOS)","🦑Você Pescou 1x  Lula Gigante 🦑 (LEGENDARIO)","🦀Você Pescou 6x  Carangueijo 🦀 (COMUM)","🦀Você Pescou 2x  Carangueijo 🦀 (COMUM)","🦀Você Pescou 8x  Carangueijo 🦀 (COMUM)","🪼Você Pescou 1x Polvo Do Mar🪼(EPICO)","🦈Você Pescou 2x Tubarão🦈 (EPICO)","🦈Você Pescou 5x Tubarão🦈 (EPICO)","🦈Você Pescou 8x Tubarão🦈 (EPICO)","🦈Você Pescou 1x Tubarão🦈 (EPICO)","🐠Você Pescou 1x Tuna Do Mar🐠 (LEGENDARIO)","🐠Você Pescou 3x Peixe Palhaço🐠 (LEGENDARIO)","🐠Você Pescou 3x Tuna Do Mar🐠 (LEGENDARIO)","🐠Você Pescou 1x Peixe Palhaço🐠 (LEGENDARIO)","🐠Você Pescou 8x Peixe Palhaço🐠 (LEGENDARIO)","🐠Você Pescou 10x Peixe Palhaço🐠 (LEGENDARIO)","🐟Você Pescou 1x Salmão🐟 (RARE)","🧜🏼‍♀️Você Pescou 5x Sereia🧜🏼‍♀️(EPICO)","🧜🏼‍♀️Você Pescou 2x Sereia🧜🏼‍♀️(EPICO)","🧜🏼‍♀️Você Pescou 1x Sereia🧜🏼‍♀️(EPICO)","🐟Você Pescou 3x Salmão🐟 (RARE)","🟡Você Pescou 1x Tilapia Dourada🟡 (MULTIPLO PONTO)","☠️🐋Você Pescou 3x Baleia Morta☠️🐋 (PERDA DE PONTOS)","🐋Você Pescou 11x Baleia Do Mar🐋(COMUM)","🐋🌈Você Pescou 1x Baleia Arco-iris🌈🐋 (EXTRA PONTOS)","🥈VOCÊ GANHOU A MEDALHA : PESCADOR PRATA🥈","🥇VOCÊ GANHOU A MEDALHA : PESCADOR OURO🥇","🏅VOCÊ GANHOU A MEDALHA : ESTRELA PESCADOR🏅","💎Evento : /camarão💎"]

cantada = ["Posso tirar uma foto sua? É para mostrar ao Papai Noel o que eu quero de presente.","Se preto fosse paixão e branco fosse carinho, o que eu sinto por você seria xadrezinho.","Qual é o número da polícia? Infelizmente, terei que te denunciar por roubar meu coração.","Meus amigos apostaram comigo que eu não conseguiria iniciar uma conversa com a pessoa mais bonita daqui. Como devemos gastar o dinheiro deles?","Prazer, eu sou um ladrão/uma ladra. Estou aqui para roubar o seu coração.","Pesquisas apontam que agente junto é erro de gramática, mas a gente separado é erro do destino.","Se nada dura para sempre, quer ser o meu nada?","Seu nome é Wi-Fi? Porque eu estou sentindo uma conexão aqui.","Está vendo aquela estrela ali? Mandei pendurar para você.","Então, além de me deixar sem ar, o que mais você faz?","Nossa, estou sentindo uma dor no peito! Espero que seja amor, porque se for infarto, eu nunca mais te verei!","As rosas são vermelhas, violetas são azuis, eu não sei rimar, mas posso namorar você?","Você foi feita(o) com velas, mel, fitinhas vermelhas e rosas? Porque te achei uma simpatia."]

piada = ["Qual é o prato preferido do Thor? Thorresmo","O que o cavalo foi fazer no orelhão? Passar trote","Qual é o rio mais azedo do mundo? O Rio Solimões","Qual é o lugar mais certo do Brasil? O sertão.","Qual é o vinho que não tem álcool? Ovinho de codorna"]

hate = ["As pessoas te odeiam 0%","As pessoas te odeiam 20%","As pessoas te odeiam 100%","As pessoas te odeiam 50%","As pessoas te odeiam 45%","As pessoas te odeiam 99%","As pessoas te odeiam 95%","As pessoas te odeiam 34%","As pessoas te odeiam 77%","As pessoas te odeiam 80%","As pessoas te odeiam 66%","As pessoas te odeiam 39%","As pessoas te odeiam 20%","As pessoas te odeiam 22%","As pessoas te odeiam 49%"]

amor = ["As pessoas te amam 0%❤️","As pessoas te amam 20%❤️","As pessoas te amam 100%❤️","As pessoas te amam 50%❤️","As pessoas te amam 45%❤️","As pessoas te amam 99%❤️","As pessoas te amam 95%❤️","As pessoas te amam 34%❤️","As pessoas te amam 77%❤️","As pessoas te amam 80%❤️","As pessoas te amam 66%❤️","As pessoas te amam 39%❤️","As pessoas te amam 20%❤️","As pessoas te amam 22%❤️","As pessoas te amam 49%❤️"]


class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("funcionando")
        await self.highrise.walk_to(Position(0.5 ,0.0 ,9.5 , "FrontLeft"))
    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} entrou na sala")   
        await self.highrise.send_whisper(user.id,f"🍓Bem vindo(a) {user.username} use 1 ao 97 ou !emote list para ver  a lista de emotes.🍓")
    
        await self.highrise.send_emote("dance-hipshake")
      
        await self.highrise.send_emote("idle-floating",user.id) 
      
    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")  
           
        if message.startswith("/pescar"):
            await self.highrise.send_whisper(user.id,"Você Está Pescando 🎣...")
          
        if message.lower() == "/pescar":
           frase = random.choice(pescar)
           await self.highrise.send_whisper(user.id,frase)
        
        if message.lower() == "/bomba":
           frase = random.choice(bomba)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/facada":
           frase = random.choice(facada)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/curativo":
           frase = random.choice(curativo)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/play":
           frase = random.choice(play)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/atirar":
           frase = random.choice(atirar)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/meu nivel de loucura":
           frase = random.choice(louca)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/loucura":
           frase = random.choice(louca)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/casa cmg?":
           frase = random.choice(casa)
           await self.highrise.chat(frase)
             
        if message.startswith("/pescar"):
           await self.highrise.react("clap",user.id)

        if message.startswith("/carpa"):
           await self.highrise.react("clap",user.id)
           await self.highrise.send_whisper(user.id,"🟡Você Pescou 1x Carpa Dourada🟡 VOCÊ GANHOU A MEDALHA : (MEGA PESCADOR)")
          
        if message.startswith("/camarão"):
           await self.highrise.react("clap",user.id)
           await self.highrise.send_whisper(user.id,"💎Você Pescou 1x Camarão De Diamante💎VOCÊ GANHOU A MEDALHA : (PESCADOR MASTER DIAMANTE )")                                
        if message.startswith("/curativo"):
           await self.highrise.react("heart",user.id)

        if message.startswith("/escudo"):
           await self.highrise.react("heart",user.id)
           await self.highrise.send_whisper(user.id,f"@{user.username} 🛡 Você Usou O Escudo🛡")

        if message.lower() == "/quantas pessoas me amam":
           frase = random.choice(amor)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/amor":
           frase = random.choice(amor)
           await self.highrise.send_whisper(user.id,frase)
            
        if message.lower() == "/quantas pessoas me odeiam":
           frase = random.choice(hate)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/odio":
           frase = random.choice(hate)
           await self.highrise.send_whisper(user.id,frase)
      
        if message.lower() == "/piada":
           frase = random.choice(piada)
           await self.highrise.chat(frase)

        if message.lower() == "/cantada":
           frase = random.choice(cantada)
           await self.highrise.chat(frase)
          
        if        message.startswith("/tele") or              message.startswith("/tp") or              message.startswith("/fly") or     message.startswith("!tele") or      message.startswith("!tp") or     message.startswith("!fly"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":            await self.teleporter(message)

        if        message.startswith("/") or              message.startswith("-") or              message.startswith(".") or          message.startswith("!"):
            await self.command_handler(user, message)
          
        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Fashion All , Wrong All , Cutey All , Superpose All , Punk All , Tiktok2 All, Tiktok8 All , Tiktok9 All , Tiktok10 All , Gagging All , Blackpink All , Creepy All , Revelation All , Bashful All , Arabesque All , Party All")

        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Pose3 All , Pose7 All , Pose5 All , Pose1 All , Enthused All , Pose8 All , Sing All , Teleport All , Telekinesis All , Casual All , Icecream All , Watch All")

        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Zombie All , Celebrate All , Kiss All , Bow All , Snowangel All , Confused All , Charging All , Wei All , Cursing All , Greedy All , Russian All , Shop All , Model All , Ren All , Tiktok4 All , Snake All , Uwu All")

        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Skating All , Time All , Gottago All  , Scritchy All , Bitnervous All , Jingle All , Curtsy All , Hot All , Hyped All ,Sleigh All , Surprise All, Repose All , Kawaii All , Touch All , Gift All , Pushit All , Tiktok All , Smooch All , Launch All")
          
        if        message.startswith("!lista") or    message.startswith("!emote list") or                                 message.startswith("!emote list") or message.startswith("!list"):
            await self.highrise.send_whisper(user.id,"!angry ,!thumbsup , !cursing , !flex , !gagging , !celebrate , !blackpink , !tiktok2 , !tiktok9 , !pennywise , !russian , !shop , !enthused , !singing ,!wrong , !guitar , !pinguin , !astronaut , !saunter , !flirt , !creepy , !watch , !revelation")
          
        if        message.startswith("!lista") or    message.startswith("!emote list") or                                 message.startswith("!emote list") or message.startswith("!list"):
            await self.highrise.send_whisper(user.id,"!tiktok10 ,!tiktok8 , !cutey , !pose3 , !pose5 , !pose1 , !pose8 , !pose7  !pose9 , !cute , !superpose , !frog , !snake , !energyball , !maniac , !teleport , !float , !telekinesi , !fight , !wei , !fashion , !boxer , !bashful , !arabesque , !party")
          
        if        message.startswith("!lista") or    message.startswith("!emote list") or                                 message.startswith("!emote list") or message.startswith("!list"):
            await self.highrise.send_whisper(user.id,"!confused , !charging , !snowangel , !hot , !snowball , !curtsy , !bow ,!model , !greedy , !tired , !shy , !wave , !hello , !lau ,!yes , !sad , !no , !kiss , !casual , !ren , !sit , !punk , !zombie , !gravity , !icecream ,!uwu , !sayso , !star")

        if        message.startswith("!lista") or    message.startswith("!emote list") or                                 message.startswith("!emote list") or message.startswith("!list"):
          await self.highrise.send_whisper(user.id,"!skating , !bitnervous , !scritchy , !timejump , !gottago , !jingle , !hyped , !sleigh , !surprise , !repose , !kawaii , !touch , !gift , !pushit , !tiktok , !salute , !attention , !smooch , !launch")
          
        if        message.startswith("/lista") or    message.startswith("/emote list") or                                 message.startswith("/emote list") or message.startswith("/list"):
            await self.highrise.send_whisper(user.id,"/angry ,/thumbsup , /cursing , /flex , /gagging , /celebrate , /blackpink , /tiktok2 , /tiktok9 , /pennywise , /russian , /shop , /enthused , /singing , /wrong , /guitar , /pinguin , /astronaut , /saunter , /flirt , /creepy , /watch , /revelation")
          
        if        message.startswith("/lista") or    message.startswith("/emote list") or                                 message.startswith("/emote list") or message.startswith("/list"):
            await self.highrise.send_whisper(user.id,"/tiktok10 , /tiktok8 , /cutey , /pose3 , /pose5 , /pose1 , /pose8 , /pose7  /pose9 , /cute , /superpose , /frog , /snake , /energyball , /maniac , /teleport , /float , /telekinesi , /fight , /wei , /fashion , /boxer , /bashful , /arabesque , /party")
          
        if        message.startswith("/lista") or    message.startswith("/emote list") or                                 message.startswith("/emote list") or message.startswith("/list"):
            await self.highrise.send_whisper(user.id,"/confused , /charging , /snowangel , /hot , /snowball , /curtsy , /bow ,/model , /greedy , /lust , /tired , /shy , /wave , /hello , /lau , /yes , /sad , /no , /kiss , /casual , /ren ,   /sit , /punk , /zombie , /gravity , /icecream ,/uwu , /sayso , /star")

        if        message.startswith("/lista") or    message.startswith("/emote list") or                                 message.startswith("/emote list") or message.startswith("/list"):
          await self.highrise.send_whisper(user.id,"/skating , /bitnervous , /scritchy , /timejump , /gottago , /jingle , /hyped , /sleigh , /surprise , /repose , /kawaii /touch , /pushit , /gift , /tiktok , /salute , /attention , /smooch , /launch")
        
        if        message.startswith("/lista") or         message.startswith("/emote list") or message.startswith("!emoteall") or message.startswith("!emote list") or message.startswith("!lista"):
            await self.highrise.send_emote("dance-floss")

        if        message.startswith("Feio") or      message.startswith("feio") or      message.startswith("veado") or message.startswith("Veado"):
            await self.highrise.chat(f"REPETE!!! {user.username} 🤬🤬")
            await self.highrise.send_emote("emote-swordfight")

        if        message.startswith("corno") or      message.startswith("Corno") or      message.startswith("Vagabundo") or message.startswith("vagabundo"):
            await self.highrise.chat(f"SEU PAI!!! {user.username} 🤬🤬")
            await self.highrise.send_emote("emote-swordfight")

        if        message.startswith("/pessoas") or      message.startswith("!pessoas"):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Há  {len(room_users)} pessoas na sala ")
            await self.highrise.send_emote("dance-floss")
                      
        if        message.startswith("gostoso") or      message.startswith("Gostoso") or      message.startswith("GOSTOSO"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_emote("idle-uwu", user.id)
            await self.highrise.chat(f"Voce tambem e gostoso(a) {user.username} 😳👉👈")

        if             message.startswith("!emotes") or message.startswith("/emotes"):
            await self.highrise.send_emote("emote-robot")
            await self.highrise.send_whisper(user.id,f"emotes disponiveis do numero 1 ao 97")

        if        message.startswith("Help") or      message.startswith("/help") or      message.startswith("!help") or message.startswith("help"):
            await self.highrise.chat(f"/lista | /pessoas | /emotes | /userinfo @ | !emoteall | /casa cmg? | /cantada | /piada / !tele @ | /play | /pescar| corno | gostoso | lindo | feio | !summon @ | !kick @")
            await self.highrise.chat(f"/odio | /amor | /loucura | /cardapio1 | /cardapio2 | [Emote] All | !emote all [Emote]")        
            await self.highrise.chat(f"{user.username} todos os codigos de ativacao devem ser usados >> ! ou /")
            await self.highrise.send_emote("dance-floss")
          
        if        message.startswith("Lindo") or      message.startswith("LINDO") or      message.startswith("lindo"):
            await self.highrise.react("heart",user.id,)
            await self.highrise.chat(f"você tambem e muito lind(a) {user.username} 🥰🥰")
            await self.highrise.send_emote("emote-shy",user.id)
            await self.highrise.send_emote("emote-blowkisses")

        if message.startswith("!palma"):
            await self.highrise.react("clap",user.id)
          
        if        message.startswith("Bom dia") or      message.startswith("Bom Dia") or      message.startswith("bom dia") or message.startswith("BOM DIA"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_whisper(user.id,f"Bom Dia {user.username} 😊🌅")

        if        message.startswith("Boa noite") or      message.startswith("boa noite") or      message.startswith("Boa Noite") or message.startswith("BOA NOITE"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_whisper(user.id,f"Boa Noite {user.username} 😊🌃🌉")

        if        message.startswith("Boa tarde") or      message.startswith("boa tarde") or      message.startswith("Boa Tarde") or message.startswith("BOA TARDE"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_whisper(user.id,f"Boa Tarde {user.username} ☀️")

        if        message.startswith("😡") or      message.startswith("🤬") or      message.startswith("😤") or             message.startswith("🤨") or             message.startswith("😒") or message.startswith("🙄"):
            await self.highrise.send_emote("emote-boxer",user.id)
   
        if        message.startswith("🤔") or      message.startswith("🧐") or      message.startswith("🥸") or             message.startswith("🫤") or message.startswith("😕"):
            await self.highrise.send_emote("emote-confused",user.id)

        if        message.startswith("🤣") or      message.startswith("😂") or             message.startswith("ja") or             message.startswith("Ha") or         message.startswith("Ka") or           message.startswith("Ja") or           message.startswith("ha") or          message.startswith("ks") or             message.startswith("kk") or             message.startswith("Kk") or message.startswith("😁") or message.startswith("😀"):
            await self.highrise.send_emote("emote-laughing",user.id)

        if        message.startswith("😗") or      message.startswith("😘") or      message.startswith("😙") or             message.startswith("💋") or             message.startswith("😚"):
            await self.highrise.send_emote("emote-kiss",user.id)
            await self.highrise.send_emote("emote-blowkisses")

        if        message.startswith("😊") or      message.startswith("🥰") or      message.startswith("😳") or message.startswith("🤗"):
            await self.highrise.send_emote("idle-uwu",user.id)
            await self.highrise.send_emote("emote-blowkisses")

        if        message.startswith("🤢") or      message.startswith("🤮") or      message.startswith("🤧") or             message.startswith("😵‍💫") or message.startswith("🤒"):
            await self.highrise.send_emote("emoji-gagging",user.id)

        if        message.startswith("😱") or      message.startswith("😬") or      message.startswith("😰") or             message.startswith("😫") or message.startswith("😨"):
            await self.highrise.send_emote("idle-nervous",user.id)

        if        message.startswith("😭") or      message.startswith("🥲") or      message.startswith("😓") or             message.startswith("😔") or message.startswith("😥"):
            await self.highrise.send_emote("emote-sad",user.id)
            
        if message.startswith("🤯"):
            await self.highrise.send_emote("emote-headblowup",user.id)

        if        message.startswith("☺️") or      message.startswith("🫣") or       message.startswith("😍") or      message.startswith("🥺") or message.startswith("🥹"):
            await self.highrise.send_emote("emote-shy2",user.id)

        if        message.startswith("😏") or     message.startswith("🙃") or     message.startswith("🤤") or     message.startswith("😋") or     message.startswith("😏") or message.startswith("😈"):
            await self.highrise.send_emote("emote-lust",user.id)           

        if        message.startswith("🥵") or message.startswith("🫠"):
            await self.highrise.send_emote("emote-hot",user.id)
                   
        if        message.startswith("!wrong") or   message.startswith("wrong") or      message.startswith("/wrong") or      message.startswith("Wrong") or message.startswith("1"):
            await self.highrise.send_emote("dance-wrong",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/fashion") or      message.startswith("fashion") or       message.startswith("!fashion") or      message.startswith("Fashion") or message.startswith("2"):
            await self.highrise.send_emote("emote-fashionista",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/gravity") or      message.startswith("gravity") or       message.startswith("!gravity") or      message.startswith("Gravity") or message.startswith("3"):
            await self.highrise.send_emote("emote-gravity",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/icecream") or                                message.startswith("icecream") or message.startswith("!icecream") or      message.startswith("Icecream") or message.startswith("4"):
            await self.highrise.send_emote("dance-icecream",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/casual") or  message.startswith("casual") or     message.startswith("!casual") or      message.startswith("Casual") or message.startswith("5"):
            await self.highrise.send_emote("idle-dance-casual",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/kiss") or      message.startswith("!kiss") or  message.startswith("kiss") or      message.startswith("Kiss") or message.startswith("6"):
            await self.highrise.send_emote("emote-kiss",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/no") or      message.startswith("no") or            message.startswith("!no") or      message.startswith("No") or message.startswith("7"):
            await self.highrise.send_emote("emote-no",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/sad") or      message.startswith("!sad") or    message.startswith("sad") or     message.startswith("Sad") or message.startswith("8"):
            await self.highrise.send_emote("emote-sad",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/yes") or      message.startswith("!yes") or    message.startswith("yes") or     message.startswith("Yes") or message.startswith("9"):
            await self.highrise.send_emote("emote-yes",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/lau") or   message.startswith("laughing") or   message.startswith("Laughing") or   message.startswith("/laughing") or   message.startswith("!laughing") or      message.startswith("!lau") or    message.startswith("Lau") or     message.startswith("lau") or message.startswith("10"):
            await self.highrise.send_emote("emote-laughing",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/hello") or message.startswith("hello") or      message.startswith("!hello") or      message.startswith("Hello") or message.startswith("11"):
            await self.highrise.send_emote("emote-hello",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/wave") or  message.startswith("wave") or     message.startswith("!wave") or      message.startswith("Wave") or message.startswith("12"):
            await self.highrise.send_emote("emote-wave",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/shy") or   message.startswith("shy") or      message.startswith("!shy") or      message.startswith("Shy") or message.startswith("13"):
            await self.highrise.send_emote("emote-shy",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/tired") or message.startswith("tired") or      message.startswith("!tired") or      message.startswith("Tired") or message.startswith("14"):
            await self.highrise.send_emote("emote-tired",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/flirt") or message.startswith("flirt") or message.startswith("flirtywave") or message.startswith("flirty") or      message.startswith("!flirt") or      message.startswith("Flirt") or          message.startswith("/Flirty") or           message.startswith("!Flirty") or           message.startswith("Flirty") or       message.startswith("!flirtywave") or    message.startswith("/flirtywave") or    message.startswith("Flirtywave") or message.startswith("15"):
            await self.highrise.send_emote("emote-lust",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/greedy") or      message.startswith("!greedy") or      message.startswith("Greedy") or message.startswith("greedy") or message.startswith("16"):
            await self.highrise.send_emote("emote-greedy",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/model") or      message.startswith("!model") or      message.startswith("Model") or  message.startswith("model") or message.startswith("17"):
            await self.highrise.send_emote("emote-model",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/bow") or      message.startswith("!bow") or      message.startswith("Bow") or    message.startswith("bow") or message.startswith("18"):
            await self.highrise.send_emote("emote-bow",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/curtsy") or      message.startswith("!curtsy") or      message.startswith("Curtsy") or message.startswith("curtsy") or message.startswith("19"):
            await self.highrise.send_emote("emote-curtsy",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/snowball") or      message.startswith("!snowball") or      message.startswith("Snowball") or                              message.startswith("snowball") or message.startswith("20"):
            await self.highrise.send_emote("emote-snowball",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/hot") or      message.startswith("!hot") or      message.startswith("Hot") or    message.startswith("hot") or message.startswith("21"):
            await self.highrise.send_emote("emote-hot",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/snowangel") or      message.startswith("!snowangel") or      message.startswith("Snowangel") or                              message.startswith("snowangel") or message.startswith("22"):
            await self.highrise.send_emote("emote-snowangel",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/charging") or      message.startswith("!charging") or      message.startswith("Charging") or                              message.startswith("charging") or message.startswith("23"):
            await self.highrise.send_emote("emote-charging",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/confused") or      message.startswith("!confused") or      message.startswith("Confused") or                              message.startswith("confused") or message.startswith("24"):
            await self.highrise.send_emote("emote-confused",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/telekinesis") or      message.startswith("!telekinesis") or      message.startswith("Telekinesis") or                            message.startswith("telekinesis") or message.startswith("25"):
            await self.highrise.send_emote("emote-telekinesis",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/float") or      message.startswith("!float") or      message.startswith("Float") or  message.startswith("float") or message.startswith("26"):
            await self.highrise.send_emote("emote-float",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/teleport") or      message.startswith("!teleport") or      message.startswith("Teleport") or                              message.startswith("teleport") or      message.startswith("27"):
            await self.highrise.send_emote("emote-teleporting",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/maniac") or      message.startswith("!maniac") or      message.startswith("Maniac") or message.startswith("maniac") or message.startswith("28"):
            await self.highrise.send_emote("emote-maniac",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/energyball") or      message.startswith("!energyball") or      message.startswith("Energyball") or                             message.startswith("eneryball") or message.startswith("29"):
            await self.highrise.send_emote("emote-energyball",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/snake") or      message.startswith("!snake") or      message.startswith("Snake") or  message.startswith("snake") or message.startswith("30"):
            await self.highrise.send_emote("emote-snake",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/frog") or      message.startswith("!frog") or      message.startswith("Frog") or   message.startswith("frog") or message.startswith("31"):
            await self.highrise.send_emote("emote-frog",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/superpose") or      message.startswith("!superpose") or      message.startswith("Superpose") or                              message.startswith("superpose") or message.startswith("32"):
            await self.highrise.send_emote("emote-superpose",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/cute") or      message.startswith("!cute") or      message.startswith("Cute") or   message.startswith("cute") or message.startswith("33"):
            await self.highrise.send_emote("emote-cute",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/pose7") or      message.startswith("!pose7") or      message.startswith("Pose7") or  message.startswith("pose7") or message.startswith("34"):
            await self.highrise.send_emote("emote-pose7",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/pose8") or      message.startswith("!pose8") or      message.startswith("Pose8") or  message.startswith("pose8") or message.startswith("35"):
            await self.highrise.send_emote("emote-pose8",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/pose1") or      message.startswith("!pose1") or      message.startswith("Pose1") or  message.startswith("pose1") or message.startswith("36"):
            await self.highrise.send_emote("emote-pose1",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/pose5") or      message.startswith("!pose5") or      message.startswith("Pose5") or  message.startswith("pose5") or message.startswith("37"):
            await self.highrise.send_emote("emote-pose5",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/pose3") or      message.startswith("!pose3") or      message.startswith("Pose3") or  message.startswith("pose3") or message.startswith("38"):
            await self.highrise.send_emote("emote-pose3",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/cutey") or      message.startswith("!cutey") or      message.startswith("Cutey") or  message.startswith("cutey") or message.startswith("39"):
            await self.highrise.send_emote("emote-cutey",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/tik10") or      message.startswith("!tik10") or      message.startswith("Tik10") or  message.startswith("tik10") or message.startswith("40"):
            await self.highrise.send_emote("dance-tiktok10",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/sing") or      message.startswith("!sing") or          message.startswith("Sing") or           message.startswith("Singing") or       message.startswith("/singing") or   message.startswith("!singing") or                              message.startswith("singing") or                              message.startswith("!singalong")  or                             message.startswith("/singalong") or message.startswith("Singaloung") or                             message.startswith("singaloung") or message.startswith("41"):
            await self.highrise.send_emote("idle_singing",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/enthused") or      message.startswith("!enthused") or      message.startswith("Enthused") or                              message.startswith("enthused") or message.startswith("42"):
            await self.highrise.send_emote("idle-enthusiastic",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/shop") or      message.startswith("!shop") or      message.startswith("Shop") or   message.startswith("shop") or   message.startswith("!shopping") or message.startswith("/shopping") or message.startswith("Shopping") or message.startswith("shopping") or message.startswith("43"):
            await self.highrise.send_emote("dance-shoppingcart",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/russian") or      message.startswith("!russian") or      message.startswith("Russian") or                              message.startswith("russian") or message.startswith("44"):
            await self.highrise.send_emote("dance-russian",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/pennywise") or      message.startswith("!pennywise") or      message.startswith("Pennywise") or                              message.startswith("pennywise") or message.startswith("45"):
            await self.highrise.send_emote("dance-pennywise",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/tik2") or      message.startswith("!tik2") or      message.startswith("Tik2") or   message.startswith("!dontstartnow") or   message.startswith("/dontstartnow") or   message.startswith("dontstartnow") or   message.startswith("Dontstartnow") or   message.startswith("tik2") or   message.startswith("46"):
            await self.highrise.send_emote("dance-tiktok2",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/blackpink") or      message.startswith("!blackpink") or      message.startswith("Blackpink") or                              message.startswith("blackpink") or message.startswith("47"):
            await self.highrise.send_emote("dance-blackpink",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/celebrate") or      message.startswith("!celebrate") or      message.startswith("Celebrate") or                              message.startswith("celebrate") or message.startswith("48"):
            await self.highrise.send_emote("emoji-celebrate",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/gagging") or      message.startswith("!gagging") or      message.startswith("Gagging") or                              message.startswith("gagging") or message.startswith("49"):
            await self.highrise.send_emote("emoji-gagging",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/flex") or      message.startswith("!flex") or      message.startswith("Flex") or   message.startswith("flex") or message.startswith("50"):
            await self.highrise.send_emote("emoji-flex",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/cursing") or      message.startswith("!cursing") or      message.startswith("Cursing") or                              message.startswith("cursing") or message.startswith("51"):
            await self.highrise.send_emote("emoji-cursing",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/thumbsup") or      message.startswith("!thumbsup") or      message.startswith("Thumbsup") or                              message.startswith("thumbsup") or message.startswith("52"):
            await self.highrise.send_emote("emoji-thumbsup",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/angry") or      message.startswith("!angry") or      message.startswith("Angry") or  message.startswith("angry") or message.startswith("53"):
            await self.highrise.send_emote("emoji-angry",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/punk") or      message.startswith("!punk") or      message.startswith("Punk") or   message.startswith("punk") or message.startswith("54"):
            await self.highrise.send_emote("emote-punkguitar",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/zombie") or      message.startswith("!zombie") or      message.startswith("Zombie") or message.startswith("zombie") or message.startswith("55"):
            await self.highrise.send_emote("emote-zombierun",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/sit") or      message.startswith("!sit") or      message.startswith("Sit") or    message.startswith("sit") or message.startswith("56"):
            await self.highrise.send_emote("idle-loop-sitfloor",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/fight") or      message.startswith("!fight") or      message.startswith("Fight") or  message.startswith("fight") or  message.startswith("!swordfight") or message.startswith("/swordfight") or message.startswith("Swordfight") or message.startswith("swordfight") or message.startswith("57"):
            await self.highrise.send_emote("emote-swordfight",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/ren") or      message.startswith("!ren") or      message.startswith("Ren") or    message.startswith("ren") or    message.startswith("!macarena") or     message.startswith("/macarena") or      message.startswith("Macarena") or message.startswith("macarena") or message.startswith("58"):
            await self.highrise.send_emote("dance-macarena",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/wei") or      message.startswith("!wei") or      message.startswith("Wei") or    message.startswith("wei") or message.startswith("!weird") or message.startswith("/weird") or message.startswith("Weird") or message.startswith("weird") or  message.startswith("59"):
            await self.highrise.send_emote("dance-weird",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/tik8") or      message.startswith("!tik8") or      message.startswith("Tik8") or           message.startswith("/savage") or           message.startswith("!savage") or           message.startswith("Savage") or message.startswith("tik8") or message.startswith("savage") or message.startswith("60"):
            await self.highrise.send_emote("dance-tiktok8",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/tik9") or      message.startswith("!tik9") or      message.startswith("Tik9") or           message.startswith("/viral") or           message.startswith("!viral") or           message.startswith("Viral") or  message.startswith("!viralgroove") or message.startswith("/viralgroove") or message.startswith("Viralgroove") or message.startswith("viralgroove") or message.startswith("tik9") or message.startswith("viral") or message.startswith("61"):
            await self.highrise.send_emote("dance-tiktok9",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/uwu") or      message.startswith("!uwu") or      message.startswith("Uwu") or    message.startswith("uwu") or message.startswith("62"):
            await self.highrise.send_emote("idle-uwu",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/tik4") or      message.startswith("!tik4") or      message.startswith("Tik4") or               message.startswith("/sayso") or               message.startswith("!sayso") or               message.startswith("Sayso") or  message.startswith("sayso") or message.startswith("tik4") or message.startswith("63"):
            await self.highrise.send_emote("idle-dance-tiktok4",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/star") or      message.startswith("!star") or      message.startswith("Star") or   message.startswith("star") or message.startswith("64"):
            await self.highrise.send_emote("emote-stargazer",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/pose9") or      message.startswith("!pose9") or      message.startswith("Pose9") or  message.startswith("pose9") or message.startswith("65"):
            await self.highrise.send_emote("emote-pose9",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/boxer") or      message.startswith("!boxer") or      message.startswith("Boxer") or  message.startswith("boxer") or message.startswith("66"):
            await self.highrise.send_emote("emote-boxer",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/guitar") or      message.startswith("!guitar") or      message.startswith("Guitar") or message.startswith("guitar") or message.startswith("67"):
            await self.highrise.send_emote("idle-guitar",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/penguin") or      message.startswith("!penguin") or      message.startswith("Penguin") or   message.startswith("penguin") or message.startswith("68"):
            await self.highrise.send_emote("dance-pinguin",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/astronaut") or      message.startswith("!astronaut") or      message.startswith("Astronaut") or                                message.startswith("astronaut") or message.startswith("69"):
            await self.highrise.send_emote("emote-astronaut",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/saunter") or      message.startswith("!saunter") or      message.startswith("Saunter") or               message.startswith("/anime") or               message.startswith("!anime") or               message.startswith("Anime") or    message.startswith("anime") or   message.startswith("saunter") or   message.startswith("70"):
            await self.highrise.send_emote("dance-anime",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/creepy") or      message.startswith("!creepy") or      message.startswith("Creepy") or   message.startswith("creepy") or message.startswith("71"):
            await self.highrise.send_emote("dance-creepypuppet",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/watch") or      message.startswith("!watch") or      message.startswith("Watch") or    message.startswith("watch") or message.startswith("72"):
            await self.highrise.send_emote("emote-creepycute",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/revelations") or      message.startswith("!revelations") or      message.startswith("Revelations") or                                message.startswith("revelations") or message.startswith("73"):
            await self.highrise.send_emote("emote-headblowup",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/bashful") or      message.startswith("!bashful") or      message.startswith("Bashful") or  message.startswith("bashful") or message.startswith("74"):
            await self.highrise.send_emote("emote-shy2",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/arabesque") or      message.startswith("!arabesque") or      message.startswith("Arabesque") or                                message.startswith("arabesque") or message.startswith("75"):
            await self.highrise.send_emote("emote-pose10",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/party") or      message.startswith("!party") or      message.startswith("Party") or    message.startswith("party") or message.startswith("76"):
            await self.highrise.send_emote("emote-celebrate",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/skating") or      message.startswith("!skating") or      message.startswith("Skating") or  message.startswith("skating") or message.startswith("77"):
            await self.highrise.send_emote("emote-iceskating",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/scritchy") or      message.startswith("!scritchy") or      message.startswith("Scritchy") or message.startswith("scritchy") or message.startswith("78"):
            await self.highrise.send_emote("idle-wild",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/bitnervous") or      message.startswith("!bitnervous") or      message.startswith("Bitnervous") or               message.startswith("!nervous") or               message.startswith("/nervous") or               message.startswith("Nervous") or  message.startswith("nervous") or   message.startswith("bitnervous") or message.startswith("79"):
            await self.highrise.send_emote("idle-nervous",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/timejump") or      message.startswith("!timejump") or      message.startswith("Timejump") or message.startswith("timejump") or message.startswith("time") or   message.startswith("Time") or   message.startswith("!time") or   message.startswith("/time") or message.startswith("80"):
            await self.highrise.send_emote("emote-timejump",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/gottago") or      message.startswith("!gottago") or      message.startswith("Gottago") or message.startswith("gottago") or  message.startswith("81"):
            await self.highrise.send_emote("idle-toilet",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/jingle") or      message.startswith("!jingle") or      message.startswith("Jingle") or  message.startswith("jingle") or message.startswith("82"):
            await self.highrise.send_emote("dance-jinglebell",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/hyped") or      message.startswith("!hyped") or      message.startswith("Hyped") or   message.startswith("hyped") or message.startswith("83"):
            await self.highrise.send_emote("emote-hyped",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/sleigh") or      message.startswith("!sleigh") or        message.startswith("sleigh") or      message.startswith("Sleigh") or message.startswith("84"):
            await self.highrise.send_emote("emote-sleigh",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/surprise") or      message.startswith("!surprise") or      message.startswith("surprise") or      message.startswith("Surprise") or message.startswith("85"):
            await self.highrise.send_emote("emote-pose6",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")
          
        if        message.startswith("/repose") or      message.startswith("!repose") or        message.startswith("repose") or      message.startswith("Repose") or message.startswith("86"):
            await self.highrise.send_emote("sit-relaxed",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/kawaii") or      message.startswith("!kawaii") or        message.startswith("kawaii") or       message.startswith("Kawaii") or message.startswith("87"):
            await self.highrise.send_emote("dance-kawai",user.id)

        if        message.startswith("/touch") or      message.startswith("!touch") or         message.startswith("touch") or      message.startswith("Touch") or message.startswith("88"):
            await self.highrise.send_emote("dance-touch",user.id)

        if        message.startswith("/gift") or      message.startswith("!gift") or          message.startswith("gift") or      message.startswith("Gift") or message.startswith("89"):
            await self.highrise.send_emote("emote-gift",user.id)

        if        message.startswith("/pushit") or      message.startswith("!pushit") or        message.startswith("pushit") or      message.startswith("Pushit") or message.startswith("90"):
            await self.highrise.send_emote("dance-employee",user.id)

        if        message.startswith("salute") or      message.startswith("!salute") or        message.startswith("salute") or      message.startswith("Salute") or message.startswith("91"):
            await self.highrise.send_emote("emote-cutesalute",user.id)

        if        message.startswith("/attention") or      message.startswith("!attention") or        message.startswith("attention") or      message.startswith("Attention") or message.startswith("92"):
            await self.highrise.send_emote("emote-salute",user.id)                                                                   

        if        message.startswith("/tiktok") or      message.startswith("!tiktok") or        message.startswith("tiktok") or    message.startswith("Tiktok") or message.startswith("93"):
            await self.highrise.send_emote("dance-tiktok11",user.id)

        if        message.startswith("/smooch") or      message.startswith("!smooch") or        message.startswith("smooch") or    message.startswith("Smooch") or message.startswith("94"):
            await self.highrise.send_emote("emote-kissing-bound",user.id)

        if        message.startswith("/launch") or      message.startswith("!launch") or        message.startswith("launch") or   message.startswith("Launch") or message.startswith("95"):
            await self.highrise.send_emote("emote-launch",user.id)

        if        message.startswith("/fairyfloat") or      message.startswith("!fairyfloat") or        message.startswith("fairyfloat") or    message.startswith("Fairyfloat") or message.startswith("96"):
            await self.highrise.send_emote("idle-floating",user.id)

        if        message.startswith("/fairytwirl") or      message.startswith("!fairytwirl") or        message.startswith("fairytwirl") or    message.startswith("Fairytwirl") or message.startswith("97"):
            await self.highrise.send_emote("emote-looping",user.id)

        if              message.startswith("Fairyfloat All") or                              message.startswith("/emote all fairyfloat") or       message.startswith("!emote all fairyfloat"):
          if user.username == "ybear_" or user.username == "ybear_" or user.username == "ybear_" or user.username == "ybear_":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-floating", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Fairyfloat] para {len(room_users)} pessoas.")

        if              message.startswith("Fairytwirl All") or                              message.startswith("/emote all fairytwirl") or       message.startswith("!emote all fairytwirl"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-looping", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Fairytwirl] para {len(room_users)} pessoas.")

        if              message.startswith("Launch All") or                              message.startswith("/emote all launch") or       message.startswith("!emote all launch"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-launch", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Launch] para {len(room_users)} pessoas.")

        if              message.startswith("Smooch All") or                              message.startswith("/emote all smooch") or       message.startswith("!emote all smooch"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-kissing-bound", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Smooch] para {len(room_users)} pessoas.")

        if              message.startswith("Pushit All") or                              message.startswith("/emote all pushit") or       message.startswith("!emote all pushit"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-employee", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pushit] para {len(room_users)} pessoas.")

        if              message.startswith("Gift All") or                              message.startswith("/emote all gift") or       message.startswith("!emote all gift"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-gift", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Gift] para {len(room_users)} pessoas.")

        if              message.startswith("Attention All") or                              message.startswith("/emote all attention") or       message.startswith("!emote all attention"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-salute", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Attention] para {len(room_users)} pessoas.")

        if              message.startswith("Salute All") or                              message.startswith("/emote all salute") or       message.startswith("!emote all salute"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cutesalute", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Salute] para {len(room_users)} pessoas.")

        if              message.startswith("Tiktok All") or                              message.startswith("/emote all tiktok") or       message.startswith("!emote all tiktok"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok11", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Tiktok] para {len(room_users)} pessoas.")
          
        if              message.startswith("Touch All") or                              message.startswith("/emote all touch") or       message.startswith("!emote all touch"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-touch", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Touch] para {len(room_users)} pessoas.")
              
        if              message.startswith("Kawaii All") or                              message.startswith("/emote all kawaii") or       message.startswith("!emote all kawaii"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-kawai", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Kawaii] para {len(room_users)} pessoas.")
          
        if              message.startswith("Hot All") or                              message.startswith("/emote all hot") or       message.startswith("!emote all hot"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hot", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Hot] para {len(room_users)} pessoas.")
      
      
        if              message.startswith("Curtsy All") or                              message.startswith("/emote all curtsy") or       message.startswith("!emote all curtsy"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-curtsy", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Curtsy] para {len(room_users)} pessoas.")

        if              message.startswith("Surprise All") or                              message.startswith("/emote all surprise") or       message.startswith("!emote all surprise"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose6", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Surprise] para {len(room_users)} pessoas.")

        if              message.startswith("Jingle All") or                              message.startswith("/emote all jingle") or       message.startswith("!emote all jingle"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-jinglebell", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Jingle] para {len(room_users)} pessoas.")

        if              message.startswith("Creepy All") or                              message.startswith("/emote all creepy") or       message.startswith("!emote all creepy"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-creepypuppet", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Creepy] para {len(room_users)} pessoas.")

        if              message.startswith("Nervous All") or message.startswith("Bitnervous All") or      message.startswith("!emote all bitnervous") or message.startswith("/emote all bitnervous") or                             message.startswith("/emote all nervous") or       message.startswith("!emote all nervous"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-nervous", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Bitnervous] para {len(room_users)} pessoas.")

        if              message.startswith("Scritchy All") or                              message.startswith("/emote all scritchy") or       message.startswith("!emote all scritchy"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-wild", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Scritchy] para {len(room_users)} pessoas.")
              
        if              message.startswith("Fashion All") or                              message.startswith("/emote all fashion") or       message.startswith("!emote all fashion"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-fashionista", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Fashion] para {len(room_users)} pessoas.")
                
        if              message.startswith("Wrong All") or                              message.startswith("/emote all wrong") or       message.startswith("!emote all wrong"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-wrong", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Wrong] para {len(room_users)} pessoas.")

        if              message.startswith("Cutey All") or                              message.startswith("/emote all cutey") or       message.startswith("!emote all cutey"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cutey", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Cutey] para {len(room_users)} pessoas.")

        if              message.startswith("Hyped All") or                              message.startswith("/emote all hyped") or       message.startswith("!emote all hyped"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hyped", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Hyped] para {len(room_users)} pessoas.")
                
        if              message.startswith("Superpose All") or                              message.startswith("/emote all superpose") or       message.startswith("!emote all superpose"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-superpose", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Superpose] para {len(room_users)} pessoas.")

        if              message.startswith("Punk All") or                              message.startswith("/emote all punk") or       message.startswith("!emote all punk"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-punkguitar", roomUser.id) 
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Punk] para {len(room_users)} pessoas.")
                
        if              message.startswith("Dontstartnow All") or message.startswith("Tiktok2 All") or      message.startswith("!emote all dontstartnow") or message.startswith("/emote all dontstartnow") or                             message.startswith("/emote all tiktok2") or       message.startswith("!emote all tiktok2"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok2", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Dontstartnow] para {len(room_users)} pessoas.")
                
                
        if              message.startswith("Savage All") or message.startswith("Tiktok8 All") or      message.startswith("!emote all savage") or message.startswith("/emote all savage") or                             message.startswith("/emote all tiktok8") or       message.startswith("!emote all tiktok8"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok8", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Savage] para {len(room_users)} pessoas.")
                
        if              message.startswith("Tiktok10 All") or                              message.startswith("/emote all tiktok10") or       message.startswith("!emote all tiktok10"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok10", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Tiktok10] para {len(room_users)} pessoas.")
                
        if              message.startswith("Viral All") or     message.startswith("!emotr all tiktok9") or        message.startswith("/emote all tiktok9") or    message.startswith("Tiktok9 All") or message.startswith("Viralgroove All") or      message.startswith("!emote all viral") or message.startswith("/emote all viralgroove") or                             message.startswith("/emote all viral") or       message.startswith("!emote all viralgroove"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok9", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Viralgroove] para {len(room_users)} pessoas.")
                
        if              message.startswith("Blackpink All") or                              message.startswith("/emote all blackpink") or       message.startswith("!emote all blackpink"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-blackpink", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Blackpink] para {len(room_users)} pessoas.")
                
        if              message.startswith("Gagging All") or                              message.startswith("/emote all gagging") or       message.startswith("!emote all gagging"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-gagging", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Gagging] para {len(room_users)} pessoas.")

        if              message.startswith("Pose3 All") or                              message.startswith("/emote all pose3") or       message.startswith("!emote all pose3"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose3", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose3] para {len(room_users)} pessoas.")

        if              message.startswith("Pose7 All") or                              message.startswith("/emote all pose7") or       message.startswith("!emote all pose7"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose7", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose7] para {len(room_users)} pessoas.")

        if              message.startswith("Pose5 All") or                              message.startswith("/emote all pose5") or       message.startswith("!emote all pose5"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose5", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose5] para {len(room_users)} pessoas.")

        if              message.startswith("Pose1 All") or                              message.startswith("/emote all pose1") or       message.startswith("!emote all pose1"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose1", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose1] para {len(room_users)} pessoas.")

        if              message.startswith("Pose8 All") or                              message.startswith("/emote all pose8") or       message.startswith("!emote all pose8"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose8", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose8] para {len(room_users)} pessoas.")
     
        if              message.startswith("Enthused All") or                              message.startswith("/emote all enthused") or       message.startswith("!emote all enthused"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-enthusiastic", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Enthused] para {len(room_users)} pessoas.")
                
        if              message.startswith("Singing All") or message.startswith("Sing All") or      message.startswith("!emote all sing") or message.startswith("/emote all sing") or                             message.startswith("/emote all singing") or       message.startswith("!emote all singing"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle_singing", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Singing] para {len(room_users)} pessoas.")

        if              message.startswith("Teleport All") or                              message.startswith("/emote all teleport") or       message.startswith("!emote all teleport"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-teleporting", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Teleporting] para {len(room_users)} pessoas.")
                
        if              message.startswith("Telekinesis All") or                              message.startswith("/emote all telekinesis") or       message.startswith("!emote all telekinesis"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-telekinesis", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Telekinesis] para {len(room_users)} pessoas.")

        if              message.startswith("Casual All") or                              message.startswith("/emote all casual") or       message.startswith("!emote all casual"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-casual", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Casual] para {len(room_users)} pessoas.")
                
        if              message.startswith("Icecream All") or                              message.startswith("/emote all icecream") or       message.startswith("!emote all icecream"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-icecream", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Icecream] para {len(room_users)} pessoas.")
                   
        if              message.startswith("Zombie All") or                              message.startswith("/emote all zombie") or       message.startswith("!emote all zombie"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-zombierun", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Zombie] para {len(room_users)} pessoas.")

        if              message.startswith("Celebrate All") or                              message.startswith("/emote all celebrate") or       message.startswith("!emote all celebrate"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-celebrate", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Celebrate] para {len(room_users)} pessoas.")

        if              message.startswith("Kiss All") or                              message.startswith("/emote all kiss") or       message.startswith("!emote all kiss"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-kiss", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Kiss] para {len(room_users)} pessoas.")

        if              message.startswith("Snowangel All") or                              message.startswith("/emote all snowangel") or       message.startswith("!emote all snowangel"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snowangel", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Snowangel] para {len(room_users)} pessoas.")

        if              message.startswith("Bow All") or                              message.startswith("/emote all bow") or       message.startswith("!emote all bow"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-bow", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Bow] para {len(room_users)} pessoas.")

        if              message.startswith("Ice All") or message.startswith("Skating All") or      message.startswith("!emote all ice") or message.startswith("/emote all skating") or                             message.startswith("/emote all ice") or       message.startswith("!emote all skating"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-iceskating", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Iceskating] para {len(room_users)} pessoas.")

        if              message.startswith("Confused All") or                              message.startswith("/emote all confused") or       message.startswith("!emote all confused"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-confused", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Confused] para {len(room_users)} pessoas.")

        if              message.startswith("Charging All") or                              message.startswith("/emote all charging") or       message.startswith("!emote all charging"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-charging", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Charging] para {len(room_users)} pessoas.")

        if              message.startswith("Weird All") or message.startswith("Wei All") or      message.startswith("!emote all wei") or message.startswith("/emote all wei") or                             message.startswith("/emote all weird") or       message.startswith("!emote all weird"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-weird", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Weird] para {len(room_users)} pessoas.")

        if              message.startswith("Greedy All") or                              message.startswith("/emote all greedy") or       message.startswith("!emote all greedy"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-greedy", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Greedy] para {len(room_users)} pessoas.")

        if              message.startswith("Cursing All") or                              message.startswith("/emote all cursing") or       message.startswith("!emote all cursing"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-cursing", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Cursing] para {len(room_users)} pessoas.")

        if              message.startswith("Russian All") or                              message.startswith("/emote all russian") or       message.startswith("!emote all russian"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-russian", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Russian] para {len(room_users)} pessoas.")

        if              message.startswith("Repose All") or                              message.startswith("/emote all repose") or       message.startswith("!emote all repose"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("sit-relaxed", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Repose] para {len(room_users)} pessoas.")
                
        if              message.startswith("Shop All") or message.startswith("Shopping All") or      message.startswith("!emote all shopping") or message.startswith("/emote all shop") or                             message.startswith("/emote all shopping") or       message.startswith("!emote all shop"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-shoppingcart", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Shopping] para {len(room_users)} pessoas.")

        if              message.startswith("Macarena All") or message.startswith("Ren All") or      message.startswith("!emote all macarena") or message.startswith("/emote all macarena") or                             message.startswith("/emote all ren") or       message.startswith("!emote all   ren "):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-macarena", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Macarena] para {len(room_users)} pessoas.")

        if              message.startswith("Snake All") or                              message.startswith("/emote all snake") or       message.startswith("!emote all snake"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snake", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Snake] para {len(room_users)} pessoas.")

        if              message.startswith("Model All") or                              message.startswith("/emote all model") or       message.startswith("!emote all model"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-model", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Model] para {len(room_users)} pessoas.")

        if              message.startswith("Sleigh All") or                              message.startswith("/emote all sleigh") or       message.startswith("!emote all sleigh"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-sleigh", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Sleigh] para {len(room_users)} pessoas.")

        if              message.startswith("Sayso All") or message.startswith("Tiktok4 All") or      message.startswith("!emote all sayso") or message.startswith("/emote all sayso") or                             message.startswith("/emote all tiktok4") or       message.startswith("!emote all tiktok4"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-tiktok4", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Sayso] para {len(room_users)} pessoas.")

        if              message.startswith("Uwu All") or                              message.startswith("/emote all uwu") or       message.startswith("!emote all uwu"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-uwu", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Uwu] para {len(room_users)} pessoas.")

        if              message.startswith("Star All") or                              message.startswith("/emote all star") or       message.startswith("!emote all star"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-stargazer", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Stargazer] para {len(room_users)} pessoas.")

        if              message.startswith("Pose9 All") or                              message.startswith("/emote all pose9") or       message.startswith("!emote all pose9"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose9", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose9] para {len(room_users)} pessoas.")

        if              message.startswith("Boxer All") or                              message.startswith("/emote all boxer") or       message.startswith("!emote all boxer"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-boxer", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Boxer] para {len(room_users)} pessoas.")

        if              message.startswith("Airguitar All") or message.startswith("Guitar All") or      message.startswith("!emote all guitar") or message.startswith("/emote all airguitar") or                             message.startswith("/emote all guitar") or       message.startswith("!emote all airguitar"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-guitar", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Airguitar] para {len(room_users)} pessoas.")

        if              message.startswith("Penguin All") or message.startswith("Pinguin All") or      message.startswith("!emote all penguin") or message.startswith("/emote all penguin") or                             message.startswith("/emote all pinguin") or       message.startswith("!emote all pinguin"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-pinguin", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Penguin] para {len(room_users)} pessoas.")
            
        if              message.startswith("Astronaut All") or message.startswith("Zero All") or      message.startswith("!emote all zero") or message.startswith("/emote all zero") or                             message.startswith("/emote all astronaut") or       message.startswith("!emote all astronaut"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-astronaut", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Astronaut] para {len(room_users)} pessoas.")
                
        if              message.startswith("Saunter All") or   message.startswith("Anime All") or   message.startswith("!emote all anime") or   message.startswith("/emote all anime") or                              message.startswith("/emote all saunter") or       message.startswith("!emote all saunter"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-anime", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Saunter] para {len(room_users)} pessoas.")

        if              message.startswith("Flirt All") or     message.startswith("!emote all flirt") or    message.startswith("/emote all flirt") or    message.startswith("!emote all flirty") or     message.startswith("Flirtywave All") or    message.startswith("/emote all flirty") or    message.startswith("/emote all flirt") or                               message.startswith("/emote all flirtywave") or       message.startswith("!emote all flirtywave"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-lust", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Flirtywave] para {len(room_users)} pessoas.")

        if              message.startswith("Watch All") or                              message.startswith("/emote all watch") or       message.startswith("!emote all watch"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-creepycute", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Watch] para {len(room_users)} pessoas.")
              
        if              message.startswith("Revelations All") or                              message.startswith("/emote all revelations") or       message.startswith("!emote all revelations"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-headblowup", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Revelations] para {len(room_users)} pessoas.")
              
        if              message.startswith("Bashful All") or                              message.startswith("/emote all bashful") or       message.startswith("!emote all bashful"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-shy2", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Bashful] para {len(room_users)} pessoas.")

        if              message.startswith("Arabesque All") or                              message.startswith("/emote all arabesque") or       message.startswith("!emote all arabesque"):
           if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose10", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Arabesque] para {len(room_users)} pessoas.")
        
        if              message.startswith("Party All") or                              message.startswith("/emote all party") or       message.startswith("!emote all party"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-celebrate", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Party] para {len(room_users)} pessoas.")
              
        if              message.startswith("Time All") or                              message.startswith("/emote all time") or       message.startswith("!emote all time"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-timejump", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Time] para {len(room_users)} pessoas.")

        if              message.startswith("Gottago All") or                              message.startswith("/emote all gottago") or       message.startswith("!emote all gottago"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-toilet", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Gottago] para {len(room_users)} pessoas.")
                  
        if message.startswith("/cardapio1"):
            await self.highrise.send_whisper(user.id,"esse é o nosso cardapio de bebidas espero que goste 😄")
                                     
        if message.startswith("/cardapio1"):
            await self.highrise.send_whisper(user.id,"/tequila , /gim , /vinho , /vinho-branco , /vodka , /whisky , /rum , /champanhe , /cachaça /conhaque , /cerveja , /coca-cola , /suco , /agua , /agua-de-coco , /toddy , /nescau")

        if message.startswith("/coca-cola"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está sua deliciosa coca cola gelada 🧊🥤 ")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/toddy"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aki está seu delicioso toddy 🥛")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/suco"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está seu delicioso suco natural 🧃")
            await self.highrise.react("thumbs", user.id)
        if message.startswith("/agua"):  
            await self.highrise.send_whisper(user.id,f"🌊aqui está sua deliciosa agua {user.username} diretamente da toneira 🌊")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/agua-de-coco"):  
            await self.highrise.send_whisper(user.id,f"🥥aki está sua aguá de coco {user.username} aproveite que está deliciosa 🥥")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/nescau"):  
            await self.highrise.send_whisper(user.id,f"aqui está {user.username} seu delicioso nescau 🥛")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/tequila"):  
            await self.highrise.send_whisper(user.id,f"{user.username} se deliciando na Tequila 😄🥃")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/gim"):
            await self.highrise.send_whisper(user.id,f"vira vira todo o gim {user.username} 🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/conhaque"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu conhaque {user.username} 🥃🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/whisky"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está seu Whisky  {user.username} 🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/rum"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está seu Rum 🥃 {user.username}")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/cachaça"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está a Sua Cachaça {user.username} não beba muito 🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/vodka"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua  Vodka {user.username} ")
            await self.highrise.react("thumbs", user.id)
           
        if message.startswith("/champanhe"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Champanhe {user.username} 🍾🥂")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/cerveja"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Cerveja {user.username} 🍺")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/vinho-branco"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Vinho-Branco {user.username}")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/vinho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Vinho {user.username}")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/cardapio2"):
            await self.highrise.send_whisper(user.id,"esse é o nosso cardapio de comidas e petiscos espero que goste 😄")
                                     
        if message.startswith("/cardapio2"):
            await self.highrise.send_whisper(user.id,"/camarão , /salada-de-alface , /salada-de-repolho , /macarrão , /pizza , /bolo-de-cenoura")

        if message.startswith("/cardapio2"):
            await self.highrise.send_whisper(user.id,"/bolo-de-morango , /açai , /sorvete , /cupcake , /sorvete , /batata-frita , /espetinho , /pão-de-alho")

        if message.startswith("/pizza"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está sua deliciosa pizza 🍕")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/bolo-de-morango"):
            await self.highrise.send_whisper(user.id,f"Aqui Está seu Delicioso Bolo de Morango {user.username} 🍰")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/salada-de-repolho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Deliciosa salada de repolho {user.username} 🥬🥬")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/camarão"):  
            await self.highrise.send_whisper(user.id,f"🍤Aqui Está seu Delicoso Camarão 🍤 {user.username} 🍤")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/macarrão"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está seu macarrão {user.username} aproveite 🍜🍝")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/salada-de-alface"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está a Sua salada de alface {user.username} com um pouco de tomates por cima 🥬🥗")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/bolo-de-cenoura"):  
            await self.highrise.send_whisper(user.id,f"aqui está seu bolo de cenoura  {user.username} 🥕🥮")
            await self.highrise.react("thumbs", user.id)
           
        if message.startswith("/açai"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Açai {user.username} 🍨 Aproveite")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/sorvete"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu sorvete {user.username} 🍦🍨")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/pão-de-alho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua pão de alho {user.username} 🥖🧄")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/batata-frita"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Batata Frita {user.username} aproveite 🍟")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/espetinho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Espetinho {user.username} 🍢🍢")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/cupcake"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu cupcake {user.username} 🧁")
            await self.highrise.react("thumbs", user.id)
              
        if        message.startswith("/tp") or      message.startswith("!tp") or      message.startswith("/tele") or          message.startswith("Tp") or          message.startswith("Tele") or  message.startswith("!tele"):
          target_username =         message.split("@")[-1].strip()
          await                     self.teleport_to_user(user, target_username)

        if                            message.startswith("Summon") or         message.startswith("Summom") or         message.startswith("!summom") or        message.startswith("/summom") or        message.startswith("/summon") or  message.startswith("!summon"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
           target_username = message.split("@")[-1].strip()
           await self.teleport_user_next_to(target_username, user)

        if              message.startswith("Carteira") or  message.startswith("Wallet") or    message.startswith("wallet") or       message.startswith("carteira"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.send_whisper(user.id,f"VALOR TOTAL : {wallet[0].amount} {wallet[0].type}")
            await self.highrise.send_emote("dance-tiktok14")
              
        if message.startswith("!kick"):
          if user.username == "ybear_":
              pass
          else:
              await self.highrise.chat("Voce não tem permissao para usar esse comando.")
              return
          #separete message into parts
          parts = message.split()
          #check if message is valid "kick @username"
          if len(parts) != 2:
              await self.highrise.chat("formato de banimento errado.")
              return
          #checks if there's a @ in the message
          if "@" not in parts[1]:
              username = parts[1]
          else:
              username = parts[1][1:]
          #check if user is in room
          room_users = (await self.highrise.get_room_users()).content
          for room_user, pos in room_users:
              if room_user.username.lower() == username.lower():
                  user_id = room_user.id
                  break
          if "user_id" not in locals():
              await self.highrise.chat("usuario não encontrado, porfavor arrume a cordenada do codigo")
              return
          #kick user
          try:
              await self.highrise.moderate_room(user_id, "kick")
          except Exception as e:
              await self.highrise.chat(f"{e}")
              return
          #send message to chat
          await self.highrise.chat(f"{username} Foi Banido da sala!!")

    async def teleport(self, user: User, position: Position):
        try:
            await self.highrise.teleport(user.id, position)
        except Exception as e:
            print(f"Caught Teleport Error: {e}")

    async def teleport_to_user(self, user: User, target_username: str) -> None:
        try:
            room_users = await self.highrise.get_room_users()
            for target, position in room_users.content:
                if target.username.lower() == target_username.lower():
                    z = position.z
                    new_z = z - 1
                    await self.teleport(user, Position(position.x, position.y, new_z, position.facing))
                    break
        except Exception as e:
            print(f"An error occurred while teleporting to {target_username}: {e}")

    async def teleport_user_next_to(self, target_username: str, requester_user: User) -> None:
        try:
            # Get the position of the requester_user
            room_users = await self.highrise.get_room_users()
            requester_position = None
            for user, position in room_users.content:
                if user.id == requester_user.id:
                    requester_position = position
                    break

            # Find the target user and their position
            for user, position in room_users.content:
                if user.username.lower() == target_username.lower():
                    z = requester_position.z
                    new_z = z + 1  # Example: Move +1 on the z-axis (upwards)
                    await self.teleport(user, Position(requester_position.x, requester_position.y, new_z, requester_position.facing))
                    break
        except Exception as e:
            print(f"An error occurred while teleporting {target_username} next to {requester_user.username}: {e}")
          
    async def teleporter(self, message: str)-> None:
        """
            Teleports the user to the specified user or coordinate
            Usage: /teleport <username> <x,y,z>
                                                                """
        #separates the message into parts
        #part 1 is the command "/teleport"
        #part 2 is the name of the user to teleport to (if it exists)
        #part 3 is the coordinates to teleport to (if it exists)
        try:
            command, username, coordinate = message.split(" ")
        except:
            
            return
        
        #checks if the user is in the room
        room_users = (await self.highrise.get_room_users()).content
        for user in room_users:
            if user[0].username.lower() == username.lower():
                user_id = user[0].id
                break
        #if the user_id isn't defined, the user isn't in the room
        if "user_id" not in locals():
            
            return
            
        #checks if the coordinate is in the correct format (x,y,z)
        try:
            x, y, z = coordinate.split(",")
        except:
          
            return
        
        #teleports the user to the specified coordinate
        await self.highrise.teleport(user_id = user_id, dest = Position(float(x), float(y), float(z)))

    async def command_handler(self, user: User, message: str):
        parts = message.split(" ")
        command = parts[0][1:]
        functions_folder = "functions"
        # Check if the function exists in the module
        for file_name in os.listdir(functions_folder):
            if file_name.endswith(".py"):
                module_name = file_name[:-3]  # Remove the '.py' extension
                module_path = os.path.join(functions_folder, file_name)
                
                # Load the module
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # Check if the function exists in the module
                if hasattr(module, command) and callable(getattr(module, command)):
                    function = getattr(module, command)
                    await function(self, user, message)
        
        # If no matching function is found
        return              

         
    async def on_whisper(self, user: User, message: str) -> None:
        print(f"{user.username} whispered: {message}")

        if        message.startswith("/tele") or              message.startswith("/tp") or              message.startswith("/fly") or     message.startswith("!tele") or      message.startswith("!tp") or     message.startswith("!fly"):
          if user.username == "ybear_" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            await self.teleporter(message)

        if        message.startswith("/") or              message.startswith("-") or              message.startswith(".") or          message.startswith("!"):
            await self.command_handler(user, message)

        if                            message.startswith("Summon") or         message.startswith("Summom") or         message.startswith("!summom") or        message.startswith("/summom") or        message.startswith("/summon") or  message.startswith("!summon"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
           target_username = message.split("@")[-1].strip()
           await self.teleport_user_next_to(target_username, user)
                              
        if              message.startswith("Carteira") or  message.startswith("Wallet") or    message.startswith("wallet") or       message.startswith("carteira"):
          if user.username == "SeuProblema" or user.username == "B_w_2" or user.username == "Matii_fofi" or user.username == "YeoneSukimi":
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.send_whisper(user.id,f"VALOR TOTAL : {wallet[0].amount} {wallet[0].type}")
            await self.highrise.send_emote("emote-blowkisses")
            
    async def on_user_move(self, user: User, pos: Position) -> None:
        print (f"{user.username} moved to {pos}")

    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
        print(f"{user.username} emoted: {emote_id}")

    async def on_user_leave(self, user: User) -> None:
        print(f"{user.username} saiu da sala")
        await self.highrise.chat(f"Volta @{user.username}! 😭")
        await self.highrise.send_emote("dance-hipshake")