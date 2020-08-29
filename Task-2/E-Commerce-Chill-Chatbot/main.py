from rivescript import RiveScript


bot = RiveScript(utf8=True)
bot.load_directory("brain")
bot.sort_replies()

print('Bot>', 'Hello, customer!')
while True:
    msg = input('You> ')
    if msg == '/q':
        quit()

    reply = bot.reply("localuser", msg)
    print ('Bot>', reply)
