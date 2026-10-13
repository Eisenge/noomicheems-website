#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the Game News section: /news/ index (5 langs) + the-sift-minecraft + wow-forever articles (5 langs),
   refresh /games/ index footers with a Game News link, and regenerate sitemap.xml (80 URLs)."""
import os, json

DEPLOY = os.path.dirname(os.path.abspath(__file__))
SITE = "https://noomicheems.online"
ORDER = ["en", "ru", "es", "pt", "id"]
LANG_LABEL = {"en": "English", "ru": "Русский", "es": "Español", "pt": "Português", "id": "Bahasa Indonesia"}

NEWS_NAME = {
    "en": "Game News",
    "ru": "Игровые новости",
    "es": "Noticias de juegos",
    "pt": "Notícias de jogos",
    "id": "Berita Game",
}
NEWS_URL = {
    "en": "/news/",
    "ru": "/ru/news/",
    "es": "/es/news/",
    "pt": "/pt/news/",
    "id": "/id/news/",
}
HOME_URL = {lo: ("/" if lo == "en" else f"/{lo}/") for lo in ORDER}

# Footer navigation used by games/news pages (previous footer + Game News).
FOOTER_NEWS = {
    "en": [("About", "/about/"), ("Controls", "/controls/"), ("How to play", "/guide/"),
           ("Game & developer", "/sources/"), ("More games", "/games/"), ("Game News", "/news/"),
           ("Privacy", "/privacy/"), ("Terms", "/terms/"), ("Help", "/help/")],
    "ru": [("О сайте", "/ru/about/"), ("Управление", "/ru/controls/"), ("Как играть", "/ru/guide/"),
           ("Игра и автор", "/ru/sources/"), ("Ещё игры", "/ru/games/"), ("Игровые новости", "/ru/news/"),
           ("Конфиденциальность", "/ru/privacy/"), ("Условия", "/ru/terms/"), ("Помощь", "/ru/help/")],
    "es": [("Acerca del sitio", "/es/about/"), ("Controles", "/es/controls/"), ("Cómo jugar", "/es/guide/"),
           ("Juego y autor", "/es/sources/"), ("Más juegos", "/es/games/"), ("Noticias de juegos", "/es/news/"),
           ("Privacidad", "/es/privacy/"), ("Condiciones", "/es/terms/"), ("Ayuda", "/es/help/")],
    "pt": [("Sobre", "/pt/about/"), ("Controles", "/pt/controls/"), ("Como jogar", "/pt/guide/"),
           ("Jogo e autor", "/pt/sources/"), ("Mais jogos", "/pt/games/"), ("Notícias de jogos", "/pt/news/"),
           ("Privacidade", "/pt/privacy/"), ("Termos", "/pt/terms/"), ("Ajuda", "/pt/help/")],
    "id": [("Tentang", "/id/about/"), ("Kontrol", "/id/controls/"), ("Cara bermain", "/id/guide/"),
           ("Game dan pembuat", "/id/sources/"), ("Game lainnya", "/id/games/"), ("Berita Game", "/id/news/"),
           ("Privasi", "/id/privacy/"), ("Ketentuan", "/id/terms/"), ("Bantuan", "/id/help/")],
}

HEADER_NAV = {
    "en": [("Play", "/#game"), ("Controls", "/controls/"), ("How to play", "/guide/")],
    "ru": [("Играть", "/ru/#game"), ("Управление", "/ru/controls/"), ("Как играть", "/ru/guide/")],
    "es": [("Jugar", "/es/#game"), ("Controles", "/es/controls/"), ("Cómo jugar", "/es/guide/")],
    "pt": [("Jogar", "/pt/#game"), ("Controles", "/pt/controls/"), ("Como jogar", "/pt/guide/")],
    "id": [("Main", "/id/#game"), ("Kontrol", "/id/controls/"), ("Cara bermain", "/id/guide/")],
}
SKIP_TXT = {
    "en": "Skip to content", "ru": "К содержимому", "es": "Ir al contenido", "pt": "Ir para o conteúdo", "id": "Ke konten utama",
}
HOME_TXT = {
    "en": "Home", "ru": "Главная", "es": "Inicio", "pt": "Início", "id": "Beranda",
}
SMALL = {
    "en": ("Independent guide ↗", "/about/"), "ru": ("Независимый сайт ↗", "/ru/about/"),
    "es": ("Sitio independiente ↗", "/es/about/"), "pt": ("Site independente ↗", "/pt/about/"),
    "id": ("Situs independen ↗", "/id/about/"),
}
FOOTER_DESC = {
    "en": "Original NoomiClone by jamesnorth. Independent site; not affiliated with its developer. Not the Noomicheems mod.",
    "ru": "Оригинальный NoomiClone от jamesnorth. Независимый сайт, не связанный с автором. Это не мод Noomicheems.",
    "es": "NoomiClone original de jamesnorth. Sitio independiente, sin afiliación al autor. No es el mod Noomicheems.",
    "pt": "NoomiClone original de jamesnorth. Site independente, sem vínculo com o autor. Não é o mod Noomicheems.",
    "id": "NoomiClone asli karya jamesnorth. Situs independen, tidak berafiliasi dengan pembuatnya. Bukan mod Noomicheems.",
}

# News index page content, per language.
NEWS = {
    "en": {
        "title": "Game News — Minecraft The Sift & World of Warcraft Forever",
        "desc": "Game news on Noomicheems: The Sift is Minecraft's first new dimension in 14 years, coming to Java & Bedrock in 2027, and World of Warcraft: Forever launches November 4, 2026.",
        "eyebrow": "GAME NEWS / INDEX",
        "h1": "Game News on Noomicheems",
        "intro": "Short, source-checked updates about games you can follow from this site. Each article links back to the browser games we cover.",
        "items": [
            ("Minecraft The Sift", "Minecraft's first new dimension in 14 years debuts in Minecraft Dungeons II and arrives in Java & Bedrock in 2027.", "/the-sift-minecraft/", "https://noomicheems.online/the-sift-minecraft/"),
            ("World of Warcraft: Forever", "Blizzard's Classic-style parallel game launches November 4, 2026 with a new Skyborne race, 9 new dungeons and 1,000+ new quests.", "/wow-forever/", "https://noomicheems.online/wow-forever/"),
        ],
    },
    "ru": {
        "title": "Игровые новости — Minecraft The Sift и World of Warcraft Forever",
        "desc": "Игровые новости на Noomicheems: The Sift — первое за 14 лет новое измерение Minecraft, которое выйдет в Java и Bedrock в 2027 году, а World of Warcraft: Forever запускается 4 ноября 2026 года.",
        "eyebrow": "ИГРОВЫЕ НОВОСТИ / УКАЗАТЕЛЬ",
        "h1": "Игровые новости на Noomicheems",
        "intro": "Короткие проверенные новости об играх, за которыми можно следить с этого сайта. Каждая статья ведёт к браузерным играм, о которых мы рассказываем.",
        "items": [
            ("Minecraft The Sift", "Первое за 14 лет новое измерение Minecraft сначала появляется в Minecraft Dungeons II, а в 2027 году придёт в Java и Bedrock.", "/ru/the-sift-minecraft/", "https://noomicheems.online/ru/the-sift-minecraft/"),
            ("World of Warcraft: Forever", "Новая игра Blizzard в духе Classic запускается 4 ноября 2026 года: новая раса Skyborne, 9 новых подземелий и более 1000 новых заданий.", "/ru/wow-forever/", "https://noomicheems.online/ru/wow-forever/"),
        ],
    },
    "es": {
        "title": "Noticias de juegos: Minecraft The Sift y World of Warcraft Forever",
        "desc": "Noticias de juegos en Noomicheems: The Sift es la primera dimensión nueva de Minecraft en 14 años, llegará a Java y Bedrock en 2027, y World of Warcraft: Forever se lanza el 4 de noviembre de 2026.",
        "eyebrow": "NOTICIAS DE JUEGOS / ÍNDICE",
        "h1": "Noticias de juegos en Noomicheems",
        "intro": "Noticias breves y verificadas sobre juegos que puedes seguir desde este sitio. Cada artículo enlaza a los juegos de navegador que cubrimos.",
        "items": [
            ("Minecraft The Sift", "La primera dimensión nueva de Minecraft en 14 años debuta en Minecraft Dungeons II y llega a Java y Bedrock en 2027.", "/es/the-sift-minecraft/", "https://noomicheems.online/es/the-sift-minecraft/"),
            ("World of Warcraft: Forever", "El juego paralelo de Blizzard en la línea de Classic se lanza el 4 de noviembre de 2026 con una nueva raza Skyborne, 9 mazmorras nuevas y más de 1.000 misiones nuevas.", "/es/wow-forever/", "https://noomicheems.online/es/wow-forever/"),
        ],
    },
    "pt": {
        "title": "Notícias de jogos: Minecraft The Sift e World of Warcraft Forever",
        "desc": "Notícias de jogos no Noomicheems: The Sift é a primeira nova dimensão do Minecraft em 14 anos, chegando ao Java e Bedrock em 2027, e World of Warcraft: Forever lança em 4 de novembro de 2026.",
        "eyebrow": "NOTÍCIAS DE JOGOS / ÍNDICE",
        "h1": "Notícias de jogos no Noomicheems",
        "intro": "Atualizações curtas e verificadas sobre jogos que você pode acompanhar por este site. Cada artigo volta aos jogos de navegador que cobrimos.",
        "items": [
            ("Minecraft The Sift", "A primeira nova dimensão do Minecraft em 14 anos estreia em Minecraft Dungeons II e chega ao Java e Bedrock em 2027.", "/pt/the-sift-minecraft/", "https://noomicheems.online/pt/the-sift-minecraft/"),
            ("World of Warcraft: Forever", "O jogo paralelo da Blizzard no estilo Classic lança em 4 de novembro de 2026 com uma nova raça Skyborne, 9 masmorras novas e mais de 1.000 missões novas.", "/pt/wow-forever/", "https://noomicheems.online/pt/wow-forever/"),
        ],
    },
    "id": {
        "title": "Berita Game — Minecraft The Sift & World of Warcraft Forever",
        "desc": "Berita game di Noomicheems: The Sift adalah dimensi baru pertama Minecraft dalam 14 tahun, hadir di Java & Bedrock pada 2027, dan World of Warcraft: Forever rilis 4 November 2026.",
        "eyebrow": "BERITA GAME / INDEKS",
        "h1": "Berita Game di Noomicheems",
        "intro": "Pembaruan singkat dan terperiksa tentang game yang bisa Anda ikuti dari situs ini. Setiap artikel menautkan kembali ke game browser yang kami bahas.",
        "items": [
            ("Minecraft The Sift", "Dimensi baru pertama Minecraft dalam 14 tahun debut di Minecraft Dungeons II dan hadir di Java & Bedrock pada 2027.", "/id/the-sift-minecraft/", "https://noomicheems.online/id/the-sift-minecraft/"),
            ("World of Warcraft: Forever", "Game paralel ala Classic dari Blizzard rilis 4 November 2026 dengan ras baru Skyborne, 9 dungeon baru, dan 1.000+ misi baru.", "/id/wow-forever/", "https://noomicheems.online/id/wow-forever/"),
        ],
    },
}

# Each article: slug -> per-language [title, description, eyebrow, h1, intro, sections, fine]
NEWS_PAGES = {
    "the-sift-minecraft": {
        "en": [
            "Minecraft The Sift: New Dimension Release Date & Details",
            "The Sift is Minecraft's first new dimension in 14 years, the fourth after the Overworld, Nether and End. It debuts in Minecraft Dungeons II and arrives in Java & Bedrock in 2027.",
            "GAME NEWS / MINECRAFT",
            "Minecraft The Sift: The New Dimension — Release Date & Details",
            "Minecraft Live 2026 introduced The Sift, Minecraft's first new dimension in more than 14 years. This page explains what it is, where you can see it first and when it reaches Java & Bedrock.",
            [
                ["h2", "What is The Sift in Minecraft?"],
                ["p", "The Sift is the new Minecraft dimension announced at Minecraft Live 2026 (September 26, 2026). It will be the game's fourth dimension after the Overworld, the Nether and the End — the first new dimension in more than 14 years. During the broadcast, part of the dimension and one of the mobs that lives there were shown. Mojang describes The Sift as \"beautiful, vibrant, and teeming with souls\", with areas such as the Meadow and the Carapace."],
                ["h2", "Where does The Sift appear first?"],
                ["p", "The dimension debuts in <a href=\"https://www.minecraft.net/\">Minecraft Dungeons II</a>, which launched on September 29, 2026. In that game, rifts appear throughout the world: if you stumble into one, it transports you to The Sift."],
                ["h2", "When does The Sift come to Minecraft Java and Bedrock?"],
                ["p", "Mojang confirmed that The Sift will come to Minecraft Java Edition and Bedrock Edition in 2027 as the game's fourth dimension. An exact release date has not been announced yet. The fastest way to experience it today is in Minecraft Dungeons II."],
                ["h2", "What is new in The Sift?"],
                ["p", "The dimension brings new locations and mobs, a signature pastel palette and unusual landscapes. Shown areas include the Meadow and the Carapace. More details are expected as the main-game release approaches."],
                ["h2", "Is The Sift free?"],
                ["p", "The update containing The Sift is part of Minecraft's regular updates. Mojang announced the dimension will arrive on Java and Bedrock Edition; the official Minecraft Live 2026 recap page confirms the 2027 plan."],
                ["h2", "More browser games and guides on this site"],
                ["p", "Looking for games you can play in a tab right now? Play <a href=\"/#game\">NoomiClone</a>, explore <a href=\"/lagos-life-game/\">Lagos Life</a>, check out <a href=\"/halo-ce-browser/\">Halo CE Browser</a> or read about <a href=\"/wow-forever/\">World of Warcraft: Forever</a>."],
            ],
            "Sources: <a href=\"https://www.minecraft.net/it-it/article/mclive_sept2026_recap\">Minecraft Live: September 2026 Recap</a> (Minecraft.net) and <a href=\"https://news.xbox.com/en-us/2026/09/26/minecraft-new-dimension-sift-dungeons-2/\">Xbox Wire</a>, checked October 11, 2026.",
        ],
        "ru": [
            "Minecraft The Sift — новое измерение: дата выхода и подробности",
            "The Sift — первое новое измерение Minecraft за 14 лет, четвёртое после Верхнего мира, Нижнего мира и Края. Появляется в Minecraft Dungeons II, в 2027 году придёт в Java и Bedrock.",
            "ИГРОВЫЕ НОВОСТИ / MINECRAFT",
            "Minecraft The Sift: новое измерение — дата выхода и подробности",
            "Minecraft Live 2026 представил The Sift — первое новое измерение Minecraft более чем за 14 лет. На этой странице — что это за измерение, где его увидеть первым и когда оно выйдет в Java и Bedrock.",
            [
                ["h2", "Что такое The Sift в Minecraft?"],
                ["p", "The Sift — новое измерение Minecraft, объявленное на Minecraft Live 2026 (26 сентября 2026 года). Оно станет четвёртым измерением игры после Верхнего мира, Нижнего мира и Края — первым новым измерением более чем за 14 лет. На трансляции показали часть измерения и одного из обитающих в нём мобов. Mojang описывает The Sift как «красивое, яркое и полное душ» измерение с такими областями, как Meadow и Carapace."],
                ["h2", "Где сначала появится The Sift?"],
                ["p", "Измерение сначала появляется в <a href=\"https://www.minecraft.net/\">Minecraft Dungeons II</a>, которое вышло 29 сентября 2026 года. В этой игре по всему миру встречаются разломы-«ріфты»: если вы наткнётесь на такой и войдёте в него, он перенесёт вас в The Sift."],
                ["h2", "Когда The Sift выйдет в Minecraft Java и Bedrock?"],
                ["p", "Mojang подтвердила, что The Sift придёт в Minecraft Java Edition и Bedrock Edition в 2027 году как четвёртое измерение игры. Точная дата релиза пока не названа. Раньше всего испытать измерение можно в Minecraft Dungeons II."],
                ["h2", "Что нового в The Sift?"],
                ["p", "В измерении новые локации и мобы, а также уникальная пастельная палитра и необычные пейзажи. Среди показанных областей — Meadow («Луг») и Carapace («Панцирь»). Больше деталей появится по мере приближения релиза в основной игре."],
                ["h2", "The Sift выйдет бесплатно?"],
                ["p", "Обновление с The Sift станет частью обычных обновлений Minecraft. Mojang объявила, что измерение придёт в Java и Bedrock Edition; страница с официальным описанием Minecraft Live 2026 подтверждает план релиза на 2027 год."],
                ["h2", "Другие браузерные игры и гиды на этом сайте"],
                ["p", "Ищете игры прямо во вкладке? Сыграйте в <a href=\"/#game\">NoomiClone</a>, изучите <a href=\"/lagos-life-game/\">Lagos Life</a>, загляните в <a href=\"/halo-ce-browser/\">Halo CE Browser</a> или прочитайте <a href=\"/wow-forever/\">про World of Warcraft: Forever</a>."],
            ],
            "Источники: <a href=\"https://www.minecraft.net/it-it/article/mclive_sept2026_recap\">Minecraft Live: September 2026 Recap</a> (Minecraft.net) и <a href=\"https://news.xbox.com/en-us/2026/09/26/minecraft-new-dimension-sift-dungeons-2/\">Xbox Wire</a>, проверено 11 октября 2026 года.",
        ],
        "es": [
            "Minecraft The Sift: la nueva dimensión — fecha de lanzamiento y detalles",
            "The Sift es la primera dimensión nueva de Minecraft en 14 años, la cuarta tras el Overworld, el Nether y el End. Aparece en Minecraft Dungeons II y llegará a Java y Bedrock en 2027.",
            "NOTICIAS DE JUEGOS / MINECRAFT",
            "Minecraft The Sift: la nueva dimensión — fecha y detalles",
            "Minecraft Live 2026 presentó The Sift, la primera dimensión nueva de Minecraft en más de 14 años. Esta página explica qué es, dónde verla primero y cuándo llegará a Java y Bedrock.",
            [
                ["h2", "¿Qué es The Sift en Minecraft?"],
                ["p", "The Sift es la nueva dimensión de Minecraft anunciada en Minecraft Live 2026 (26 de septiembre de 2026). Será la cuarta dimensión del juego, tras Overworld, Nether y End, y la primera dimensión nueva en más de 14 años. Durante la retransmisión se mostró parte de la dimensión y uno de sus mobs. Mojang describe The Sift como un lugar «bello, vibrante y repleto de almas», con áreas como el Meadow y la Carapace."],
                ["h2", "¿Dónde aparece primero The Sift?"],
                ["p", "La dimensión aparece primero en <a href=\"https://www.minecraft.net/\">Minecraft Dungeons II</a>, lanzado el 29 de septiembre de 2026. En ese juego hay grietas («rifts») por todo el mundo: si tropiezas con una y entras, te transporta a The Sift."],
                ["h2", "¿Cuándo llega The Sift a Minecraft Java y Bedrock?"],
                ["p", "Mojang confirmó que The Sift llegará a Minecraft Java Edition y Bedrock Edition en 2027 como cuarta dimensión del juego. La fecha exacta aún no se ha anunciado. La forma más rápida de probarla es en Minecraft Dungeons II."],
                ["h2", "¿Qué hay de nuevo en The Sift?"],
                ["p", "La dimensión incluye nuevas zonas y mobs, una paleta pastel característica y paisajes poco habituales. Entre las áreas mostradas están el Meadow («Prado») y la Carapace («Caparazón»). Habrá más detalles conforme se acerque el lanzamiento en el juego principal."],
                ["h2", "¿The Sift será gratis?"],
                ["p", "La actualización con The Sift forma parte de las actualizaciones normales de Minecraft. Mojang anunció que la dimensión llegará a Java y Bedrock Edition; la página oficial de Minecraft Live 2026 confirma el plan para 2027."],
                ["h2", "Más juegos de navegador y guías en este sitio"],
                ["p", "¿Buscas juegos para una pestaña? Juega a <a href=\"/#game\">NoomiClone</a>, explora <a href=\"/lagos-life-game/\">Lagos Life</a>, mira <a href=\"/halo-ce-browser/\">Halo CE Browser</a> o lee sobre <a href=\"/wow-forever/\">World of Warcraft: Forever</a>."],
            ],
            "Fuentes: <a href=\"https://www.minecraft.net/it-it/article/mclive_sept2026_recap\">Minecraft Live: September 2026 Recap</a> (Minecraft.net) y <a href=\"https://news.xbox.com/en-us/2026/09/26/minecraft-new-dimension-sift-dungeons-2/\">Xbox Wire</a>, consultado el 11 de octubre de 2026.",
        ],
        "pt": [
            "Minecraft The Sift: a nova dimensão — data de lançamento e detalhes",
            "The Sift é a primeira nova dimensão do Minecraft em 14 anos, a quarta depois do Overworld, Nether e End. Aparece em Minecraft Dungeons II e chega ao Java e Bedrock em 2027.",
            "NOTÍCIAS DE JOGOS / MINECRAFT",
            "Minecraft The Sift: a nova dimensão — data e detalhes",
            "O Minecraft Live 2026 apresentou The Sift, a primeira nova dimensão do Minecraft em mais de 14 anos. Esta página explica o que é, onde ver primeiro e quando chegará ao Java e Bedrock.",
            [
                ["h2", "O que é The Sift no Minecraft?"],
                ["p", "The Sift é a nova dimensão do Minecraft anunciada no Minecraft Live 2026 (26 de setembro de 2026). Será a quarta dimensão do jogo, depois de Overworld, Nether e End, e a primeira nova dimensão em mais de 14 anos. Durante a transmissão, foi mostrada parte da dimensão e um dos mobs que a habitam. A Mojang descreve The Sift como «bonita, vibrante e cheia de almas», com áreas como o Meadow e a Carapace."],
                ["h2", "Onde The Sift aparece primeiro?"],
                ["p", "A dimensão aparece primeiro em <a href=\"https://www.minecraft.net/\">Minecraft Dungeons II</a>, lançado em 29 de setembro de 2026. Nesse jogo há fendas («rifts») pelo mundo: se você tropeçar numa e entrar, ela transporta você para The Sift."],
                ["h2", "Quando The Sift chega ao Minecraft Java e Bedrock?"],
                ["p", "A Mojang confirmou que The Sift chegará ao Minecraft Java Edition e Bedrock Edition em 2027 como quarta dimensão do jogo. A data exata ainda não foi anunciada. A forma mais rápida de experimentar é em Minecraft Dungeons II."],
                ["h2", "O que há de novo em The Sift?"],
                ["p", "A dimensão traz novas áreas e mobs, uma paleta pastel característica e paisagens incomuns. Entre as áreas mostradas estão o Meadow («Prado») e a Carapace («Carapaça»). Haverá mais detalhes conforme o lançamento no jogo principal se aproxima."],
                ["h2", "The Sift será grátis?"],
                ["p", "A atualização com The Sift faz parte das atualizações normais do Minecraft. A Mojang anunciou que a dimensão chegará ao Java e Bedrock Edition; a página oficial do Minecraft Live 2026 confirma o plano para 2027."],
                ["h2", "Mais jogos de navegador e guias neste site"],
                ["p", "Procurando jogos para uma aba? Jogue <a href=\"/#game\">NoomiClone</a>, explore <a href=\"/lagos-life-game/\">Lagos Life</a>, veja <a href=\"/halo-ce-browser/\">Halo CE Browser</a> ou leia sobre <a href=\"/wow-forever/\">World of Warcraft: Forever</a>."],
            ],
            "Fontes: <a href=\"https://www.minecraft.net/it-it/article/mclive_sept2026_recap\">Minecraft Live: September 2026 Recap</a> (Minecraft.net) e <a href=\"https://news.xbox.com/en-us/2026/09/26/minecraft-new-dimension-sift-dungeons-2/\">Xbox Wire</a>, consultado em 11 de outubro de 2026.",
        ],
        "id": [
            "Minecraft The Sift: Dimensi Baru — Tanggal Rilis dan Detailnya",
            "The Sift adalah dimensi baru pertama Minecraft dalam 14 tahun, yang keempat setelah Overworld, Nether, dan End. Muncul di Minecraft Dungeons II dan hadir di Java & Bedrock pada 2027.",
            "BERITA GAME / MINECRAFT",
            "Minecraft The Sift: Dimensi Baru — Tanggal dan Detail",
            "Minecraft Live 2026 memperkenalkan The Sift, dimensi baru pertama Minecraft dalam lebih dari 14 tahun. Halaman ini menjelaskan apa itu, di mana melihatnya lebih dulu, dan kapan hadir di Java & Bedrock.",
            [
                ["h2", "Apa itu The Sift di Minecraft?"],
                ["p", "The Sift adalah dimensi baru Minecraft yang diumumkan di Minecraft Live 2026 (26 September 2026). Dimensi ini akan menjadi dimensi keempat game, setelah Overworld, Nether, dan End—yang pertama dalam lebih dari 14 tahun. Dalam siaran, ditampilkan sebagian dimensi dan salah satu mob yang menghuninya. Mojang menggambarkan The Sift sebagai tempat yang «indah, semarak, dan penuh jiwa», dengan area seperti Meadow dan Carapace."],
                ["h2", "Di mana The Sift muncul pertama kali?"],
                ["p", "Dimensi ini muncul pertama kali di <a href=\"https://www.minecraft.net/\">Minecraft Dungeons II</a>, yang rilis 29 September 2026. Di game itu ada celah («rift») di seluruh dunia: jika Anda menemukannya dan masuk, celah itu membawa Anda ke The Sift."],
                ["h2", "Kapan The Sift hadir di Minecraft Java dan Bedrock?"],
                ["p", "Mojang mengonfirmasi bahwa The Sift akan hadir di Minecraft Java Edition dan Bedrock Edition pada 2027 sebagai dimensi keempat game. Tanggal pastinya belum diumumkan. Cara tercepat mencobanya adalah lewat Minecraft Dungeons II."],
                ["h2", "Apa yang baru di The Sift?"],
                ["p", "Dimensi ini menghadirkan area dan mob baru, palet pastel khas, serta pemandangan yang tidak biasa. Di antara area yang ditampilkan adalah Meadow («Padang») dan Carapace («Karapas»). Detail lebih banyak akan muncul menjelang rilis di game utama."],
                ["h2", "Apakah The Sift gratis?"],
                ["p", "Pembaruan berisi The Sift adalah bagian dari pembaruan biasa Minecraft. Mojang mengumumkan dimensi ini akan hadir di Java dan Bedrock Edition; halaman resmi Minecraft Live 2026 mengonfirmasi rencana rilis 2027."],
                ["h2", "Game browser dan panduan lain di situs ini"],
                ["p", "Mencari game yang bisa dimainkan di tab? Mainkan <a href=\"/#game\">NoomiClone</a>, jelajahi <a href=\"/lagos-life-game/\">Lagos Life</a>, lihat <a href=\"/halo-ce-browser/\">Halo CE Browser</a>, atau baca tentang <a href=\"/wow-forever/\">World of Warcraft: Forever</a>."],
            ],
            "Sumber: <a href=\"https://www.minecraft.net/it-it/article/mclive_sept2026_recap\">Minecraft Live: September 2026 Recap</a> (Minecraft.net) dan <a href=\"https://news.xbox.com/en-us/2026/09/26/minecraft-new-dimension-sift-dungeons-2/\">Xbox Wire</a>, diperiksa 11 Oktober 2026.",
        ],
    },
    "wow-forever": {
        "en": [
            "World of Warcraft: Forever Release Date, Beta & What We Know",
            "World of Warcraft: Forever launches November 4, 2026. Blizzard's Classic-style parallel game in original Azeroth: level 60, a new Skyborne race, 9 new dungeons, beta from September 17.",
            "GAME NEWS / WORLD OF WARCRAFT",
            "World of Warcraft: Forever — Release Date, Beta & What We Know",
            "Blizzard announced World of Warcraft: Forever at BlizzCon 2026: a permanent Classic-style version alongside modern WoW and Classic. This page covers the launch date, beta, new race and new content.",
            [
                ["h2", "What is World of Warcraft: Forever?"],
                ["p", "World of Warcraft: Forever is Blizzard's new game announced on September 13, 2026 at BlizzCon. It is a permanent parallel world alongside modern WoW and WoW Classic — not a mode or a season: Blizzard's official recap says \"this is not a mode, a season, or a new version of Classic\". Set after the events of Warcraft III Reforged: Forsaken Kingdom and before Molten Core, you return to the original continents, adventure to level 60, and keep progressing through new stories."],
                ["h2", "When does World of Warcraft: Forever launch?"],
                ["p", "The game launches globally on <b>November 4, 2026 at 3:00 p.m. PDT</b>. Access is included with your World of Warcraft subscription or Game Time. Beta began September 17, 2026, and new raids unlock on December 9."],
                ["h2", "What's new in WoW Forever?"],
                ["ul", ["<b>New zones</b> — restoring Mount Hyjal, the hidden history of Shen'dralas, the Riverglades frontier and the Zephras Isle starting zone.", "<b>New playable race: Skyborne</b> — choose Horde (Shaman) or Alliance (Mage); Warrior, Hunter, Rogue and Druid are also available with new forms.", "<b>More than 1,000 new quests</b> — new and reimagined stories woven through the entire level 1–60 journey.", "<b>9 new dungeons</b> — including the Hall of Thanes, the Ruins of Lordaeron and the City of Dalaran.", "<b>Raids and PvP</b> — Hyjal Summit (20 players), Barrow Deeps (10 players) and the Darkspear Islands 15 vs 15 Battleground."]],
                ["h2", "What is the philosophy of WoW Forever?"],
                ["p", "Blizzard describes four pillars: approachable and familiar, the world as the main character, the journey before the destination, and protecting the social experience. That means no flying mounts, no level scaling, and rewards that come from playing the game: leveling, dungeons, exploration and cooperation."],
                ["h2", "How much does WoW Forever cost?"],
                ["p", "Access is included with your World of Warcraft subscription or Game Time. Separately, optional upgrade editions are available for pre-purchase on the Battle.net Shop: Skyborne Heroic Pack, Skyborne Epic Pack (with beta access) and the limited-time Warcraft Forever Collection."],
                ["h2", "More browser games and guides on this site"],
                ["p", "Want to play right now, with nothing to install? Play <a href=\"/#game\">NoomiClone</a>, check out <a href=\"/lagos-life-game/\">Lagos Life</a> or read about <a href=\"/the-sift-minecraft/\">the new The Sift dimension in Minecraft</a>."],
            ],
            "Sources: <a href=\"https://news.blizzard.com/en-gb/article/24302093/carve-a-new-path-with-world-of-warcraft-forever\">Blizzard News</a> and <a href=\"https://worldofwarcraft.blizzard.com/en-us/news/24303862/world-of-warcraft-forever-whats-next-panel-recap\">World of Warcraft: Forever What's Next Panel Recap</a>, checked October 11, 2026.",
        ],
        "ru": [
            "World of Warcraft: Forever — дата выхода, бета и что известно",
            "World of Warcraft: Forever запускается 4 ноября 2026 года. Параллельная игра Blizzard в духе Classic в оригинальной Азероте: уровень 60, новая раса Skyborne, 9 новых подземелий, бета с 17 сентября.",
            "ИГРОВЫЕ НОВОСТИ / WORLD OF WARCRAFT",
            "World of Warcraft: Forever — дата выхода, бета и что известно",
            "Blizzard анонсировала World of Warcraft: Forever на BlizzCon 2026: постоянная версия игры в духе Classic рядом с современной WoW и Classic. На этой странице — дата запуска, бета, новая раса и новинки.",
            [
                ["h2", "Что такое World of Warcraft: Forever?"],
                ["p", "World of Warcraft: Forever — новая игра Blizzard, анонсированная 13 сентября 2026 года на BlizzCon. Это постоянный параллельный мир рядом с современной WoW и WoW Classic, а не режим или сезон: в официальном обзоре Blizzard пишет, что «это не режим, не сезон и не новая версия Classic». Действие разворачивается после событий Warcraft III Reforged: Forsaken Kingdom и до Molten Core — вы возвращаетесь в оригинальные континенты, прокачиваетесь до 60 уровня и продолжаете путешествие по новым историям."],
                ["h2", "Когда выходит World of Warcraft: Forever?"],
                ["p", "Запуск по всему миру — <b>4 ноября 2026 года в 15:00 по тихоокеанскому времени</b>. Доступ входит в подписку World of Warcraft или в игровое время. Бета началась 17 сентября 2026 года; новые рейды откроются 9 декабря."],
                ["h2", "Что нового в WoW Forever?"],
                ["ul", ["<b>Новые зоны</b> — восстановление горы Хиджал, скрытая история Шен'дралас, фронтир Риверглэйдс и стартовая островная зона Зефрас.", "<b>Новая раса Skyborne</b> — на выбор Орда (шаман) или Альянс (маг); доступны также воин, охотник, разбойник и друид с новыми формами.", "<b>Более 1000 новых заданий</b> — новые и переосмысленные истории по всему пути 1–60.", "<b>9 новых подземелий</b> — включая Hall of Thanes, Ruins of Lordaeron и City of Dalaran.", "<b>Рейды и PvP</b> — Hyjal Summit (20 игроков), Barrow Deeps (10 игроков) и поле боя Darkspear Islands 15×15."]],
                ["h2", "Какая философия у WoW Forever?"],
                ["p", "Blizzard описывает четыре столпа: знакомый и доступный мир, мир как главный герой, путь важнее цели и защита социального опыта. Поэтому в игре нет летающих ездовых и масштабирования уровней, а награды приходят за саму игру — прокачку, подземелья, исследование и общение."],
                ["h2", "Сколько стоит WoW Forever?"],
                ["p", "Доступ в игру входит в подписку World of Warcraft или игровое время. Отдельно можно предзаказать опциональные версии-улучшения в магазине Battle.net: Skyborne Heroic Pack, Skyborne Epic Pack (с доступом к бете) и ограниченную по времени Warcraft Forever Collection."],
                ["h2", "Другие браузерные игры и гиды на этом сайте"],
                ["p", "Хочется сыграть прямо сейчас, без установки? Сыграйте в <a href=\"/#game\">NoomiClone</a>, посмотрите <a href=\"/lagos-life-game/\">Lagos Life</a> или почитайте <a href=\"/the-sift-minecraft/\">о новом измерении The Sift в Minecraft</a>."],
            ],
            "Источники: <a href=\"https://news.blizzard.com/en-gb/article/24302093/carve-a-new-path-with-world-of-warcraft-forever\">Blizzard News</a> и <a href=\"https://worldofwarcraft.blizzard.com/en-us/news/24303862/world-of-warcraft-forever-whats-next-panel-recap\">World of Warcraft: Forever What's Next Panel Recap</a>, проверено 11 октября 2026 года.",
        ],
        "es": [
            "World of Warcraft: Forever — fecha de lanzamiento, beta y lo que sabemos",
            "World of Warcraft: Forever se lanza el 4 de noviembre de 2026. El juego paralelo de Blizzard al estilo Classic en una Azeroth original: nivel 60, nueva raza Skyborne, 9 mazmorras nuevas, beta desde el 17 de septiembre.",
            "NOTICIAS DE JUEGOS / WORLD OF WARCRAFT",
            "World of Warcraft: Forever — fecha, beta y lo que sabemos",
            "Blizzard anunció World of Warcraft: Forever en la BlizzCon 2026: una versión permanente al estilo Classic junto a la WoW moderna y Classic. Esta página explica la fecha de lanzamiento, la beta, la nueva raza y las novedades.",
            [
                ["h2", "¿Qué es World of Warcraft: Forever?"],
                ["p", "World of Warcraft: Forever es el nuevo juego de Blizzard anunciado el 13 de septiembre de 2026 en la BlizzCon. Es un mundo paralelo permanente junto a WoW moderna y WoW Classic, no un modo ni una temporada: el resumen oficial de Blizzard dice que «no es un modo, ni una temporada, ni una nueva versión de Classic». La historia transcurre tras los eventos de Warcraft III Reforged: Forsaken Kingdom y antes de Molten Core: vuelves a los continentes originales, subes hasta el nivel 60 y sigues avanzando por historias nuevas."],
                ["h2", "¿Cuándo se lanza World of Warcraft: Forever?"],
                ["p", "Lanzamiento mundial — <b>4 de noviembre de 2026 a las 15:00 (hora del Pacífico)</b>. El acceso está incluido con la suscripción de World of Warcraft o el tiempo de juego. La beta empezó el 17 de septiembre de 2026 y las nuevas incursiones se abren el 9 de diciembre."],
                ["h2", "¿Qué hay de nuevo en WoW Forever?"],
                ["ul", ["<b>Zonas nuevas</b> — la restauración de Monte Hyjal, la historia oculta de Shen'dralas, la frontera de Riverglades y la zona inicial de la Isla Zephras.", "<b>Nueva raza Skyborne</b> — elige Horda (chamán) o Alianza (mago); también guerrero, cazador, pícaro y druida con formas nuevas.", "<b>Más de 1.000 misiones nuevas</b> — historias nuevas y reinventadas por todo el camino del 1 al 60.", "<b>9 mazmorras nuevas</b> — incluidas Hall of Thanes, Ruins of Lordaeron y City of Dalaran.", "<b>Incursiones y PvP</b> — Hyjal Summit (20 jugadores), Barrow Deeps (10 jugadores) y el campo de batalla Darkspear Islands 15 contra 15."]],
                ["h2", "¿Cuál es la filosofía de WoW Forever?"],
                ["p", "Blizzard describe cuatro pilares: un mundo familiar y accesible, el mundo como protagonista, el camino antes que el destino y proteger la experiencia social. Por eso no hay monturas voladoras ni escalado de niveles, y las recompensas llegan por jugar: subir de nivel, mazmorras, exploración y compañía."],
                ["h2", "¿Cuánto cuesta WoW Forever?"],
                ["p", "El acceso al juego está incluido con la suscripción de World of Warcraft o el tiempo de juego. Por separado puedes reservar ediciones de mejora opcionales en la tienda de Battle.net: Skyborne Heroic Pack, Skyborne Epic Pack (con acceso a la beta) y la Warcraft Forever Collection por tiempo limitado."],
                ["h2", "Más juegos de navegador y guías en este sitio"],
                ["p", "¿Quieres jugar ya, sin instalar nada? Juega a <a href=\"/#game\">NoomiClone</a>, mira el <a href=\"/lagos-life-game/\">juego Lagos Life</a> o lee <a href=\"/the-sift-minecraft/\">sobre la nueva dimensión The Sift de Minecraft</a>."],
            ],
            "Fuentes: <a href=\"https://news.blizzard.com/en-gb/article/24302093/carve-a-new-path-with-world-of-warcraft-forever\">Blizzard News</a> y <a href=\"https://worldofwarcraft.blizzard.com/en-us/news/24303862/world-of-warcraft-forever-whats-next-panel-recap\">World of Warcraft: Forever What's Next Panel Recap</a>, consultado el 11 de octubre de 2026.",
        ],
        "pt": [
            "World of Warcraft: Forever — data de lançamento, beta e o que sabemos",
            "World of Warcraft: Forever lança em 4 de novembro de 2026. O jogo paralelo da Blizzard ao estilo Classic numa Azeroth original: nível 60, nova raça Skyborne, 9 masmorras novas, beta desde 17 de setembro.",
            "NOTÍCIAS DE JOGOS / WORLD OF WARCRAFT",
            "World of Warcraft: Forever — data, beta e o que sabemos",
            "A Blizzard anunciou World of Warcraft: Forever na BlizzCon 2026: uma versão permanente ao estilo Classic ao lado do WoW moderno e do Classic. Esta página explica a data de lançamento, a beta, a nova raça e as novidades.",
            [
                ["h2", "O que é World of Warcraft: Forever?"],
                ["p", "World of Warcraft: Forever é o novo jogo da Blizzard anunciado em 13 de setembro de 2026 na BlizzCon. É um mundo paralelo permanente ao lado do WoW moderno e do WoW Classic, não um modo ou temporada: o resumo oficial da Blizzard diz que «não é um modo, nem uma temporada, nem uma nova versão do Classic». A história se passa após os eventos de Warcraft III Reforged: Forsaken Kingdom e antes de Molten Core: você volta aos continentes originais, sobe até o nível 60 e segue por histórias novas."],
                ["h2", "Quando World of Warcraft: Forever é lançado?"],
                ["p", "Lançamento mundial — <b>4 de novembro de 2026 às 15h (horário do Pacífico)</b>. O acesso está incluído na assinatura de World of Warcraft ou no tempo de jogo. A beta começou em 17 de setembro de 2026 e as novas raides abrem em 9 de dezembro."],
                ["h2", "O que há de novo em WoW Forever?"],
                ["ul", ["<b>Zonas novas</b> — a restauração de Monte Hyjal, a história oculta de Shen'dralas, a fronteira de Riverglades e a zona inicial da Ilha Zephras.", "<b>Nova raça Skyborne</b> — escolha Horda (xamã) ou Aliança (mago); também guerreiro, caçador, ladino e druida com formas novas.", "<b>Mais de 1.000 missões novas</b> — histórias novas e reinventadas por todo o caminho do 1 ao 60.", "<b>9 masmorras novas</b> — incluindo Hall of Thanes, Ruins of Lordaeron e City of Dalaran.", "<b>Raides e PvP</b> — Hyjal Summit (20 jogadores), Barrow Deeps (10 jogadores) e o campo de batalha Darkspear Islands 15 contra 15."]],
                ["h2", "Qual é a filosofia do WoW Forever?"],
                ["p", "A Blizzard descreve quatro pilares: um mundo familiar e acessível, o mundo como protagonista, o caminho antes do destino e proteger a experiência social. Por isso não há montarias voadoras nem escalonamento de nível, e as recompensas vêm de jogar: subir de nível, masmorras, exploração e companhia."],
                ["h2", "Quanto custa WoW Forever?"],
                ["p", "O acesso ao jogo está incluído na assinatura de World of Warcraft ou no tempo de jogo. Separadamente, você pode pré-comprar edições de melhoria opcionais na loja Battle.net: Skyborne Heroic Pack, Skyborne Epic Pack (com acesso à beta) e a Warcraft Forever Collection por tempo limitado."],
                ["h2", "Mais jogos de navegador e guias neste site"],
                ["p", "Quer jogar agora, sem instalar nada? Jogue <a href=\"/#game\">NoomiClone</a>, confira o <a href=\"/lagos-life-game/\">jogo Lagos Life</a> ou leia <a href=\"/the-sift-minecraft/\">sobre a nova dimensão The Sift do Minecraft</a>."],
            ],
            "Fontes: <a href=\"https://news.blizzard.com/en-gb/article/24302093/carve-a-new-path-with-world-of-warcraft-forever\">Blizzard News</a> e <a href=\"https://worldofwarcraft.blizzard.com/en-us/news/24303862/world-of-warcraft-forever-whats-next-panel-recap\">World of Warcraft: Forever What's Next Panel Recap</a>, consultado em 11 de outubro de 2026.",
        ],
        "id": [
            "World of Warcraft: Forever — Tanggal Rilis, Beta, dan yang Kami Tahu",
            "World of Warcraft: Forever rilis 4 November 2026. Game paralel ala Classic dari Blizzard di Azeroth asli: level 60, ras baru Skyborne, 9 dungeon baru, beta mulai 17 September.",
            "BERITA GAME / WORLD OF WARCRAFT",
            "World of Warcraft: Forever — Tanggal, Beta, dan yang Kami Tahu",
            "Blizzard mengumumkan World of Warcraft: Forever di BlizzCon 2026: versi permanen ala Classic di samping WoW modern dan Classic. Halaman ini menjelaskan tanggal rilis, beta, ras baru, dan hal-hal baru lainnya.",
            [
                ["h2", "Apa itu World of Warcraft: Forever?"],
                ["p", "World of Warcraft: Forever adalah game baru Blizzard yang diumumkan pada 13 September 2026 di BlizzCon. Ini dunia paralel permanen di samping WoW modern dan WoW Classic, bukan mode atau musim: ringkasan resmi Blizzard menyebut «ini bukan mode, bukan musim, dan bukan versi baru Classic». Kisahnya berlangsung setelah peristiwa Warcraft III Reforged: Forsaken Kingdom dan sebelum Molten Core: Anda kembali ke benua asli, naik hingga level 60, dan melanjutkan perjalanan lewat cerita-cerita baru."],
                ["h2", "Kapan World of Warcraft: Forever rilis?"],
                ["p", "Rilis global — <b>4 November 2026 pukul 15.00 Waktu Pasifik</b>. Akses sudah termasuk dalam langganan World of Warcraft atau game time. Beta dimulai 17 September 2026, dan raid baru dibuka 9 Desember."],
                ["h2", "Apa yang baru di WoW Forever?"],
                ["ul", ["<b>Zona baru</b> — pemulihan Gunung Hyjal, kisah tersembunyi Shen'dralas, perbatasan Riverglades, dan zona awal Pulau Zephras.", "<b>Ras baru Skyborne</b> — pilih Horde (shaman) atau Alliance (mage); tersedia juga warrior, hunter, rogue, dan druid dengan bentuk baru.", "<b>Lebih dari 1.000 misi baru</b> — kisah baru dan kisah lama yang dibayangkan ulang di sepanjang perjalanan level 1–60.", "<b>9 dungeon baru</b> — termasuk Hall of Thanes, Ruins of Lordaeron, dan City of Dalaran.", "<b>Raid dan PvP</b> — Hyjal Summit (20 pemain), Barrow Deeps (10 pemain), dan medan perang Darkspear Islands 15 lawan 15."]],
                ["h2", "Apa filosofi WoW Forever?"],
                ["p", "Blizzard menyebut empat pilar: dunia yang akrab dan mudah diakses, dunia sebagai tokoh utama, perjalanan sebelum tujuan, dan melindungi pengalaman sosial. Karena itu tidak ada mount terbang dan tidak ada penskalaan level, dan hadiah datang dari bermain: naik level, dungeon, menjelajah, dan berkumpul."],
                ["h2", "Berapa harga WoW Forever?"],
                ["p", "Akses ke game sudah termasuk langganan World of Warcraft atau game time. Secara terpisah, Anda bisa pre-order edisi peningkatan opsional di toko Battle.net: Skyborne Heroic Pack, Skyborne Epic Pack (dengan akses beta), dan Warcraft Forever Collection edisi terbatas."],
                ["h2", "Game browser dan panduan lain di situs ini"],
                ["p", "Mau bermain sekarang, tanpa instalasi? Mainkan <a href=\"/#game\">NoomiClone</a>, cek <a href=\"/lagos-life-game/\">game Lagos Life</a>, atau baca <a href=\"/the-sift-minecraft/\">tentang dimensi baru The Sift di Minecraft</a>."],
            ],
            "Sumber: <a href=\"https://news.blizzard.com/en-gb/article/24302093/carve-a-new-path-with-world-of-warcraft-forever\">Blizzard News</a> dan <a href=\"https://worldofwarcraft.blizzard.com/en-us/news/24303862/world-of-warcraft-forever-whats-next-panel-recap\">World of Warcraft: Forever What's Next Panel Recap</a>, diperiksa 11 Oktober 2026.",
        ],
    },
}

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def render_sections(sections):
    out = []
    for tag, content in sections:
        if tag == "h2":
            out.append(f"<h2>{content}</h2>")
        elif tag == "p":
            out.append(f"<p>{content}</p>")
        elif tag == "ul":
            out.append("<ul>" + "".join(f"<li>{li}</li>" for li in content) + "</ul>")
    return "\n".join(out)

def hreflangs(slug_or_dir, is_dir=False):
    out = []
    for lo in ORDER:
        if is_dir:
            href = f"{SITE}/news/" if lo == "en" else f"{SITE}/{lo}/news/"
        else:
            href = f"{SITE}/{slug_or_dir}/" if lo == "en" else f"{SITE}/{lo}/{slug_or_dir}/"
        out.append(f'<link rel="alternate" hreflang="{lo}" href="{href}">')
    xd = f"{SITE}/news/" if is_dir else f"{SITE}/{slug_or_dir}/"
    out.append(f'<link rel="alternate" hreflang="x-default" href="{xd}">')
    return "\n".join(out)

def langs_nav(lang, slug_or_dir, is_dir=False):
    out = []
    for lo in ORDER:
        if is_dir:
            href = "/news/" if lo == "en" else f"/{lo}/news/"
        else:
            href = f"/{slug_or_dir}/" if lo == "en" else f"/{lo}/{slug_or_dir}/"
        cur = ' aria-current="page"' if lo == lang else ""
        out.append(f'<a href="{href}" lang="{lo}" hreflang="{lo}"{cur}>{LANG_LABEL[lo]}</a>')
    return "".join(out)

def head(lang, title, desc, url, hl_extra=""):
    return (f'<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="robots" content="index,follow"><title>{esc(title)}</title><meta name="description" content="{esc(desc)}">'
            f'<meta name="theme-color" content="#171a1b"><link rel="icon" href="/favicon.svg">'
            f'<link rel="stylesheet" href="/style.css?v=20261010"><script src="/app.js?v=20261010" defer></script>'
            f'<link rel="canonical" href="{url}">{hl_extra}'
            f'<meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}">'
            f'<meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}">'
            f'<meta name="twitter:card" content="summary">'
            f'<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "WebPage", "name": {json.dumps(title, ensure_ascii=False)}, "url": "{url}", "description": {json.dumps(desc, ensure_ascii=False)}, "inLanguage": "{lang}", "isPartOf": {{"@type": "WebSite", "name": "Noomicheems", "url": "{SITE}/"}}}}</script>'
            f'<meta name="google-adsense-account" content="ca-pub-1284741242592931"><script src="/analytics.js?v=20261010" defer></script>')

def shell(lang, title, desc, url, hl_extra, body, nav_slug=None, nav_dir=False):
    header_nav_html = "".join(f'<a href="{h}">{t}</a>' for t, h in HEADER_NAV[lang])
    footer_nav_html = "".join(f'<a href="{h}">{t}</a>' for t, h in FOOTER_NEWS[lang])
    lang_nav_html = langs_nav(lang, nav_slug, nav_dir)
    return (f'<!doctype html><html lang="{lang}"><head>{head(lang, title, desc, url, hl_extra)}</head>'
            f'<body><a class="skip" href="#main">{SKIP_TXT[lang]}</a>'
            f'<header><a class="brand" href="{HOME_URL[lang]}">n<span>↗</span> <b>noomicheems</b></a>'
            f'<nav aria-label="Main">{header_nav_html}</nav>'
            f'<a class="small" href="{SMALL[lang][1]}">{SMALL[lang][0]}</a></header>'
            f'<nav class="languages" aria-label="Language">{lang_nav_html}</nav>'
            f'<main id="main">{body}</main>'
            f'<footer><a class="brand" href="{HOME_URL[lang]}">noomicheems<span>↗</span></a><p>{FOOTER_DESC[lang]}</p>'
            f'<nav aria-label="Footer">{footer_nav_html}</nav></footer>'
            f'<script src="/app.js?v=20261010" defer></script></body></html>')

def build_news_index(lang):
    n = NEWS[lang]
    url = f"{SITE}/news/" if lang == "en" else f"{SITE}/{lang}/news/"
    home_href = HOME_URL[lang]
    bread = json.dumps([
        {"@type": "ListItem", "position": 1, "name": "Noomicheems", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": NEWS_NAME[lang], "item": url},
    ], ensure_ascii=False)
    items_html = ""
    item_list = []
    for name, blurb, href, item_url in n["items"]:
        items_html += f'<li><h2><a href="{href}">{name}</a></h2><p>{blurb}</p></li>'
        item_list.append({"@type": "ListItem", "position": len(item_list) + 1,
                          "name": name, "url": item_url or (f"{SITE}{href}" if href.startswith("/") else href)})
    crumb_visible = (f'<nav class="breadcrumbs" aria-label="Breadcrumb">'
                     f'<a href="{home_href}">{HOME_TXT[lang]}</a><span aria-hidden="true">›</span>'
                     f'<span aria-current="page">{NEWS_NAME[lang]}</span></nav>')
    item_ld = json.dumps({"@type": "ItemList", "itemListElement": item_list}, ensure_ascii=False)
    body = (f'<article class="article">{crumb_visible}<p class="eyebrow">{esc(n["eyebrow"])}</p>'
            f'<h1>{esc(n["h1"])}</h1><p class="intro">{n["intro"]}</p><ul class="game-index">{items_html}</ul>'
            f'<p class="fine">Game news index · Independent site · Sources cited on each article page.</p>'
            f'</article>')
    html = shell(lang, n["title"], n["desc"], url, hreflangs(None, True), body, nav_slug=None, nav_dir=True)
    # inject BreadcrumbList + ItemList JSON-LD before the adsense meta
    html = html.replace('<meta name="google-adsense-account"',
        f'<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": {bread}}}</script>'
        f'<script type="application/ld+json">{item_ld}</script><meta name="google-adsense-account"', 1)
    return html

def build_news_article(lang, slug):
    p = NEWS_PAGES[slug][lang]
    t, d, eyebrow, h1, intro, sections, fine = p
    url = f"{SITE}/{slug}/" if lang == "en" else f"{SITE}/{lang}/{slug}/"
    home_href = HOME_URL[lang]
    page_short = {"the-sift-minecraft": "The Sift Minecraft", "wow-forever": "World of Warcraft: Forever"}[slug]
    bread = json.dumps([
        {"@type": "ListItem", "position": 1, "name": "Noomicheems", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": NEWS_NAME[lang], "item": f"{SITE}/news/" if lang == "en" else f"{SITE}/{lang}/news/"},
        {"@type": "ListItem", "position": 3, "name": page_short, "item": url},
    ], ensure_ascii=False)
    crumb_visible = (f'<nav class="breadcrumbs" aria-label="Breadcrumb">'
                     f'<a href="{home_href}">{HOME_TXT[lang]}</a><span aria-hidden="true">›</span>'
                     f'<a href="{NEWS_URL[lang]}">{NEWS_NAME[lang]}</a><span aria-hidden="true">›</span>'
                     f'<span aria-current="page">{page_short}</span></nav>')
    fine_html = f'<p class="fine">{fine}</p>' if fine else ""
    body = (f'<article class="article">{crumb_visible}<p class="eyebrow">{esc(eyebrow)}</p>'
            f'<h1>{esc(h1)}</h1><p class="intro">{intro}</p>{render_sections(sections)}{fine_html}</article>')
    html = shell(lang, t, d, url, hreflangs(slug), body, nav_slug=slug, nav_dir=False)
    html = html.replace('<meta name="google-adsense-account"',
        f'<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": {bread}}}</script>'
        f'<meta name="google-adsense-account"', 1)
    return html

count = 0
# 1) News index pages (5 languages)
for lang in ORDER:
    html = build_news_index(lang)
    d = os.path.join(DEPLOY, "news") if lang == "en" else os.path.join(DEPLOY, lang, "news")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    count += 1
    print("wrote", lang, "news")

# 2) News article pages (2 slugs x 5 languages)
for slug in NEWS_PAGES:
    for lang in ORDER:
        html = build_news_article(lang, slug)
        d = os.path.join(DEPLOY, slug) if lang == "en" else os.path.join(DEPLOY, lang, slug)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        count += 1
        print("wrote", lang, slug)

# 3) Regenerate sitemap: 16 slugs per language x 5 = 80 URLs
slugs = ["about", "controls", "guide", "help", "privacy", "sources", "terms", "index",
         "lagos-life-game", "halo-ce-browser", "freeze-tag-meaning", "noomiclone-tips", "games",
         "news", "the-sift-minecraft", "wow-forever"]
lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for lang in ORDER:
    for slug in slugs:
        if slug == "index":
            url = f"{SITE}/" if lang == "en" else f"{SITE}/{lang}/"
        else:
            url = f"{SITE}/{slug}/" if lang == "en" else f"{SITE}/{lang}/{slug}/"
        lines.append(f"  <url><loc>{url}</loc><lastmod>2026-10-11</lastmod></url>")
lines.append("</urlset>")
with open(os.path.join(DEPLOY, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("sitemap written:", len(lines) - 3, "urls")
print("TOTAL", count)
