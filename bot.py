# Кароч починил все кроме ff и creative2

from telegram import Update
from telegram.ext import (
    Application, CommandHandler, CallbackContext
)
from random import choice, randint


# Создаём приложение
TOKEN = "1617299064:AAG1GXe3WBg6Lmh_mkxtF8rZ-OWpLfst9MI"
app = Application.builder().token(TOKEN).build()

# Обработчики команд
async def bday(update: Update, context: CallbackContext):
    num = randint(1, 12)
    if num in {1, 3, 5, 7, 8, 10, 12}:
        result = f"{randint(1, 31)}{choice([' of January', ' of March', ' of May', ' of July', ' of August', ' of October', ' of December'])}"
    elif num in {4, 6, 9, 11}:
        result = f"{randint(1, 30)}{choice([' of April', ' of June', ' of September', ' of November'])}"
    else:
        result = f"{randint(1, 29)} of February"
    await update.message.reply_text(result)


async def creative(update: Update, context: CallbackContext):
    keywords = [
        "Watchmen", "Red library", "Story", "Witness", "Cavalier", "Angler",
        "Bygone", "Augmented", "Wildfire", "Performer", "Chimera", "Foundry",
        "December", "Academic", "Elemental", "M&S", "Machina", "Tri-Chi",
        "Infamous", "Tricksy", "Kin", "Big Hat", "Sooey", "Pig", "Wizz-Bang",
        "Swampfiend", "Crossroads", "Jockey", "Syndicate", "Frontier", "DUA",
        "Umbra", "Seeker", "Apex", "Wastrel", "EVS", "Cadmus", "Guard",
        "Marshal", "Asylum", "Elite", "Mimic", "Journalist", "Family", "Witch Hunter",
        "Nightmare", "Savage", "Nephilim", "Fae", "Woe", "Puppet", "Grim",
        "Plague", "Tormented", "Amalgam", "Bandit", "Obliteration", "Witchling",
        "Mercenary", "Freikorps", "Experimental", "Urami", "Forgotten", "Revenant",
        "Transmortis", "Redchapel", "Ancestor", "Retainer", "Zombie", "Returned",
        "Oni", "Honeypot", "Last Blossom", "Monk", "Qi and Gong", "Horseman",
        "Fungal", "Vanguard", "Sayuri"
    ]
    first = choice(keywords)
    keywords.remove(first)
    second = choice(keywords)
    result = f"{first} + {second}"
    await update.message.reply_text(result)

	
async def creative2(update: Update, context: CallbackContext):
    keywords = [
        "Watchmen", "Red library", "Story", "Witness", "Cavalier", "Angler",
        "Bygone", "Augmented", "Wildfire", "Performer", "Chimera", "Foundry",
        "December", "Academic", "Elemental", "M&S", "Machina", "Tri-Chi",
        "Infamous", "Tricksy", "Kin", "Big Hat", "Sooey", "Pig", "Wizz-Bang",
        "Swampfiend", "Crossroads", "Jockey", "Syndicate", "Frontier", "DUA",
        "Umbra", "Seeker", "Apex", "Wastrel", "EVS", "Cadmus", "Guard",
        "Marshal", "Asylum", "Elite", "Mimic", "Journalist", "Family", "Witch Hunter",
        "Nightmare", "Savage", "Nephilim", "Fae", "Woe", "Puppet", "Grim",
        "Plague", "Tormented", "Amalgam", "Bandit", "Obliteration", "Witchling",
        "Mercenary", "Freikorps", "Experimental", "Urami", "Forgotten", "Revenant",
        "Transmortis", "Redchapel", "Ancestor", "Retainer", "Zombie", "Returned",
        "Oni", "Honeypot", "Last Blossom", "Monk", "Qi and Gong", "Horseman",
        "Fungal", "Vanguard", "Sayuri"
    ]
    first = choice(keywords)
    keywords.remove(first)
    second = choice(keywords)
    num = randint(0, 3)
    types = ['Beast', 'Construct', choice(['Living', 'Undead'])]
    type_modifiers = []
    if first == "Puppet" or second == "Puppet":
        type_modifiers.append("Construct")
        types.remove("Construct")
        num = max(0, num - 1)
    if first == "Apex" or second == "Apex":
        chance = randint(1, 10)
        if chance <= 6:
            type_modifiers.append("Beast")
            types.remove("Beast")
            num = max(0, num - 1)
    result_types = type_modifiers + sample(types, k=num)
    result = f"{first} + {second} | {' '.join(result_types)}"
    await update.message.reply_text(result)


