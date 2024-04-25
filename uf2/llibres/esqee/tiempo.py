import xml.etree.ElementTree as ET
def calcular_dades(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    total_precipitacio = 0
    total_temperatura = 0
    count_precipitacio = 0
    count_temperatura = 0
    for dia in root.iter('dia'):
        for prob_precipitacion in dia.iter('prob_precipitacion'):
            if prob_precipitacion.text is not None:
                total_precipitacio += float(prob_precipitacion.text)
                count_precipitacio += 1
        for temperatura in dia.iter('temperatura'):
            for dato in temperatura.iter('dato'):
                if dato.text is not None:
                    total_temperatura += float(dato.text)
                    count_temperatura += 1

    probabilitat_precipitacio = total_precipitacio / count_precipitacio if count_precipitacio else 0
    temperatura_mitjana = total_temperatura / count_temperatura if count_temperatura else 0
    print(f'Probabilitat de precipitació: {probabilitat_precipitacio}')
    print(f'Temperatura mitjana: {temperatura_mitjana}')
calcular_dades('localidad_17202.xml')