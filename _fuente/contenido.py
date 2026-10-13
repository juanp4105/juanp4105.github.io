# -*- coding: utf-8 -*-
"""
Contenido del sitio de Juan Pablo Arrobo Agila.

Para actualizar el sitio:
  1. Edite este archivo (textos, publicaciones, cursos).
  2. Ejecute:  python3 _fuente/build.py
  3. Suba los archivos generados a GitHub.

Cada texto traducible es un diccionario con las claves "es", "en" y "pt".
"""

SITIO = {
    "url": "https://juanp4105.github.io",
    "nombre": "Juan Pablo Arrobo Agila",
    "nombre_corto": "Juan Pablo Arrobo",
    "email": "juanp4105@gmail.com",          # principal: contacto y capacitaciones
    "email_inst": "jparrobo1@utpl.edu.ec",   # secundario: asuntos académicos de la UTPL
    "actualizado": "2026-10-13",
}

IDIOMAS = [
    {"code": "es", "label": "ES", "bandera": "ec", "nombre": "Español", "dir": ""},
    {"code": "en", "label": "EN", "bandera": "us", "nombre": "English", "dir": "en/"},
    {"code": "pt", "label": "PT", "bandera": "br", "nombre": "Português", "dir": "pt/"},
]

PAGINAS = [
    {"id": "inicio", "archivo": "index.html",
     "nav": {"es": "Inicio", "en": "Home", "pt": "Início"}},
    {"id": "capacitacion", "archivo": "capacitacion-ia.html",
     "nav": {"es": "Cursos de IA", "en": "AI courses", "pt": "Cursos de IA"}},
    {"id": "docencia", "archivo": "docencia.html",
     "nav": {"es": "Docencia", "en": "Teaching", "pt": "Docência"}},
    {"id": "investigacion", "archivo": "investigacion.html",
     "nav": {"es": "Investigación", "en": "Research", "pt": "Pesquisa"}},
    {"id": "publicaciones", "archivo": "publicaciones.html",
     "nav": {"es": "Publicaciones", "en": "Publications", "pt": "Publicações"}},
    {"id": "contacto", "archivo": "contacto.html",
     "nav": {"es": "Contacto", "en": "Contact", "pt": "Contato"}},
]

PERFILES = [
    {"nombre": "ORCID", "url": "https://orcid.org/0000-0002-6315-2218", "id": "0000-0002-6315-2218"},
    {"nombre": "Google Scholar", "url": "https://scholar.google.com/citations?user=IQBQmWMAAAAJ&hl=es", "id": "IQBQmWMAAAAJ"},
    {"nombre": "Scopus", "url": "https://www.scopus.com/authid/detail.uri?authorId=56891569100", "id": "56891569100"},
    {"nombre": "ResearchGate", "url": "https://www.researchgate.net/profile/Juan_Arrobo-Agila", "id": "Juan_Arrobo-Agila"},
    {"nombre": "LinkedIn", "url": "https://www.linkedin.com/in/juanp4105/", "id": "juanp4105"},
    {"nombre": {"es": "Portal de investigación UTPL", "en": "UTPL research portal", "pt": "Portal de pesquisa UTPL"},
     "url": "https://investigacion.utpl.edu.ec/jparrobo1", "id": "jparrobo1"},
]

