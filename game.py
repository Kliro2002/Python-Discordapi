import random
import discord
from discord.utils import get
import asyncio

prefix = "g"
prefixl = "l"
TOKEN = 'Token einfügen'

client = discord.Client()

# Listen fürs Wörterraten

listestadt = ['berlin','delhi', 'magdeburg', 'potsdam', 'madrid', 'toronto', 'wien', 'tokio','peking', 'mumbai', 'münchen', 'burg'] # Städte
listeauto = ['vw', 'bmw', 'ford', 'chevrolet', 'toyota', 'audi', 'skoda', 'opel', 'porsche' , 'nissan',  'honda', 'jeep'] # Automarken
listetier = ['alpaka', 'biber', 'dachs', 'delfin', 'elch', 'esel', 'elefant', 'fuchs', 'gepard', 'giraffe', 'maus'] # Tiere
# Variablen 
wortcount = 0           #Variable für das teilweise Anzeigen des Geheimwortes bei Wortraten-Game
stopp = 0               #Hilfsvariable für Wortraten-Game
stopp2 = 0              #Hilfsvariable für Wortraten-Game
worter = 0              #Zähler für erratene Wörter bei Wortraten-Game
wortfalsch = 0          #Zähler für falsche Wörter bei Wortraten-Game
zahlenmeister = 0       #Zähler für Zufallszahl-Game Bereich 1-100
zahlenmeister2 = 0       #Zähler für Zufallszahl-Game Bereich individuel
ssp = 0                 #Zähler für gewonnene Schere-Stein-Papier-Game
sspf = 0                #Zähler für verlorene Schere-Stein-Papier-Game
sicherheit = 0

@client.event
async def on_message(message):
    global geheimwort, leben, wortcount , stopp, stopp2, worter ,  wortfalsch, zahlenmeister,zahlenmeister2, ssp, sspf, sicherheit 
      
