import os
#os.system : pour faire du bash
#os.remove :une fonction de l'os

"""
# dans ce cas il lance tous les scripts
scripts_to_run = [
    "python call_externe.py",
    "rm -r test"
]

for script in scripts_to_run:
    os.system(script)
# print(os.system("python ~/Documents/projects/pierreIrisDetection/IrisDetection/detection.py"))
"""


'''
permet:
    d'executer plusieurs commandes
    de s'arrêter lorsqu'une commande plante
    de reprendre à ladite commande lorsqu'on relance rename_images.py
'''

def app():
    LOG_NAME = "~LOG.txt"
    starting_index = 0

    try:
        log_file = open(LOG_NAME, "r")

        print("Le script a planté la dernière fois que vous l'avez lancé. \
        Voulez-vous reprendre là où vous en étiez?")
        answer = input("(Type y/N)")

        if answer.lower() == 'y':
            data = log_file.read()
            starting_index = int(data)
            log_file.close()
            os.remove(LOG_NAME)
            print("Reprise à partir de la "+str(starting_index)+"{rank} \
            commande".format(rank = "ère" if starting_index == 1 else "ème"))

    except FileNotFoundError:
        pass

    scripts_to_run = [
        "python --version",
        "python call_externe.py",
        "rm -r test"
    ]

    for i in range (starting_index, len(scripts_to_run)):
        script = scripts_to_run[i]
        if (os.system(script) != 0) :
            print("Une erreur est survenue, script arrêté subitement")

            log_file = open(LOG_NAME, "w")
            log_file.write(str(i))
            log_file.close()
            break


if __name__ == "__main__":
    app()
