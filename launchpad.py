import streamlit as st
import base64
import datetime
import io

st.set_page_config(page_title="Startup Validator", layout="wide")

# ---------- Sidebar Navigation ----------
menu = [
    "1. Validazione Idea",
    "2. Target Persona",
    "3. Pianificazione",
    "4. Esperimenti",
    "5. Metriche & Business",
    "6. Marketing & Esecuzione",
    "7. Feedback",
    "8. Pitch Finale"
]


st.sidebar.title("🚀 Startup Launchpad")
selection = st.sidebar.radio("Naviga tra le fasi:", menu)

# ---------- Report Collector ----------
if 'report' not in st.session_state:
    st.session_state.report = {}

# ---------- Fase 1: Validazione Idea ----------
if selection == "1. Validazione Idea":
    st.title("✅ Validazione dell'Idea")

    with st.container():
        st.subheader("📋 Reality Test Checklist")
        checklist_output = []

        categories = {
            "Business Model": [
                "E’ stato realizzato un Business Model Canvas",
                "Sono stati indicati i problemi",
                "Sono stati considerati almeno 4 competitor"
            ],
            "Value Proposition": [
                "Gli assi scelti costituiscono valore per il cliente",
                "Il posizionamento è chiaramente espresso",
                "La UVP riporta i Job-To-Be-Done",
                "Sono state generate almeno 3 Unique Value Proposition"
            ],
            "Personas": [
                "Sono state considerate almeno 2 Personas",
                "I Job-To-Be-Done sono credibili o derivati da interviste",
                "Le Personas sono chiaramente distinte"
            ],
            "Awareness & Customer Journey": [
                "Sono stati individuati i 5 stadi di Awareness",
                "Sono stati individuati almeno 2 problemi dove agire",
                "La Customer Journey è basata su esperti/clienti",
                "La fase di Awareness si appoggia ai Touchpoint",
                "La fase di Activation si riferisce alla Value Proposition"
            ],
            "Metriche e Canali": [
                "Sono state decise metriche chiare per ogni step",
                "Sono state eseguite ricerche su Facebook",
                "Sono state eseguite ricerche su Amazon",
                "Sono state eseguite ricerche su Google"
            ],
            "Concorrenza e Vantaggio": [
                "Sono stati indicati i clienti",
                "Sono state indicate le alternative",
                "Sono stati indicati i vantaggi",
                "Sono stati individuati contenuti azionabili"
            ]
        }

        for category, items in categories.items():
            st.markdown(f"### 🔹 {category}")
            cols = st.columns(2)
            for i, item in enumerate(items):
                with cols[i % 2]:
                    response = st.checkbox(item, key=item)
                    checklist_output.append(f"[{'x' if response else ' '}] {item}")

        st.session_state.report["Reality Test Checklist"] = "\n".join(checklist_output)

    with st.container():
        st.subheader("📘 Check sulle 22 Leggi Immutabili del Marketing")
        leggi_domande = [
            ("Law of Leadership", "Sei il numero uno della tua categoria?"),
            ("Law of Category", "Hai creato una nuova categoria?"),
            ("Law of Mind", "Sei percepito come chi ha inventato quello che offri?"),
            ("Law of Perception", "Ci sono percezioni forti che influenzano il tuo posizionamento?"),
            ("Law of Focus", "Il tuo brand è focalizzato su un singolo concetto?"),
            ("Law of Exclusivity", "Condividi concetti chiave con concorrenti o sei unico?"),
            ("Law of Ladder", "Hai posizionato il tuo brand rispetto a una gerarchia mentale esistente?"),
            ("Law of Duality", "Hai chiaro chi è il tuo principale competitor?"),
            ("Law of Opposite", "Hai posizionato il tuo prodotto come alternativa/opposto al leader?"),
            ("Law of Division", "Hai tenuto conto della segmentazione del tuo mercato?"),
            ("Law of Perspective", "Hai una visione di lungo periodo del tuo brand?"),
            ("Law of Line Extension", "Hai evitato di diluire il brand con troppe offerte?"),
            ("Law of Sacrifice", "Hai rinunciato consapevolmente a certe nicchie per rafforzare il focus?"),
            ("Law of Attributes", "Hai identificato attributi forti e differenzianti?"),
            ("Law of Candor", "Utilizzi l'onestà per rafforzare la credibilità del tuo messaggio?"),
            ("Law of Singularity", "Hai una leva unica per cambiare le regole del mercato?"),
            ("Law of Unpredictability", "Hai un piano per adattarti ai cambiamenti del mercato?"),
            ("Law of Success", "La tua strategia non è ostacolata dall'ego?"),
            ("Law of Failure", "Hai un piano per fallimenti o test negativi?"),
            ("Law of Hype", "Eviti il rumore eccessivo e punti alla sostanza?"),
            ("Law of Acceleration", "Hai costruito un sistema per la crescita sostenibile?"),
            ("Law of Resources", "Hai risorse chiare per sostenere marketing e crescita?")
        ]
        leggi_output = []
        for legge, domanda in leggi_domande:
            st.markdown(f"**{legge}**")
            risposta = st.radio(f"{domanda}", ["Sì", "No"], key=legge)
            leggi_output.append(f"{legge}: {domanda} - Risposta: {risposta}")
        st.session_state.report["22 Leggi Immutabili del Marketing"] = "\n".join(leggi_output)

    with st.container():
        st.subheader("🧠 5 Livelli di Consapevolezza del Mercato")
        livelli = [
            "1. Inconsapevole",
            "2. Consapevole del problema",
            "3. Consapevole della soluzione",
            "4. Consapevole del prodotto",
            "5. Totalmente consapevole"
        ]
        awareness_output = []
        for livello in livelli:
            note = st.text_area(f"{livello} - Come comunicheresti a questo livello?", key=livello)
            awareness_output.append(f"{livello}: {note}")
        st.session_state.report["5 Livelli di Consapevolezza del Mercato"] = "\n".join(awareness_output)