# Gameauswahl/Übersicht Kommandos

    if message.author == client.user:
        return
    if message.content.startswith('!start'):
        embed = discord.Embed(title="Gameauswahl und Befehlsübersicht")
        embed.add_field(name="!wortraten", value= "Galgenraten (Wortedition)", inline=False)
        embed.add_field(name="!zahlenraten", value="Errate die Zahl", inline=False)
        embed.add_field(name="!ssp", value="Schere-Stein-Papier-Game", inline=False)
        embed.add_field(name="!stats", value="Statistiken", inline=True)
        embed.add_field(name="!hilfe ", value="Informationen zum Bot", inline=False)
        await message.channel.send(content=None, embed=embed)
  
 # Spiel: Wortraten 
  
    if message.content.startswith('!wortraten'):
        embed = discord.Embed(title="Willkommen bei Wortraten", description= "Suche dir einen Themenbereich aus")
        embed.add_field(name="!stadt", value= "Städte", inline=False)
        embed.add_field(name="!auto", value="Automarken", inline=False)
        embed.add_field(name="!tier", value="Tiere", inline=False)
        embed.add_field(name="Auswahl", value="l <Thema>", inline=True)
        embed.add_field(name="Beispiel :" , value= " l auto",inline=False)
        await message.channel.send(content=None, embed=embed)
  
        
    elif (message.content[0] == prefixl):
        cmd_liste = message.content.split(" ")[0]
        cmd_l = message.content.split(" ")[1]
        
        if (cmd_l == 'auto'):
            await message.channel.send(' Du hast dich für die Wortgruppe Auto entschieden.')
            geheimwort = random.choice(listeauto)
            langewort= len(geheimwort)
            leben =  langewort
            await message.channel.send('Das Wort besteht aus ' + str(langewort) + ' Buchstaben.')
            await message.channel.send(' Versuche das neue Wort dirket zu erraten! Benutze dafür g <wort> .' )
            await message.channel.send('(Beispiel: "g mercedes" )')            
            stopp = 0
            stopp2 = 0
            sicherheit = 0
            wortcount = 0
            
        if (cmd_l == 'stadt'):
            await message.channel.send(' Du hast dich für die Wortgruppe Stadt entschieden.')
            geheimwort = random.choice(listestadt)
            langewort= len(geheimwort)
            leben =  langewort
            await message.channel.send('Das Wort besteht aus ' + str(langewort) + ' Buchstaben.')
            await message.channel.send(' Versuche das  Wort dirket zu erraten! Benutze dafür g <wort> .' )
            await message.channel.send('(Beispiel: "g altstadt" )')      
            stopp = 0
            stopp2 = 0
            sicherheit = 0
            wortcount = 0

        if (cmd_l == 'tier'):
            await message.channel.send(' Du hast dich für die Wortgruppe Tiere entschieden.')
            geheimwort = random.choice(listetier)
            langewort= len(geheimwort)
            leben =  langewort
            await message.channel.send('Das Wort besteht aus ' + str(langewort) + ' Buchstaben.')
            await message.channel.send(' Versuche das neue Wort dirket zu erraten! Benutze dafür g <wort> .' )
            await message.channel.send('(Beispiel: "g vogel" )')     
            stopp = 0
            stopp2 = 0
            sicherheit = 0
            wortcount = 0
   
    elif (message.content[0] == prefix):
        cmd =message.content.split(" ")[0]
        cmd_wort = message.content.split(" ")[1]
        
        if cmd_wort == geheimwort:
              if stopp == 1:
                  await message.channel.send('Du hast das Wort schon erraten!')
              elif (sicherheit == 0) and (leben >= 0):
                  await message.channel.send('Glückwunsch, du hast das Wort erraten!')
                  await message.channel.send('Lust auf eine weitere Runde ? Schreibe !wortraten  um alle Kategorien anzuzeigen!')
                  await message.channel.send('Oder schreibe l <Thema> um die Kategorie direkt auszuwählen.')
                  member = message.author
                  role = get(member.guild.roles, name="Wortmeister")
                  await member.add_roles(role)
                  stopp = stopp + 1
                  worter = worter +1
                  sicherheit = 1
                  wortcount = 0
                  leben = 0          
                             
        elif cmd_wort != geheimwort and sicherheit != 1:
            if stopp2 == 1:
                await message.channel.send('Du hast das Wort nicht erraten. Bitte wähle ein Neues aus!')             
                
            else:
                await message.channel.send('Schade, das war nicht das gesuchte Wort.')
                
                leben = leben - 1
                wortcount = wortcount + 1
                wortgewählt = geheimwort
                if  leben >= 0:
                    await message.channel.send('Gesuchtes Wort: '+(wortgewählt[0:int(wortcount)]))
                    if (leben != 0):
                        await message.channel.send('(Noch ' + str(leben) + ' Versuche)')
                elif (leben <= 0 ):
                    await message.channel.send('Keine Versuche mehr!')
                    # Gibt Stopp-Bild aus
                    embed = discord.Embed()
                    embed.set_image(url="https://cdn.pixabay.com/photo/2019/01/30/11/52/businessman-3964425__340.jpg")
                    await message.channel.send(content=None, embed=embed)
                    
                    
                    await message.channel.send('Lust auf eine weitere Runde ? Schreibe !wortraten um alle Kategorien anzuzeigen!  Oder wähle eine Kategorie aus!')
                    member = message.author
                    role = get(member.guild.roles, name="Wortmeister")
                    await member.remove_roles(role)
                    wortfalsch = wortfalsch + 1
                    stopp2 = stopp2 +1
                    sicherheit = 2
                elif leben == 0:
                    falsch = 1
        if sicherheit == 1:
             await message.channel.send('Bitte neue Kategorie/Wort auswählen!') 
           
 # Zahlenraten           
                
    elif message.content.startswith('!zahlenraten'):
        message_parts = message.content.split(' ')
        # Startmenü "Zahlenraten"
        if len(message_parts) == 1 and message_parts[0] == '!zahlenraten':
            await message.channel.send('Willkommen bei Zahlenraten')
            await message.channel.send('Errate die Zahl im Bereich zwischen 1 und 100. Nur ein Versuch!')
            await message.channel.send('Um eine Zahl zu raten gebe !zahlenraten <deine Zahl> ein')
            await message.channel.send('Falls du deinen Bereich selbst festlegen möchtest, benutze !zahlenraten  <niedrigste Zahl> <höchste Zahl> <deine Zahl> .')
        #Zahlenraten - Bereich 0-100
        elif len(message_parts) == 2 :
            zahleingabe = message_parts[1]
            await message.channel.send('Du hast die Zahl ' + str(zahleingabe) + ' eingegeben.')
            zahleingabe = int(zahleingabe)
            zahl = random.randint(0, 100)
            if (zahleingabe == zahl):
                await message.channel.send('Du hast die Zufallszahl (' + str(zahl) + ') erraten.')
                zahlenmeister = zahlenmeister + 1
                member = message.author
                role = get(member.guild.roles, name="Zahlenmeister")
                await member.add_roles(role)
            elif (zahleingabe != zahl) :
                 await message.channel.send(str(zahleingabe) + ' war nicht die gesuchte Zahl.')
                 await message.channel.send('Die Zufallszahl war ' + str(zahl) + ' .')
       #Zahlenraten - bereich individuell  
        elif len(message_parts) == 4 and message_parts[0] == '!zahlenraten' :
            minzahl = message_parts[1]
            maxzahl = message_parts[2]
            zahleingabe = message_parts[3]
            await message.channel.send('Du hast die Zahl ' + str(zahleingabe) + ' eingegeben.')
            zahleingabe = int(zahleingabe)
            zahl = random.randint(int(minzahl), int(maxzahl))
            if (zahleingabe == zahl):
                await message.channel.send('Du hast die Zufallszahl im Bereich ' + str(minzahl)+ ' bis ' + str(maxzahl) + ' erraten.')
                zahlenmeister2 = zahlenmeister2 + 1
            elif (zahleingabe != zahl) :
                 await message.channel.send(str(zahleingabe) + ' war nicht die gesuchte Zahl.')
                 await message.channel.send('Die Zufallszahl war ' + str(zahl) + ' .')           
    
     # Schere Stein Papier
     
    elif message.content.startswith('!ssp'):
        message_parts = message.content.split(' ')
        if len(message_parts) == 1 and message_parts[0] == '!ssp':
            await message.channel.send('Willkommen bei Schere Stein Papier.')
            await message.channel.send('Um deine Eingabe zu tätigen gebe !ssp <Eingabe> ein.')
            await message.channel.send('(Beispiel:   "!ssp schere" ein)')
        elif len(message_parts) == 2 :
            eingabep = message_parts[1]
            moves = ['schere', 'stein', 'papier']
            if eingabep in moves:
                eingabebot = random.choice(moves)
                await message.channel.send('Du hast ' + str(eingabep)   + ' ausgewählt.')
                await message.channel.send('Bot hat ' + str(eingabebot) + ' ausgewählt.')
                if (eingabep == eingabebot):
                     msg =  ('Bot und {0.author.mention} haben beide ' + str(eingabebot) + ' genommen. Deshalb Unentschieden.') .format(message)
                     await message.channel.send(msg)
                elif (eingabep == 'papier' ) and (eingabebot == 'stein'):
                    msg =  ('{0.author.mention} hat gewonnen.') .format(message)
                    await message.channel.send(msg)
                    ssp = ssp + 1
                elif (eingabep == 'schere' ) and (eingabebot == 'papier'):
                    msg =  ('{0.author.mention} hat gewonnen.') .format(message)
                    await message.channel.send(msg)
                    ssp = ssp + 1
                elif (eingabep == 'stein' ) and (eingabebot == 'schere'):
                    msg =  ('{0.author.mention} hat gewonnen.') .format(message)
                    await message.channel.send(msg)
                    ssp = ssp + 1
                elif (eingabep == 'papier' ) and (eingabebot == 'schere'):
                    await message.channel.send('Bot hat gewonnen!')
                    sspf = sspf = sspf + 1
                elif (eingabep == 'schere' ) and (eingabebot == 'papier'):
                    await message.channel.send('Bot hat gewonnen!')
                elif (eingabep == 'stein' ) and (eingabebot == 'schere'):
                    await message.channel.send('Bot hat gewonnen!')
                    sspf = sspf +1
                elif (eingabep == 'stein' ) and (eingabebot == 'papier'):
                    await message.channel.send('Bot hat gewonnen!')
                    sspf = sspf + 1
                elif (eingabep == 'schere' ) and (eingabebot == 'stein'):
                    await message.channel.send('Bot hat gewonnen!')
                    sspf = sspf +1
            else:
                await message.channel.send('Spielereingabe nicht erkannt. Mögliche Eingaben "papier" oder "stein" oder "schere".')
  #Hilfe/Informationen zum Bot   
    elif message.content.startswith('!hilfe'):
          await message.channel.send('Informationen:')
          await message.channel.send('Dieser Bot stellt Sologames für Spieler zur Verfügung.')
          await message.channel.send('Um die vollständige Funktionsfähigkeit des Bots zu erhalten, wird empfohlen zwei Rollen "Wortmeister" und "Zahlenmeister" zu erstellen. Die Rolle des Bots muss dabei über den beiden Rollen sein.')
          await message.channel.send('Beim Spielen mit dem Bot bitte Kleinschreibung verwenden!')
     
     #Statistik

    elif message.content.startswith('!stats'):
        await message.channel.send('Gesamtbewertung:')
        await message.channel.send('Wörter erratet:                                                ' + str(worter))
        await message.channel.send('Wörter nicht erratet:                                      ' + str(wortfalsch))
        await message.channel.send('Zahlen erratet (100er Bereich):                   ' + str(zahlenmeister))
        await message.channel.send('Zahlen erratet (individuel):                           ' + str(zahlenmeister2))
        await message.channel.send('Schere-Stein-Papier gewonnen:                  ' + str(ssp))
        await message.channel.send('Schere-Stein-Papier verloren:                      ' + str(sspf))   

async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)