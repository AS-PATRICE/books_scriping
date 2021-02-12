# Book Scraping: Analyse de marché avec Python.

# Information générale:
Ce programme extrait les données sur le site de vente de livre (http://books.toscrape.com/) dans le cadre d'une analyse de marché.<br/>
Il est essentiellement élaboré en laguage python qui s'exécute à la demande et qui recupérer certaines informations sur des livres au moment de son exécution.
***
# Description.

Le programme s'organise autour de quatre principales méthodes: <br/>
<li>La première "get-product-info" visite la page de chaque livre pour y extraire les informations préalablement sélectionnées sur le livre: titre du livre, prix, url du livre, description, etc.<br/>
<li>La seconde "get_category_info" parcours toutes les pages de catégorie des livres avec prise en compte de la paginnation et y extrait l'url de chaque livre. Cet url est ensuite envoyés à la fonction "get_product_info".<br/>
<li>La fonction "get_all_category" récupère les urls des différentes catégories.Ces urls sont ensuite envoyés à la fonction "get_category_info".<br/>
<li>Enfin, la fonction "save_product_info" se charge de recupérer toutes les informations extraites sur chaque page de livre  et de les stocker dans des fichiers.csv correspondants.<br/>Ces fichier ainsi que l'image de chaque livre sont enregistrés dans un dossier(dossier fille) qui porte le nom de la catégorie concernée. L'ensemble des dossiers est rangé dans un dossier appelé Catégories(dossier parent).<br/>

***
# Technologie utilisée:

Les programme est entièrement écrit en language Python.

***
# Exécution:

** Pour son exécution, il est necessaire de créer et d'activer l'environnement virtuel. Le fichier requirement.txt liste l'ensemble des modules utiles au bon fonctionnement du script. En plus de ces modules, il est faut importer certains modules tels que:<br/>
	<li>os: pour la gestion des dossier et des fichiers<br/>
	<li>re: pour les expression régulière (au niveau de la nomination de chaque image)<br/>
	<li>csv: pour la gestion des fichiers.csv<br/>
** Le lancement du programme se fait en ligne de commande à partir d'un terminal python.

***
