import sys

def help_panel():
    print("Usage :")
    print("python3 vigenere.py 'mensaje' 'key' ")


def identify_caracter(caracter):
    if(ord(caracter)>64 and ord(caracter)<91):
        return True
    elif(ord(caracter)>96 and ord(caracter)<123):
        return True
    else:
        return False
    return False


def is_minus(caracter):
    if((ord(caracter)>96) and ord(caracter)<123):
        return True
    else:
        return False
    
    return False

def change_minus(caracter,es_minus):
    if(es_minus):
        return chr(ord(caracter)+32)

    return caracter

def change_upper(caracter):
    if(ord(caracter) > 90):
        return chr(ord(caracter)-32)

    return caracter

def letra_por_letra(key,mensaje,es_minus,result):
    inicio=ord(key)-65
    final=ord(mensaje)-65

    contador=inicio
    for i in range(26):
        if(contador==final):
            if(es_minus):
                result.append(change_minus(chr(i+65),es_minus))
                break                
            else:               
                result.append(chr(i+65))
                break
        contador=contador+1
        
        if(contador==26):
            contador=0


def vigenere(mensaje,key):
    result=[]
    if(len(mensaje)==len(key)):
        for i in range(len(mensaje)):
            es_minus=is_minus(mensaje[i])
            letter_key=change_upper(key[i])
            letter_message=change_upper(mensaje[i])
            letra_por_letra(letter_key,letter_message,es_minus,result)
    elif(len(mensaje) > len(key)):
        numero_temp=0
        tmp_bool=False
        guardado=False
        for i in range(len(mensaje)):
            if(i >= len(key)):            
                if(identify_caracter(mensaje[i])):
                    es_minus=is_minus(mensaje[i])
                    letter_key=''
                    letter_key=change_upper(key[numero_temp%len(key)])
                    letter_message=change_upper(mensaje[i])
                    letra_por_letra(letter_key,letter_message,es_minus,result)
                    numero_temp=numero_temp+1
                else:
                    result.append(mensaje[i])
                    if(tmp_bool==False):
                        numero_temp=i+1
                        tmp_bool=True

                
            else:
                if(identify_caracter(mensaje[i])):
                    es_minus=is_minus(mensaje[i])
                    letter_key=''
                    letter_key=change_upper(key[numero_temp%len(key)])
                    letter_message=change_upper(mensaje[i])
                    letra_por_letra(letter_key,letter_message,es_minus,result)
                    numero_temp=numero_temp+1
                else:
                    result.append(mensaje[i])
                    if(tmp_bool==False):
                        numero_temp=i
                        tmp_bool=True

    else:
        for i in range(len(key)):
            if(i >= len(mensaje)):
                es_minus=is_minus(mensaje[i%len(mensaje)])
                letter_key=change_upper(key[i])
                letter_message=change_upper(mensaje[i%len(mensaje)])
                letra_por_letra(letter_key,letter_message,es_minus,result)            
            else:
                es_minus=is_minus(mensaje[i%len(mensaje)])
                letter_key=change_upper(key[i])
                letter_message=change_upper(mensaje[i])
                letra_por_letra(letter_key,letter_message,es_minus,result)
    print("Resultado : ")
    for i in result:
        print(i,end='')
    print('')


try:
    mensaje=str(sys.argv[1])
    key=str(sys.argv[2])
    vigenere(mensaje,key)
except:
    help_panel()

