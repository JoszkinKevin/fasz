import streamlit as st

def main():
  st.title("Valutaváltás")

  szam1 = st.number_input(label="Mennyi pénz: ")

  muvelet = st.selectbox("Pénznem: ",("dollár","euro"))

  

  result = 0
  if muvelet == "dollár":
    result = szam1 * 3
  elif muvelet == "euro":
    result = szam1 * 4
  st.write(f"Eredmény: {result}")

if __name__ == '__main__':
  main()
