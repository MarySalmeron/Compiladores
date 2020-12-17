import re
from Tokens import *

#Keyword - palabra reservada
#ID - identificador
#Delimiter - delimitador
#Arithmetic - operaciones aritméticas
#Assigment - asignación
#EOF - end of file
#Error - Palabra no válida

TokensLst=[ 
    Tokens("EOF","\#","EOF"),
    Tokens("EOL","\\"+chr(10),"EOL"),
    Tokens("function","function","keyword"),
    Tokens("let","let","keyword"),
    Tokens("return","return","keyword"),
    Tokens("LParent","\(","Delimiter"),
    Tokens("RParent","\)","Delimiter"),
    Tokens("LBraket","\{","Delimiter"),
    Tokens("RBraket","\}","Delimiter"),
    Tokens("Comma","\,","Delimiter"),
    Tokens("+","\+","Arithmetic"),
    Tokens("-","\-","Arithmetic"),
    Tokens("*","\*","Arithmetic"),
    Tokens("/","\/","Arithmetic"),
    Tokens("=","\=","Assigment"),
    Tokens("Identifier","[^0-9\+\-\:\*\/\(\)\%\&\|]([^\+\-\:\*\/\(\)\%\&\|\{\}]*)","ID"), 
    Tokens("ERROR","","Error"),
]

# Recibe una palabra y regresa el tipo de token
def TokenType(word: str) -> Tokens:
    for Token in TokensLst:
        if Token.Name != "ERROR":
            find=re.match(Token.Regex,word)
            if find is not None:
                return Token
    exit()

def SeparatesWords(Text: str):
    words=[]
    auxWord=""
    i=0
    while i<len(Text):
        if Text[i]==" ":
            words.append(auxWord)
            auxWord=""
        elif TokenType(Text[i]).Type=="Delimiter" or TokenType(Text[i]).Type=="Arithmetic" or TokenType(Text[i]).Type=="Assigment":
            if auxWord!="":
                words.append(auxWord)
            words.append(Text[i])
            auxWord=""
        elif TokenType(Text[i]).Type=="EOL":
            if auxWord!="":
                words.append(auxWord)
            auxWord=""
            while True:
                i+=1
                if Text[i]!=" ":
                    i-=1
                    break
        elif TokenType(Text[i]).Type=="EOF":
            words.append(Text[i])
            auxWord=""
        else:
            auxWord+=Text[i]
        i+=1
    return words
            

def CodeToTokens(code: str) -> str:
    TokensTxt=""
    words = SeparatesWords(code)
    print(words)
    for word in words:
        _TokenType=TokenType(word).Type
        if _TokenType=="keyword":
            _TokenType=word
        elif _TokenType=="ID":
            _TokenType="ID("+word+")"
        elif _TokenType=="Delimiter":
            _TokenType=TokenType(word).Name
        TokensTxt+=_TokenType+" "
    
    return TokensTxt


codigoFuente=""

with open("codigoFuente.js") as texto:
    codigoFuente=texto.read()
codigoFuente+="#"

print(CodeToTokens(codigoFuente))