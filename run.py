from flask import Flask
from threading import Thread
from highrise.__main__ import main, BotDefinition
from importlib import import_module
import time
import asyncio

class WebServer:
    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route('/')
        def index() -> str:
            return "Funcionando"

    def run(self) -> None:
        self.app.run(host='0.0.0.0', port=8081)

    def keep_alive(self):
        t = Thread(target=self.run)
        t.start()

class RunBot:
    room_id = "664e49f8373a36e65adb291f"
    bot_token = "6434ffb6a365f746498f776ec4b2f4e20071cfe36e282424329853943e8bf365"
    bot_file = "main"
    bot_class = "Bot"

    def __init__(self) -> None:
        # Importa o módulo e a classe do bot dinamicamente
        bot_module = import_module(self.bot_file)
        bot_class = getattr(bot_module, self.bot_class)
        
        # Define as configurações do bot
        self.definitions = [
            BotDefinition(
                bot_class(),
                self.room_id, 
                self.bot_token
            )
        ]  # Mais classes BotDefinition podem ser adicionadas à lista

    async def run_main(self):
        await main(self.definitions)

    def run_loop(self) -> None:
        while True:
            try:
                asyncio.run(self.run_main())
            except Exception as e:
                print("Error: ", e)
                time.sleep(5)

if __name__ == "__main__":
    # Inicializa o servidor Web
    WebServer().keep_alive()

    # Executa o loop do bot
    RunBot().run_loop()
