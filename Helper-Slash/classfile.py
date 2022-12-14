import discord 
from discord.ext import commands

class Select(discord.ui.Select):
		def __init__(self):
				options=[
						discord.SelectOption(value="Option 0",label="Help Command",description="?help"),
						discord.SelectOption(value="Option 1",label="Calculateur de Stats",description="?boost_heros"),
						discord.SelectOption(value="Option 2",label="Bugs du jeux",description="?glitch"),
						discord.SelectOption(value="Option 3",label="Le Glitch...",description="?talent"),
						discord.SelectOption(value="Option 4",label="Arbre de Talents",description="?qr"),
						discord.SelectOption(value="Option 5",label="Tableau des QuickRaid",description="?all_tierlist"),
						discord.SelectOption(value="Option 6",label="Toutes les TierLists",description="?doc_oeufs"),
						discord.SelectOption(value="Option 7",label="Document des oeufs",description="?runes_effect"),
						discord.SelectOption(value="Option 8",label="Tuto installer une apk",description="?conseil"),
						discord.SelectOption(value="Option 9",label="Description des Skills",description="?skin"),
						discord.SelectOption(value="Option 10",label="Toutes les runes",description="?level_egg"),
						discord.SelectOption(value="Option 11",label="Guide Labyrinthe",description="?guide_laby"),
						discord.SelectOption(value="Option 12",label="Rentabilit√©/Prix des skin",description="?pvp"),
						discord.SelectOption(value="Option 13",label="Nombre d'oeufs pour les levels",description="?stats_calc"),
						discord.SelectOption(value="Option 14",label="Guide pour le laby",description="?sylvan_command"),
						discord.SelectOption(value="Option 15",label="Fonctionnement du PvP",description="?stuff_pvp"),
						discord.SelectOption(value="Option 16",label="Commande pour classement discord",description="?abreviation"),
						discord.SelectOption(value="Option 17",label="Commandes du bot Sylvan",description="?offre_item"),
						discord.SelectOption(value="Option 18",label="TierList stuff PvP",description="?stuff_pve1"),
						discord.SelectOption(value="Option 19",label="Toutes les abr√©viations ",description="?stuff_pve2"),
						discord.SelectOption(value="Option 20",label="Tous les boosts des H√©ros",description="?shards_evo"),
						discord.SelectOption(value="Option 21",label="Conseil pour tout le monde",description="?conseil"),
						]
				super().__init__(placeholder="Clique ici pour choisir une autre commande ",max_values=1,min_values=1,options=options)
		async def callback(self, interaction: discord.Interaction):
			#0#########ERROR / HELP#######################
			help=discord.Embed(
			title="Voici toutes les commandes propos√©es :",description = "",color=0xFF5733)
			help.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			help.add_field(name="Commandes",value="?heros_laby \n?discord_archero \n?sylvan_command \n?abreviation \n?pvp \n?qr \n?stuff_pve \n?stuff_pvp \n?laby_guide \n?conseil \n?oeufs_level \n?talent \n?doc_oeufs \n?stats_calc", inline= True)
			help.add_field(name="Commandes",value="?stats_joyaux \n?stuff_fusion \n?joyaux_fusion \n?rune_effect \n?offre_item \n?index_archive \n?skin \n?all_tierlist \n?shards_evo \n?tuto_apk \n?archero_compilation \n?glitch \n?boost_heros \n?rank_help",inline=True)
			#1#########BOOST HEROS#######################
			boost_heros=discord.Embed(
			title="Voici tout les boost passif que donne les h√©ros",url = "",description = "",color=0xFF5733)
			boost_heros.set_image(url = "https://cdn.discordapp.com/attachments/624522840783192074/899356977422041198/unknown.png")
			#2##########GLITCH##########################
			glitch=discord.Embed(
			title="PAS DE GLITCH DANS CE SERVEUR",url="https://www.youtube.com/channel/UCJoV9pAMDRvD70JV7iLwA2g",description = "C'est sujet qui peut aboutir √† un ban du serveur",color=0xFF5733)
			glitch.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			glitch.add_field(name="D√©finition Glitch :",value="A partir du moment o√Ļ tu influes sur le jeu de mani√®re anormal par un kill de l'app, ou autre, c'est du glitch, donc pas autoris√© ici.", inline=False)
			glitch.add_field(name="C'est √©crit dans le r√®glement",value="donc pas d'excuses", inline=False)
			glitch.set_footer(text="Si vous voulez en parler c'est en message priv√© !")
			#3##########TALENT TREE#####################
			talent_tree=discord.Embed(
			title="Talent Tree",url="https://docs.google.com/spreadsheets/d/1Wu5yNEMrnoTGimhS5a2qfKHuZvHSRXyxLhkbok3nTX0/edit#gid=0",description = "",color=0xFF5733)
			talent_tree.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			talent_tree.add_field(name="Voici le lien qui vous m√®nera au gsheet",value="https://docs.google.com/spreadsheets/d/1Wu5yNEMrnoTGimhS5a2qfKHuZvHSRXyxLhkbok3nTX0/edit#gid=0", inline=False)
			talent_tree.add_field(name=":warning: ATTENTION LES NOUVEAUX TALENTS SONT VALABLES QUE POUR CEUX QUI AVAIS FINIS LES TALENTS AVANT LA MAJ DES RUNES  ",value="https://docs.google.com/spreadsheets/d/1IHrFHEIuuCGkgt1c39jrtsscZhNcFLCxKzdROl1EktM/edit?usp=sharing", inline=False)
			#4##########QR##############################
			qr=discord.Embed(
			title="Voici le gsheet qui donne acc√®s au tableau de QuickRaid",url="https://docs.google.com/spreadsheets/d/1gI3lxMxjVT3iLb-71kyNrAGE8a4rhAp_tSo7IDwNm3w/edit#gid=808920507",description = "",color=0xFF5733)
			qr.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			qr.add_field(name="QR (Raid √©clair)",value="https://docs.google.com/spreadsheets/d/1gI3lxMxjVT3iLb-71kyNrAGE8a4rhAp_tSo7IDwNm3w/edit#gid=808920507",inline=True)
			#5##########ALL-TIERLIST####################
			all_tierlist=discord.Embed(
			title="Voici le gsheet qui donne acc√®s aux TierList",url="https://docs.google.com/spreadsheets/d/1vm2xlsrUYbgXDYP7lmh60I4CBWkTLKA5YBhzrY-t0Tw/edit#gid=380709681",description = "",color=0xFF5733)
			all_tierlist.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			all_tierlist.add_field(name="Tierlist stuff PvP et PvE, et une TierList skill en Endless ",value="https://docs.google.com/spreadsheets/d/1vm2xlsrUYbgXDYP7lmh60I4CBWkTLKA5YBhzrY-t0Tw/edit#gid=380709681",inline=True)
			all_tierlist.set_footer(text="Attention !!! Il faut parfois savoir faire preuve de bon sens, donc ne prenez pas cette tierlist aux pieds de la lettre")
			#6##########DOC-OEUFS######################
			doc_oeufs=discord.Embed(
			title="Archero info Couveuse", url="https://docs.google.com/spreadsheets/d/1bfq-F1BoT3FO-Nerg7KFn3jE5IMy768uokjLN5b7WCw/edit#gid=1801182798",description = "",color=0xFF5733)
			doc_oeufs.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			doc_oeufs.add_field(name="R√©alis√© par LuhCaran & Doodam's1402 vous y trouverez les stats de tout les mob/boss mais aussi rapidement trouver dans quel chapitre il se situe .",value="https://docs.google.com/spreadsheets/d/1bfq-F1BoT3FO-Nerg7KFn3jE5IMy768uokjLN5b7WCw/edit#gid=1801182798",inline=True)
			doc_oeufs.add_field(name="Tr√®s pratique !",value="Vous retrouverez toutes les infos concernant les oeufs de niveau 0 et vous pouvez aussi trouver les stats √† chaque niveau dans l'onglet 'Stats Compl√®te'",inline=True)
			#7##########RUNES-EFFECT###################
			runes_effect=discord.Embed(
			title="Voici un gdoc dans lequel vous trouverez chaque ligne de runes disponible", url="https://docs.google.com/spreadsheets/d/1Y2C0yY-Ht5XDEYcA85XSnM51G8bguFIWE8LL7AMCVc0/edit#gid=0",description = "",color=0xFF5733)
			runes_effect.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			runes_effect.add_field(name="R√©alis√© par Chaos (un mec du discord officiel)",value="https://docs.google.com/spreadsheets/d/1Y2C0yY-Ht5XDEYcA85XSnM51G8bguFIWE8LL7AMCVc0/edit#gid=0",inline=True)
			runes_effect.set_footer(text="Il est possible que les nouvelles ligne ne soit pas ajout√© dans le gdoc !")
			#8##########CONSEIL########################
			conseil=discord.Embed(
			title="FAQ archero", url="https://docs.google.com/document/d/18ASAbf1qCAAGmrF1LtXOxHaY66n1Rko6Dd4DGrGeoxQ/edit",description = "",color=0xFF5733)
			conseil.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			conseil.add_field(name="R√©alis√© par Vawaxe ce gdoc est destin√© aux d√©butant qui on besoin de conseil",value="https://docs.google.com/document/d/18ASAbf1qCAAGmrF1LtXOxHaY66n1Rko6Dd4DGrGeoxQ/edit",inline=True)
			conseil.set_footer(text="Vous y trouverez une tierlist du meilleur √©quipement et plein de conseil m√™me utile aux personne plus avanc√©es dans le jeux !")
			#9##########SKIN###########################
			skin=discord.Embed(
			title="Voici un document qui vous donnera le prix de tout les skins",url="https://docs.google.com/spreadsheets/d/1EcvyN2NGT3k8hDrIk14CsUmyILzMDOJidKKEDDB2dSU/edit#gid=0",description = "",color=0xFF5733)
			skin.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			skin.add_field(name="Vous y trouverez tous les skins avec leurs prix et leurs boost",value="https://docs.google.com/spreadsheets/d/1EcvyN2NGT3k8hDrIk14CsUmyILzMDOJidKKEDDB2dSU/edit#gid=0",inline=True)
			#10##########OEUFS-LEVEL####################
			level_egg=discord.Embed(
			title="Voici le nombre d'oeufs √† avoir pour monter l'√©toile d'un mob boss :", url="https://docs.google.com/spreadsheets/d/1EcvyN2NGT3k8hDrIk14CsUmyILzMDOJidKKEDDB2dSU/edit#gid=0",description = "Il en faut 42 en tout pour monter un oeufs lvl10 et 86 pour le monter lvl15!",color=0xFF5733)
			level_egg.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			level_egg.add_field(name="L'oeuf pour d√©bloquer le mob/boss n'est pas pris en compte",value="1 :star: = 1 oeuf \n 2 :star: = 1  oeuf \n 3 :star: = 2 oeufs \n 4 :star: = 2 oeufs \n 5 :star: = 3 oeufs \n 6 :star: = 4 oeufs \n 7 :star: = 5 oeufs \n 8 :star: = 6 oeufs \n 9 :star: = 8 oeufs \n 10 :star: = 10 oeufs\n 11 :star: = 15 oeufs\n 12 :star: = 4 oeufs\n 13 :star: = 6 oeufs\n 14 :star: = 8 oeufs\n 15 :star: = 12 oeufs",inline=True)
			#11##########LABY-GUIDES###################
			guide_laby=discord.Embed(
			title="Voici comment marche l'event Labyrinthe",description = "",color=0xFF5733)
			guide_laby.add_field(name="Voici la signification de chaque couleur des portails dans le laby ",value="https://discord.com/channels/504559824617603082/607110270250385418/888317966574313502",inline=False)
			guide_laby.add_field(name="Et l√† c'est le pattern √† suivre pour rendre le laby plus facile car il suffit juste de prendre un maximum de portail orange et violet",value="https://media.discordapp.net/attachments/745978877691822133/1037382160790851604/MazePaths.png?width=570&height=670",inline=False)
			guide_laby.set_footer(text="Comment le lire: \nPar exemple sur la ligne 0ÔłŹ‚É£4ÔłŹ‚É£ūüĒĶ semaine 1 : vous devriez prendre le portail bleu √† la 4√®me salle.\n‚ö™ = Any Portal\nūüü† = Orange Portal\nūüüĘ = Green Portal\nūüĒĶ = Blue Portal\nūüü£ = Purple Portal")
			#12#########PVP#############################
			pvp=discord.Embed(
			title="Si vous cherchez √† savoir comment marche le PvP, ce document est fait pour vous !",url = "https://docs.google.com/spreadsheets/d/1gZsuhfJR6LzpLxlC8Kj40aeRKn9LeEPjC63whaj_Cts/edit#gid=0",description = "",color=0xFF5733)
			pvp.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			pvp.add_field(name="Vous y trouverez comment marche le syst√®me de groupe",value="https://docs.google.com/spreadsheets/d/1gZsuhfJR6LzpLxlC8Kj40aeRKn9LeEPjC63whaj_Cts/edit#gid=0",inline=False)
			#13##########STATS CALC##############
			stats_calc=discord.Embed(
			title="Calculateur de Stats Version Updated",description = "",color=0xFF5733)
			stats_calc.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			stats_calc.add_field(name='Stats Calculator',value="https://docs.google.com/spreadsheets/d/1NIfusyFcHqo-UzhGGpro03AxfXLXZFd1AIsOYGcP9zU/edit?usp=sharing ", inline= True)
			stats_calc.add_field(name=" Petite indication :",value="2 choses importantes : \n-Si vous rencontrer un bug/trop gros √©cart de valeurs veuillez me Mp \n-Il faut aussi savoir qu'a chaque Mise √† jour du jeux il faudra re-remplir les valeurs sauf si vous souhaiter garder la version non-update", inline= True)
			#14##########SYLVAN COMMAND#################
			sylvan_command=discord.Embed(
			title="Voici les commandes de Sylvan",url = "", description = "",color=0xFF5733)
			sylvan_command.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			sylvan_command.add_field(name="Prix Upgrade Item  (de 0 √† 120)",value="Sylvan item cost ?? to ??",inline=False)
			sylvan_command.add_field(name="Prix Upgrade H√©ros (de 0 √† 110)",value="Sylvan hero cost ?? to ??",inline=False)
			sylvan_command.add_field(name="Prix Upgrade talent (de 0 √† 193)",value="Sylvan talent cost ?? to ??",inline=False)
			sylvan_command.add_field(name="Stats item",value="Sylvan + nom de l'item en anglais",inline=False)
			sylvan_command.set_footer(text="Vous pouvez aussi rejoindre ce Serveur :https://discord.gg/eAqZquTF6X \n puis aller dans le channel <#670976125014638593>")
			#15##########STUFF PVP######################
			stuff_pvp=discord.Embed(
			title="",url = "",description = "",color=0xFF5733)
			stuff_pvp.set_image(url = "https://cdn.discordapp.com/attachments/607110270250385418/889796930023088128/tierlist_pvp.png")
			#16##########ABBREVIATION###################
			abreviation=discord.Embed(
			title="Voici toutes les Abr√©viation que l'on utilise souvent",url = "",description = "",color=0xFF5733)
			abreviation.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			abreviation.add_field(name="Liste des Abr√©viations",value="PDS = pierre de sang\nQR = QuickRaid \nRdG = Royaume de Glace \nCdG = Contrat de g√©ant \nDBR= demon blade rain \nAoC = Art du Combat \nALE = Ancient Legendary \nLeg = Legendary \nES = √©pique splendide \nHm = h√©roic mode \nNm = Normal mode \nStaff = B√Ęton du harceleur \ncac = corps √† corps\nPVP = player versus player \nPVE = player versus environment",inline=False)
			#17##########OFFRE ITEM#####################
			offre_item=discord.Embed(
			title="Merci Lovii pour cette astuce :yum:",url = "",description = "",color=0xFF5733)
			offre_item.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			offre_item.add_field(name="Pr√©parez la :credit_card:",value="Faut √™tre s√Ľr que la derni√®re offre ait plus de 24h. \nMettre son perso √† poil avec juste l'item voulu (avoir 2 items de m√™me raret√©). \nBien kill le jeu. \nEn ouvrant, aller fusionner. \nSi √ßa ne marche pas, prendre l'autre item et refusionner \nEt si √ßa ne fonctionne toujours pas, r√©installer le jeu \nLa premi√®re action du jeu d√©finit l'offre que vous allez obtenir (golds, runes...)",inline=False)
			offre_item.set_footer(text="Spoiler : Oui c'est un glitch mais vu que √ßa touche √† l'argent bah on dit rien xD")
			#18##########STUFF PVE 1####################
			stuff_pve1=discord.Embed(
			title="Voici une tierlist des items ALE",url = "",description = "",color=0xFF5733)
			stuff_pve1.set_image(url = "https://cdn.discordapp.com/attachments/889452351587495948/1009518971847975023/unknown.png")
			#19##########STUFF PVE 2####################
			stuff_pve2=discord.Embed(
			title="Voici une tierlist des items Mythic",url = "",description = "",color=0xFF5733)
			stuff_pve2.set_image(url = "https://cdn.discordapp.com/attachments/889452351587495948/1009536113301524490/unknown.png")
			#20##########SHARDS EVO#####################
			shards_evo=discord.Embed(
			title="",url = "",description = "",color=0xFF5733)
			shards_evo.set_image(url = "https://cdn.discordapp.com/attachments/607110270250385418/939878194507563048/InShot_20220206_143932779.jpg")
			#20##########CONSEIL#####################
			conseil=discord.Embed(
			title="FAQ archero", url="https://docs.google.com/document/d/18ASAbf1qCAAGmrF1LtXOxHaY66n1Rko6Dd4DGrGeoxQ/edit",description = "",color=0xFF5733)
			conseil.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			conseil.add_field(name="R√©alis√© par Vawaxe ce gdoc est destin√© aux d√©butant qui on besoin de conseil",value="https://docs.google.com/document/d/18ASAbf1qCAAGmrF1LtXOxHaY66n1Rko6Dd4DGrGeoxQ/edit",inline=True)
			conseil.set_footer(text="Vous y trouverez une tierlist du meilleur √©quipement et plein de conseil m√™me utile aux personne plus avanc√©es dans le jeux !")
			
			


			if self.values[0] == "Option 1":
				await interaction.response.edit_message(embed=boost_heros)
			elif self.values[0] == "Option 2":
				await interaction.response.edit_message(embed=glitch)
			elif self.values[0] == "Option 3":
				await interaction.response.edit_message(embed=talent_tree)
			elif self.values[0] == "Option 4":
				await interaction.response.edit_message(embed=qr)
			elif self.values[0] == "Option 5":
				await interaction.response.edit_message(embed=all_tierlist)
			elif self.values[0] == "Option 6":
				await interaction.response.edit_message(embed=doc_oeufs)
			elif self.values[0] == "Option 7":
				await interaction.response.edit_message(embed=runes_effect)
			elif self.values[0] == "Option 8":
				await interaction.response.edit_message(embed=conseil)
			elif self.values[0] == "Option 9":
				await interaction.response.edit_message(embed=skin)
			elif self.values[0] == "Option 10":
				await interaction.response.edit_message(embed=level_egg)
			elif self.values[0] == "Option 11":
				await interaction.response.edit_message(embed=guide_laby)
			elif self.values[0] == "Option 12":
				await interaction.response.edit_message(embed=pvp)
			elif self.values[0] == "Option 13":
				await interaction.response.edit_message(embed=stats_calc)
			elif self.values[0] == "Option 14":
				await interaction.response.edit_message(embed=sylvan_command)
			elif self.values[0] == "Option 15":
				await interaction.response.edit_message(embed=stuff_pvp)
			elif self.values[0] == "Option 16":
				await interaction.response.edit_message(embed=abreviation)
			elif self.values[0] == "Option 17":
				await interaction.response.edit_message(embed=offre_item)
			elif self.values[0] == "Option 18":
				await interaction.response.edit_message(embed=stuff_pve1)
			elif self.values[0] == "Option 19":
				await interaction.response.edit_message(embed=stuff_pve2)
			elif self.values[0] == "Option 20":
				await interaction.response.edit_message(embed=shards_evo)
			elif self.values[0] == "Option 21":
				await interaction.response.edit_message(embed=conseil)
			else:
				await interaction.response.edit_message(embed=help)

class SelectView(discord.ui.View):
	def __init__(self, *, timeout = None):
		super().__init__(timeout=timeout)
		self.add_item(Select())