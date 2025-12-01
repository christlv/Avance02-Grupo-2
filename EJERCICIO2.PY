import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Sesión 2 | ISIL", layout="centered")

st.title("Segmentación de Clientes por Comportamiento Digital | Timeline")
st.write("Autor: Christian Torres | ISIL")
st.write("EDA - segmentación y el análisis del comportamiento digital")

# Para evitar errores al mostrar código que usa df
df = pd.DataFrame()

base_url = "https://raw.githubusercontent.com/christlv/Avance02-Grupo-2/main/GRAFICOS/"
imagenes = {
   1: base_url + "GRAFICO2.png",
   2: base_url + "GRAFICO3.png",
   3: base_url + "GRAFICO4.png",
   4: base_url + "GRAFICO5.png",
   5: base_url + "GRAFICO6.png"
}

opcion = st.slider("Selecciona un punto del timeline", 1, 5, 1)
st.image(imagenes[opcion], use_container_width=True)

# Mostrar código según la opción
if opcion == 1:
    st.info("**Distribución de adopción digital**")
    st.code("""
# Contar los valores de la columna
counts = df['digital_adoption_likelihood'].value_counts()

# Crear el gráfico de barras
ax = counts.plot(kind='bar', color=['skyblue','orange'])
plt.title('Distribución de adopción digital')

# Agregar etiquetas encima de cada barra
for i, val in enumerate(counts):
    ax.text(i, val + 5, str(val), ha='center', va='bottom')
plt.show()
""", language="python")

elif opcion == 2:
    st.info("**Distribución de género de clientes**")
    st.code("""
# Crear el countplot
ax = sns.countplot(data=df, x='CustGender', palette=['pink','skyblue'])
plt.title('Distribución de género de clientes')

# Agregar etiquetas encima de las barras
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width()/2., p.get_height()),
                ha='center', va='bottom', fontsize=10)
plt.show()
""", language="python")

elif opcion == 3:
    st.info("**Distribución de Digital Activity Score**")
    st.code("""
sns.histplot(df['DigitalActivityScore'], bins=30)
plt.title('Distribución de Digital Activity Score')
plt.show()
""", language="python")

elif opcion == 4:
    st.info("**Relación entre transacciones digitales y presenciales**")
    st.code("""
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x='DigitalTransactionsCount', y='BranchTransactionsCount')
plt.title('Relación entre transacciones digitales y presenciales')
plt.show()
""", language="python")

elif opcion == 5:
    st.info("**Tipos de tarjeta por cliente**")
    st.code("""
color_map = {
    'Black': '#000000',
    'Platinum': '#E5E4E2',
    'Gold': '#FFD700',
    'Classic': '#1E90FF'
}

# Crear el countplot
ax = sns.countplot(data=df, x='CreditCardType', palette=color_map)
plt.title('Tipos de tarjeta por cliente')

# Agregar etiquetas encima de cada barra
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{int(height)}',
                (p.get_x() + p.get_width()/2., height + 5),
                ha='center', va='bottom',
                fontsize=10,
                color='white')
plt.show()
""", language="python")

