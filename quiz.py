import streamlit as st

st.title("NAIVEDYA QUIZ 😏")

score = 0

A = st.text_input("NAIVEDYA'S FAVOURITE GAME")
B = st.text_input("WHO NAIVEDYA LIKED THE MOST IN PERSON HE MET?")
C = st.text_input("NAIVEDYA'S FAVOURITE ACTOR/ACTRESS")
D = st.text_input("NAIVEDYA'S FAVOURITE SONG")
E = st.text_input("NAIVEDYA'S FAVOURITE MOVIE/SERIES")
F = st.text_input("WHICH MARTIAL ARTS DOES NAIVEDYA KNOW?")
G = st.text_input("NAIVEDYA'S BEST FRIEND?")
H = st.text_input("IN WHICH UNIVERSITY NAIVEDYA WANTS TO STUDY?")
I = st.text_input("WHAT NAIVEDYA WANTS TO BE IN PROFESSION?")
J = st.text_input("WHO NAIVEDYA LOVES?")

if st.button("SUBMIT 😏"):
    
    if A.upper() == "FOOTBALL":
        score += 1
    else:
        st.write("Q1 WRONG ❌")

    if B.upper() == "AARNA":
        score += 1
    else:
        st.write("Q2 WRONG ❌")

    if C.upper() == "SADIE SINK":
        score += 1
    else:
        st.write("Q3 WRONG ❌")

    if D.upper() == "LOVE ME NOT":
        score += 1
    else:
        st.write("Q4 WRONG ❌")

    if E.upper() == "STRANGER THINGS":
        score += 1
    else:
        st.write("Q5 WRONG ❌")

    if F.upper() == "KARATE":
        score += 1
    else:
        st.write("Q6 WRONG ❌")

    if G.upper() == "ANUBHAV":
        score += 1
    else:
        st.write("Q7 WRONG ❌")

    if H.upper() == "U PENN" or H.upper() == "UNIVERSITY OF PENNSYLVANIA":
        score += 1
    else:
        st.write("Q8 WRONG ❌")

    if I.upper() == "ACTUARY":
        score += 1
    else:
        st.write("Q9 WRONG ❌")

    if J == ".":
        score += 1
    else:
        st.write("Q10 WRONG ❌")

    st.write("YOUR SCORE:", score)

    if score > 9:
        st.write("BEST FRIEND 😎🔥")
    elif score > 7:
        st.write("CLOSE FRIEND 😏")
    elif score > 5:
        st.write("GOOD 😌")
    elif score < 3:
        st.write("DOOB KE MAR JA MAGARMACH KI AULAD 🐊")
