import streamlit as st

def main():
  st.title("Valutaváltás")

  szam1 = st.number_input(label="Mennyi pénz: ")

  muvelet = st.selectbox("Pénznem: ",("dollár","euro"))

  dollar = "0,0029"
  euro = "0,0026" 

  result = 0
  if muvelet == "dollár":
    result = szam1 * dollar
  elif muvelet == "euro":
    result = szam1 * dollar
  st.write(f"Eredmény: {result}")

if __name__ == '__main__':
  main()