# ---------- Fase 2: Target Persona ----------
if selection == "2. Target Persona":
    st.title("🎯 Target Persona")

    with st.container():
        st.subheader("👤 Lean Persona 1")
        lean_fields = [
            "Nome",
            "Ruolo / Professione",
            "Età",
            "Obiettivi principali",
            "Problemi principali",
            "Dove passa il tempo online",
            "Comportamenti d'acquisto",
            "Tecnologie che usa"
        ]
        persona1 = []
        for field in lean_fields:
            value = st.text_input(f"{field} (Persona 1)", key=f"lean1_{field}")
            persona1.append(f"{field}: {value}")

        st.subheader("👤 Lean Persona 2")
        persona2 = []
        for field in lean_fields:
            value = st.text_input(f"{field} (Persona 2)", key=f"lean2_{field}")
            persona2.append(f"{field}: {value}")

        st.session_state.report["Lean Persona"] = "\nPersona 1:\n" + "\n".join(persona1) + "\n\nPersona 2:\n" + "\n".join(persona2)

    with st.container():
        st.subheader("🧬 Marketing Persona")
        marketing_fields = {
            "Nome della Persona": "",
            "Background e interessi": "",
            "Comportamento digitale": "",
            "Frustrazioni o paure": "",
            "Obiettivi professionali o personali": "",
            "Messaggi che funzionano": "",
            "Canali preferiti": "",
            "Motivazioni all'acquisto": ""
        }
        marketing_results = []
        for field in marketing_fields:
            value = st.text_area(f"{field}", key=f"marketing_{field}")
            marketing_results.append(f"{field}: {value}")
        st.session_state.report["Marketing Persona"] = "\n".join(marketing_results)

