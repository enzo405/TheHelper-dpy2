import discord 
from discord.ext import commands
from bot_auth import TOKENH
# import database_handler as Mydb
from discord import app_commands
from discord.ui import *
from classfile import SelectView
from typing import Optional
import asyncio
from datetime import datetime

test_guild = discord.Object(id=889452351130312714)
ada_guild = discord.Object(id=504559824617603082)
artichaud_guild = discord.Object(id=900046546656182322)
channel_command = [736659714670198794, 948565096366481428, 948681408640073818, 889881030188748810]
# db = Mydb.DatabaseHandler()

class get_user:
	def __init__(self,bot:discord.Client):
		self.TheHelper:discord.User = bot.get_user(707200529738235925)


class abot(commands.Bot):
	def __init__(self):
		intents = discord.Intents.all()
		super().__init__(intents = intents,command_prefix="?", help_command = None, case_insensitive=True)
		self.synced = False #we use this so the bot doesn't sync commands more than once
		self.added = False

	async def on_ready(ctx):
		await ctx.wait_until_ready()
		timestamp = datetime.now()
		print(f"We have logged in as {ctx.user} at {timestamp}")

TheHelper = abot()
tree = TheHelper.tree

#--------------------- SlashCommand ---------------------

@tree.command(name="clear",description="delete spam message")
@app_commands.checks.has_any_role(672529613167001630,504568245139800067,504568053292335122) #helper / admin / chef
@app_commands.describe(message_id="message id you want to delete")
async def clear(ctx:discord.Interaction,message_id:str):
	msg = await ctx.channel.fetch_message(message_id)
	author_message = msg.author.id
	await msg.delete()
	await ctx.response.send_message(f"You have deleted <@{author_message}>'s message\n```{msg.content} ```", ephemeral=True)

@tree.command(name="rank_help",description="Comment rentre t'on dans le leaderboard ?")
async def rank_help(ctx:discord.Interaction):
	user = await TheHelper.fetch_user("382930544385851392")
	em1=discord.Embed(
	title="Comment rentrer dans le classement ?",url="https://adarmy.herokuapp.com/classement/",color=0xFF5733)
	em1.add_field(name="Rentrer vos stats",value="/stats *attaque* *pv* \nVoici un exemple = ``/stats 10001 50001``", inline=False)
	em1.add_field(name="Connaitre ton rank ",value="``?rank``", inline=False)
	em1.add_field(name="Connaitre le top10",value="https://adarmy.herokuapp.com/classement/", inline=False)
	em1.add_field(name="Free To Play",value=f"Preuves à envoyer en MP à <@{user.id}> :\n-Un screen du compte (menu d'accueil)\n-Un screen du nombre de tenues que vous possédez\n-Un screen de vos stats", inline=False)
	em1.add_field(name="Chapitre",value=f"Preuves à envoyer en MP à <@{user.id}> :\n-Un screen des chapitres sur lesquels vous êtes bloqués (nm et hm)\n-Un screen de vos stats", inline=False)
	em1.set_footer(text="Cela ne sert à rien de mettre des stats au pif, je vérifierai vos entrés")
	await ctx.response.send_message(embed=em1)


@tree.command(name="youtube",description="Besoin d'un petit tuto ? fait-toi plaisir ;)")
@app_commands.choices(youtube=[
				app_commands.Choice(name="Comment DÉBLOQUER l'AUTEL DES HÉROS ! ARCHERO", value="1"),
				app_commands.Choice(name="COMMENT TRANSFERER SON COMPTE DE TÉLÉPHONE ! ARCHERO", value="2"),
				app_commands.Choice(name="QUEL EST LE MEILLEUR HÉROS en 2022 ! TIER LIST ARCHERO", value="3"),
				app_commands.Choice(name="COMMENT RÉCUPÉRER LES RESSOURCES D'UN ITEM ! ARCHERO", value="4"),
				app_commands.Choice(name="Quel CHAPITRE FARM en 2022 ? ARCHERO", value="5"),
				app_commands.Choice(name="COMMENT GAGNER DU STUFF VERT EN RUN ! ARCHERO", value="6"),
				app_commands.Choice(name="TIER LIST ARCHERO 2022 ARMES PVP !", value="7"),
				app_commands.Choice(name="TIER LIST ARCHERO 2022 ARMES PVE !", value="8"),
				app_commands.Choice(name="LOUPES & MINERAIS ! ARCHERO", value="9"),
				app_commands.Choice(name="GUIDE COMPLET ! AUTEL D'ÉQUIPEMENT ! ARCHERO", value="10"),
				app_commands.Choice(name="NE FAITES PLUS JAMAIS CETTE ERREUR !!! ARCHERO", value="11"),
				app_commands.Choice(name="Apprendre à Step sur Archero", value="12"),
		]
	)
