# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta o abrimos el folder desde visual Studio Code 

# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Opcional: Activaremos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu ordenador.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu ordenador.
# OJO: Debes antes tener instalado Streamlit en tu ordenador, 
## también debes antes definir la ruta de tus archivos y 
## tener un script de Python (nombre_de_tu_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC3.py
# python -m streamlit run nombre_de_tu_script.py

# Librería principal para desarrollar aplicaciones web con Streamlit.
import streamlit as st
# Herramienta para crear menús de navegación personalizados en Streamlit.
from streamlit_option_menu import option_menu
# Este módulo permite incrustar componentes personalizados escritos en HTML, CSS y JavaScript dentro de una aplicación.
# components.html() permite mostrar código HTML interactivo directamente en la interfaz.
import streamlit.components.v1 as components

# Menú vertical en una barra lateral
# Crea una barra lateral (sidebar) en la aplicación.
#with st.sidebar:
    #selected = option_menu("Selecciona una sección: ",['Inicio', 'Experiencia', 'Gráficos'] , 
        #icons=['0-circle','1-circle', '2-circle'], menu_icon="filetype-py", default_index=0)
    # Crea un menú de selected dentro de la barra lateral -> option_menu(...)
    # Título que se mostrará encima del menú -> "Selecciona una sección: "
    # Lista de selected disponibles para navegar -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['0-circle','1-circle', '2-circle']
    # Icono principal que aparece junto al título del menú -> menu_icon="filetype-py"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0

# Menú horizontal en una barra horizontal
# OJO: Se puede eliminar el título del menú con None
# Crea un menú de navegación horizontal y guarda la opción seleccionada por el usuario en la variable 'selected'
selected = option_menu(
    menu_title=None, 
    options=['Inicio', 'Experiencia', 'Gráficos'], 
    icons=['grid-fill', 'person-vcard-fill', 'pencil-square'], 
    menu_icon=None, default_index=0, orientation="horizontal")
    # Título que aparece antes de las selected del menú -> menu_title="Selecciona una sección: "
    # Lista de selected que estarán disponibles en el menú -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['person-heart', 'globe-americas', 'pencil-square']
    # Icono principal que aparece junto al título del menú -> menu_icon="cast"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0
    # Hace que el menú se muestre horizontalmente en lugar de verticalmente -> orientation="horizontal"

# Verifica si el usuario ha seleccionado la opción "Inicio" en el menú de navegación horizontal.
# OJO: En caso que elijas el menú de la barra lateral (sidebar) debes cambiar "selected" por "selected"
if selected == 'Inicio':
    st.markdown("<h1 style='text-align: center;'>MI BLOG</h1>", unsafe_allow_html=True)
    # Muestra un título principal utilizando HTML -> st.markdown("...", unsafe_allow_html=True)
    # La etiqueta <h1> define un encabezado de nivel 1 -> "<h1 ...>...</h1>"
    # El estilo CSS 'text-align: center' centra el texto -> style='text-align: center;'
    # unsafe_allow_html=True permite que Streamlit interprete y renderice el código HTML incluido en la cadena

    # Crea dos columnas de igual tamaño para organizar el contenido de forma horizontal en la aplicación.
    col1, col2 = st.columns(2)

    # Muestra una imagen en la primera columna
    col1.image("jenny.png", caption='Jenny', width=370)
    # "ellie.png" es el archivo de imagen que se visualizará -> Aquí debes reemplazar por tu foto de perfil
    # El texto "Ellie" aparecerá como descripción de la imagen
    # width=300 establece el ancho de la imagen en 300 píxeles

    # Define una cadena de texto multilínea que contiene una guía para redactar una presentación personal.
    texto = """
    Soy Jenny, una estudiante de la carrera de Publicidad en la Pontificia Universidad Católica del Perú. Me apasiona la creatividad y la comunicación, y disfruto explorando nuevas ideas y conceptos en el mundo de la publicidad. En mi tiempo libre, me gusta leer, viajar y descubrir nuevas culturas.
    En el futuro, me gustaría trabajar en una agencia de publicidad reconocida, donde pueda aplicar mis conocimientos y habilidades para crear campañas efectivas y memorables.
    En mis tiempos libres me gusta bailar y tocar el piano, actualmente estoy creando una banda de musica con mis hermanos. También disfruto de la fotografía y la edición de videos, lo que me permite expresar mi creatividad de diferentes maneras.
    """

    # Muestra el texto en la segunda columna utilizando HTML
    col2.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto}</div>", unsafe_allow_html=True)
    # El estilo CSS justifica el texto y establece un tamaño de fuente de 18 píxeles
    # f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>"
    # unsafe_allow_html=True permite que Streamlit interprete las etiquetas HTML incluidas en la cadena

