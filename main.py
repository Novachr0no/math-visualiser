import streamlit as st
import numpy as np
import plotly.graph_objects as go

# ---------------------------------------------------------
# Konfigurimi i faqes
# ---------------------------------------------------------
st.set_page_config(
    page_title="🎓 100 Vjet Shkollë & Matematika në Teknologji",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<h1 style="text-align:center; color:white; font-size:42px;">
🎓 100 Vjet Shkollë & Matematika në Teknologji
</h1>
<h3 style="text-align:center; color:lightgray; font-weight:normal;">
Një aplikacion interaktiv nga Departamenti i Matematikës dhe Teknologjisë
</h3>
<hr style="margin-top:15px; margin-bottom:25px;">
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar — kontrolli kryesor
# ---------------------------------------------------------
st.sidebar.title("⚙️ Kontrolli kryesor")
section = st.sidebar.radio("Zgjidh seksionin:", ["Vizualizues Funksionesh", "Seria Fourier"])
st.sidebar.markdown("---")
xmin = st.sidebar.number_input("Vlera minimale për x", value=-10.0)
xmax = st.sidebar.number_input("Vlera maksimale për x", value=10.0)
num_points = st.sidebar.slider("Numri i pikave (rezolucioni)", 200, 5000, 1300)

# ---------------------------------------------------------
# Funksionet matematikore
# ---------------------------------------------------------
x = np.linspace(xmin, xmax, num_points)

if section == "Vizualizues Funksionesh":
    st.header("Vizualizues Funksionesh")

    function_type = st.selectbox(
        "Zgjidh funksionin:",
        ["Lineare", "Kuadratike", "Kubike", "Sinus", "Kosinus", "Eksponenciale", "Logaritmike"]
    )

    if function_type == "Lineare":
        st.latex(r"f(x) = a \cdot x + b")
        with st.expander("⚙️ Parametrat e funksionit"):
            a = st.slider("Koeficienti a (pjerrësia)", -10.0, 10.0, 1.0, step=0.1)
            b = st.slider("Koeficienti b (ndërprerja me boshtin y)", -10.0, 10.0, 0.0, step=0.1)
        y = a * x + b

    elif function_type == "Kuadratike":
        st.latex(r"f(x) = a \cdot x^2 + b \cdot x + c")
        with st.expander("⚙️ Parametrat e funksionit"):
            a = st.slider("Koeficienti a (hapja e paraboles)", -5.0, 5.0, 1.0, step=0.1)
            b = st.slider("Koeficienti b (zhvendosja horizontale)", -5.0, 5.0, 0.0, step=0.1)
            c = st.slider("Koeficienti c (zhvendosja vertikale)", -5.0, 5.0, 0.0, step=0.1)
        y = a * x**2 + b * x + c

    elif function_type == "Kubike":
        st.latex(r"f(x) = a \cdot x^3 + b \cdot x^2 + c \cdot x")
        with st.expander("⚙️ Parametrat e funksionit"):
            a = st.slider("Koeficienti a (forma e përgjithshme)", -3.0, 3.0, 1.0, step=0.1)
            b = st.slider("Koeficienti b (ndryshon pjerrësinë)", -3.0, 3.0, 0.0, step=0.1)
            c = st.slider("Koeficienti c (zhvendosja lineare)", -3.0, 3.0, 0.0, step=0.1)
        y = a * x**3 + b * x**2 + c * x

    elif function_type == "Sinus":
        st.latex(r"f(x) = a \cdot \sin(bx + c)")
        with st.expander("⚙️ Parametrat e funksionit"):
            a = st.slider("Koeficienti a (amplituda)", -5.0, 5.0, 1.0, step=0.1)
            b = st.slider("Koeficienti b (frekuenca)", -10.0, 10.0, 1.0, step=0.1)
            c = st.slider("Koeficienti c (fazë fillestare)", -10.0, 10.0, 0.0, step=0.1)
        y = a * np.sin(b * x + c)

    elif function_type == "Kosinus":
        st.latex(r"f(x) = a \cdot \cos(bx + c)")
        with st.expander("⚙️ Parametrat e funksionit"):
            a = st.slider("Koeficienti a (amplituda)", -5.0, 5.0, 1.0, step=0.1)
            b = st.slider("Koeficienti b (frekuenca)", -10.0, 10.0, 1.0, step=0.1)
            c = st.slider("Koeficienti c (fazë fillestare)", -10.0, 10.0, 0.0, step=0.1)
        y = a * np.cos(b * x + c)

    elif function_type == "Eksponenciale":
        st.latex(r"f(x) = a \cdot e^{bx}")
        with st.expander("⚙️ Parametrat e funksionit"):
            a = st.slider("Koeficienti a (shkalla e rritjes)", -5.0, 5.0, 1.0, step=0.1)
            b = st.slider("Koeficienti b (përshpejtimi i rritjes)", -5.0, 5.0, 1.0, step=0.1)
        y = a * np.exp(b * x)

    elif function_type == "Logaritmike":
        st.latex(r"f(x) = a \cdot \ln(bx) + c")
        with st.expander("⚙️ Parametrat e funksionit"):
            a = st.slider("Koeficienti a (zmadhohet/kthehet grafiku)", -5.0, 5.0, 1.0, step=0.1)
            b = st.slider("Koeficienti b (ndryshimi i bazës)", 0.1, 5.0, 1.0, step=0.1)
            c = st.slider("Koeficienti c (zhvendosje vertikale)", -5.0, 5.0, 0.0, step=0.1)
        x = np.linspace(0.1, xmax, num_points)
        y = a * np.log(b * x) + c

    # Vizualizimi me Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(width=3, color='cyan'), name="f(x)"))
    fig.update_layout(
        title=f"Grafiku i funksionit — {function_type}",
        xaxis_title="Boshti X",
        yaxis_title="Boshti Y",
        template="plotly_dark",
        hovermode="x unified",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("📘 Shpjegim i funksionit"):
        st.markdown("""
        Ky seksion ju lejon të ndryshoni koeficientët e funksioneve dhe të shihni sesi ndikojnë në formën e grafikut:
        - **a** përcakton pjerrësinë ose amplitudën.
        - **b** ndikon në frekuencë ose në zhvendosjen horizontale.
        - **c** zhvendos grafikun vertikalisht ose ndryshon fazën.
        """)

# ---------------------------------------------------------
# Seria Fourier
# ---------------------------------------------------------
else:
    st.header("Seria Fourier — Ndërtimi i Valëve")

    st.markdown("""
    Këtu mund të shihni sesi valë të ndryshme (katrore, trekëndore, apo dhëmbë) mund të ndërtohen me **valë sinusoidale**.
    Rritni numrin e harmonikëve për të parë sesi përmirësohet përafërsia e formës.
    """)

    waveform = st.selectbox("Zgjidh formën e valës:", ["Valë katrore", "Valë trekëndore", "Valë dhëmbë"])
    n_terms = st.slider("Numri i harmonikëve:", 1, 50, 10)
    T = st.number_input("Periudha T:", value=3.14)

    x = np.linspace(-T, T, num_points)
    y = np.zeros_like(x)

    if waveform == "Valë katrore":
        st.latex(r"f(x) = \frac{4}{\pi}(\sin(x) + \frac{1}{3}\sin(3x) + \frac{1}{5}\sin(5x) + ...)")
        for n in range(1, n_terms * 2, 2):
            y += (4 / np.pi) * np.sin(n * np.pi * x / T) / n
    elif waveform == "Valë trekëndore":
        st.latex(r"f(x) = \frac{8}{\pi^2}(\sin(x) - \frac{1}{9}\sin(3x) + \frac{1}{25}\sin(5x) - ...)")
        for n in range(1, n_terms * 2, 2):
            y += (8 / np.pi**2) * ((-1)**((n - 1) // 2)) * np.sin(n * np.pi * x / T) / (n**2)
    elif waveform == "Valë dhëmbë":
        st.latex(r"f(x) = -\frac{2}{\pi}(\sin(x) + \frac{1}{2}\sin(2x) + \frac{1}{3}\sin(3x) + ...)")
        for n in range(1, n_terms + 1):
            y += (-2 / np.pi) * np.sin(n * np.pi * x / T) / n

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f"Aproksimimi ({n_terms} terma)", line=dict(color='orange', width=3)))

    if waveform == "Valë katrore":
        y_true = np.sign(np.sin(np.pi * x / T))
    elif waveform == "Valë trekëndore":
        y_true = 2 * np.abs(2 * (x / T - np.floor(x / T + 0.5))) - 1
    elif waveform == "Valë dhëmbë":
        y_true = 2 * (x / T - np.floor(x / T + 0.5))

    fig.add_trace(go.Scatter(x=x, y=y_true, mode='lines', name="Valë ideale", line=dict(color='cyan', dash='dot')))
    fig.update_layout(
        title=f"Seria Fourier — {waveform}",
        xaxis_title="Koha (x)",
        yaxis_title="Amplituda",
        template="plotly_dark",
        hovermode="x unified",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("📘 Shpjegim i Serisë Fourier"):
        st.markdown("""
        Seria Fourier përshkruan sesi një sinjal periodik mund të përftohet duke shtuar shumë **valë sinusoidale**.
        - **Valë katrore**: përbëhet vetëm nga harmonikët tek.
        - **Valë trekëndore**: amplitudat bien me katrorin e numrit të harmonikut.
        - **Valë dhëmbë**: përfshin të gjithë harmonikët, me amplitudë që bie me 1/n.
        """)

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:gray;'>© 2025 - Për 100-vjetorin e shkollës • Krijuar nga <b>Amir Kovaci</b></p>",
    unsafe_allow_html=True
)