# ---------------------------------------------------------------- textos generales
T = {
    "rol": {
        "es": "Docente investigador en Comunicación",
        "en": "Communication scholar and lecturer",
        "pt": "Professor e pesquisador em Comunicação",
    },
    "afiliacion": {
        "es": "Universidad Técnica Particular de Loja (UTPL), Ecuador",
        "en": "Universidad Técnica Particular de Loja (UTPL), Ecuador",
        "pt": "Universidad Técnica Particular de Loja (UTPL), Equador",
    },
    "departamento": {
        "es": "Departamento de Comunicación y Artes, Facultad de Ciencias Sociales, Educación y Humanidades",
        "en": "Department of Communication and Arts, Faculty of Social Sciences, Education and Humanities",
        "pt": "Departamento de Comunicação e Artes, Faculdade de Ciências Sociais, Educação e Humanidades",
    },
    "lema": {
        "es": "Estudio cómo las imágenes, los sonidos y ahora los algoritmos producen sentido, y llevo esas preguntas al aula.",
        "en": "I study how images, sounds and now algorithms make meaning, and I bring those questions into the classroom.",
        "pt": "Estudo como imagens, sons e agora algoritmos produzem sentido, e levo essas perguntas para a sala de aula.",
    },
    "descripcion_meta": {
        "es": "Juan Pablo Arrobo Agila, Ph.D. Docente investigador de la UTPL en comunicación y cultura audiovisual, semiótica de la imagen, narrativas sonoras e inteligencia artificial.",
        "en": "Juan Pablo Arrobo Agila, Ph.D. UTPL scholar in communication and audiovisual culture, visual semiotics, sound narratives and artificial intelligence.",
        "pt": "Juan Pablo Arrobo Agila, Ph.D. Pesquisador da UTPL em comunicação e cultura audiovisual, semiótica da imagem, narrativas sonoras e inteligência artificial.",
    },
    "bio_corta": {
        "es": [
            "Doctor en Comunicación por la Universidad de Huelva (España, 2021, <em>cum laude</em>). Magíster en Gerencia y Liderazgo Educacional (UTPL, 2014) y en Comunicación, Ideación y Creación de Contenidos con Inteligencia Artificial (UTPL, 2026).",
            "Es docente titular a tiempo completo de la UTPL desde 2019. Antes enseñó durante once años en la Pontificia Universidad Católica del Ecuador, sede Santo Domingo (2008–2019), donde dirigió la carrera de Comunicación Social entre 2013 y 2015.",
            "Su investigación se ocupa de la comunicación y la cultura audiovisual: la imagen y su significado, las nuevas narrativas audiovisuales y sonoras, y el papel de la inteligencia artificial en la producción y la enseñanza de la comunicación. Integra los grupos de investigación Comunicación y Cultura Audiovisual (GICA) e Innovación Tecnológica Educativa (GITEINNOEDUCA), y evalúa artículos para revistas científicas nacionales e internacionales.",
        ],
        "en": [
            "Ph.D. in Communication from the University of Huelva (Spain, 2021, <em>cum laude</em>). Master's degrees in Educational Management and Leadership (UTPL, 2014) and in Communication, Ideation and Content Creation with Artificial Intelligence (UTPL, 2026).",
            "He has been a tenured full-time lecturer at UTPL since 2019. Before that he taught for eleven years at the Pontificia Universidad Católica del Ecuador, Santo Domingo campus (2008–2019), where he directed the Social Communication programme from 2013 to 2015.",
            "His research deals with communication and audiovisual culture: the image and its meaning, new audiovisual and sound narratives, and the role of artificial intelligence in producing and teaching communication. He belongs to the research groups Communication and Audiovisual Culture (GICA) and Educational Technology Innovation (GITEINNOEDUCA), and reviews for national and international scholarly journals.",
        ],
        "pt": [
            "Doutor em Comunicação pela Universidade de Huelva (Espanha, 2021, <em>cum laude</em>). Mestre em Gestão e Liderança Educacional (UTPL, 2014) e em Comunicação, Ideação e Criação de Conteúdos com Inteligência Artificial (UTPL, 2026).",
            "É professor titular em tempo integral da UTPL desde 2019. Antes lecionou durante onze anos na Pontificia Universidad Católica del Ecuador, sede Santo Domingo (2008–2019), onde dirigiu o curso de Comunicação Social entre 2013 e 2015.",
            "Sua pesquisa trata da comunicação e da cultura audiovisual: a imagem e seu significado, as novas narrativas audiovisuais e sonoras, e o papel da inteligência artificial na produção e no ensino da comunicação. Integra os grupos de pesquisa Comunicação e Cultura Audiovisual (GICA) e Inovação Tecnológica Educativa (GITEINNOEDUCA) e avalia artigos para periódicos científicos nacionais e internacionais.",
        ],
    },
    # botones y etiquetas
    "ver_publicaciones": {"es": "Ver publicaciones", "en": "See publications", "pt": "Ver publicações"},
    "escribir": {"es": "Escribir un correo", "en": "Send an email", "pt": "Enviar um e-mail"},
    "ver_todo": {"es": "Ver todas", "en": "See all", "pt": "Ver todas"},
    "ir_cursos": {"es": "Ver los cursos", "en": "See the courses", "pt": "Ver os cursos"},
    "saltar": {"es": "Saltar al contenido", "en": "Skip to content", "pt": "Pular para o conteúdo"},
    "menu": {"es": "Menú", "en": "Menu", "pt": "Menu"},
    "idioma": {"es": "Idioma", "en": "Language", "pt": "Idioma"},
    "pie": {
        "es": "Fuente: redes académicas de Juan Pablo Arrobo-Agila.",
        "en": "Source: academic networks of Juan Pablo Arrobo-Agila.",
        "pt": "Fonte: redes acadêmicas de Juan Pablo Arrobo-Agila.",
    },
    # cifras
    "cifras_titulo": {"es": "Trayectoria en cifras", "en": "Record at a glance", "pt": "Trajetória em números"},
    "cifras_fuente": {
        "es": "Según el portal de investigación de la UTPL.",
        "en": "According to the UTPL research portal.",
        "pt": "Segundo o portal de pesquisa da UTPL.",
    },
    "c_articulos": {"es": "artículos científicos", "en": "journal articles", "pt": "artigos científicos"},
    "c_libros": {"es": "libros y obras colectivas", "en": "books and edited volumes", "pt": "livros e obras coletivas"},
    "c_proyectos": {"es": "proyectos de investigación, vinculación e innovación", "en": "research, outreach and innovation projects", "pt": "projetos de pesquisa, extensão e inovação"},
    "c_tesis": {"es": "trabajos de titulación dirigidos", "en": "theses supervised", "pt": "trabalhos de conclusão orientados"},
    # inicio
    "inicio_lineas": {"es": "Qué investigo", "en": "What I research", "pt": "O que pesquiso"},
    "inicio_recientes": {"es": "Publicaciones recientes", "en": "Recent publications", "pt": "Publicações recentes"},
    "inicio_ia_titulo": {"es": "Aprende haciendo con IA", "en": "Learn by doing with AI", "pt": "Aprenda fazendo com IA"},
    "inicio_ia_texto": {
        "es": "Talleres y cursos para que docentes de escuela, colegio y universidad usen la IA generativa con criterio pedagógico, creativo y ético.",
        "en": "Workshops and courses that help school and university teachers use generative AI with pedagogical, creative and ethical judgement.",
        "pt": "Oficinas e cursos para que professores da educação básica e do ensino superior usem a IA generativa com critério pedagógico, criativo e ético.",
    },
}

# ---------------------------------------------------------------- formación
FORMACION = [
    {"anio": "2026",
     "grado": {"es": "Magíster en Comunicación, Ideación y Creación de Contenidos con Inteligencia Artificial",
               "en": "Master's in Communication, Ideation and Content Creation with Artificial Intelligence",
               "pt": "Mestrado em Comunicação, Ideação e Criação de Conteúdos com Inteligência Artificial"},
     "inst": "Universidad Técnica Particular de Loja, Ecuador"},
    {"anio": "2021",
     "grado": {"es": "Doctor en Comunicación, mención <em>cum laude</em>",
               "en": "Ph.D. in Communication, <em>cum laude</em>",
               "pt": "Doutor em Comunicação, menção <em>cum laude</em>"},
     "inst": "Universidad de Huelva, España"},
    {"anio": "2014",
     "grado": {"es": "Magíster en Gerencia y Liderazgo Educacional",
               "en": "Master's in Educational Management and Leadership",
               "pt": "Mestrado em Gestão e Liderança Educacional"},
     "inst": "Universidad Técnica Particular de Loja, Ecuador"},
]

CERTIFICACIONES_IA = [
    {"anio": "2025",
     "titulo": {"es": "Microcredencial ChatGPT para Profesionales: Aplicaciones y Estrategias Avanzadas",
                "en": "Micro-credential ChatGPT for Professionals: Advanced Applications and Strategies",
                "pt": "Microcredencial ChatGPT para Profissionais: Aplicações e Estratégias Avançadas"},
     "inst": "Universidad de Granada, España"},
    {"anio": "2025",
     "titulo": {"es": "Curso de Especialización en Inteligencia Artificial en el Audiovisual",
                "en": "Specialisation Course in Artificial Intelligence in Audiovisual Production",
                "pt": "Curso de Especialização em Inteligência Artificial no Audiovisual"},
     "inst": "RTVE, España"},
    {"anio": "2025",
     "titulo": {"es": "Certificación en Competencias Digitales para Producción Multimedia con IA",
                "en": "Certificate in Digital Skills for Multimedia Production with AI",
                "pt": "Certificação em Competências Digitais para Produção Multimídia com IA"},
     "inst": "Universidad Técnica Particular de Loja, Ecuador"},
]