elif selected == 'Experiencia':
    st.markdown("<h1 style='text-align: center;'>EXTRAORDINARIO", unsafe_allow_html=True)

    # Agregar un  texto para la respuesta
    texto_2 = """
    Mi experiencia sobre mi aprendisaje a programar ha sido muy enriquecedora y desafiante. Al principio, me sentí un poco abrumada por la cantidad de conceptos nuevos y la lógica detrás de la programación. Sin embargo, con práctica y dedicación, comencé a comprender cómo funcionan los algoritmos y cómo estructurar mi código de manera eficiente.
    Con lo aprendido me gustaria hacer mi propia pagina para mi negocio de publicidad y marketing digital. Aprender esto me ayuda a tener una mejor comprensión de cómo funcionan las aplicaciones web y cómo puedo optimizar mi trabajo en el campo de la publicidad. Asimismo, abrirme mas oportunidades laborales en el futuro, ya que la programación es una habilidad muy demandada en el mercado laboral actual.
    quí escribe tu experiencia aprendiendo a programar. 
    A continuación podran observar un video que resume mi experiencia aprendiendo a programar y como me ha ayudado en mi vida profesional y personal.\n
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # Formato A
    # Agregamos todo los videos realizados en las prácticas anteriores
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video 1 - PC1")
    # Inserta un video de YouTube directamente en la aplicación.
    # El usuario puede reproducirlo sin salir de Streamlit.
    st.video("video dos.mp4")
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presenta una de mi PC, donde aborde explique temas visto en clases, en esta oportunidad se abordo las operaciones Blooleanos. "
    )

    # Formato B
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video 1 - PC2 (Google Drive)")
    # Crea un botón que redirige al usuario a un video alojado en Google Drive. 
    # Al hacer clic, el video se abrirá en una nueva pestaña del navegador.
    st.link_button(
            "Ver video",
            "https://drive.google.com/file/d/1pAvQkjASpW3likErvwr-84f4gBN3NBB2/view?usp=sharing"
        )
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presenta mi segunda PC que realize, donde aborde el tema de BUCLE FOR y BUCLE WHILE. "
    )

elif selected == 'Gráficos':
    st.markdown("<h2 style='text-align: center;'>Nombre a la sección 'Gráficos'</h2>", unsafe_allow_html=True)

    graficos = ['Gráfico_1', 'Gráfico_2', 'Mapa_1']

    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Gráfico_1':
        # Título de la sección
        st.subheader("📊 Gráfico 1: Palabras")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
            Aquí debe ir una breve interpretación de tu gráfico.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen utilizando tres columnas
        col3, col4, col5 = st.columns([1, 5, 1])

        with col4:
            st.image(
                "PALABRAS.png",
                width=800
            )

    elif grafico_seleccionado == 'Gráfico_2':
        # Título de la sección
        st.subheader("📊 Gráfico 2: Familias lingüísticas")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Aquí debe ir una breve interpretación del gráfico.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "BARRA.png",
                width=800
            )
    elif grafico_seleccionado == 'Mapa_1':
        # Título de la sección
        st.subheader("🗺️ Mapa 1: Mapa")

        # Interpretación del mapa
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Aquí debe ir una breve interpretación del mapa.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Cargar el mapa HTML generado previamente
        with open("jenny.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        # Mostrar el mapa interactivo
        components.html(
            html_content,
            height=600
        )
