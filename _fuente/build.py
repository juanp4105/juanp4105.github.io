# -*- coding: utf-8 -*-
"""
Genera el sitio estático en tres idiomas.

Uso (desde la carpeta raíz del sitio):
    python3 _fuente/build.py

Escribe index.html y las demás páginas en la raíz (español), en en/ (inglés)
y en pt/ (portugués), además de sitemap.xml.
"""
import os
import sys
from collections import OrderedDict

from jinja2 import Environment, FileSystemLoader, select_autoescape

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
import contenido as C  # noqa: E402

# Textos propios de cada página (encabezados e introducciones)
P = {
    "investigacion_titulo": {"es": "Investigación", "en": "Research", "pt": "Pesquisa"},
    "investigacion_intro": {
        "es": "Mi trabajo se ubica en la línea de Comunicación y Cultura Audiovisual. Cuatro ejes organizan lo que publico y los proyectos en los que participo.",
        "en": "My work sits within the Communication and Audiovisual Culture research line. Four strands organise what I publish and the projects I take part in.",
        "pt": "Meu trabalho se situa na linha de Comunicação e Cultura Audiovisual. Quatro eixos organizam o que publico e os projetos de que participo.",
    },
    "lineas_titulo": {"es": "Líneas de investigación", "en": "Research lines", "pt": "Linhas de pesquisa"},
    "relacionadas": {"es": "Publicaciones de esta línea", "en": "Publications in this line", "pt": "Publicações desta linha"},
    "grupos_titulo": {"es": "Grupos de investigación", "en": "Research groups", "pt": "Grupos de pesquisa"},
    "proyectos_titulo": {"es": "Proyectos", "en": "Projects", "pt": "Projetos"},
    "proyectos_nota": {
        "es": "Proyectos de investigación y vinculación registrados en la UTPL. Los proyectos de innovación docente están en Docencia.",
        "en": "Research and outreach projects registered at UTPL. Teaching innovation projects are listed under Teaching.",
        "pt": "Projetos de pesquisa e extensão registrados na UTPL. Os projetos de inovação docente estão em Docência.",
    },
    "formacion_titulo": {"es": "Formación", "en": "Education", "pt": "Formação"},
    "pub_titulo": {"es": "Publicaciones", "en": "Publications", "pt": "Publicações"},
    "pub_intro": {
        "es": "Artículos, capítulos y actas en formato APA 7, con enlace al DOI cuando existe. La lista completa y las citas actualizadas están en Google Scholar, ORCID y Scopus.",
        "en": "Articles, chapters and proceedings in APA 7 style, with a DOI link where one exists. The full list and up-to-date citations are on Google Scholar, ORCID and Scopus.",
        "pt": "Artigos, capítulos e anais no formato APA 7, com link para o DOI quando existe. A lista completa e as citações atualizadas estão no Google Scholar, ORCID e Scopus.",
    },
    "filtrar": {"es": "Mostrar", "en": "Show", "pt": "Mostrar"},
    "todas": {"es": "Todas", "en": "All", "pt": "Todas"},
    "libros_titulo": {"es": "Libros y obras colectivas", "en": "Books and edited volumes", "pt": "Livros e obras coletivas"},
    "libros_nota": {
        "es": "Libros en los que he participado como autor, coautor o coordinador, según el registro de la UTPL.",
        "en": "Books I have contributed to as author, co-author or editor, according to the UTPL record.",
        "pt": "Livros dos quais participei como autor, coautor ou organizador, segundo o registro da UTPL.",
    },
    "ver_registro": {"es": "Ver registro", "en": "View record", "pt": "Ver registro"},
    "doc_titulo": {"es": "Docencia", "en": "Teaching", "pt": "Docência"},
    "doc_intro": {
        "es": "Enseño semiótica, comunicación audiovisual y radio en la carrera de Comunicación de la UTPL, y acompaño trabajos de titulación de grado y posgrado. Desde 2019 la mayor parte de mis proyectos de innovación docente prueba formatos sonoros, visuales y, más recientemente, de inteligencia artificial.",
        "en": "I teach semiotics, audiovisual communication and radio in UTPL's Communication degree, and supervise undergraduate and postgraduate theses. Since 2019 most of my teaching innovation projects have tested sound and visual formats and, more recently, artificial intelligence.",
        "pt": "Ensino semiótica, comunicação audiovisual e rádio no curso de Comunicação da UTPL e oriento trabalhos de conclusão de graduação e pós-graduação. Desde 2019, a maior parte dos meus projetos de inovação docente testa formatos sonoros, visuais e, mais recentemente, de inteligência artificial.",
    },
    "asignaturas_titulo": {"es": "Asignaturas", "en": "Courses", "pt": "Disciplinas"},
    "tesis_titulo": {"es": "Dirección de trabajos de titulación", "en": "Thesis supervision", "pt": "Orientação de trabalhos de conclusão"},
    "tesis_texto": {
        "es": "He dirigido 30 trabajos de titulación de grado y de maestría en la UTPL, sobre narrativas digitales, comunicación audiovisual y medios. Los trabajos se pueden consultar en el repositorio institucional.",
        "en": "I have supervised 30 undergraduate and master's theses at UTPL on digital narratives, audiovisual communication and media. The theses are available in the institutional repository.",
        "pt": "Orientei 30 trabalhos de conclusão de graduação e de mestrado na UTPL sobre narrativas digitais, comunicação audiovisual e mídia. Os trabalhos podem ser consultados no repositório institucional.",
    },
    "repositorio": {"es": "Abrir el repositorio de la UTPL", "en": "Open the UTPL repository", "pt": "Abrir o repositório da UTPL"},
    "innovacion_titulo": {"es": "Proyectos de innovación docente", "en": "Teaching innovation projects", "pt": "Projetos de inovação docente"},
    "trayectoria_titulo": {"es": "Trayectoria", "en": "Career", "pt": "Trajetória"},
    "cap_titulo": {"es": "Capacitación en inteligencia artificial", "en": "Training in artificial intelligence", "pt": "Formação em inteligência artificial"},
    "contacto_titulo": {"es": "Contacto", "en": "Contact", "pt": "Contato"},
    "contacto_intro": {
        "es": "Puede escribirme para proponer colaboraciones de investigación, invitarme a evaluar artículos o a dar una conferencia, o coordinar un curso de capacitación en IA para su institución.",
        "en": "Write to me to propose research collaborations, invite me to review a manuscript or give a talk, or arrange an AI training course for your institution.",
        "pt": "Escreva-me para propor colaborações de pesquisa, convidar-me para avaliar artigos ou dar uma palestra, ou combinar um curso de formação em IA para sua instituição.",
    },
    "correo": {"es": "Correo institucional", "en": "University email", "pt": "E-mail institucional"},
    "ubicacion": {"es": "Ubicación", "en": "Location", "pt": "Localização"},
    "ubicacion_texto": {
        "es": "Universidad Técnica Particular de Loja, San Cayetano Alto, Loja, Ecuador",
        "en": "Universidad Técnica Particular de Loja, San Cayetano Alto, Loja, Ecuador",
        "pt": "Universidad Técnica Particular de Loja, San Cayetano Alto, Loja, Equador",
    },
    "perfiles_titulo": {"es": "Perfiles académicos", "en": "Academic profiles", "pt": "Perfis acadêmicos"},
    "no_encontrada": {"es": "Esta página no existe", "en": "This page doesn't exist", "pt": "Esta página não existe"},
    "no_encontrada_texto": {
        "es": "Puede que el enlace haya cambiado. Vuelva al inicio o use el menú.",
        "en": "The link may have changed. Go back to the home page or use the menu.",
        "pt": "O link pode ter mudado. Volte ao início ou use o menu.",
    },
    "volver_inicio": {"es": "Volver al inicio", "en": "Back to home", "pt": "Voltar ao início"},
}