TRAYECTORIA = [
    {"periodo": {"es": "2019 – actualidad", "en": "2019 – present", "pt": "2019 – atual"},
     "cargo": {"es": "Docente titular a tiempo completo", "en": "Tenured full-time lecturer", "pt": "Professor titular em tempo integral"},
     "inst": "Universidad Técnica Particular de Loja"},
    {"periodo": {"es": "2026 – actualidad", "en": "2026 – present", "pt": "2026 – atual"},
     "cargo": {"es": "Integrante del equipo de calidad, Tecnología en Creación Audiovisual Digital",
               "en": "Quality committee member, Digital Audiovisual Creation programme",
               "pt": "Membro da equipe de qualidade, Tecnologia em Criação Audiovisual Digital"},
     "inst": "UTPL"},
    {"periodo": {"es": "2022 – 2026", "en": "2022 – 2026", "pt": "2022 – 2026"},
     "cargo": {"es": "Integrante del equipo de calidad, carrera de Comunicación",
               "en": "Quality committee member, Communication programme",
               "pt": "Membro da equipe de qualidade, curso de Comunicação"},
     "inst": "UTPL"},
    {"periodo": {"es": "2013 – 2015", "en": "2013 – 2015", "pt": "2013 – 2015"},
     "cargo": {"es": "Director de la carrera de Comunicación Social", "en": "Director, Social Communication programme", "pt": "Diretor do curso de Comunicação Social"},
     "inst": "Pontificia Universidad Católica del Ecuador, sede Santo Domingo"},
    {"periodo": {"es": "2008 – 2019", "en": "2008 – 2019", "pt": "2008 – 2019"},
     "cargo": {"es": "Docente", "en": "Lecturer", "pt": "Professor"},
     "inst": "Pontificia Universidad Católica del Ecuador, sede Santo Domingo"},
]

# ---------------------------------------------------------------- investigación
LINEAS = [
    {"id": "imagen",
     "titulo": {"es": "Imagen, signo y significado", "en": "Image, sign and meaning", "pt": "Imagem, signo e significado"},
     "texto": {
        "es": "Lectura semiótica de las formas visuales que circulan en la cultura mediática: memes, fotografía, paisaje urbano y símbolos nacionales. La pregunta de fondo es cómo una imagen llega a significar algo para una comunidad.",
        "en": "A semiotic reading of the visual forms that circulate in media culture: memes, photography, urban landscape and national symbols. The underlying question is how an image comes to mean something to a community.",
        "pt": "Leitura semiótica das formas visuais que circulam na cultura midiática: memes, fotografia, paisagem urbana e símbolos nacionais. A pergunta de fundo é como uma imagem passa a significar algo para uma comunidade.",
     }},
    {"id": "narrativas",
     "titulo": {"es": "Narrativas audiovisuales y sonoras", "en": "Audiovisual and sound narratives", "pt": "Narrativas audiovisuais e sonoras"},
     "texto": {
        "es": "Relatos en plataformas digitales, radio en línea y podcast, con atención a la oralidad y al patrimonio: cómo las leyendas, las tradiciones y la experiencia urbana encuentran nuevos formatos.",
        "en": "Stories on digital platforms, online radio and podcasts, with attention to orality and heritage: how legends, traditions and urban experience find new formats.",
        "pt": "Relatos em plataformas digitais, rádio online e podcast, com atenção à oralidade e ao patrimônio: como lendas, tradições e a experiência urbana encontram novos formatos.",
     }},
    {"id": "ia",
     "titulo": {"es": "Inteligencia artificial y comunicación", "en": "Artificial intelligence and communication", "pt": "Inteligência artificial e comunicação"},
     "texto": {
        "es": "Usos de la IA en la narrativa sonora y la producción de contenidos, y los dilemas éticos que abre para el periodismo: desinformación, autoría y gobernanza de las narrativas digitales.",
        "en": "Uses of AI in sound narrative and content production, and the ethical dilemmas it opens for journalism: disinformation, authorship and the governance of digital narratives.",
        "pt": "Usos da IA na narrativa sonora e na produção de conteúdos, e os dilemas éticos que ela abre para o jornalismo: desinformação, autoria e governança das narrativas digitais.",
     }},
    {"id": "competencias",
     "titulo": {"es": "Alfabetización mediática y periodismo", "en": "Media literacy and journalism", "pt": "Alfabetização midiática e jornalismo"},
     "texto": {
        "es": "Competencias audiovisuales de adolescentes y estudiantes de comunicación, ciudadanía comunicacional y calidad periodística en la cobertura de crisis.",
        "en": "Audiovisual competences of adolescents and communication students, communicative citizenship and journalistic quality in crisis coverage.",
        "pt": "Competências audiovisuais de adolescentes e estudantes de comunicação, cidadania comunicacional e qualidade jornalística na cobertura de crises.",
     }},
]

GRUPOS = [
    {"sigla": "GICA",
     "nombre": {"es": "Comunicación y Cultura Audiovisual", "en": "Communication and Audiovisual Culture", "pt": "Comunicação e Cultura Audiovisual"},
     "url": "https://investigacion.utpl.edu.ec/grupos"},
    {"sigla": "GITEINNOEDUCA",
     "nombre": {"es": "Innovación Tecnológica Educativa", "en": "Educational Technology Innovation", "pt": "Inovação Tecnológica Educativa"},
     "url": "https://investigacion.utpl.edu.ec/grupos/giteinnoeduca"},
]

ESTADO = {
    "curso": {"es": "En curso", "en": "Ongoing", "pt": "Em andamento"},
    "fin": {"es": "Finalizado", "en": "Completed", "pt": "Concluído"},
}

PROYECTOS = [
    {"anio": 2026, "estado": "curso", "tipo": {"es": "Investigación", "en": "Research", "pt": "Pesquisa"},
     "titulo": "Inteligencia artificial, desinformación y crisis de la verdad: gobernanza ética y alfabetización mediática en las narrativas digitales de Iberoamérica"},
    {"anio": 2026, "estado": "curso", "tipo": {"es": "Investigación", "en": "Research", "pt": "Pesquisa"},
     "titulo": "Dilemas éticos y narrativas multimedia frente a la IA. Perspectivas de periodistas y académicos latinoamericanos"},
    {"anio": 2021, "estado": "curso", "tipo": {"es": "Vinculación", "en": "Outreach", "pt": "Extensão"},
     "titulo": "Análisis de los espacios mediáticos y las competencias informacionales de usuarios y empresas"},
    {"anio": 2021, "estado": "fin", "tipo": {"es": "Investigación", "en": "Research", "pt": "Pesquisa"},
     "titulo": "Horizonte humanístico en las competencias comunicativas audiovisuales y nuevas narrativas de los adolescentes ecuatorianos"},
    {"anio": 2020, "estado": "fin", "tipo": {"es": "Investigación", "en": "Research", "pt": "Pesquisa"},
     "titulo": "Desarrollo de un modelo de intervención de los ciudadanos en los medios locales de comunicación social del Ecuador"},
    {"anio": 2020, "estado": "fin", "tipo": {"es": "Investigación", "en": "Research", "pt": "Pesquisa"},
     "titulo": "Estrategias y formatos de comunicación radiofónica y televisiva para la participación ciudadana frente a la COVID-19"},
]

