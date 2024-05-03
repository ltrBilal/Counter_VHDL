# Counter_VHDL
Ce projet propose une solution automatisée pour la génération de code VHDL et de son test bench afin de créer un compteur de 0 à n. 
En ajustant les paramètres dans le fichier [generate_VHDL.py](generate_VHDL.py), vous pouvez définir la limite supérieure du compteur selon vos besoins. 

Une fois ces valeurs définies, exécutez simplement le script Python generate_VHDL.py pour générer le code VHDL correspondant. 

Le script lance ensuite une simulation et compare les résultats obtenus avec les valeurs attendues, enregistrant les résultats de la simulation dans [output_file.txt](./output_file.txt) et les valeurs attendues dans [expected_file.txt](./expected_file.txt). 

Il convient de noter que les résultats attendus sont générés automatiquement à l'aide du script [expected_results.py](./expected_results.py), qui est également lancé par le script [generate_VHDL.py](./generate_VHDL.py).

Outils nécessaires:

  [GHDL](https://github.com/ghdl/ghdl) : Un outil open-source pour la simulation et la synthèse du VHDL.
  
  Python
