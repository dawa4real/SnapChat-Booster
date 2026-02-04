import webbrowser
import os
import platform
import subprocess


k_URL_DISCORD = "https://discord.gg/GCgz35fH"
k_URL_GITHUB = "https://github.com/dawa4real/SnapChat-Booster"
k_NOM_IMAGE = "Star.gif"

def ouvrir_ressources():
    print(f"Ouverture de Discord...")
    webbrowser.open(k_URL_DISCORD)
    webbrowser.open(k_URL_GITHUB)
    
    if os.path.exists(k_NOM_IMAGE):
        print(f"Ouverture de l'image {k_NOM_IMAGE}...")
        
        if platform.system() == "Windows":
            os.startfile(k_NOM_IMAGE)
        elif platform.system() == "Darwin":
            subprocess.call(["open", k_NOM_IMAGE])
        else: 
            subprocess.call(["xdg-open", k_NOM_IMAGE])
    else:
        print(f"Erreur : Le fichier {k_NOM_IMAGE} est introuvable dans le dossier du script.")

if __name__ == "__main__":
    ouvrir_ressources()