async def youtube(ctx:discord.Interaction,youtube:str):
	if youtube == "1":
		await ctx.response.send_message("https://youtu.be/JoZ4BhRZsRU")
	elif youtube == "2":
		await ctx.response.send_message("https://youtu.be/syPW3S6vtAo")
	elif youtube == "3":
		await ctx.response.send_message("https://youtu.be/vh3smt_1NNk")
	elif youtube == "4":
		await ctx.response.send_message("https://youtu.be/DG16UoSoBOM")
	elif youtube == "5":
		await ctx.response.send_message("https://youtu.be/07rxbzpp1tA")
	elif youtube == "6":
		await ctx.response.send_message("https://youtu.be/CfnR-YtiZ4M")
	elif youtube == "7":
		await ctx.response.send_message("https://youtu.be/RH9cSNKjky8")
	elif youtube == "8":
		await ctx.response.send_message("https://youtu.be/_HNuroLTSjs")
	elif youtube == "9":
		await ctx.response.send_message("https://youtu.be/5FJZ5cUFV6E")
	elif youtube == "10":
		await ctx.response.send_message("https://youtu.be/VxY-q_EwwOM")
	elif youtube == "11":
		await ctx.response.send_message("https://youtu.be/mjwg-TKLm-M")
	elif youtube == "12":
		await ctx.response.send_message("https://youtu.be/Nm9LOBTn3kE")
	else:
		await ctx.response.send_message("Tu n'a pas ou mal choisi la vidéo, réessaie...")




# @tree.command(name="stats",description="Ajoute tes stats sur le leaderboard")
# @app_commands.describe(attaque="Votre attaque ingame")
# @app_commands.describe(pv="Vos pv ingame")
# @app_commands.describe(chapitre_nm="chapitre normal TERMINÉ !")
# @app_commands.describe(chapitre_hm="chapitre hard TERMINÉ !")
# async def stats(ctx:discord.Interaction, attaque:int, pv:int, chapitre_nm:int=0, chapitre_hm:int=0):
# 	chat = TheHelper.get_channel(952673377787711529)
# 	luhcaran = await TheHelper.fetch_user(382930544385851392)
# 	author = await TheHelper.fetch_user(ctx.user.id)
# 	name = author.display_name.replace("'","")
# 	list_id_already_registered = db.column("SELECT id FROM Stats")
# 	em1=discord.Embed(
# 	title="Stats Confirmation",url = "https://adarmy.herokuapp.com/classement/",description = "",color=0x5733FF)
# 	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
# 	em1.add_field(name=f"✅ Vos stats viennent d'être envoyé à LuhCaran#9802 et sont maintenant en attente de confirmation !",value=f"Veuillez m'envoyer un screen de vos stats svp (----><@{luhcaran.id}>)\nVous pouvez demander à avoir le statuts Free To Play (faites `?rank_help` pour + d'info)",inline=False)
# 	await ctx.response.send_message(embed=em1)
# 	confirm = await chat.send(f"<@{ctx.user.id}> à utilisé la commande ``/stats {attaque} {pv} {chapitre_nm} {chapitre_hm}``! ||<@{luhcaran.id}>||")
# 	try:
# 		reaction, user = await TheHelper.wait_for('reaction_add', timeout = 3600)
# 	except asyncio.TimeoutError:
# 		await chat.send(f"Tu n'a surement pas eu le temps d'accepter : ``/stats <@{ctx.user.id}> {attaque} {pv} {chapitre_nm} {chapitre_hm}`` !")
# 		await confirm.delete()
# 		return
# 	else:
# 		if str(reaction.emoji) == "\U00002705":
# 			if ctx.user.id not in list_id_already_registered:
# 				db.create_person(ctx.user.id, name, attaque, pv)
# 				db.set_chapter(ctx.user.id, chapitre_nm, chapitre_hm)
# 				await confirm.reply(f"Vous venez de confirmer les stats de {name}",delete_after=15)
# 				await asyncio.sleep(5)
# 				await confirm.delete()
# 			elif ctx.user.id in list_id_already_registered:
# 				db.change_stats(ctx.user.id, name, attaque, pv)
# 				db.set_chapter(ctx.user.id, chapitre_nm, chapitre_hm)
# 				await confirm.reply(f"Vous venez de confirmer les stats de {name}",delete_after=15)
# 				await asyncio.sleep(5)
# 				await confirm.delete()
# 			target = ctx.user
# 			place = db.column("SELECT id FROM Stats ORDER BY attaque DESC")
# 			target_F2P = db.column(f"SELECT F2P FROM Stats WHERE id={target.id}")
# 			target_atk2 = db.column(f"SELECT attaque FROM Stats WHERE id={target.id}")
# 			target_pv2 = db.column(f"SELECT pv FROM Stats WHERE id={target.id}")
# 			target_chapitreHm = db.column(f"SELECT ChapterHm FROM Stats WHERE id={target.id}")
# 			target_chapitreNm = db.column(f"SELECT ChapterNm FROM Stats WHERE id={target.id}")
# 			target_atk = str(target_atk2).replace("]","").replace("[","")
# 			target_pv = str(target_pv2).replace("]","").replace("[","")
# 			F2P = str(target_F2P).replace("]","").replace("[","").replace("None","❌").replace("'","")
# 			chapitreNm = str(target_chapitreNm).replace("]","").replace("[","").replace("None","Pas précisé")
# 			chapitreHm = str(target_chapitreHm).replace("]","").replace("[","").replace("None","Pas précisé")
# 			em1=discord.Embed(
# 			title=f"Voici les Stats de {target.display_name}",url="https://adarmy.herokuapp.com/classement/",color=0x5733FF)
# 			em1.add_field(name=f"Tu es n°{place.index(target.id)+1} sur {len(place)}",value=f"> **Attaque** --> {target_atk}\n> **Pv** --> {target_pv}\n> **Chapitre Nm** --> {chapitreNm}\n> **Chapitre Hm** --> {chapitreHm}\n> **Free To Play** --> {F2P}",inline=False)
# 			em1.set_thumbnail(url= target.avatar)
# 			em1.set_footer(text="https://adarmy.herokuapp.com/classement/")
# 			await ctx.user.send(embed=em1)
# 		if str(reaction.emoji) == "\U0000274c":
# 			await confirm.reply(f"Les stats de {name} n'ont pas été confirmées",delete_after=15)
# 			await asyncio.sleep(5)
# 			await confirm.delete()



