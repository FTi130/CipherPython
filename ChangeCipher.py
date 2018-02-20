simal=[chr(x)for x in range(65,91)]
simak=('!','@','#','$','%','^','&','*','(',')','-','=', '+','?',':',';','<','>','/','[',']','{','}','|','.',',','~')
mode=input('[E]ncrypt|[D]ecrypt: ').upper()
URmessage=input('Что шифровать: ').upper()
keys=dict(zip(simal,simak))
def encrdecr(mode,message,final=''):
    if mode =='E':
        for symbol in message:
            if symbol in keys:
                final+=keys[symbol]
    else:
        for symbol in message:
            for key in keys:
                if symbol == keys[key]: final += key
    return final
print ('Зашифровано/расшифровано', encrdecr(mode,URmessage))

            
            
    
