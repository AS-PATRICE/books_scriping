# Book Scraping: Analyse de marché avec Python.

# Information générale:
Ce programme extrait les données sur le site de vente de livre (http://books.toscrape.com/) dans le cadre d'une analyse de marché.<br/>
Essentiellement élaboré en laguage python, il s'exécute à la demande dans le but de recupérer certaines informations sur des livres au moment de son exécution.
***
# Description.

Le programme s'organise autour de quatre principales méthodes: <br/>
<li>La première "get-product-info" visite la page de chaque livre pour y extraire les informations préalablement sélectionnées sur le livre: titre du livre, prix, url du livre, description, etc.<br/>
<li>La seconde "get_category_info" parcours toutes les pages de catégorie des livres avec prise en compte de la paginnation et y extrait l'url de chaque livre. Cet url est ensuite envoyés à la fonction "get_product_info".<br/>
<li>La fonction "get_all_category" récupère les urls des différentes catégories.Ces urls sont ensuite envoyés à la fonction "get_category_info".<br/>
<li>Enfin, la fonction "save_product_info" se charge de recupérer toutes les informations extraites sur chaque page de livre  et de les stocker dans des fichiers.csv correspondants.<br/>Ces fichier ainsi que l'image de chaque livre sont enregistrés dans un dossier(dossier fille) qui porte le nom de la catégorie concernée. Tous les dossiers de catégorie sont rangés dans un dossier principal  appelé Catégories(dossier parent).<br/>

***
# Exécution:

Pour son exécution, il faut dans un premier temps le cloner dans un dépot local. Pour cela il convient de créer un nouveau dossier et d'y accèder en ligne de commande. Ensuite, il faut copier le lien du repository (du code) sur github et revenir dans son terminal taper les deux commandes suivantes pour clonnage: <br/>

<li>git remote add books_scraping https://github.com/AS-PATRICE/books_scriping.git<br/>
<li>git clone https://github.com/AS-PATRICE/books_scriping.git<br/><br/>

Dans un second temps il est necessaire de créer et d'activer l’environnement virtuel.<br/>
<li> On le créer en saisissant ces commandes dans le terminal: "python -m venv env".<br/>
<li> Pour l’activer : "source env/bin/activate".<br/>
<li> il faut installer les modules à partir du fichier requirement.txt avec la commande suivante : "pip install -r requirement.txt"
Pour vérifier si les dépendances sont bien installées on fait "pip freeze" pour voir leur liste.<br/><br/>
	

Pour finir, il convient d'ouvrir le fichier books.py et de l'exéxuter en appuyant sur le bouton run de son IDE.

***
