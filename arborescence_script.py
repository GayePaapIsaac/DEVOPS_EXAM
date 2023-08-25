

from pathlib import Path

def mon_arbre(dossier_parent):
       #dossier parent 
       parent=[f"{dossier_parent}"]
       directories=[str(parent[0])+"/data/raw", str(parent[0])+"/data/cleaned", str(parent[0])+"/docs",
              str(parent[0])+"/models", str(parent[0])+"/notebooks", str(parent[0])+"/reports",
              str(parent[0])+"/src"]

       files=[str(parent[0])+'/LICENCE',str(parent[0])+'/Makefile',str(parent[0])+'/README.md',str(parent[0])+'/.gitignore',
              str(parent[0])+'/requierement.txt', str(directories[-1]+'/utils.py')]

       list(map(lambda x: Path(x).mkdir(parents=True,exist_ok=True),parent))
       list(map(lambda x:Path(x).mkdir(parents=True,exist_ok=True),directories))
       list(map(lambda x:Path(x).touch(exist_ok=True),files))