INNOVACION = [
    (2025, "ChatGPT y su aplicación en el entorno de la comunicación y el periodismo"),
    (2025, "Leyendas ecuatorianas no contadas que renacen con voz e imagen en movimiento a través de IA"),
    (2023, "Memeando la comunicación: análisis semiótico de los memes mediáticos"),
    (2021, "Uso de Instagram para procesos de enseñanza-aprendizaje de la comunicación en Colombia y Ecuador"),
    (2021, "Buenas prácticas de rendición de cuentas en los medios de comunicación"),
    (2021, "Voces ciudadanas en la comunicación"),
    (2020, "Enseñanza de tradiciones, cuentos y leyendas ecuatorianas a través de elementos sonoros"),
    (2020, "Construcción de audiojuegos como herramienta de enseñanza y de valoración del sonido en la educación"),
    (2020, "Enseñanza del entorno de la comunicación social a través de diálogos con los líderes del Ecuador"),
    (2020, "Ciudadanía comunicacional emergente"),
    (2020, "Gamificación de videos educativos para mejorar la enseñanza de la biología"),
    (2020, "Generación de recursos educativos para la enseñanza de la administración estratégica"),
    (2019, "Mejoramiento del Museo Matilde Hidalgo de Prócel a través de la aplicación de técnicas de comunicación integral"),
]

