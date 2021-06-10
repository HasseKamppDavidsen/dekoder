import streamlit as st
import pandas as pd

def oversaetBogstav(tegn, df_over, key):
    df_num = df_over[df_over["bogstav"] == tegn] 
    if df_num.empty:
        number = letter
    else:
        number = str(df_num.iloc[0,0]+key)
    return number


d = {
    'tal': [1, 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28], 
    'bogstav': ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z","æ","ø","å"]
    }

df_over = pd.DataFrame(data=d)

st.title("Den hemmelige dekoder...")
st.write("Dekoderen kan bruges til at lave og afkode beskeder")


secs = st.text_input("Skriv nøglen her :")
secs = str(secs).lower()

letters = st.text_input("Skriv din besked her :")
letters = str(letters).lower()

key =''

numbers = []
kode = "."
df_num = pd.DataFrame()

if st.button('Oversæt'):
    if len(letters) > 0:

        # if len(secs) > 0:
        #     for sec in secs:
        #         number = str(oversaetBogstav(sec, df_over, 0))
        #         key += number
        # else:
        #     key = 0

        # while len(str(key))>1:
        #     digi = 0
        #     for k in str(key):
        #         digi += int(k)
        #     key = str(digi)
        digi = 9

        for letter in letters:
            number = oversaetBogstav(letter, df_over, digi)
            kode += number + '.'
        st.write(kode)
    else:
        st.write("Skriv først en besked der skal oversættes")