async def draw(update: Update, context: CallbackContext):
    num = randint(1, 56)
    result = (
        "Shattered Joker" if num == 55 else
        "Red Joker" if num == 54 else
        "Black Joker" if num == 53 else
        f"{randint(1, 13)}{choice([' of Crows', ' of Rams', ' of Tomes', ' of Masks'])}"
    )
    await update.message.reply_text(result)


def ff(update: Update, context: CallbackContext):
    num, cardvalue, result = randint(1, 55), randint(1, 13), ''
    if cardvalue <= 6:
        cardvalue = str(cardvalue) + choice([
            ' of Crows. Вороны кричат по твою душу, их клювы готовятся к пиршеству. Твоя судьба — мрак и гибель, мертвый груз под гнетом крылатого предвестника смерти.',
            ' of Rams. Бараны бьются рогами, ломая кости и преграды, но их сила не принесет тебе победы. Судьба сломит тебя, как рога этих существ под тяжестью отчаяния.',
            ' of Tomes. Страницы книг запятнаны кровью и пылью забвения. В них записаны твои ошибки и печальный конец, который, как древний скрип пергамента, неумолим.',
            ' of Masks. Маски вокруг тебя прячут свое коварство и злой умысел. Судьба играет с тобой, как актер на сцене, чье имя забыто, а игра навсегда остается в тени.'
        ])
    elif cardvalue <= 10:
        cardvalue = str(cardvalue) + choice([
            ' of Crows. Крылья воронов колышутся на ветру, предвещая дорогу вперед. Судьба не решена — перед тобой тернистый путь, и лишь твои шаги решат, что будет дальше.',
            ' of Rams. Рога баранов трутся друг о друга, звеня как вызов судьбе. Ты столкнешься с испытаниями, но сможешь устоять. Выбор за тобой: упасть или выстоять в борьбе.',
            ' of Tomes. Страницы книг шуршат под твоей рукой, но многое остается неясным. Твоя судьба записана, но ты можешь изменить ее строки, если будешь достаточно внимателен и решителен.',
            ' of Masks. Глаза, смотрящие на тебя из под маски, скрывают свои намерения. Ты вступаешь в игру судьбы, в которой правила быстро меняются. Всё зависит от того, какую роль выберешь ты.'
        ])
    else:
        cardvalue = str(cardvalue) + choice([
            ' of Crows. Воронье молчит, как предвестник перемен. Их глаза блестят мудростью, а крылья прячут тайны успеха. Твоя судьба — высоко парить над землей, достигнув недосягаемых высот.',
            ' of Rams. Бараны благоволят тебе. Они — символ силы и стойкости, а твоя судьба — процветание и изобилие, ведь сила баранов ведет к уверенной победе.',
            ' of Tomes. В книгах написано о твоем успехе. Слова на страницах светятся от будущих свершений, рассказывая историю триумфа, который еще только предстоит пережить.',
            ' of Masks. Маска скрывает улыбку триумфатора. Под ней — лицо того, кто умело управляет судьбой, используя хитрость и мудрость. И это лицо - твоё.'
        ])
    if num == 55:
        result = 'Black Joker. Время молиться своим богам.'
    elif num == 54:
        result = 'Red Joker. Звезды благосклонны к тебе, и ветер судьбы дует в твою сторону. Все пути ведут к успеху, как бы далеко они ни уходили. Шансы оборачиваются в твою пользу, и даже случайные встречи открывают двери к триумфу. Твоя судьба — словно рука, касающаяся золота, превращая всё вокруг в свет и процветание.'
    else:
        result = cardvalue
    update.message.reply_text(result)