# ---------------------------------------------------------------- publicaciones
# tipo: indexado | capitulo | congreso | regional | divulgacion
# linea: id de LINEAS (para relacionar en la página de investigación)
PUBLICACIONES = [
    {"anio": 2025, "tipo": "indexado", "linea": "narrativas",
     "ref": "Arrobo-Agila, J. P., Suing Ortiz, A., & Barrazueta, P. (2025). Narraciones audiovisuales en América Latina ante la inseguridad: Bogotá, Guayaquil y San Salvador en plataformas digitales. <em>Street Art &amp; Urban Creativity, 11</em>(8), 51–64.",
     "doi": "10.62161/sauc.v11.6082"},
    {"anio": 2025, "tipo": "indexado", "linea": "imagen",
     "ref": "Arrobo-Agila, J. P., Gonzales Córdova, M. P., & Barrazueta Molina, P. (2025). El lenguaje y el significado de los memes mediáticos desde una perspectiva semiótica. <em>European Public &amp; Social Innovation Review, 10</em>, 1–18.",
     "doi": "10.31637/epsir-2025-1040"},
    {"anio": 2025, "tipo": "indexado", "linea": "narrativas",
     "ref": "Arrobo-Agila, J. P., Suing, A., Loyola Sarmiento, M., & Almachi Oñate, C. (2025). Transformando la oralidad: El podcast para conservar tradiciones y leyendas ecuatorianas. <em>VISUAL REVIEW. International Visual Culture Review, 17</em>(5), 99–111.",
     "doi": "10.62161/revvisual.v17.5925"},
    {"anio": 2024, "tipo": "indexado", "linea": "narrativas",
     "ref": "Yaguana Romero, H., & Arrobo-Agila, J. P. (2024). Impacto del burnout y estrés laboral en productoras audiovisuales de Ecuador: Un enfoque investigativo. <em>European Public &amp; Social Innovation Review, 9</em>, 1–16.",
     "doi": "10.31637/epsir-2024-1025"},
    {"anio": 2024, "tipo": "regional", "linea": "imagen",
     "ref": "Punín, M. I., Arrobo Agila, J. P., & Mendoza, M. del C. (2024). Cantemos todos: Semántica de himnos nacionales de Colombia, Ecuador, Perú y Venezuela. <em>Textos y Contextos, 1</em>(28).",
     "doi": "10.29166/tyc.v1i28.5058"},
    {"anio": 2023, "tipo": "indexado", "linea": "competencias",
     "ref": "Suing, A., Arrobo-Agila, J. P., Coronado-Otavalo, X., Galarza-Ligña, V., & Reascos-Trujillo, A. (2023). Audiovisual competences in times of COVID-19: The role of educational actors in media and digital learning of adolescents. <em>Sustainability, 15</em>(7), 6323.",
     "doi": "10.3390/su15076323"},
    {"anio": 2023, "tipo": "capitulo", "linea": "competencias",
     "ref": "Suing, A., Arrobo-Agila, J. P., & González-Rentería, V. (2023). Perspectives of media competence in communication and journalism careers in the Andean area. En <em>Smart Innovation, Systems and Technologies</em> (pp. 555–565). Springer Nature Singapore.",
     "doi": "10.1007/978-981-19-6585-2_49"},
    {"anio": 2022, "tipo": "indexado", "linea": "ia",
     "ref": "Yaguana Romero, H., Arrobo-Agila, J. P., & Rene Jaramillo, A. (2022). La inteligencia artificial en la narrativa sonora. Estudio de caso. <em>Anàlisi, 66</em>, 9–23.",
     "doi": "10.5565/rev/analisi.3476"},
    {"anio": 2022, "tipo": "indexado", "linea": "competencias",
     "ref": "Fernández-Álvarez, N., Yaguana-Romero, H., & Arrobo-Agila, J. P. (2022). Internet, dispositivos inteligentes y familia, caso de estudio, estudiantes UTPL Madrid. <em>TECHNO REVIEW. International Technology, Science and Society Review, 12</em>(4), 1–8.",
     "doi": "10.37467/revtechno.v11.4474"},
    {"anio": 2022, "tipo": "indexado", "linea": "competencias",
     "ref": "Vega-Saritama, C. X., Yaguana-Romero, H. A., & Arrobo-Agila, J. P. (2022). Uso del celular en el periodístico deportivo, caso de estudio Loja – Ecuador. <em>VISUAL REVIEW. International Visual Culture Review, 10</em>(3), 1–10.",
     "doi": "10.37467/revvisual.v9.3599"},
    {"anio": 2022, "tipo": "indexado", "linea": "imagen",
     "ref": "Barrazueta, P., Arrobo, J. P., & Cartuche Flores, C. (2022). Abrazos y protección. Emociones incluidas. <em>Fotocinema. Revista Científica de Cine y Fotografía</em>, (24), 397–415.",
     "doi": "10.24310/Fotocinema.2022.vi24.13706"},
    {"anio": 2022, "tipo": "indexado", "linea": "competencias",
     "ref": "<em>Teaching of communicators facing the digital transition. UTPL case</em> (2022). Scopus.",
     "url": "https://www.scopus.com/record/display.uri?eid=2-s2.0-85127545921&origin=resultslist", "incompleta": True},
    {"anio": 2022, "tipo": "regional", "linea": "competencias",
     "ref": "Suing, A., Arrobo-Agila, J. P., & Carrión, N. (2022). Uso de medios sociales en los estudios de licenciatura en comunicación en Ecuador. <em>Brazilian Journal of Development, 8</em>(11), 73952–73963.",
     "doi": "10.34117/bjdv8n11-210"},
    {"anio": 2021, "tipo": "indexado", "linea": "competencias",
     "ref": "<em>El papel de las redes sociales en los desastres naturales. El caso de Facebook y el terremoto de Ecuador en 2016</em> (2021). Scopus.",
     "url": "https://www.scopus.com/record/display.uri?eid=2-s2.0-85101921381&origin=resultslist", "incompleta": True},
    {"anio": 2021, "tipo": "indexado", "linea": "narrativas",
     "ref": "<em>Formato audiovisual para la intervención ciudadana en los medios de comunicación</em> (2021). Scopus.",
     "url": "https://www.scopus.com/record/display.uri?eid=2-s2.0-85128728212&origin=resultslist", "incompleta": True},
    {"anio": 2021, "tipo": "indexado", "linea": "competencias",
     "ref": "<em>Propuesta para innovación en la enseñanza de comunicación. Caso: Diálogos con líderes</em> (2021). Scopus.",
     "url": "https://www.scopus.com/record/display.uri?eid=2-s2.0-85118728128&origin=resultslist", "incompleta": True},
    {"anio": 2021, "tipo": "congreso", "linea": "narrativas",
     "ref": "Yaguana Romero, H., Romero, M. N., & Arrobo Agila, J. P. (2021). Online radio in Ecuador: Findings and new features. En <em>2021 16th Iberian Conference on Information Systems and Technologies (CISTI)</em> (pp. 1–5). IEEE.",
     "doi": "10.23919/CISTI52073.2021.9476351"},
    {"anio": 2021, "tipo": "congreso", "linea": "competencias",
     "ref": "Suing, A., Carpio-Jiménez, L., Ordóñez, K., & Arrobo, J. P. (2021). Presence and characteristics of communicational citizenship in Ecuador's mass media. En <em>2021 16th Iberian Conference on Information Systems and Technologies (CISTI)</em> (pp. 1–5). IEEE.",
     "doi": "10.23919/CISTI52073.2021.9476648"},
    {"anio": 2020, "tipo": "indexado", "linea": "competencias",
     "ref": "<em>La dimensión humana en la cobertura periodística de las consecuencias de los terremotos ocurridos en Perú (2007) y Ecuador (2016)</em> (2020). Scopus.",
     "url": "https://www.scopus.com/record/display.uri?eid=2-s2.0-85079459318&origin=resultslist", "incompleta": True},
    {"anio": 2020, "tipo": "regional", "linea": "competencias",
     "ref": "Arrobo-Agila, J. P., Mendoza, M., & Aguaded, J. I. (2020). La calidad periodística en la cobertura de terremotos: Caso Ecuador. <em>Ámbitos. Revista Internacional de Comunicación</em>, (50), 193–207.",
     "doi": "10.12795/Ambitos.2020.i50.13"},
    {"anio": 2020, "tipo": "congreso", "linea": "competencias",
     "ref": "Suing, A., Puertas-Hidalgo, R., & Arrobo, J. P. (2020). Conditions demanded by Ecuadorian students to start communication companies. En <em>2020 15th Iberian Conference on Information Systems and Technologies (CISTI)</em> (pp. 1–4). IEEE.",
     "doi": "10.23919/CISTI49556.2020.9141054"},
    {"anio": 2017, "tipo": "regional", "linea": "competencias",
     "ref": "Suing, A., Arrobo, J. P., & Carrión, N. (2017). Empleo de las redes sociales en la formación de comunicadores sociales en Ecuador. <em>Interfaces Científicas – Educação, 5</em>(3), 9–16.",
     "doi": "10.17564/2316-3828.2017v5n3p9-16"},
    {"anio": 2015, "tipo": "congreso", "linea": "narrativas",
     "ref": "Suing, A., & Arrobo, J. P. (2015). Social networks of cultural programs in television of Ecuador. En <em>2015 10th Iberian Conference on Information Systems and Technologies (CISTI)</em> (pp. 1–6). IEEE.",
     "doi": "10.1109/CISTI.2015.7170584"},
    {"anio": 2015, "tipo": "divulgacion", "linea": "narrativas",
     "ref": "<em>Social media in the promotion of cultural content in television, analysis of case in Ecuador</em> (2015). Revista de Comunicación.",
     "url": "https://revistadecomunicacion.com/issue/view/166/22", "incompleta": True},
]

TIPOS_PUB = {
    "indexado": {"es": "Artículos en Scopus y Web of Science", "en": "Scopus and Web of Science articles", "pt": "Artigos na Scopus e Web of Science"},
    "regional": {"es": "Artículos en revistas regionales", "en": "Articles in regional journals", "pt": "Artigos em periódicos regionais"},
    "capitulo": {"es": "Capítulos de libro", "en": "Book chapters", "pt": "Capítulos de livro"},
    "congreso": {"es": "Actas de congreso", "en": "Conference proceedings", "pt": "Anais de congresso"},
    "divulgacion": {"es": "Divulgación", "en": "Outreach", "pt": "Divulgação"},
}