# @tree.command(name="dbh_command",description="only available for LuhCaran", guild=test_guild)
# @app_commands.describe(target_id="id de la personne")
# @app_commands.describe(attaque="attaque de la personne")
# @app_commands.describe(pv="pv de la personne")
# @app_commands.describe(chapitre_nm="chapitre normal mode de la personne")
# @app_commands.describe(chapitre_hm="chapitre hard mode de la personne")
# async def dbh_command(ctx:discord.Interaction, target_id:str, attaque:int, pv:int,chapitre_nm:int=0,chapitre_hm:int=0):
# 	chat = TheHelper.get_channel(952673377787711529)
# 	user = await TheHelper.fetch_user(382930544385851392)
# 	target = await TheHelper.fetch_user(target_id)
# 	name = target.display_name.replace("'","").replace('"','')
# 	list_id_already_registered = db.column("SELECT id FROM Stats")
# 	em1=discord.Embed(
# 	title="Stats Confirmation",url = "https://adarmy.herokuapp.com/classement/",description = "",color=0x5733FF)
# 	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
# 	em1.add_field(name=f"Pour @{name}",value=f"Si je résume bien, <@{target_id}> aura : \n> **Attaque** --> {attaque}\n> **Pv** --> {pv}\n> **Chapitre Nm** --> {chapitre_nm}\n> **Chapitre Hm** --> {chapitre_hm}",inline=False)
# 	await ctx.response.send_message(embed=em1)
# 	confirm = await chat.send(f":white_check_mark: **{name}** à utilisé la commande ``/stats {attaque} {pv}``! ||<@{user.id}>||")
# 	try:
# 		reaction, user = await TheHelper.wait_for('reaction_add', timeout = 3600)
# 	except asyncio.TimeoutError:
# 		await chat.send(f"Pour **{name}**, tu n'a surement pas eu le temps d'accepter,\nFait cette commande si tu veux accepter sinon ignore ce message : ``/stats {target_id} {attaque} {pv}`` !")
# 		await confirm.delete()
# 		return
# 	else:
# 		if str(reaction.emoji) == "\U00002705":
# 			if target_id not in list_id_already_registered:
# 				db.create_person(target.id, name, attaque, pv)
# 				db.set_chapter(target.id, chapitre_nm, chapitre_hm)
# 				await confirm.reply(f"Vous venez de confirmer les stats de {name}",delete_after=15)
# 				await asyncio.sleep(5)
# 				await confirm.delete()
# 			elif target_id in list_id_already_registered:
# 				db.change_stats(target.id, name, attaque, pv)
# 				db.set_chapter(target.id, chapitre_nm, chapitre_hm)
# 				await confirm.reply(f"Vous venez de confirmer les stats de {name}",delete_after=15)
# 				await asyncio.sleep(5)
# 				await confirm.delete()
# 			place = db.column("SELECT id FROM Stats ORDER BY attaque DESC")
# 			target_F2P = db.column(f"SELECT F2P FROM Stats WHERE id={target.id}")
# 			target_atk2 = db.column(f"SELECT attaque FROM Stats WHERE id={target.id}")
# 			target_pv2 = db.column(f"SELECT pv FROM Stats WHERE id={target.id}")
# 			target_chapitreHm = db.column(f"SELECT ChapterHm FROM Stats WHERE id={target.id}")
# 			target_chapitreNm = db.column(f"SELECT ChapterNm FROM Stats WHERE id={target.id}")
# 			target_atk = str(target_atk2).replace("]","").replace("[","")
# 			target_pv = str(target_pv2).replace("]","").replace("[","")
# 			F2P = str(target_F2P).replace("]","").replace("[","").replace("None","❌").replace("'","")
# 			chapitreNm = str(target_chapitreNm).replace("]","").replace("[","").replace("None","Pas précisé")
# 			chapitreHm = str(target_chapitreHm).replace("]","").replace("[","").replace("None","Pas précisé")
# 			em1=discord.Embed(
# 			title=f"Voici les Stats de {target.display_name}",url="https://adarmy.herokuapp.com/classement/",color=0x5733FF)
# 			em1.add_field(name=f"Tu es n°{place.index(target.id)+1} sur {len(place)}",value=f"> **Attaque** --> {target_atk}\n> **Pv** --> {target_pv}\n> **Chapitre Nm** --> {chapitreNm}\n> **Chapitre Hm** --> {chapitreHm}\n> **Free To Play** --> {F2P}",inline=False)
# 			em1.set_thumbnail(url= target.avatar)
# 			em1.set_footer(text="https://adarmy.herokuapp.com/classement/")
# 			await ctx.channel.send(embed=em1)
# 		if str(reaction.emoji) == "\U0000274c":
# 			await confirm.reply(f"Les stats de {name} n'ont pas été confirmées",delete_after=15)
# 			await asyncio.sleep(5)
# 			await confirm.delete()