async def map(update: Update, context: CallbackContext):
    pool = [
        "Altar of the Lost [1]", "Arctic Lodge [2]", "Automatic Lighthouse [3]", "Bottle Up [4]", "Cactus Fields [5]",
        "Chugga Chugga Lew Lew [6]", "Come and Take It [7]", "Crumbling Biomes [8]", "Desolate Wasteland [9]",
        "Dworzec w Krakowie [10]", "End of Line [11]", "Fire in the Hole [12]", "Fireball Island [13]",
        "Forest Ruins [14]", "Fortified Village [15]", "Graves Not Hills [16]", "Industry [17]",
        "Kiwi vs Poland [18]", "Last Stop [19]", "Lazy River [20]", "Metal Church [24]", "Moon Waltz [22]",
        "MSU Siege [23]", "Nomad Market [24]", "Northern Path [25]", "Oasis [26]", "Paths of Rubbish [27]",
        "Quarantine Zone [28]", "Questionable Ethics [29]", "Razed Outpost [30]", "Skunkworks [31]", "Snow Way [32]",
        "South Park [33]", "Summer Town [34]", "Supply Drop [35]", "Tama Imienia Wiekszego Bobra [36]",
        "Trading Stop [37]", "Transfer Point [38]", "Tundra Frontier [39]", "Undertakers Rest [40]",
        "Warsaw Uprising [41]", "Winters End [42]", "Winter Village [43]", "Full Wallet Of Steam [44]",
        "Grassland Barterville [45]", "Haven [46]", "Quench This [47]", "Railside Meadows [48]",
        "Sparks Workshop [49]", "Wildwood Market [50]", "Cigarette Town [51]", "Bring Down The Wall [52]",
        "Badlands Depot [53]", "Paradise Corner [54]", "Snowvella [55]", "Ransack the Castle [56]",
        "Darkest Dungeon [57]", "The Narrow Pass [58]", "Shadow and Bone [59]", "Sandstorm [60]",
        "Gentle Plains [61]", "Greenbelt [62]", "Grey Zone [63]", "Lost Grove [64]",
        "Krosan Town Revisited [65]", "December Rage Revisited [66]", "Snowy Retreat [67]", "Bayou Town [68]",
        "Do it right this time [69]", "Secret Hideway [70]", "Forest Ambush [71]", "Brass [72]",
        "War Torn [73]"
    ]
    chosen_map = choice(pool)
    result = f"Ваша карта - {chosen_map}. Приятной игры!"
    await update.message.reply_text(result)


async def bg(update: Update, context: CallbackContext):
    hero = [
        "An Evil Wizard", "A Dragon", "The drow", "Goblins", "Kobolds", "A mind flayer", "Evil cultists", "Orcs", "Trolls",
        "A banshee", "A demon lord", "An archdevil", "Giants", "Vampires", "Gnolls", "A werewolf", "A djinni", "A mimic",
        "A tarrasque", "A beholder", "A hag coven", "A lich", "Barbarians", "An aboleth", "A succubus",
        "A criminal organization", "A gelatinous cube", "A necromancer", "Corrupt nobles", "A death knight", "The BBEG",
        "The bard", "Natural selection", "The dm"
    ]
    action = [
        "killed", "murdered", "slaughtered", "massacred", "assassinated", "brainwashed", "captured", "banished", "enslaved",
        "betrayed", "sacrificed", "mauled", "stole", "blackmailed", "conned", "framed", "humiliated", "pillaged", "ruined",
        "ate", "cursed", "befriended", "seduced"
    ]
    victim = [
        "my family", "my hometown", "my parents", "my clan", "my siblings", "my mentors", "my significant other",
        "my master", "my side squeeze", "my apprentice", "my friends", "my previous adventuring party",
        "everyone I knew", "my crew of sailors", "my crew of pirates", "my crew of noble outlaws", "my crew of thieves",
        "the tavern I basically lived in", "my start-up business", "my military unit", "my social status", "my treasure",
        "my aspirations", "my confidence", "my honor", "my imaginary friends"
    ]
    outcome = [
        "and it will have no effect on how I roleplay my character.", "and now I'm a murder hobo.",
        "and now I'm a lawful good stick in the mud.", "and now I seek vengeance.", "and now I trust no one.",
        "and now I have a bleak outlook of the world.", "and now I strive to live by their ideals.",
        "and now I must become stronger.", "and now I seek to bring back what I have lost.",
        "and now I vow to prevent that from happening to anyone else.", "and now I am haunted by their memory.",
        "and now I seek to uncover the truth about what happened.", "and now I fear it will happen again.",
        "and now I am stronger because of it.", "and now I'm an alcoholic.", "and now I have multiclassed into warlock.",
        "and now I'm Batman."
    ]
    result = f"{choice(hero)} {choice(action)} {choice(victim)} {choice(outcome)}"
    await update.message.reply_text(result)



# Добавляем обработчики в приложение
app.add_handler(CommandHandler("bday", bday))
app.add_handler(CommandHandler("creative", creative))
app.add_handler(CommandHandler("creative2", creative2))
app.add_handler(CommandHandler("draw", draw))
app.add_handler(CommandHandler("ff", ff))
app.add_handler(CommandHandler("map", map))
app.add_handler(CommandHandler("bg", bg))

# Запуск приложения
if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling()
