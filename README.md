***
# Information générale:
Ce programme vise extraire les donnée sur le site de vente de de livre (http://books.toscrape.com/) dans le cadre d'une analyse de marché.<br/>
Il s'agit d'un programme essentiellement élaboré en laguage python et qui est exécutable à la demande dans le but de recupérer certaines information sur des livres au moment de son exécution.

### Nom du projet: 
Analyse de marché avec Python.

### Auteur. 
AS-Patrice
### Date de création. 	
Févier 2021
### Description.
Il est organisé autour de quatre principales fonctions: <br/>
-la première "get-product-info" visite la page de chaque livre pour y extraire les informations préalablement sélectionnées sur le livre: titre du livre, prix, url du livre, description...<br/>
-La seconde "get_category_info" parcours toutes les pages de catégorie des livres avec prise en compte de la paginnation et y extrait l'url de chaque livre. Cet url est ensuite envoyés à la fonction "get_product_info".<br/>
-La fonction "save_product_info" se charge de recupérer toutes les informations extraites sur chaque page de livre  et les stocke dans des fichiers correspondants.<br/>Ces fichier ainsi que les images de chaque livre sont enregistrés dans un dossier(dossier fille) qui porte le nom de la catégorie concernée. L'ensemble des dossier est rangé dans un dossier appelé catégories(dossier parent).<br/>
-Enfin, la fonction "get_all_category" récupère les urls des différentes catégories.Ces urls sont ensuite envoyés à la fonction "get_category_info".<br/>
***

# Technologie utilisée:

Les programme est entièrement écrit en language Python.

# Exécution:

** Pour son exécution, il est necessaire de créer et activer l'environnement virtuel. Le fichier requirement.txt liste l'ensemble des modules installés. En plus de ces modules, il est necessaire d'importer certains modules telques:<br/>
	-Os: pour la gestion des dossier et des fichiers<br/>
	-re: pour les expression régulière (au niveau de la nomination de chaque image)<br/>
	-csv: pour la gestion des fichiers.csv<br/>
** Le lancement du programme se fait en ligne de commande à partir d'un terminal python.

***