# #--------------------- DATABASE ADMIN /HOST COMMAND ---------------------

# @TheHelper.command(name="dbh_rm")
# @commands.is_owner()
# async def dbhost_remove_user(ctx:discord.Interaction, target: discord.User):
# 	chat = TheHelper.get_channel(952673377787711529)
# 	await ctx.reply(f"Une attente à la confirmation vient d'être envoyé dans <#{chat}> pour supprimer les stats de <@{target.id}>", delete_after=10, mention_author=True)
# 	confirm = await chat.send(f":white_check_mark: **{ctx.author}** à utilisé la commande ``{ctx.message.content}`` pour supprimer les stats de {target}")
# 	try:
# 		reaction, user = await TheHelper.wait_for('reaction_add', timeout = 3600)
# 	except asyncio.TimeoutError:
# 		await confirm.reply(f"**Temps écoulé !** Fait cette commande : ``?dbh_rm <@!{target.id}>`` !")
# 		return
# 	else:
# 		if str(reaction.emoji) == "\U00002705":
# 			db.delete_person(target.id)
# 			await confirm.reply(f"Les stats de {target} ont bien été supprimées",delete_after=15)
# 			await asyncio.sleep(5)
# 			await confirm.delete()
# 		if str(reaction.emoji) == "\U0000274c":
# 			await confirm.reply(f"Les stats de {target} n'ont pas été supprimé",delete_after=15)
# 			await asyncio.sleep(5)
# 			await confirm.delete()

# @TheHelper.command(name="dbh_f2p")
# async def dbhost_free_to_play(ctx:discord.Interaction, target: discord.User, response):
# 	luhcaran = await TheHelper.fetch_user("382930544385851392")
# 	if ctx.author.id == luhcaran.id:
# 		db.free_to_play(target.id, response)
# 		await ctx.reply(f"{target} a maintenant `{response}` dans F2P",delete_after=15)
# 	else:
# 		await ctx.reply(f"Tu n'a pas accès a cette commande seul <@{luhcaran.id}> peut", delete_after = 15, mention_author=True)

# @TheHelper.command(name="dbh_help")
# async def dbhost_help_command(ctx):
# 	luhcaran = await TheHelper.fetch_user("382930544385851392")
# 	em1=discord.Embed(
# 	title="Commande pour Database Host",url="https://www.youtube.com/channel/UCJoV9pAMDRvD70JV7iLwA2g",color=0xFF5733)
# 	em1.add_field(name="Créer un profil",value="``?dbh_cp <@123456789901> 10000 50000``", inline=False)
# 	em1.add_field(name="Changer les stats",value="``?dbh_ep <@123456789901> 10001 50001``", inline=False)
# 	em1.add_field(name="Supprimer les stats",value="``?dbh_rm <@123456789901>``", inline=False)
# 	em1.add_field(name="Status F2P",value="``?dbh_f2p <@123456789901> ✅/❌``", inline=False)
# 	em1.add_field(name="Insérer chapitre",value="``?dbh_ch <@123456789901> 21 24``", inline=False)
# 	await luhcaran.send(embed=em1)

