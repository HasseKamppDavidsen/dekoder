import streamlit as st
import pandas as pd

# Oversæt bogstav til tal
def oversaetBogstav(tegn, df_over, key):
    df_num = df_over[df_over["bogstav"] == tegn] 
    if df_num.empty:
        number = tegn
    else:
        number = str(df_num.iloc[0,0]+key)
    return number

# Oversæt tal til bogstav
def oversaetTal(tegn, df_over, key):
    df_num = df_over[df_over["tal"] == tegn-key]
    if df_num.empty:
        number = tegn
    else:
        number = str(df_num.iloc[0,1])
    return number

# Udregn tværsum af nøglen
def findDigi(secs):
    key =''
    digi = 0
    if len(secs) > 0:
        for sec in secs:
            number = str(oversaetBogstav(sec, df_over, 0))
            key += number
    else:
        key = 0

    while len(str(key))>1:
        digi = 0
        for k in str(key):
            digi += int(k)
        key = str(digi)
    return digi

d = {
    'tal': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28], 
    'bogstav': ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z","æ","ø","å"]
    }

df_over = pd.DataFrame(data=d)

st.title("Vibes hemmelige kodegenerator...")
st.write("Dekoderen kan bruges til at lave og afkode beskeder")

secs = st.text_input("Skriv nøglen her :")
secs = str(secs).lower()

letters = st.text_input("Skriv din besked her :")
letters = str(letters).lower()

key =''
numbers = []

df_num = pd.DataFrame()
digi = 0


# Lav bogstaver om til tal
if st.button('Oversæt besked'):

    kode = '.'

    if len(letters) > 0:

        digi = findDigi(secs)

        for letter in letters:
            number = oversaetBogstav(letter, df_over, digi)
            kode += number + '.'
        st.code(kode)
    else:
        st.code("Skriv først en besked der skal oversættes")


## Lav tal om til bogstaver
talKode = st.text_input("Skriv din talkode her :")
talKode = str(talKode).lower()

if st.button('Oversæt kode'):
    
    kode = ''

    # Check at der er en kode
    if len(talKode) > 0:
    
        talKode = talKode.replace(' ','.')
        checkCode = talKode.replace('.','')
        
        # Check om koden består af de rigtige tegn
        if checkCode.isdigit():
            
            digi = findDigi(secs)
            
            splitKode = talKode.split(sep='.')

            for split in splitKode:

                # Check om der er mellemrum
                if split != ' ' and split != '.' and split != '':
                    # Check at tallene ikke er for store eller små
                    if int(split)-digi < 29 and int(split)-digi > 0:
                        bogstav = oversaetTal(int(split), df_over, digi)
                        kode += bogstav
                    else:
                       kode = 'Koden er ikke gyldig! Check at tallene passer til nølgen'
                else:
                    kode += ' '
        else:
            kode = 'Koden er ikke gyldig! Check at den kun består af tal, punktum og mellemrum'
    else:
        kode = "Skriv først en kode der skal oversættes"

    st.code(kode)