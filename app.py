import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(page_title="Invitaciones Mágicas", page_icon="✉️", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=IM+Fell+English+SC&display=swap');

body {
    background-color: #0d1b2a;
    color: #f0e6d2;
}

.hogwarts-letter {
    background: url('https://www.transparenttextures.com/patterns/paper.png'), #fdf6e3;
    color: #3e2723;
    padding: 40px;
    border: 2px solid #8b6914;
    border-radius: 10px;
    font-family: 'IM Fell English SC', serif;
    box-shadow: 0 0 20px rgba(0,0,0,0.5);
    animation: fadeIn 2s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}

.ticket-flight {
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    padding: 30px;
    border-radius: 15px;
    font-family: 'Arial', sans-serif;
    box-shadow: 0 0 20px rgba(0,0,0,0.4);
    animation: slideIn 1.5s ease-in-out;
}

@keyframes slideIn {
    from { opacity: 0; transform: translateX(-50px); }
    to { opacity: 1; transform: translateX(0); }
}

h1, h2 {
    font-family: 'Cinzel', serif;
    color: #ffd700;
}
</style>
""", unsafe_allow_html=True)

def guardar_respuesta(archivo, nombre, respuesta):
    data = {
        "nombre": nombre,
        "respuesta": respuesta,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            lista = json.load(f)
    else:
        lista = []
    lista.append(data)
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

tab1, tab2 = st.tabs(["📜 Carta de Hogwarts", "✈️ Pase de Abordar Mágico"])

with tab1:
    st.title("📜 Invitación Mágica al Cine")
    st.markdown("""
    <div class="hogwarts-letter">
        <h2>Estimada Maga de buen Corazón Mágico,</h2>
        <p>Me complace invitarte a una <strong>función especial de Harry Potter</strong> el día:</p>
        <h3>📅 15 de noviembre</h3>
        <p>En el Salón Común de las Fanáticas (Shopping Don Pedro).</p>
        <p>Habrá:</p>
        <ul>
            <li>🍿 Palomitas mágicas</li>
            <li>🧙‍♀️ Concurso de disfraces</li>
            <li>🎁 Sorpresas mágicas</li>
        </ul>
        <p>Espero contar con tu presencia. No olvides tu varita.</p>
        <p>Atentamente,</p>
        <p><strong>Yisus Dumbledore</strong><br>Director de Eventos Mágicos</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("¿Aceptas esta invitación mágica?")
    nombre_hp = st.text_input("Tu nombre mágico:", key="nombre_hp")
    respuesta_hp = st.radio("¿Vendrás?", ("Sí, ¡mi escoba ya está lista!", "Sí, !iré con mi libro de pociones!"), key="respuesta_hp")

    if st.button("Enviar respuesta mágica"):
        if nombre_hp.strip() == "":
            st.warning("Por favor, ingresa tu nombre.")
        else:
            guardar_respuesta("respuestas_harry_potter.json", nombre_hp, respuesta_hp)
            st.success("¡Respuesta enviada! Esperamos verte pronto.")

with tab2:
    st.title("✈️ Pase de Abordar Mágico")
    st.markdown("""
    <div class="ticket-flight">
        <h2>✈️ Invitación a un Vuelo Mágico</h2>
        <p><strong>Origen:</strong> Popayán (Aeropuerto más cercano)</p>
        <p><strong>Destino:</strong> Un país de ensueño ^^</p>
        <p><strong>Fecha:</strong> 22/01/2026</p>
        <p><strong>Vuelo:</strong> MX-2025-MAGIC</p>
        <p><strong>Puerta:</strong> 9 ¾ (obviamente)</p>
        <p>Equipaje emocional permitido. Maletas mágicas bienvenidas. Los boletos están cubiertos.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("¿Te apuntas a esta aventura?")
    nombre_vuelo = st.text_input("Tu nombre para el pasaporte mágico:", key="nombre_vuelo")
    respuesta_vuelo = st.radio("¿Volarás para esta aventura?", ("Sí, ¡mi escoba no puede esperar!", "Sí, !estoy lista para esta aventura!"), key="respuesta_vuelo")

    if st.button("Enviar respuesta de vuelo"):
        if nombre_vuelo.strip() == "":
            st.warning("Por favor, ingresa tu nombre.")
        else:
            guardar_respuesta("respuestas_vuelo_magico.json", nombre_vuelo, respuesta_vuelo)
            st.success("¡Respuesta de vuelo registrada! Nos vemos en el cielo.")

#if st.checkbox("Ver respuestas guardadas"):
#    st.subheader("Respuestas de Harry Potter")
#    if os.path.exists("respuestas_harry_potter.json"):
#        with open("respuestas_harry_potter.json", "r", encoding="utf-8") as f:
#            data = json.load(f)
#        for r in data:
#            st.write(f"- **{r['nombre']}**: {r['respuesta']} ({r['fecha']})")
#    else:
#        st.info("Sin respuestas aún.")

#    st.subheader("Respuestas del Vuelo Mágico")
#    if os.path.exists("respuestas_vuelo_magico.json"):
#        with open("respuestas_vuelo_magico.json", "r", encoding="utf-8") as f:
#            data = json.load(f)
#        for r in data:
#            st.write(f"- **{r['nombre']}**: {r['respuesta']} ({r['fecha']})")
#    else:
#        st.info("Sin respuestas aún.")
