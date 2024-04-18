import os
import datetime
import logging

# Configurar el sistema de logging
format_logs = '[%(asctime)s] %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=format_logs)

# Afegir un gestor per escriure en un fitxer
gestor_fitxer = logging.FileHandler("recorrido.log")
gestor_fitxer.setLevel(logging.INFO)
gestor_fitxer.setFormatter(logging.Formatter(format_logs))
logging.getLogger('').addHandler(gestor_fitxer)

def recorrer_arbre_directoris(directori):
    try:
        contingut = os.listdir(directori)
    except PermissionError as e:
        logging.error(f'Error de permisos en accedir a {directori}: {e}')
        return

    for element in contingut:
        ruta_element = os.path.join(directori, element)

        if os.path.isdir(ruta_element):
            logging.info(f'Directori: {ruta_element}')
            recorrer_arbre_directoris(ruta_element)
        else:
            try:
                logging.info(f'Fitxer: {ruta_element}')
            except Exception as e:
                logging.error(f'Error en processar {ruta_element}: {e}')

def principal():
    directori_inicial = input("Introdueix la ruta del directori inicial: ")

    if not os.path.isdir(directori_inicial):
        logging.error('El directori especificat no existeix.')
    else:
        logging.info('Recorregut de l\'arbre de directoris:')
        temps_inici = datetime.datetime.now()
        recorrer_arbre_directoris(directori_inicial)
        temps_final = datetime.datetime.now()
        temps_transcorregut = temps_final - temps_inici
        logging.info(f'Temps transcorregut: {temps_transcorregut}')

if __name__ == "__main__":
    principal()