# ---------- Fase 3: Pianificazione ----------
if selection == "3. Pianificazione":
    st.title("📅 Pianificazione")

    with st.container():
        st.subheader("GANTT Planning")
        gantt_data = []
        num_rows = st.number_input("Quante attività vuoi pianificare?", min_value=1, max_value=20, value=3, step=1)
        for i in range(num_rows):
            st.markdown(f"**Attività {i+1}**")
            col1, col2, col3 = st.columns(3)
            with col1:
                task = st.text_input(f"Nome attività {i+1}", key=f"task_{i}")
            with col2:
                start = st.date_input(f"Inizio {i+1}", key=f"start_{i}")
            with col3:
                end = st.date_input(f"Fine {i+1}", key=f"end_{i}")
            gantt_data.append(f"Attività: {task}, Inizio: {start}, Fine: {end}")
        st.session_state.report["GANTT Planning"] = "".join(gantt_data)

    with st.container():
        st.subheader("📊 AAARRR Framework")
        funnel_steps = [
            "Acquisition",
            "Activation",
            "Retention",
            "Referral",
            "Revenue"
        ]
        aaaar_output = []
        for step in funnel_steps:
            st.markdown(f"### {step}")
            metric = st.text_input(f"KPI per {step}", key=f"kpi_{step}")
            action = st.text_area(f"Azioni da intraprendere per {step}", key=f"action_{step}")
            aaaar_output.append(f"{step}KPI: {metric}Azioni: {action}")
        st.session_state.report["AAARRR Canvas"] = "".join(aaaar_output)

# ---------- Fase 4: Esperimenti ----------
if selection == "4. Esperimenti":
    st.title("🧪 Esperimenti")

    with st.container():
        st.subheader("📌 Definizione Esperimenti")
        num_exp = st.number_input("Quanti esperimenti vuoi definire?", min_value=1, max_value=10, value=3, step=1)
        esperimenti = []
        for i in range(num_exp):
            st.markdown(f"**Esperimento {i+1}**")
            nome = st.text_input(f"Nome esperimento {i+1}", key=f"nome_exp_{i}")
            obiettivo = st.text_area(f"Obiettivo dell'esperimento {i+1}", key=f"obiettivo_exp_{i}")
            ipotesi = st.text_area(f"Ipotesi da testare {i+1}", key=f"ipotesi_exp_{i}")
            metrica = st.text_input(f"Metrica di validazione {i+1}", key=f"metrica_exp_{i}")
            criterio = st.text_input(f"Criterio di successo {i+1}", key=f"criterio_exp_{i}")
            esperimenti.append(f"Esperimento {i+1}Nome: {nome}Obiettivo: {obiettivo}Ipotesi: {ipotesi}Metrica: {metrica}Criterio: {criterio}")
        st.session_state.report["Esperimenti"] = "".join(esperimenti)

# ---------- Fase 5: Metriche & Business ----------
if selection == "5. Metriche & Business":
    st.title("📈 Metriche & Business Model")

    with st.container():
        st.subheader("📌 Metriche principali")
        metriche = []
        for i in range(5):
            metrica = st.text_input(f"Nome metrica {i+1}", key=f"metrica_nome_{i}")
            obiettivo = st.text_input(f"Obiettivo metrica {i+1}", key=f"metrica_target_{i}")
            unit = st.text_input(f"Unità di misura {i+1}", key=f"metrica_unit_{i}")
            metriche.append(f"Metrica: {metrica}, Obiettivo: {obiettivo}, Unità: {unit}")
        st.session_state.report["Metriche"] = "".join(metriche)

    with st.container():
        st.subheader("💰 Modello di Business")
        business_inputs = {
            "Struttura dei costi": "",
            "Fonti di ricavo": "",
            "Strategia di prezzo": "",
            "Margine atteso": "",
            "Canali di vendita": "",
            "Partnership strategiche": ""
        }
        business_output = []
        for campo in business_inputs:
            valore = st.text_area(campo, key=f"biz_{campo}")
            business_output.append(f"{campo}: {valore}")
        st.session_state.report["Business Model"] = "".join(business_output)

