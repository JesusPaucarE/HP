import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="Invitación Mágica al Cine",
    page_icon="⚡",
    layout="centered",
)

st.markdown("""
<style>
    .main {
        background-color: #0d1b2a;
        color: #f0e6d2;
    }
    h1, h2, h3 {
        font-family: 'Cinzel', serif;
        color: #ffd700;
    }
    .invitacion {
        background-color: #1b263b;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #ffd700;
        margin-bottom: 20px;
    }
    .aceptar {
        background-color: #2a9d8f;
        color: white;
        font-weight: bold;
    }
    .rechazar {
        background-color: #e76f51;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚡ Invitación Mágica al Cine ⚡")
st.subheader("¡Una experiencia de Harry Potter como nunca antes!")

st.markdown("""
<div class="invitacion">
    <h2>¡Estás invitada, elegida de Hogwarts!</h2>
    <p>El día <strong>15 de noviembre</strong> se llevará a cabo una función especial de cine con todas las películas de <strong>Harry Potter</strong>.</p>
    <p>Habrá:</p>
    <ul>
        <li>🍿 Palomitas mágicas</li>
        <li>🧙‍♀️ Concurso de disfraces</li>
        <li>📚 Trivia del mundo mágico</li>
        <li>🎁 Sorpasas para los más fieles fans</li>
    </ul>
    <p>¿Te atreves a acompañarnos en esta aventura?</p>
</div>
""", unsafe_allow_html=True)

st.header("¿Aceptas la invitación?")

nombre = st.text_input("Escribe tu nombre mágico:")
respuesta = st.radio("¿Vendrás a la función?", ("Sí, ¡quiero ser parte de la magia!", "No, prefiero quedarme en el mundo muggle"))

if st.button("Enviar respuesta"):
    if nombre.strip() == "":
        st.warning("Por favor, ingresa tu nombre antes de enviar.")
    else:
        respuesta_dict = {
            "nombre": nombre,
            "respuesta": respuesta,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        archivo_respuestas = "respuestas_invitacion.json"

        if os.path.exists(archivo_respuestas):
            with open(archivo_respuestas, "r", encoding="utf-8") as f:
                respuestas = json.load(f)
        else:
            respuestas = []

        respuestas.append(respuesta_dict)

        with open(archivo_respuestas, "w", encoding="utf-8") as f:
            json.dump(respuestas, f, ensure_ascii=False, indent=4)

        st.success("¡Tu respuesta ha sido enviada con éxito!")

        if "Sí" in respuesta:
            st.balloons()
            st.markdown("🎉 ¡Nos vemos el 15 de noviembre! Trae tu varita y tu mejor disfraz.")
        else:
            st.markdown("😢 Qué pena... pero si cambias de opinión, ¡la puerta de Hogwarts siempre estará abierta!")

if st.checkbox("Ver respuestas guardadas"):
    if os.path.exists("respuestas_invitacion.json"):
        with open("respuestas_invitacion.json", "r", encoding="utf-8") as f:
            respuestas = json.load(f)
        st.write("Respuestas recibidas:")
        for r in respuestas:
            st.write(f"- **{r['nombre']}**: {r['respuesta']} ({r['fecha']})")
    else:
        st.info("Aún no se han guardado respuestas.")