LIBROS = [
    {"anio": 2023, "tipo": "divulgacion", "titulo": "La ciudad habla: La contaminación visual y su impacto en los centros históricos"},
    {"anio": 2023, "tipo": "cientifico", "titulo": "La investigación al servicio de la sociedad, Tomo II"},
    {"anio": 2022, "tipo": "divulgacion", "titulo": "El giro audiovisual, entre lo humano y lo tecnológico. Las perspectivas de las plataformas, pantallas y sonoridades"},
    {"anio": 2022, "tipo": "divulgacion", "titulo": "Comunicación audiovisual, educación y tecnología. Cruces y experiencias con el entorno digital"},
    {"anio": 2022, "tipo": "divulgacion", "titulo": "Redes sociales y ciudadanía. Ciberculturas para el aprendizaje"},
    {"anio": 2022, "tipo": "actas", "titulo": "Libro de actas del Congreso CUICIID 2022"},
    {"anio": 2021, "tipo": "cientifico", "titulo": "Ecosistema de una pandemia. COVID-19, la transformación mundial"},
    {"anio": 2021, "tipo": "actas", "titulo": "Universidad, innovación e investigación ante el horizonte 2030"},
    {"anio": 2021, "tipo": "actas", "titulo": "Memorias X Investiga UTPL. Webinars 2021"},
    {"anio": 2020, "tipo": "actas", "titulo": "Memorias IX Investiga UTPL 2020"},
    {"anio": 2018, "tipo": "cientifico", "titulo": "La comunicación ante el ciudadano"},
    {"anio": 2018, "tipo": "actas", "titulo": "CUICIID 2018: Congreso Universitario Internacional sobre la Comunicación en la Profesión y en la Universidad de Hoy"},
    {"anio": 2018, "tipo": "actas", "titulo": "Las TIC como plataforma de teleformación e innovación educativa en las aulas"},
]

TIPOS_LIBRO = {
    "cientifico": {"es": "Libro científico", "en": "Scholarly book", "pt": "Livro científico"},
    "divulgacion": {"es": "Libro de divulgación", "en": "Outreach book", "pt": "Livro de divulgação"},
    "actas": {"es": "Libro de actas", "en": "Proceedings volume", "pt": "Livro de anais"},
}

# ---------------------------------------------------------------- docencia
ASIGNATURAS = [
    {"nombre": {"es": "Semiótica", "en": "Semiotics", "pt": "Semiótica"},
     "nivel": {"es": "Grado, Comunicación. Desde 2021, presencial, a distancia y en línea.",
               "en": "Undergraduate, Communication. Since 2021, on campus, distance and online.",
               "pt": "Graduação, Comunicação. Desde 2021, presencial, a distância e online."}},
    {"nombre": {"es": "Tendencias de la Comunicación", "en": "Trends in Communication", "pt": "Tendências da Comunicação"},
     "nivel": {"es": "Grado, Comunicación.", "en": "Undergraduate, Communication.", "pt": "Graduação, Comunicação."}},
    {"nombre": {"es": "Radio", "en": "Radio", "pt": "Rádio"},
     "nivel": {"es": "Grado, Comunicación.", "en": "Undergraduate, Communication.", "pt": "Graduação, Comunicação."}},
    {"nombre": {"es": "Comunicación audiovisual, humanismo y tecnología", "en": "Audiovisual Communication, Humanism and Technology", "pt": "Comunicação audiovisual, humanismo e tecnologia"},
     "nivel": {"es": "Grado, Comunicación.", "en": "Undergraduate, Communication.", "pt": "Graduação, Comunicação."}},
    {"nombre": {"es": "Analítica del aprendizaje para la innovación", "en": "Learning Analytics for Innovation", "pt": "Analítica da aprendizagem para a inovação"},
     "nivel": {"es": "Posgrado, en línea. Desde 2025.", "en": "Postgraduate, online. Since 2025.", "pt": "Pós-graduação, online. Desde 2025."}},
    {"nombre": {"es": "Prácticum, trabajo de titulación e integración curricular", "en": "Practicum, final projects and capstone", "pt": "Prática, trabalho de conclusão e integração curricular"},
     "nivel": {"es": "Grado en Comunicación y Tecnología en Creación Audiovisual Digital.",
               "en": "Communication degree and Digital Audiovisual Creation technical programme.",
               "pt": "Graduação em Comunicação e Tecnologia em Criação Audiovisual Digital."}},
]

