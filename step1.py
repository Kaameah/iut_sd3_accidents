import pandas as pd
import os

# Dossier contenant les fichiers CSV
dossier_data = 'data'

# Liste des noms de fichiers CSV à fusionner
noms_fichiers = ['carac.csv', 'lieux.csv', 'veh.csv', 'vict.csv']

# Nouveau dossier pour enregistrer le fichier fusionné
nouveau_dossier = 'step1'

# Assurez-vous que le nouveau dossier existe, sinon créez-le
if not os.path.exists(nouveau_dossier):
    os.makedirs(nouveau_dossier)

# Initialisez un DataFrame vide pour stocker les données fusionnées
df_fusion = pd.DataFrame()

# Parcourez la liste des fichiers CSV et fusionnez-les
for fichier in noms_fichiers:
    chemin_fichier = os.path.join(dossier_data, fichier)
    if os.path.exists(chemin_fichier):
        df_temp = pd.read_csv(chemin_fichier, sep = ';')  # Assurez-vous de spécifier l'encodage correct
        df_fusion = pd.concat([df_fusion, df_temp], ignore_index=True)

# Enregistrez le DataFrame fusionné dans un nouveau fichier CSV
chemin_fusion_csv = os.path.join(nouveau_dossier, 'merged_data.csv')
df_fusion.to_csv(chemin_fusion_csv, index=False, sep=';')  # Assurez-vous de spécifier l'encodage correct