# ---------- Fase 6: Marketing & Esecuzione ----------
if selection == "6. Marketing & Esecuzione":
    st.title("📣 Marketing & Esecuzione")

    with st.container():
        st.subheader("📌 Piano Editoriale")
        num_post = st.number_input("Quanti contenuti vuoi pianificare?", min_value=1, max_value=10, value=3, step=1)
        editorial_plan = []
        for i in range(num_post):
            st.markdown(f"**Contenuto {i+1}**")
            canale = st.text_input(f"Canale (es. Instagram, Blog) {i+1}", key=f"canale_{i}")
            tipo = st.text_input(f"Tipo di contenuto {i+1}", key=f"tipo_{i}")
            tema = st.text_area(f"Tema / Messaggio chiave {i+1}", key=f"tema_{i}")
            data = st.date_input(f"Data pubblicazione {i+1}", key=f"data_{i}")
            editorial_plan.append(f"Contenuto {i+1}Canale: {canale}Tipo: {tipo}Tema: {tema}Data: {data}")
        st.session_state.report["Piano Editoriale"] = "".join(editorial_plan)

    with st.container():
        st.subheader("🚀 Strategia di Lancio")
        lancio = st.text_area("Descrivi le fasi principali della strategia di lancio:", key="strategia_lancio")
        st.session_state.report["Strategia di Lancio"] = lancio

# ---------- Fase 7: Feedback ----------
if selection == "7. Feedback":
    st.title("💬 Raccolta Feedback")

    with st.container():
        st.subheader("📣 Feedback Utente")
        num_feedback = st.number_input("Quanti feedback vuoi registrare?", min_value=1, max_value=10, value=3, step=1)
        feedback_list = []
        for i in range(num_feedback):
            st.markdown(f"**Feedback {i+1}**")
            fonte = st.text_input(f"Fonte del feedback {i+1} (es. cliente, tester)", key=f"fonte_{i}")
            nota = st.text_area(f"Testo del feedback {i+1}", key=f"nota_{i}")
            azione = st.text_area(f"Azioni da intraprendere {i+1}", key=f"azione_{i}")
            feedback_list.append(f"Feedback {i+1}Fonte: {fonte}Nota: {nota}Azione: {azione}")
        st.session_state.report["Feedback"] = "".join(feedback_list)

# ---------- Fase 8: Pitch Finale ----------
if selection == "8. Pitch Finale":
    st.title("🎤 Pitch Finale")

    with st.container():
        st.subheader("🧾 Sommario Executive")
        executive_summary = st.text_area("Inserisci un riassunto sintetico del progetto:", key="executive_summary")

    with st.container():
        st.subheader("📌 Value Proposition Chiave")
        vp_key = st.text_area("Qual è la proposta di valore centrale?", key="vp_key")

    with st.container():
        st.subheader("📈 Dati e Traguardi")
        milestones = st.text_area("Indica i principali traguardi raggiunti e i dati validati:", key="milestones")

    with st.container():
        st.subheader("🚀 Prossimi Passi e Richieste")
        next_steps = st.text_area("Quali sono i prossimi step e cosa chiedi (team, budget, supporto)?", key="next_steps")

    pitch = f"""
Executive Summary:
{executive_summary}

Value Proposition:
{vp_key}

Traguardi:
{milestones}

Prossimi Passi:
{next_steps}
"""
    st.session_state.report["Pitch Finale"] = pitch

# ---------- Export Report ----------
def generate_report():
    report_md = f"# Startup Report\nCreato il: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    for key, content in st.session_state.report.items():
        report_md += f"\n## {key}\n{content}\n"
    return report_md

def download_button(text, filename):
    b64 = base64.b64encode(text.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">📄 Scarica il Report</a>'
    return href

st.sidebar.markdown("---")
st.sidebar.markdown("### 📥 Esporta il Report")
if st.sidebar.button("Genera Report"):
    report_text = generate_report()
    st.sidebar.markdown(download_button(report_text, "startup_report.txt"), unsafe_allow_html=True)

# ---------- Style Enhancements ----------