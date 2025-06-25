# meme_dict
#Dicccionario_1
meme_dict = {
    "CRINGE": "Algo excepcionalmente rar o embarazozo",
    "LOL": "Una respuesta a algo gracioso",
    "ROLF": "Una respuesta a una broma",
    "SHEESH":"Ligera desaprobación",
    "CREEPY":"Aterrador, siniestro",
    "AGGRO":"Ponerse agresivo/enojado"
}
    

while TRUE:
    word=input("Escribe una palabra que no entiendas (Usa mayusculas)")
    if word in meme_dict:
        print(meme_dict[word])
    elif word not in meme_dict and word!="fin":
        print("Aun no tenemos esa palabra... La agregaremos pronto")
    if word =="fin":
        break