# #--------------------- USER DATABASE COMMAND ---------------------

# @TheHelper.command(name="rank")
# async def display_rank(ctx:discord.Interaction, target: Optional[discord.User]):
# 	target = target or ctx.author
# 	place = db.column("SELECT id FROM Stats ORDER BY attaque DESC")
# 	target_F2P = db.column(f"SELECT F2P FROM Stats WHERE id={target.id}")
# 	target_atk2 = db.column(f"SELECT attaque FROM Stats WHERE id={target.id}")
# 	target_pv2 = db.column(f"SELECT pv FROM Stats WHERE id={target.id}")
# 	target_chapitreHm = db.column(f"SELECT ChapterHm FROM Stats WHERE id={target.id}")
# 	target_chapitreNm = db.column(f"SELECT ChapterNm FROM Stats WHERE id={target.id}")
# 	target_atk = str(target_atk2).replace("]","").replace("[","")
# 	target_pv = str(target_pv2).replace("]","").replace("[","")
# 	F2P = str(target_F2P).replace("]","").replace("[","").replace("None","❌").replace("'","")
# 	chapitreNm = str(target_chapitreNm).replace("]","").replace("[","").replace("None","Pas précisé")
# 	chapitreHm = str(target_chapitreHm).replace("]","").replace("[","").replace("None","Pas précisé")
# 	try:
# 		em1=discord.Embed(
# 		title=f"Voici les Stats de {target.display_name}",url="https://adarmy.herokuapp.com/classement/",color=0x5733FF)
# 		em1.add_field(name=f"Tu es n°{place.index(target.id)+1} sur {len(place)}",value=f"> **Attaque** --> {target_atk}\n> **Pv** --> {target_pv}\n> **Chapitre Nm** --> {chapitreNm}\n> **Chapitre Hm** --> {chapitreHm}\n> **Free To Play** --> {F2P}",inline=False)
# 		em1.set_thumbnail(url= target.avatar)
# 		em1.set_footer(text="https://adarmy.herokuapp.com/classement/")
# 		await ctx.channel.send(embed=em1)
# 	except ValueError:
# 		await ctx.channel.send(f"{target.display_name} n'est pas présent dans le classement.", delete_after = 6)


#--------------------- EMBED COMMAND ---------------------


@TheHelper.command()
async def sync(ctx) -> None:
	synced = await TheHelper.tree.sync()
	print("synced")
	await ctx.channel.send(
		f"Synced {len(synced)} commands to the current guild."
	)