# ---------------------------------------------------------------- capacitación IA
CURSOS = [
    {
        "id": "docencia-produccion",
        "titulo": {"es": "Herramientas de inteligencia artificial para la docencia y la producción creativa",
                   "en": "Artificial intelligence tools for teaching and creative production",
                   "pt": "Ferramentas de inteligência artificial para a docência e a produção criativa"},
        "formato": {"es": "Curso", "en": "Course", "pt": "Curso"},
        "publico": {"es": "Docentes y estudiantes interesados en la producción de contenidos",
                    "en": "Teachers and students interested in content production",
                    "pt": "Professores e estudantes interessados na produção de conteúdos"},
        "duracion": {"es": "40 horas académicas, en tres módulos", "en": "40 academic hours, in three modules", "pt": "40 horas acadêmicas, em três módulos"},
        "modalidad": {"es": "En línea, en fechas y horarios de acuerdo a su disponibilidad", "en": "Online, on dates and times that suit you", "pt": "Online, em datas e horários de acordo com sua disponibilidade"},
        "imagen": {"archivo": "curso-herramientas-ia",
                   "alt": {"es": "Afiche del curso Herramientas de IA para la docencia y la producción creativa, con Juan Pablo Arrobo, Ph.D.: 40 horas académicas, modalidad en línea, fechas y horario de acuerdo a su disponibilidad, certificado avalado por el Instituto Japón.",
                           "en": "Poster for the course AI Tools for Teaching and Creative Production with Juan Pablo Arrobo, Ph.D.: 40 academic hours, online, dates and times to suit you, certificate endorsed by Instituto Japón.",
                           "pt": "Cartaz do curso Ferramentas de IA para a docência e a produção criativa com Juan Pablo Arrobo, Ph.D.: 40 horas acadêmicas, online, datas e horários de acordo com sua disponibilidade, certificado chancelado pelo Instituto Japón."}},
        "resumen": {
            "es": "Parte de una pregunta básica, qué puede y qué no puede hacer la IA generativa, y termina en la producción de un video de 30 segundos con logo, guion técnico, storyboard y audio. En el camino se trabaja la escritura de prompts, la verificación de resultados y los chatbots educativos.",
            "en": "It starts from a basic question, what generative AI can and cannot do, and ends with the production of a 30-second video with logo, technical script, storyboard and audio. Along the way it covers prompt writing, checking outputs and educational chatbots.",
            "pt": "Parte de uma pergunta básica, o que a IA generativa pode e não pode fazer, e termina na produção de um vídeo de 30 segundos com logotipo, roteiro técnico, storyboard e áudio. No caminho, trabalha-se a escrita de prompts, a verificação de resultados e os chatbots educativos.",
        },
        "contenidos": {
            "es": ["Fundamentos pedagógicos: la naturaleza probabilística de la IA y la opacidad algorítmica",
                   "Ética, sesgos, autoría e integridad académica; validación con fuentes",
                   "Estructura del prompt: rol, contexto, información, propósito y formato",
                   "Chatbots educativos por asignatura y nivel",
                   "IA para investigar y organizar ideas visualmente",
                   "Producción audiovisual: guion, voz, música, imagen y edición"],
            "en": ["Pedagogical foundations: the probabilistic nature of AI and algorithmic opacity",
                   "Ethics, bias, authorship and academic integrity; checking against sources",
                   "Prompt structure: role, context, information, purpose and format",
                   "Educational chatbots by subject and level",
                   "AI for research and visual organisation of ideas",
                   "Audiovisual production: script, voice, music, image and editing"],
            "pt": ["Fundamentos pedagógicos: a natureza probabilística da IA e a opacidade algorítmica",
                   "Ética, vieses, autoria e integridade acadêmica; validação com fontes",
                   "Estrutura do prompt: papel, contexto, informação, propósito e formato",
                   "Chatbots educativos por disciplina e nível",
                   "IA para pesquisar e organizar ideias visualmente",
                   "Produção audiovisual: roteiro, voz, música, imagem e edição"],
        },
        "productos": {
            "es": ["Un chatbot educativo configurado para una asignatura",
                   "Un video de 30 segundos producido con IA, del guion al montaje"],
            "en": ["An educational chatbot set up for one subject",
                   "A 30-second video produced with AI, from script to edit"],
            "pt": ["Um chatbot educativo configurado para uma disciplina",
                   "Um vídeo de 30 segundos produzido com IA, do roteiro à montagem"],
        },
        "herramientas": ["ChatGPT", "Gemini", "Google AI Studio", "NotebookLM", "Napkin AI", "Leonardo AI", "Suno", "ElevenLabs", "CapCut"],
        "enlace": None,
    },
    {
        "id": "recursos-docentes",
        "titulo": {"es": "Creación de recursos docentes con IA",
                   "en": "Creating teaching resources with AI",
                   "pt": "Criação de recursos docentes com IA"},
        "formato": {"es": "Curso", "en": "Course", "pt": "Curso"},
        "publico": {"es": "Docentes de bachillerato y universidad",
                    "en": "Upper-secondary and university teachers",
                    "pt": "Professores do ensino médio e universitário"},
        "duracion": {"es": "40 horas académicas", "en": "40 academic hours", "pt": "40 horas acadêmicas"},
        "modalidad": {"es": "Presencial o en línea", "en": "In person or online", "pt": "Presencial ou online"},
        "resumen": {
            "es": "Un taller para producir, con IA generativa, los materiales de una unidad didáctica completa y publicarlos en el aula virtual. El punto de partida no es la herramienta sino el objetivo de aprendizaje: primero se decide qué debe lograr el estudiante y después qué recurso lo ayuda.",
            "en": "A workshop for producing, with generative AI, the materials for a complete teaching unit and publishing them in the virtual classroom. The starting point is the learning goal, not the tool: first decide what students should achieve, then which resource helps them get there.",
            "pt": "Uma oficina para produzir, com IA generativa, os materiais de uma unidade didática completa e publicá-los no ambiente virtual. O ponto de partida não é a ferramenta, mas o objetivo de aprendizagem: primeiro se decide o que o estudante deve alcançar e depois qual recurso o ajuda.",
        },
        "contenidos": {
            "es": ["Del prompt al complemento",
                   "El nuevo prompt se llama Skills",
                   "Materiales escritos: guías de estudio, casos, rúbricas y bancos de preguntas",
                   "Recursos visuales: infografías, esquemas e ilustraciones",
                   "Audio y video: narración con voz sintética, podcast y video con avatar",
                   "Uso de chatbots para el aula y la gestión académica",
                   "Recursos accesibles: un mismo material adaptado a distintos niveles, lectura fácil y subtítulos",
                   "Evaluación en tiempos de IA: tareas que la IA no resuelve sola y que muestran el proceso del estudiante",
                   "Verificación, derechos de autor y transparencia en el uso de IA"],
            "en": ["From prompt to plug-in",
                   "The new prompt is called Skills",
                   "Written materials: study guides, cases, rubrics and question banks",
                   "Visual resources: infographics, diagrams and illustrations",
                   "Audio and video: synthetic-voice narration, podcasts and avatar video",
                   "Chatbots for the classroom and academic management",
                   "Accessible resources: one material adapted to different levels, easy-read versions and captions",
                   "Assessment in the age of AI: tasks AI cannot solve alone and that show the student's process",
                   "Fact-checking, copyright and transparency about AI use"],
            "pt": ["Do prompt ao complemento",
                   "O novo prompt se chama Skills",
                   "Materiais escritos: guias de estudo, casos, rubricas e bancos de questões",
                   "Recursos visuais: infográficos, esquemas e ilustrações",
                   "Áudio e vídeo: narração com voz sintética, podcast e vídeo com avatar",
                   "Uso de chatbots para a sala de aula e a gestão acadêmica",
                   "Recursos acessíveis: um mesmo material adaptado a diferentes níveis, leitura fácil e legendas",
                   "Avaliação em tempos de IA: tarefas que a IA não resolve sozinha e que mostram o processo do estudante",
                   "Verificação, direitos autorais e transparência no uso de IA"],
        },
        "productos": {
            "es": ["Un kit de recursos para una unidad didáctica real, listo para el aula virtual",
                   "Una guía propia de prompts para seguir produciendo materiales"],
            "en": ["A resource kit for a real teaching unit, ready for the virtual classroom",
                   "A personal prompt guide to keep producing materials"],
            "pt": ["Um kit de recursos para uma unidade didática real, pronto para o ambiente virtual",
                   "Um guia próprio de prompts para continuar produzindo materiais"],
        },
        "herramientas": ["ChatGPT", "Claude", "Gemini", "NotebookLM", "Napkin", "Leonardo", "Canva", "ElevenLabs", "HeyGen"],
        "enlace": None,
    },
    {
        "id": "tiza-codigo",
        "titulo": {"es": "De la tiza al código: la educación evoluciona con la IA",
                   "en": "From chalk to code: education evolves with AI",
                   "pt": "Do giz ao código: a educação evolui com a IA"},
        "formato": {"es": "Taller", "en": "Workshop", "pt": "Oficina"},
        "publico": {"es": "Docentes de educación primaria y secundaria",
                    "en": "Primary and secondary school teachers",
                    "pt": "Professores do ensino fundamental e médio"},
        "duracion": {"es": "10 horas, teoría y práctica", "en": "10 hours, theory and practice", "pt": "10 horas, teoria e prática"},
        "modalidad": {"es": "Presencial, grupos de 30 a 40 docentes", "en": "In person, groups of 30 to 40 teachers", "pt": "Presencial, grupos de 30 a 40 professores"},
        "resumen": {
            "es": "Un taller para llevar la IA generativa al aula escolar con sentido pedagógico. Los docentes trabajan por nivel o área (Lengua, Ciencias, Matemática) y salen con productos que pueden usar al día siguiente en sus clases.",
            "en": "A workshop for bringing generative AI into the school classroom with a clear pedagogical purpose. Teachers work by level or subject (Language, Science, Maths) and leave with materials they can use in class the next day.",
            "pt": "Uma oficina para levar a IA generativa à sala de aula escolar com sentido pedagógico. Os professores trabalham por nível ou área (Língua, Ciências, Matemática) e saem com produtos que podem usar no dia seguinte.",
        },
        "contenidos": {
            "es": ["Asistentes conversacionales y chatbots educativos por área",
                   "Planificación asistida y organización de ideas: mapas, esquemas y documentos",
                   "Creación de imágenes, música, video y avatares para recursos didácticos",
                   "Transcripción y resumen de sesiones",
                   "Uso ético de la IA en la escuela: la IA potencia al docente, no lo reemplaza"],
            "en": ["Conversational assistants and subject-specific educational chatbots",
                   "AI-assisted planning and idea organisation: maps, diagrams and documents",
                   "Creating images, music, video and avatars for teaching resources",
                   "Transcribing and summarising sessions",
                   "Ethical AI use at school: AI empowers teachers, it does not replace them"],
            "pt": ["Assistentes conversacionais e chatbots educativos por área",
                   "Planejamento assistido e organização de ideias: mapas, esquemas e documentos",
                   "Criação de imagens, música, vídeo e avatares para recursos didáticos",
                   "Transcrição e resumo de sessões",
                   "Uso ético da IA na escola: a IA potencializa o professor, não o substitui"],
        },
        "productos": {
            "es": ["Secuencias didácticas que integran herramientas de IA",
                   "Recursos visuales, narrativos y audiovisuales generados con IA",
                   "Portafolio digital docente con planificación asistida",
                   "Propuesta de integración curricular de la IA para la institución"],
            "en": ["Lesson sequences that integrate AI tools",
                   "Visual, narrative and audiovisual resources generated with AI",
                   "A digital teaching portfolio with AI-assisted planning",
                   "A proposal for integrating AI into the school curriculum"],
            "pt": ["Sequências didáticas que integram ferramentas de IA",
                   "Recursos visuais, narrativos e audiovisuais gerados com IA",
                   "Portfólio digital docente com planejamento assistido",
                   "Proposta de integração curricular da IA para a instituição"],
        },
        "herramientas": ["ChatGPT", "Chatbots educativos", "NotebookLM", "Notion", "Napkin", "Ideamap.ai", "Tactiq", "Leonardo", "Suno", "Runway", "HeyGen"],
        "enlace": None,
    },
]