def tr(valor, lang):
    """Devuelve el texto en el idioma pedido; acepta str o dict por idioma."""
    if isinstance(valor, dict):
        return valor.get(lang) or valor.get("es")
    return valor


def construir():
    env = Environment(
        loader=FileSystemLoader(os.path.join(AQUI, "plantillas")),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    pubs = sorted(C.PUBLICACIONES, key=lambda p: -p["anio"])
    por_anio = OrderedDict()
    for p in pubs:
        por_anio.setdefault(p["anio"], []).append(p)
    tipos_presentes = [t for t in C.TIPOS_PUB if any(p["tipo"] == t for p in pubs)]

    escritos = []
    for idioma in C.IDIOMAS:
        lang = idioma["code"]
        prefijo = "../" if idioma["dir"] else ""
        for pag in C.PAGINAS + [{"id": "404", "archivo": "404.html", "nav": {"es": "404", "en": "404", "pt": "404"}}]:
            if pag["id"] == "404" and lang != "es":
                continue  # GitHub Pages solo usa /404.html
            plantilla = env.get_template(pag["id"] + ".html")
            # enlaces a la misma página en los otros idiomas
            alternos = []
            for otro in C.IDIOMAS:
                ruta = otro["dir"] + (pag["archivo"] if pag["archivo"] != "index.html" else "")
                href = ("/" + otro["dir"]) if pag["id"] == "404" else prefijo + (ruta or "./")
                alternos.append({**otro, "href": href, "abs": C.SITIO["url"] + "/" + ruta})
            ctx = dict(
                C=C, P=P, lang=lang, idioma=idioma, pagina=pag, prefijo=prefijo,
                raiz=prefijo if pag["id"] != "404" else "/",
                t=lambda v, _l=lang: tr(v, _l), alternos=alternos,
                pubs=pubs, por_anio=por_anio, tipos_presentes=tipos_presentes,
            )
            html = plantilla.render(**ctx)
            destino = os.path.join(RAIZ, idioma["dir"], pag["archivo"])
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with open(destino, "w", encoding="utf-8") as f:
                f.write(html)
            escritos.append(os.path.relpath(destino, RAIZ))

    # sitemap
    urls = []
    for idioma in C.IDIOMAS:
        for pag in C.PAGINAS:
            ruta = idioma["dir"] + (pag["archivo"] if pag["archivo"] != "index.html" else "")
            urls.append(f"  <url><loc>{C.SITIO['url']}/{ruta}</loc><lastmod>{C.SITIO['actualizado']}</lastmod></url>")
    with open(os.path.join(RAIZ, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + "\n".join(urls) + "\n</urlset>\n")
    with open(os.path.join(RAIZ, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {C.SITIO['url']}/sitemap.xml\n")
    print(f"{len(escritos)} páginas generadas.")


if __name__ == "__main__":
    construir()