@TheHelper.command()
async def help(ctx):
	if ctx.channel.id in channel_command: 
		em0=discord.Embed(
		title="Voici toutes les commandes proposées :",description = "",color=0xFF5733)
		em0.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
		em0.add_field(name="Commandes",value="?heros_laby \n?discord_archero \n?sylvan_command \n?abreviation \n?pvp \n?qr \n?stuff_pve \n?stuff_pvp \n?laby_guide \n?conseil \n?oeufs_level \n?talent \n?doc_oeufs \n?stats_calc", inline= True)
		em0.add_field(name="Commandes",value="?stats_joyaux \n?stuff_fusion \n?joyaux_fusion \n?rune_effect \n?offre_item \n?index_archive \n?skin \n?all_tierlist \n?shards_evo \n?tuto_apk \n?archero_compilation \n?glitch \n?boost_heros \n?rank_help",inline=True)
		await ctx.channel.send(embed=em0,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def stats_calc(ctx):
	em1=discord.Embed(
	title="Calculateur de Stats Version Updated",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name='Stats Calculator',value="https://docs.google.com/spreadsheets/d/1NIfusyFcHqo-UzhGGpro03AxfXLXZFd1AIsOYGcP9zU/edit?usp=sharing ", inline= True)
	em1.add_field(name=" Petite indication :",value="2 choses importantes : \n-Si vous rencontrer un bug/trop gros écart de valeurs veuillez me Mp \n-Il faut aussi savoir qu'a chaque Mise à jour du jeux il faudra re-remplir les valeurs sauf si vous souhaiter garder la version non-update", inline= True)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def glitch(ctx):
	em1=discord.Embed(
	title="PAS DE GLITCH DANS CE SERVEUR",url="https://www.youtube.com/channel/UCJoV9pAMDRvD70JV7iLwA2g",description = "C'est sujet qui peut aboutir à un ban du serveur",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Définition Glitch :",value="A partir du moment où tu influes sur le jeu de manière anormal par un kill de l'app, ou autre, c'est du glitch, donc pas autorisé ici.", inline=False)
	em1.add_field(name="C'est écrit dans le règlement",value="donc pas d'excuses", inline=False)
	em1.set_footer(text="Si vous voulez en parler c'est en message privé !")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def talent(ctx):
	em1=discord.Embed(
	title="Talent Tree",url="https://docs.google.com/spreadsheets/d/1Wu5yNEMrnoTGimhS5a2qfKHuZvHSRXyxLhkbok3nTX0/edit#gid=0",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Voici le lien qui vous mènera au gsheet",value="https://docs.google.com/spreadsheets/d/1Wu5yNEMrnoTGimhS5a2qfKHuZvHSRXyxLhkbok3nTX0/edit#gid=0", inline=False)
	em1.add_field(name=":warning: ATTENTION LES NOUVEAUX TALENTS SONT VALABLES QUE POUR CEUX QUI AVAIS FINIS LES TALENTS AVANT LA MAJ DES RUNES  ",value="https://docs.google.com/spreadsheets/d/1IHrFHEIuuCGkgt1c39jrtsscZhNcFLCxKzdROl1EktM/edit?usp=sharing", inline=False)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def QR(ctx):
	em1=discord.Embed(
	title="Voici le gsheet qui donne accès au tableau de QuickRaid",url="https://docs.google.com/spreadsheets/d/1gI3lxMxjVT3iLb-71kyNrAGE8a4rhAp_tSo7IDwNm3w/edit#gid=808920507",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="QR (Raid éclair)",value="https://docs.google.com/spreadsheets/d/1gI3lxMxjVT3iLb-71kyNrAGE8a4rhAp_tSo7IDwNm3w/edit#gid=808920507",inline=True)
	em1.set_footer(text="Il est en francais et anglais car je l'ai partagé avec le discord Officiel")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def all_tierlist(ctx):
	em1=discord.Embed(
	title="Voici le gsheet qui donne accès aux TierList",url="https://docs.google.com/spreadsheets/d/1vm2xlsrUYbgXDYP7lmh60I4CBWkTLKA5YBhzrY-t0Tw/edit#gid=380709681",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Tierlist stuff PvP et PvE, et une TierList skill en Endless ",value="https://docs.google.com/spreadsheets/d/1vm2xlsrUYbgXDYP7lmh60I4CBWkTLKA5YBhzrY-t0Tw/edit#gid=380709681",inline=True)
	em1.set_footer(text="Attention !!! Il faut parfois savoir faire preuve de bon sens, donc ne prenez pas cette tierlist aux pieds de la lettre")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def index_archive(ctx):
	em1=discord.Embed(
	title="Voici un gdoc qui recense tout les documents présent dans Archives",url="https://docs.google.com/document/d/1Y8EGuiOL2t6alAgz7_Uyib5hADUNlnTJbMK3hE3Xxtc/edit",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Il a été réalisé par Flora",value="https://docs.google.com/document/d/1Y8EGuiOL2t6alAgz7_Uyib5hADUNlnTJbMK3hE3Xxtc/edit",inline=True)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def doc_oeufs(ctx):
	em1=discord.Embed(
	title="Archero info Couveuse", url="https://docs.google.com/spreadsheets/d/1bfq-F1BoT3FO-Nerg7KFn3jE5IMy768uokjLN5b7WCw/edit#gid=1801182798",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Réalisé par LuhCaran & Doodam's1402 vous y trouverez les stats de tout les mob/boss mais aussi rapidement trouver dans quel chapitre il se situe .",value="https://docs.google.com/spreadsheets/d/1bfq-F1BoT3FO-Nerg7KFn3jE5IMy768uokjLN5b7WCw/edit#gid=1801182798",inline=True)
	em1.add_field(name="Très pratique !",value="Vous retrouverez toutes les infos concernant les oeufs de niveau 0 et vous pouvez aussi trouver les stats à chaque niveau dans l'onglet 'Stats Complète'",inline=True)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def archero_compilation(ctx):
	em1=discord.Embed(
	title="Voici un gdoc réalisé par LanderZ", url="https://discord.com/channels/504559824617603082/607110270250385418/885938275712381028",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Dans ce gdoc vous retrouverez TOUTES, absolument toutes les info d'Archero",value="https://discord.com/channels/504559824617603082/607110270250385418/885938275712381028",inline=True)
	em1.add_field(name="Il y a :",value="-Hero Evolution and Evolution Stats \n -Daily Events past calendar \n -Jewels \n -Mystery Mine, Hero Buffs and Battle Contracts \n -Ancient Maze Bosses \n -Lucky Spin Events \n -Outfits \n -Avatars and Frames \n -Support Hero Daily Event Affinity Boosts \n -Chapter bonuses [gold per wheels, Quick Raids, etc.]",inline=True)
	em1.set_footer(text="Spoiler : Le document est en anglais !!")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def tuto_apk(ctx):
	em1=discord.Embed(
	title="Voici un tuto réalisé par Flora", url="https://docs.google.com/document/d/1_dMG8fEA5g86V_c4FY_2Kmu3NG9H4at-xUIdd4ueWWA/edit",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Apprenez comment installer une apk pour avoir les dernière MAJ avant les iOs",value="https://docs.google.com/document/d/1_dMG8fEA5g86V_c4FY_2Kmu3NG9H4at-xUIdd4ueWWA/edit",inline=True)
	em1.set_footer(text="Car oui seul les Android peuvent installer une Apk !! ")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def rune_effect(ctx):
	em1=discord.Embed(
	title="Voici un gdoc dans lequel vous trouverez chaque ligne de runes disponible", url="https://docs.google.com/spreadsheets/d/1Y2C0yY-Ht5XDEYcA85XSnM51G8bguFIWE8LL7AMCVc0/edit#gid=0",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Réalisé par Chaos (un mec du discord officiel)",value="https://docs.google.com/spreadsheets/d/1Y2C0yY-Ht5XDEYcA85XSnM51G8bguFIWE8LL7AMCVc0/edit#gid=0",inline=True)
	em1.set_footer(text="Il est possible que les nouvelles ligne ne soit pas ajouté dans le gdoc !")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def conseil(ctx):
	em1=discord.Embed(
	title="FAQ archero", url="https://docs.google.com/document/d/18ASAbf1qCAAGmrF1LtXOxHaY66n1Rko6Dd4DGrGeoxQ/edit",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Réalisé par Vawaxe ce gdoc est destiné aux débutant qui on besoin de conseil",value="https://docs.google.com/document/d/18ASAbf1qCAAGmrF1LtXOxHaY66n1Rko6Dd4DGrGeoxQ/edit",inline=True)
	em1.set_footer(text="Vous y trouverez une tierlist du meilleur équipement et plein de conseil même utile aux personne plus avancées dans le jeux !")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def skin(ctx):
	em1=discord.Embed(
	title="Voici un document qui vous donnera le prix de tout les skins",url="https://docs.google.com/spreadsheets/d/1EcvyN2NGT3k8hDrIk14CsUmyILzMDOJidKKEDDB2dSU/edit#gid=0",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Vous y trouverez tous les skins avec leurs prix et leurs boost",value="https://docs.google.com/spreadsheets/d/1EcvyN2NGT3k8hDrIk14CsUmyILzMDOJidKKEDDB2dSU/edit#gid=0",inline=True)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def oeufs_level(ctx):
	em1=discord.Embed(
	title="Voici le nombre d'oeufs à avoir pour monter l'étoile d'un mob boss :", url="https://docs.google.com/spreadsheets/d/1EcvyN2NGT3k8hDrIk14CsUmyILzMDOJidKKEDDB2dSU/edit#gid=0",description = "Il en faut 42 en tout pour monter un oeufs lvl10 et 86 pour le monter lvl15!",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="L'oeuf pour débloquer le mob/boss n'est pas pris en compte",value="1 :star: = 1 oeuf \n 2 :star: = 1  oeuf \n 3 :star: = 2 oeufs \n 4 :star: = 2 oeufs \n 5 :star: = 3 oeufs \n 6 :star: = 4 oeufs \n 7 :star: = 5 oeufs \n 8 :star: = 6 oeufs \n 9 :star: = 8 oeufs \n 10 :star: = 10 oeufs\n 11 :star: = 15 oeufs\n 12 :star: = 4 oeufs\n 13 :star: = 6 oeufs\n 14 :star: = 8 oeufs\n 15 :star: = 12 oeufs",inline=True)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def laby_guide(ctx):
	em1=discord.Embed(
	title="Voici comment marche l'event Labyrinthe",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Voici la signification de chaque couleur des portails dans le laby ",value="https://discord.com/channels/504559824617603082/607110270250385418/888317966574313502",inline=False)
	em1.add_field(name="Et là c'est le pattern à suivre pour rendre le laby plus facile car il suffit juste de prendre un maximum de portail orange et violet",value="https://media.discordapp.net/attachments/745978877691822133/1037382160790851604/MazePaths.png?width=570&height=670",inline=False)
	em1.set_footer(text="Comment le lire: \nPar exemple sur la ligne 0️⃣4️⃣🔵 semaine 1 : vous devriez prendre le portail bleu à la 4ème salle.\n⚪ = Any Portal\n🟠 = Orange Portal\n🟢 = Green Portal\n🔵 = Blue Portal\n🟣 = Purple Portal")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def pvp(ctx):
	em1=discord.Embed(
	title="Si vous cherchez à savoir comment marche le PvP, ce document est fait pour vous !",url = "https://docs.google.com/spreadsheets/d/1gZsuhfJR6LzpLxlC8Kj40aeRKn9LeEPjC63whaj_Cts/edit#gid=0",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Vous y trouverez comment marche le système de groupe",value="https://docs.google.com/spreadsheets/d/1gZsuhfJR6LzpLxlC8Kj40aeRKn9LeEPjC63whaj_Cts/edit#gid=0",inline=False)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def sylvan_command(ctx):
	em1=discord.Embed(
	title="Voici les commandes de Sylvan",url = "", description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Prix Upgrade Item  (de 0 à 120)",value="Sylvan item cost ?? to ??",inline=False)
	em1.add_field(name="Prix Upgrade Héros (de 0 à 110)",value="Sylvan hero cost ?? to ??",inline=False)
	em1.add_field(name="Prix Upgrade talent (de 0 à 193)",value="Sylvan talent cost ?? to ??",inline=False)
	em1.add_field(name="Stats item",value="Sylvan + nom de l'item en anglais",inline=False)
	em1.set_footer(text="Vous pouvez aussi rejoindre ce Serveur :https://discord.gg/eAqZquTF6X \n puis aller dans le channel <#670976125014638593>")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def stuff_pvp(ctx):
	em1=discord.Embed(
	title="",url = "",description = "",color=0xFF5733)
	em1.set_image(url = "https://cdn.discordapp.com/attachments/607110270250385418/889796930023088128/tierlist_pvp.png")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def abreviation(ctx):
	em1=discord.Embed(
	title="Voici toutes les Abréviation que l'on utilise souvent",url = "",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Liste des Abréviations",value="PDS = pierre de sang\nQR = QuickRaid \nRdG = Royaume de Glace \nCdG = Contrat de géant \nDBR= demon blade rain \nAoC = Art du Combat \nALE = Ancient Legendary \nLeg = Legendary \nES = épique splendide \nHm = héroic mode \nNm = Normal mode \nStaff = Bâton du harceleur \ncac = corps à corps\nPVP = player versus player \nPVE = player versus environment",inline=False)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def boost_heros(ctx):
	em1=discord.Embed(
	title="Voici tout les boost passif que donne les héros",url = "",description = "",color=0xFF5733)
	em1.set_image(url = "https://cdn.discordapp.com/attachments/624522840783192074/899356977422041198/unknown.png")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def offre_item(ctx):
	em1=discord.Embed(
	title="Merci Lovii pour cette astuce :yum:",url = "",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Préparez la :credit_card:",value="Faut être sûr que la dernière offre ait plus de 24h. \nMettre son perso à poil avec juste l'item voulu (avoir 2 items de même rareté). \nBien kill le jeu. \nEn ouvrant, aller fusionner. \nSi ça ne marche pas, prendre l'autre item et refusionner \nEt si ça ne fonctionne toujours pas, réinstaller le jeu \nLa première action du jeu définit l'offre que vous allez obtenir (golds, runes...)",inline=False)
	em1.set_footer(text="Spoiler : Oui c'est un glitch mais vu que ça touche à l'argent bah on dit rien xD")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def stuff_pve(ctx):
	em1=discord.Embed(
	title="Voici une tierlist des items ALE",url = "",description = "",color=0xFF5733)
	em1.set_image(url = "https://media.discordapp.net/attachments/1018889785571540994/1021890519875469442/General-Tier-List_1.png?width=1082&height=754")
	em2=discord.Embed(
	title="Voici une tierlist des items Mythic",url = "",description = "",color=0xFF5733)
	em2.set_image(url = "https://media.discordapp.net/attachments/1018889785571540994/1021890520420716665/Mythic-Tier-List_1.png?width=1082&height=754")
	if (ctx.channel.id in channel_command):
		await ctx.channel.send(embed=em1,view=SelectView())
		await ctx.channel.send(embed=em2)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def shards_evo(ctx):
	em1=discord.Embed(
	title="",url = "",description = "",color=0xFF5733)
	em1.set_image(url = "https://cdn.discordapp.com/attachments/607110270250385418/939878194507563048/InShot_20220206_143932779.jpg")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1,view=SelectView())
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def joyaux_fusion(ctx):
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send("https://cdn.discordapp.com/attachments/604720918182232074/892118488175489064/unknown.png")
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def heros_laby(ctx):
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send("https://cdn.discordapp.com/attachments/607110270250385418/847431973244108810/image0.png")
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def stuff_fusion(ctx):
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send("https://media.discordapp.net/attachments/889452351587495948/927346154289655869/Screenshot_20220103-004121.jpg")
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def stats_joyaux(ctx):
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send("https://cdn.discordapp.com/attachments/607110270250385418/918104338289786880/jewles_landerz.png")
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@TheHelper.command()
async def discord_archero(ctx):
	if (ctx.channel.id in channel_command): 
			await ctx.channel.send("Voici le lien qui permet de rejoindre le discord officiel pas très officiel, car l'admin du discord n'est rien d'autre qu'un ancien dévelopeur de HABBY : https://discord.gg/d7w6FxhHjj")
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()


TheHelper.run(TOKENH)