PESTANAS = {
    "secciones": {"es": "Secciones de esta página", "en": "Sections on this page", "pt": "Seções desta página"},
    "perfil": {"es": "Perfil", "en": "Profile", "pt": "Perfil"},
    "lineas": {"es": "Qué investigo", "en": "What I research", "pt": "O que pesquiso"},
    "recientes": {"es": "Publicaciones recientes", "en": "Recent publications", "pt": "Publicações recentes"},
    "ia": {"es": "Capacitación en IA", "en": "AI training", "pt": "Formação em IA"},
    "otras": {"es": "Capítulos, actas y divulgación", "en": "Chapters, proceedings and outreach", "pt": "Capítulos, anais e divulgação"},
    "instructor": {"es": "Formación del instructor", "en": "Instructor's credentials", "pt": "Formação do instrutor"},
}

TC = {  # textos de la página de capacitación
    "intro": {
        "es": "Aprenda a usar la inteligencia artificial con criterio pedagógico: qué hace bien, dónde se equivoca y cómo convertirla en una aliada para enseñar mejor. Cada curso combina práctica guiada y reflexión, y termina con materiales que usted lleva directamente a su aula.",
        "en": "Learn to use artificial intelligence with sound pedagogical judgement: what it does well, where it gets things wrong and how to make it an ally for better teaching. Each course combines guided practice and reflection, and ends with materials you can take straight into your classroom.",
        "pt": "Aprenda a usar a inteligência artificial com critério pedagógico: o que ela faz bem, onde erra e como transformá-la em aliada para ensinar melhor. Cada curso combina prática guiada e reflexão e termina com materiais que você leva diretamente para sua sala de aula.",
    },
    "publico": {"es": "Dirigido a", "en": "For", "pt": "Público"},
    "duracion": {"es": "Duración", "en": "Length", "pt": "Duração"},
    "modalidad": {"es": "Modalidad", "en": "Format", "pt": "Modalidade"},
    "contenidos": {"es": "Temáticas", "en": "Topics", "pt": "Temáticas"},
    "productos": {"es": "Lo que se lleva cada participante", "en": "What participants take away", "pt": "O que cada participante leva"},
    "herramientas": {"es": "Herramientas", "en": "Tools", "pt": "Ferramentas"},
    "solicitar": {"es": "Solicitar información", "en": "Request information", "pt": "Solicitar informações"},
    "asunto": {"es": "Consulta sobre el curso", "en": "Enquiry about the course", "pt": "Consulta sobre o curso"},
    "aval_titulo": {"es": "Formación del instructor en IA", "en": "Instructor's AI credentials", "pt": "Formação do instrutor em IA"},
    "innov_titulo": {"es": "Proyectos de innovación docente con IA", "en": "Teaching innovation projects with AI", "pt": "Projetos de inovação docente com IA"},
    "a_medida": {
        "es": "Los cursos se adaptan al nivel educativo, al número de participantes y a la plataforma de la institución. Escríbame para coordinar fechas, contenidos y certificación.",
        "en": "Courses are adapted to the educational level, group size and the institution's platform. Write to me to arrange dates, contents and certification.",
        "pt": "Os cursos se adaptam ao nível de ensino, ao número de participantes e à plataforma da instituição. Escreva-me para combinar datas, conteúdos e certificação.",
    },
}
