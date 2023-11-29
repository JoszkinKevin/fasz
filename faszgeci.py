import streamlit as st

def main():
  st.title("Valutaváltás")

  szam1 = st.number_input(label="Mennyi pénz: ")

  muvelet = st.selectbox("Pénznem: ",("dollár","euro"))

  

  result = 0
  if muvelet == "dollár":
    result = szam1 * 344
  elif muvelet == "euro":
    result = szam1 * 377
  st.write(f"Eredmény: {result}")

if __name__ == '__main__':
  main()
