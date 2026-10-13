#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the 4 new pages in ru/es/pt/id from the live-site template."""
import os, json

DEPLOY = os.path.dirname(os.path.abspath(__file__))
SITE = "https://noomicheems.online"

LANGS = {
    "ru": {
        "skip": "К содержимому",
        "header_nav": [("Играть", "/ru/#game"), ("Управление", "/ru/controls/"), ("Как играть", "/ru/guide/")],
        "small": ("Независимый сайт ↗", "/ru/about/"),
        "lang_label": "Язык",
        "home": "Главная",
        "games_name": "Игры в браузере",
        "footer_desc": "Оригинальный NoomiClone от jamesnorth. Независимый сайт, не связанный с автором. Это не мод Noomicheems.",
        "footer_nav": [
            ("О сайте", "/ru/about/"), ("Управление", "/ru/controls/"), ("Как играть", "/ru/guide/"),
            ("Игра и автор", "/ru/sources/"), ("Ещё игры", "/ru/games/"),
            ("Конфиденциальность", "/ru/privacy/"), ("Условия", "/ru/terms/"), ("Помощь", "/ru/help/"),
        ],
    },
    "es": {
        "skip": "Ir al contenido",
        "header_nav": [("Jugar", "/es/#game"), ("Controles", "/es/controls/"), ("Cómo jugar", "/es/guide/")],
        "small": ("Sitio independiente ↗", "/es/about/"),
        "lang_label": "Idioma",
        "home": "Inicio",
        "games_name": "Juegos de navegador",
        "footer_desc": "NoomiClone original de jamesnorth. Sitio independiente, sin afiliación al autor. No es el mod Noomicheems.",
        "footer_nav": [
            ("Acerca del sitio", "/es/about/"), ("Controles", "/es/controls/"), ("Cómo jugar", "/es/guide/"),
            ("Juego y autor", "/es/sources/"), ("Más juegos", "/es/games/"),
            ("Privacidad", "/es/privacy/"), ("Condiciones", "/es/terms/"), ("Ayuda", "/es/help/"),
        ],
    },
    "pt": {
        "skip": "Ir para o conteúdo",
        "header_nav": [("Jogar", "/pt/#game"), ("Controles", "/pt/controls/"), ("Como jogar", "/pt/guide/")],
        "small": ("Site independente ↗", "/pt/about/"),
        "lang_label": "Idioma",
        "home": "Início",
        "games_name": "Jogos de navegador",
        "footer_desc": "NoomiClone original de jamesnorth. Site independente, sem vínculo com o autor. Não é o mod Noomicheems.",
        "footer_nav": [
            ("Sobre", "/pt/about/"), ("Controles", "/pt/controls/"), ("Como jogar", "/pt/guide/"),
            ("Jogo e autor", "/pt/sources/"), ("Mais jogos", "/pt/games/"),
            ("Privacidade", "/pt/privacy/"), ("Termos", "/pt/terms/"), ("Ajuda", "/pt/help/"),
        ],
    },
    "id": {
        "skip": "Ke konten utama",
        "header_nav": [("Main", "/id/#game"), ("Kontrol", "/id/controls/"), ("Cara bermain", "/id/guide/")],
        "small": ("Situs independen ↗", "/id/about/"),
        "lang_label": "Bahasa",
        "home": "Beranda",
        "games_name": "Game Browser",
        "footer_desc": "NoomiClone asli karya jamesnorth. Situs independen, tidak berafiliasi dengan pembuatnya. Bukan mod Noomicheems.",
        "footer_nav": [
            ("Tentang", "/id/about/"), ("Kontrol", "/id/controls/"), ("Cara bermain", "/id/guide/"),
            ("Game dan pembuat", "/id/sources/"), ("Game lainnya", "/id/games/"),
            ("Privasi", "/id/privacy/"), ("Ketentuan", "/id/terms/"), ("Bantuan", "/id/help/"),
        ],
    },
}

EN = {
    "skip": "Skip to content",
    "header_nav": [("Play", "/#game"), ("Controls", "/controls/"), ("How to play", "/guide/")],
    "small": ("Independent site ↗", "/about/"),
    "lang_label": "Language",
    "home": "Home",
    "games_name": "Browser Games",
    "footer_desc": "Original NoomiClone by jamesnorth. Independent site; not affiliated with its developer. Not the Noomicheems mod.",
    "footer_nav": [
        ("About", "/about/"), ("Controls", "/controls/"), ("How to play", "/guide/"),
        ("Game & developer", "/sources/"), ("More games", "/games/"),
        ("Privacy", "/privacy/"), ("Terms", "/terms/"), ("Help", "/help/"),
    ],
}

# Page display names for breadcrumbs and the games index, per language.
PAGE_SHORT = {
    "lagos-life-game": {"en": "Lagos Life Game", "ru": "Lagos Life Game", "es": "Lagos Life Game", "pt": "Lagos Life Game", "id": "Lagos Life Game"},
    "halo-ce-browser": {"en": "Halo CE Browser", "ru": "Halo CE Browser", "es": "Halo CE Browser", "pt": "Halo CE Browser", "id": "Halo CE Browser"},
    "freeze-tag-meaning": {"en": "Freeze Tag", "ru": "Freeze Tag", "es": "Freeze Tag", "pt": "Freeze Tag", "id": "Freeze Tag"},
    "noomiclone-tips": {"en": "NoomiClone Tips", "ru": "NoomiClone: советы", "es": "Consejos de NoomiClone", "pt": "Dicas de NoomiClone", "id": "Tips NoomiClone"},
}

# Games index page content, per language.
GAMES = {
    "en": {
        "title": "Browser Games — Play & Learn About Games in Your Browser",
        "desc": "Index of browser games covered on Noomicheems: play NoomiClone, read about Lagos Life, Halo CE Browser, freeze tag rules and NoomiClone tips.",
        "eyebrow": "BROWSER GAMES / INDEX",
        "h1": "Browser Games on Noomicheems",
        "intro": "Everything on this site in one place: the playable original NoomiClone and the browser games and terms we cover. Each entry links to its guide.",
        "items": [
            ("NoomiClone", "Play the original physics bar game right on the homepage — arch, tuck, release.", "/#game", None),
            ("Lagos Life Game", "Free browser life simulator set in Lagos: how to start, work, earn and rent.", "/lagos-life-game/", "https://noomicheems.online/lagos-life-game/"),
            ("Halo CE Browser", "Unofficial fan port running Halo: Combat Evolved in a browser tab.", "/halo-ce-browser/", "https://noomicheems.online/halo-ce-browser/"),
            ("Freeze Tag", "What freeze tag means, its rules and common variations of the playground classic.", "/freeze-tag-meaning/", "https://noomicheems.online/freeze-tag-meaning/"),
            ("NoomiClone Tips", "Practice tips for the browser version: timing, focus and one-variable-at-a-time.", "/noomiclone-tips/", "https://noomicheems.online/noomiclone-tips/"),
        ],
    },
    "ru": {
        "title": "Игры в браузере — играйте и узнавайте об играх в браузере",
        "desc": "Указатель браузерных игр на Noomicheems: играйте в NoomiClone, читайте о Lagos Life, Halo CE Browser, правилах freeze tag и советах по NoomiClone.",
        "eyebrow": "БРАУЗЕРНЫЕ ИГРЫ / УКАЗАТЕЛЬ",
        "h1": "Браузерные игры на Noomicheems",
        "intro": "Всё на этом сайте в одном месте: играбельный оригинальный NoomiClone и браузерные игры и термины, о которых мы рассказываем. Каждая запись ведёт к своему гиду.",
        "items": [
            ("NoomiClone", "Играйте в оригинальную физическую игру на перекладине прямо на главной — прогиб, группировка, отпускание.", "/ru/#game", None),
            ("Lagos Life Game", "Бесплатный браузерный симулятор жизни в Лагосе: как начать, работать, зарабатывать и снимать жильё.", "/ru/lagos-life-game/", "https://noomicheems.online/ru/lagos-life-game/"),
            ("Halo CE Browser", "Неофициальный фанатский порт, запускающий Halo: Combat Evolved во вкладке браузера.", "/ru/halo-ce-browser/", "https://noomicheems.online/ru/halo-ce-browser/"),
            ("Freeze Tag", "Что значит freeze tag, правила и распространённые варианты дворовой классики.", "/ru/freeze-tag-meaning/", "https://noomicheems.online/ru/freeze-tag-meaning/"),
            ("NoomiClone: советы", "Советы для браузерной версии: тайминг, фокус и по одной переменной за раз.", "/ru/noomiclone-tips/", "https://noomicheems.online/ru/noomiclone-tips/"),
        ],
    },
    "es": {
        "title": "Juegos de navegador: juega y aprende sobre juegos en tu navegador",
        "desc": "Índice de juegos de navegador en Noomicheems: juega a NoomiClone, lee sobre Lagos Life, Halo CE Browser, las reglas de freeze tag y consejos de NoomiClone.",
        "eyebrow": "JUEGOS DE NAVEGADOR / ÍNDICE",
        "h1": "Juegos de navegador en Noomicheems",
        "intro": "Todo en este sitio en un lugar: el NoomiClone original jugable y los juegos y términos de navegador que cubrimos. Cada entrada enlaza a su guía.",
        "items": [
            ("NoomiClone", "Juega al juego de física original en la barra desde la página principal: arquea, agrupa, suelta.", "/es/#game", None),
            ("Lagos Life Game", "Simulador de vida gratis en el navegador ambientado en Lagos: cómo empezar, trabajar, ganar y alquilar.", "/es/lagos-life-game/", "https://noomicheems.online/es/lagos-life-game/"),
            ("Halo CE Browser", "Port no oficial de fans que ejecuta Halo: Combat Evolved en una pestaña.", "/es/halo-ce-browser/", "https://noomicheems.online/es/halo-ce-browser/"),
            ("Freeze Tag", "Qué significa freeze tag, sus reglas y variantes comunes del clásico de patio.", "/es/freeze-tag-meaning/", "https://noomicheems.online/es/freeze-tag-meaning/"),
            ("Consejos de NoomiClone", "Consejos para la versión de navegador: ritmo, enfoque y una variable a la vez.", "/es/noomiclone-tips/", "https://noomicheems.online/es/noomiclone-tips/"),
        ],
    },
    "pt": {
        "title": "Jogos de navegador: jogue e aprenda sobre jogos no navegador",
        "desc": "Índice de jogos de navegador no Noomicheems: jogue NoomiClone, leia sobre Lagos Life, Halo CE Browser, as regras de freeze tag e dicas de NoomiClone.",
        "eyebrow": "JOGOS DE NAVEGADOR / ÍNDICE",
        "h1": "Jogos de navegador no Noomicheems",
        "intro": "Tudo neste site em um lugar: o NoomiClone original jogável e os jogos e termos de navegador que cobrimos. Cada entrada leva ao seu guia.",
        "items": [
            ("NoomiClone", "Jogue o jogo de física original na barra direto na página inicial: arqueie, agrupe, solte.", "/pt/#game", None),
            ("Lagos Life Game", "Simulador de vida grátis no navegador ambientado em Lagos: como começar, trabalhar, ganhar e alugar.", "/pt/lagos-life-game/", "https://noomicheems.online/pt/lagos-life-game/"),
            ("Halo CE Browser", "Port não oficial de fãs que roda Halo: Combat Evolved numa aba do navegador.", "/pt/halo-ce-browser/", "https://noomicheems.online/pt/halo-ce-browser/"),
            ("Freeze Tag", "O que significa freeze tag, suas regras e variações comuns do clássico de quintal.", "/pt/freeze-tag-meaning/", "https://noomicheems.online/pt/freeze-tag-meaning/"),
            ("Dicas de NoomiClone", "Dicas para a versão de navegador: ritmo, foco e uma variável por vez.", "/pt/noomiclone-tips/", "https://noomicheems.online/pt/noomiclone-tips/"),
        ],
    },
    "id": {
        "title": "Game Browser: Mainkan dan Pelajari Game di Browser Anda",
        "desc": "Indeks game browser di Noomicheems: mainkan NoomiClone, baca tentang Lagos Life, Halo CE Browser, aturan freeze tag, dan tips NoomiClone.",
        "eyebrow": "GAME BROWSER / INDEKS",
        "h1": "Game Browser di Noomicheems",
        "intro": "Semua di situs ini dalam satu tempat: NoomiClone asli yang bisa dimainkan dan game serta istilah browser yang kami bahas. Setiap entri menautkan ke panduannya.",
        "items": [
            ("NoomiClone", "Mainkan game fisika palang asli langsung di halaman utama — melengkung, menekuk, melepas.", "/id/#game", None),
            ("Lagos Life Game", "Simulator kehidupan gratis di browser berlatar Lagos: cara memulai, bekerja, mencari uang, dan menyewa.", "/id/lagos-life-game/", "https://noomicheems.online/id/lagos-life-game/"),
            ("Halo CE Browser", "Port penggemar tidak resmi yang menjalankan Halo: Combat Evolved di tab browser.", "/id/halo-ce-browser/", "https://noomicheems.online/id/halo-ce-browser/"),
            ("Freeze Tag", "Apa arti freeze tag, aturannya, dan variasi umum klasik halaman rumah.", "/id/freeze-tag-meaning/", "https://noomicheems.online/id/freeze-tag-meaning/"),
            ("Tips NoomiClone", "Tips untuk versi browser: waktu, fokus, dan satu variabel per kali.", "/id/noomiclone-tips/", "https://noomicheems.online/id/noomiclone-tips/"),
        ],
    },
}

# Each page: slug, then per-language [title, description, eyebrow, h1, intro,
# sections(list of [tag, content]) , fine(optional)]
PAGES = {
    "lagos-life-game": {
        "ru": [
            "Lagos Life Game — как играть в бесплатный браузерный симулятор жизни",
            "Lagos Life — бесплатный браузерный симулятор жизни в Лагосе. Официальный сайт, как начать играть, работа, деньги и аренда жилья.",
            "БРАУЗЕРНЫЕ ИГРЫ / СИМУЛЯТОР ЖИЗНИ",
            "Lagos Life Game: как играть в браузерный симулятор жизни",
            "Lagos Life — бесплатная браузерная многопользовательская игра, симулятор жизни в Лагосе (Нигерия). На этой странице — где играть, как начать и чем заняться в игре.",
            [
                ["h2", "Что такое игра Lagos Life?"],
                ["p", "Lagos Life — бесплатный браузерный симулятор жизни от нигерийского разработчика Шалома Райхамена. Игра вышла 1 октября 2026 года и быстро росла: по сообщениям, за первую неделю в неё сыграли более двух миллионов человек. Вы создаёте персонажа, ищете работу, зарабатываете деньги и строите жизнь в виртуальном Лагосе — по форме это похоже на симулятор жизни вроде The Sims, но игра полностью идёт в браузере."],
                ["h2", "Где играть в Lagos Life"],
                ["p", "Официальная игра находится на сайте <a href=\"https://lagoslife.app/\">lagoslife.app</a>. Она работает в браузере, регистрация бесплатная. Интерфейс оригинальной игры остаётся на английском, устанавливать ничего не нужно."],
                ["h2", "Как играть в Lagos Life"],
                ["ul", ["<b>Создайте аккаунт</b> — зарегистрируйтесь бесплатно на официальном сайте и войдите в игру.", "<b>Создайте персонажа</b> — начните свою историю в Лагосе и выберите, как жить в городе.", "<b>Найдите работу и зарабатывайте</b> — работа — основной цикл: зарабатывайте, тратьте и управляйте средствами.", "<b>Получите жильё</b> — арендуйте или покупайте недвижимость по мере развития.", "<b>Исследуйте Лагос</b> — мир заимствует детали реальной жизни Лагоса: от уличных сцен до местных локаций."]],
                ["h2", "Lagos Life и Lagos Lifestyle — это одно и то же?"],
                ["p", "Оба запроса ведут к одной браузерной игре. Кто-то пишет «lagos lifestyle game», кто-то — «lagos life game»; официальный сайт использует название Lagos Life."],
                ["h2", "Это официальный сайт Lagos Life?"],
                ["p", "Нет. Это независимая страница-гид. Игру Lagos Life создал Шалом Райхамен; эта страница лишь объясняет, где найти и как играть."],
                ["h2", "Ещё браузерные игры на этом сайте"],
                ["p", "Ищете другие игры в браузере? Попробуйте <a href=\"/#game\">NoomiClone</a>, <a href=\"/halo-ce-browser/\">Halo CE Browser</a> или почитайте, <a href=\"/freeze-tag-meaning/\">что значит freeze tag</a>."],
            ],
            "Источники: <a href=\"https://lagoslife.app/\">lagoslife.app</a> (официальная игра) и <a href=\"https://www.withinnigeria.com/2026/10/09/lagos-life-game-how-to-play-nigerias-viral-life-simulator-and-build-your-virtual-life/\">Within Nigeria</a>, проверено 10 октября 2026 года.",
        ],
        "es": [
            "Lagos Life Game: cómo jugar al simulador de vida gratis en el navegador",
            "Lagos Life es un simulador de vida gratis en el navegador ambientado en Lagos. Juego oficial, cómo jugar, trabajar, ganar dinero y alquilar una casa.",
            "JUEGOS DE NAVEGADOR / SIMULADOR DE VIDA",
            "Lagos Life Game: cómo jugar al simulador de vida del navegador",
            "Lagos Life es un juego multijugador gratis en el navegador que funciona como un simulador de vida ambientado en Lagos (Nigeria). Esta página explica dónde jugar, cómo empezar y qué hacer dentro.",
            [
                ["h2", "¿Qué es el juego Lagos Life?"],
                ["p", "Lagos Life es un simulador de vida gratis en el navegador creado por la desarrolladora nigeriana Shalom Rayhamen. Se lanzó el 1 de octubre de 2026 y creció rápido: según informes, superó los dos millones de jugadores en su primera semana. Creas un personaje, encuentras trabajo, ganas dinero y construyes una vida en un Lagos virtual, con una forma similar a un simulador de vida como Los Sims, pero jugado enteramente en el navegador."],
                ["h2", "Dónde jugar a Lagos Life"],
                ["p", "El juego oficial está en <a href=\"https://lagoslife.app/\">lagoslife.app</a>. Funciona en el navegador y el registro es gratis. La interfaz original del juego sigue en inglés y no hace falta instalar nada."],
                ["h2", "Cómo jugar a Lagos Life"],
                ["ul", ["<b>Crea una cuenta</b> — regístrate gratis en el sitio oficial y entra al juego.", "<b>Crea tu personaje</b> — empieza tu propia historia en Lagos y elige cómo vivir en la ciudad.", "<b>Encuentra trabajo y gana dinero</b> — el trabajo es el ciclo central: gana, gasta y administra lo que tienes.", "<b>Consigue una casa</b> — alquila o compra una propiedad según avanzas.", "<b>Explora Lagos</b> — el mundo toma prestados detalles de la vida real de Lagos, desde escenas callejeras hasta sitios locales."]],
                ["h2", "¿Lagos Life es lo mismo que Lagos Lifestyle?"],
                ["p", "Ambas frases de búsqueda llevan al mismo juego de navegador. Unos escriben «lagos lifestyle game» y otros «lagos life game»; el sitio oficial usa el nombre Lagos Life."],
                ["h2", "¿Es este el sitio oficial de Lagos Life?"],
                ["p", "No. Esta es una página de guía independiente. Lagos Life lo hizo Shalom Rayhamen; esta página solo explica cómo encontrar y jugar."],
                ["h2", "Más juegos de navegador en este sitio"],
                ["p", "¿Buscas más juegos para jugar en una pestaña? Prueba <a href=\"/#game\">NoomiClone</a>, <a href=\"/halo-ce-browser/\">Halo CE Browser</a> o lee <a href=\"/freeze-tag-meaning/\">qué significa freeze tag</a>."],
            ],
            "Fuentes: <a href=\"https://lagoslife.app/\">lagoslife.app</a> (juego oficial) y <a href=\"https://www.withinnigeria.com/2026/10/09/lagos-life-game-how-to-play-nigerias-viral-life-simulator-and-build-your-virtual-life/\">Within Nigeria</a>, consultado el 10 de octubre de 2026.",
        ],
        "pt": [
            "Lagos Life Game: como jogar o simulador de vida grátis no navegador",
            "Lagos Life é um simulador de vida grátis no navegador ambientado em Lagos. Jogo oficial, como jogar, trabalhar, ganhar dinheiro e alugar casa.",
            "JOGOS DE NAVEGADOR / SIMULADOR DE VIDA",
            "Lagos Life Game: como jogar o simulador de vida do navegador",
            "Lagos Life é um jogo multijogador grátis no navegador que funciona como um simulador de vida ambientado em Lagos (Nigéria). Esta página mostra onde jogar, como começar e o que fazer dentro do jogo.",
            [
                ["h2", "O que é o jogo Lagos Life?"],
                ["p", "Lagos Life é um simulador de vida grátis no navegador criado pela desenvolvedora nigeriana Shalom Rayhamen. Foi lançado em 1º de outubro de 2026 e cresceu rápido: segundo reportagens, passou de dois milhões de jogadores na primeira semana. Você cria um personagem, encontra trabalho, ganha dinheiro e constrói uma vida em um Lagos virtual, com formato parecido com um simulador de vida como The Sims, mas jogado inteiramente no navegador."],
                ["h2", "Onde jogar Lagos Life"],
                ["p", "O jogo oficial está em <a href=\"https://lagoslife.app/\">lagoslife.app</a>. Funciona no navegador e o cadastro é grátis. A interface original do jogo continua em inglês e não é preciso instalar nada."],
                ["h2", "Como jogar Lagos Life"],
                ["ul", ["<b>Crie uma conta</b> — cadastre-se grátis no site oficial e entre no jogo.", "<b>Crie seu personagem</b> — comece sua própria história em Lagos e escolha como viver na cidade.", "<b>Arranje trabalho e ganhe dinheiro</b> — o trabalho é o ciclo central: ganhe, gaste e administre o que tem.", "<b>Consiga uma casa</b> — alugue ou compre um imóvel conforme avança.", "<b>Explore Lagos</b> — o mundo usa detalhes da vida real de Lagos, de cenas de rua a pontos locais."]],
                ["h2", "Lagos Life é o mesmo que Lagos Lifestyle?"],
                ["p", "As duas frases de busca levam ao mesmo jogo de navegador. Alguns escrevem «lagos lifestyle game», outros «lagos life game»; o site oficial usa o nome Lagos Life."],
                ["h2", "Este é o site oficial de Lagos Life?"],
                ["p", "Não. Esta é uma página de guia independente. Lagos Life foi feito por Shalom Rayhamen; esta página apenas explica como encontrar e jogar."],
                ["h2", "Mais jogos de navegador neste site"],
                ["p", "Procurando outros jogos para jogar numa aba? Experimente <a href=\"/#game\">NoomiClone</a>, <a href=\"/halo-ce-browser/\">Halo CE Browser</a> ou leia <a href=\"/freeze-tag-meaning/\">o que significa freeze tag</a>."],
            ],
            "Fontes: <a href=\"https://lagoslife.app/\">lagoslife.app</a> (jogo oficial) e <a href=\"https://www.withinnigeria.com/2026/10/09/lagos-life-game-how-to-play-nigerias-viral-life-simulator-and-build-your-virtual-life/\">Within Nigeria</a>, consultado em 10 de outubro de 2026.",
        ],
        "id": [
            "Lagos Life Game: Cara Memainkan Simulator Kehidupan di Browser",
            "Lagos Life adalah simulator kehidupan gratis di browser yang berlatar Lagos. Temukan game resmi, cara bermain, bekerja, mencari uang, dan menyewa rumah.",
            "GAME BROWSER / SIMULATOR KEHIDUPAN",
            "Lagos Life Game: Cara Memainkan Simulator Kehidupan di Browser",
            "Lagos Life adalah game multipemain gratis di browser yang berfungsi seperti simulator kehidupan berlatar Lagos, Nigeria. Halaman ini menjelaskan tempat bermain, cara memulai, dan apa yang dilakukan di dalam game.",
            [
                ["h2", "Apa itu game Lagos Life?"],
                ["p", "Lagos Life adalah simulator kehidupan gratis di browser buatan developer Nigeria Shalom Rayhamen. Game ini rilis pada 1 Oktober 2026 dan tumbuh cepat: laporan menyebut lebih dari dua juta pemain dalam minggu pertama. Anda membuat karakter, mencari pekerjaan, menghasilkan uang, dan membangun kehidupan di Lagos virtual—bentuknya mirip simulator kehidupan seperti The Sims, tetapi dimainkan sepenuhnya di browser."],
                ["h2", "Tempat bermain Lagos Life"],
                ["p", "Game resminya ada di <a href=\"https://lagoslife.app/\">lagoslife.app</a>. Game berjalan di browser dan pendaftarannya gratis. Antarmuka game asli tetap berbahasa Inggris, dan Anda tidak perlu menginstal apa pun."],
                ["h2", "Cara bermain Lagos Life"],
                ["ul", ["<b>Buat akun</b> — daftar gratis di situs resmi dan masuk ke game.", "<b>Buat karakter Anda</b> — mulai kisah Lagos Anda sendiri dan pilih bagaimana hidup di kota.", "<b>Cari kerja dan hasilkan uang</b> — pekerjaan adalah inti permainan: hasilkan, belanjakan, dan kelola yang Anda punya.", "<b>Dapatkan rumah</b> — sewa atau beli properti seiring kemajuan Anda.", "<b>Jelajahi Lagos</b> — dunia ini meminjam detail kehidupan Lagos yang nyata, dari pemandangan jalan hingga tempat lokal."]],
                ["h2", "Apakah Lagos Life sama dengan Lagos Lifestyle?"],
                ["p", "Kedua frasa pencarian mengarah ke game browser yang sama. Sebagian menulis «lagos lifestyle game», sebagian menulis «lagos life game»; situs resmi memakai nama Lagos Life."],
                ["h2", "Apakah ini situs resmi Lagos Life?"],
                ["p", "Bukan. Ini adalah halaman panduan independen. Lagos Life dibuat oleh Shalom Rayhamen; halaman ini hanya menjelaskan cara menemukan dan memainkannya."],
                ["h2", "Game browser lain di situs ini"],
                ["p", "Mencari game lain yang bisa dimainkan di tab? Coba <a href=\"/#game\">NoomiClone</a>, <a href=\"/halo-ce-browser/\">Halo CE Browser</a>, atau baca <a href=\"/freeze-tag-meaning/\">arti freeze tag</a>."],
            ],
            "Sumber: <a href=\"https://lagoslife.app/\">lagoslife.app</a> (game resmi) dan <a href=\"https://www.withinnigeria.com/2026/10/09/lagos-life-game-how-to-play-nigerias-viral-life-simulator-and-build-your-virtual-life/\">Within Nigeria</a>, diperiksa 10 Oktober 2026.",
        ],
    },
    "halo-ce-browser": {
        "ru": [
            "Halo CE Browser — играйте в Halo: Combat Evolved в браузере",
            "Halo CE Browser — неофициальный фанатский порт, запускающий Halo: Combat Evolved во вкладке браузера: кампания, кооператив и экспериментальные комнаты на 128 игроков.",
            "БРАУЗЕРНЫЕ ИГРЫ / ШУТЕР ОТ ПЕРВОГО ЛИЦА",
            "Halo CE Browser: Halo: Combat Evolved во вкладке",
            "Halo CE Browser — неофициальный фанатский проект, который запускает оригинальную Halo: Combat Evolved во вкладке браузера. Установка и лаунчер не нужны; на этой странице — что работает, что экспериментально и на что обратить внимание.",
            [
                ["h2", "Что такое Halo CE Browser?"],
                ["p", "В конце сентября 2026 года разработчик Митч Хайнс выпустил неофициальный браузерный порт оригинальной Xbox-версии Halo: Combat Evolved. Он построен на проекте декомпиляции Halo CE Universal и не является продуктом Microsoft. По сообщениям, кампания запускается прямо во вкладке браузера, без установки и лаунчера."],
                ["h2", "Что доступно в браузерной версии?"],
                ["ul", ["<b>Полная кампания</b> — оригинальная кампания во вкладке.", "<b>Кооператив на разделённом экране</b> — по сообщениям, работает.", "<b>Классические карты и режимы</b> — карты включают Blood Gulch, Battle Creek и Sidewinder; режимы — Slayer, Team Slayer, CTF, Oddball, King of the Hill и Race.", "<b>Экспериментальные комнаты до 128 игроков</b> — комнаты открываются по пригласительным ссылкам через peer-to-peer. Потолок в 128 игроков не протестирован, поэтому большие комнаты считайте экспериментальными.", "<b>Управление</b> — поддерживаются мышь и клавиатура, а также раскладка в стиле Xbox."]],
                ["h2", "Как играть в Halo CE в браузере"],
                ["p", "Откройте браузерную сборку на настольном ПК, дождитесь загрузки и играйте. Мобильные браузеры не рекомендуются: по сообщениям, порт плохо работает на iOS и Android. В зависимости от сборки вам могут понадобиться собственные файлы игры — следуйте актуальным инструкциям проекта."],
                ["p", "Статья на <a href=\"https://www.eteknix.com/unofficial-halo-combat-evolved-browser-port-arrives-with-split-screen-co-op-and-128-person-multiplayer/\">eTeknix</a> ведёт к играбельной браузерной сборке; сам проект декомпиляции размещён в репозитории <a href=\"https://github.com/cybersecurity/halo-ce-universal\">Halo CE Universal</a> на GitHub. Мы не размещаем игру у себя."],
                ["h2", "Halo CE Browser официальный?"],
                ["p", "Нет. Это независимая фанатская работа, не связанная с Microsoft и с официальными ремейками. Доступность и производительность могут меняться в любой момент."],
                ["h2", "Ещё браузерные игры на этом сайте"],
                ["p", "Хочется чего-то полегче во вкладке? Сыграйте в <a href=\"/#game\">NoomiClone</a>, посмотрите <a href=\"/lagos-life-game/\">игру Lagos Life</a> или почитайте, <a href=\"/freeze-tag-meaning/\">что значит freeze tag и его правила</a>."],
            ],
            "Источники: <a href=\"https://www.eteknix.com/unofficial-halo-combat-evolved-browser-port-arrives-with-split-screen-co-op-and-128-person-multiplayer/\">eTeknix</a> и <a href=\"https://www.indiekings.com/2026/10/halo-combat-evolved-runs-in-browser.html\">Indie Kings</a>, проверено 10 октября 2026 года.",
        ],
        "es": [
            "Halo CE Browser: juega a Halo: Combat Evolved en tu navegador",
            "Halo CE Browser es un port no oficial de fans que ejecuta Halo: Combat Evolved en una pestaña: campaña, cooperativo en pantalla dividida y salas experimentales de 128 jugadores.",
            "JUEGOS DE NAVEGADOR / SHOOTER EN PRIMERA PERSONA",
            "Halo CE Browser: Halo: Combat Evolved en una pestaña",
            "Halo CE Browser es un proyecto no oficial de fans que ejecuta la Halo: Combat Evolved original en una pestaña del navegador. No hace falta instalador ni launcher; esta página explica qué funciona, qué es experimental y qué tener en cuenta.",
            [
                ["h2", "¿Qué es Halo CE Browser?"],
                ["p", "A finales de septiembre de 2026, el desarrollador Mitch Hynes publicó un port no oficial en el navegador de la versión original de Xbox de Halo: Combat Evolved. Se basa en el proyecto de descompilación Halo CE Universal y no es un producto de Microsoft. Según los informes, la campaña carga directamente en una pestaña, sin instalación ni launcher."],
                ["h2", "¿Qué puedes hacer en la versión de navegador?"],
                ["ul", ["<b>Campaña completa</b> — juega a la campaña original en una pestaña.", "<b>Cooperativo en pantalla dividida</b> — según informes, funciona.", "<b>Mapas y modos clásicos</b> — mapas como Blood Gulch, Battle Creek y Sidewinder; modos Slayer, Team Slayer, CTF, Oddball, King of the Hill y Race.", "<b>Salas experimentales de 128 jugadores</b> — las salas se unen por enlace de invitación con red peer-to-peer. El límite de 128 no está probado, así que trata las salas grandes como experimentales.", "<b>Controles</b> — se admiten ratón y teclado, además de una distribución estilo Xbox."]],
                ["h2", "Cómo jugar a Halo CE en tu navegador"],
                ["p", "Abre la versión de navegador en un PC de escritorio, espera a que cargue y empieza a jugar. No se recomiendan los navegadores móviles: según informes, el port funciona mal en iOS y Android. Dependiendo de la versión, puede que necesites tus propios archivos del juego; sigue las instrucciones actuales del proyecto."],
                ["p", "El artículo independiente de <a href=\"https://www.eteknix.com/unofficial-halo-combat-evolved-browser-port-arrives-with-split-screen-co-op-and-128-person-multiplayer/\">eTeknix</a> enlaza a la versión jugable; el proyecto de descompilación está en el repositorio <a href=\"https://github.com/cybersecurity/halo-ce-universal\">Halo CE Universal</a> en GitHub. No alojamos el juego aquí."],
                ["h2", "¿Halo CE Browser es oficial?"],
                ["p", "No. Es trabajo independiente de fans, sin relación con Microsoft ni con ningún remake oficial. La disponibilidad y el rendimiento pueden cambiar en cualquier momento."],
                ["h2", "Más juegos de navegador en este sitio"],
                ["p", "¿Prefieres algo más ligero en una pestaña? Juega a <a href=\"/#game\">NoomiClone</a>, mira el <a href=\"/lagos-life-game/\">juego Lagos Life</a> o lee <a href=\"/freeze-tag-meaning/\">qué significa freeze tag y sus reglas</a>."],
            ],
            "Fuentes: <a href=\"https://www.eteknix.com/unofficial-halo-combat-evolved-browser-port-arrives-with-split-screen-co-op-and-128-person-multiplayer/\">eTeknix</a> y <a href=\"https://www.indiekings.com/2026/10/halo-combat-evolved-runs-in-browser.html\">Indie Kings</a>, consultado el 10 de octubre de 2026.",
        ],
        "pt": [
            "Halo CE Browser: jogue Halo: Combat Evolved no navegador",
            "Halo CE Browser é um port não oficial de fãs que roda Halo: Combat Evolved numa aba: campanha, cooperativo em tela dividida e salas experimentais com 128 jogadores.",
            "JOGOS DE NAVEGADOR / TIRO EM PRIMEIRA PESSOA",
            "Halo CE Browser: Halo: Combat Evolved numa aba",
            "Halo CE Browser é um projeto não oficial de fãs que roda o Halo: Combat Evolved original numa aba do navegador. Não precisa de instalador nem launcher; esta página explica o que funciona, o que é experimental e o que observar.",
            [
                ["h2", "O que é o Halo CE Browser?"],
                ["p", "No fim de setembro de 2026, o desenvolvedor Mitch Hynes lançou um port não oficial no navegador da versão original de Xbox de Halo: Combat Evolved. Ele se baseia no projeto de descompilação Halo CE Universal e não é um produto da Microsoft. Segundo reportagens, a campanha carrega direto numa aba, sem instalação nem launcher."],
                ["h2", "O que dá para fazer na versão de navegador?"],
                ["ul", ["<b>Campanha completa</b> — jogue a campanha original numa aba.", "<b>Cooperativo em tela dividida</b> — segundo reportagens, funciona.", "<b>Mapas e modos clássicos</b> — mapas como Blood Gulch, Battle Creek e Sidewinder; modos Slayer, Team Slayer, CTF, Oddball, King of the Hill e Race.", "<b>Salas experimentais com 128 jogadores</b> — as salas entram por link de convite com rede peer-to-peer. O teto de 128 não foi testado, então trate salas grandes como experimentais.", "<b>Controles</b> — suportam mouse e teclado, além de um layout estilo Xbox."]],
                ["h2", "Como jogar Halo CE no navegador"],
                ["p", "Abra a versão de navegador num PC de mesa, espere carregar e comece a jogar. Navegadores móveis não são recomendados: segundo reportagens, o port roda mal em iOS e Android. Dependendo da versão, talvez você precise dos próprios arquivos do jogo; siga as instruções atuais do projeto."],
                ["p", "O artigo independente da <a href=\"https://www.eteknix.com/unofficial-halo-combat-evolved-browser-port-arrives-with-split-screen-co-op-and-128-person-multiplayer/\">eTeknix</a> linka para a versão jogável; o projeto de descompilação está no repositório <a href=\"https://github.com/cybersecurity/halo-ce-universal\">Halo CE Universal</a> no GitHub. Não hospedamos o jogo aqui."],
                ["h2", "O Halo CE Browser é oficial?"],
                ["p", "Não. É trabalho independente de fãs, sem relação com a Microsoft e separado de qualquer remake oficial. Disponibilidade e desempenho podem mudar a qualquer momento."],
                ["h2", "Mais jogos de navegador neste site"],
                ["p", "Prefere algo mais leve numa aba? Jogue <a href=\"/#game\">NoomiClone</a>, confira o <a href=\"/lagos-life-game/\">jogo Lagos Life</a> ou leia <a href=\"/freeze-tag-meaning/\">o que significa freeze tag e suas regras</a>."],
            ],
            "Fontes: <a href=\"https://www.eteknix.com/unofficial-halo-combat-evolved-browser-port-arrives-with-split-screen-co-op-and-128-person-multiplayer/\">eTeknix</a> e <a href=\"https://www.indiekings.com/2026/10/halo-combat-evolved-runs-in-browser.html\">Indie Kings</a>, consultado em 10 de outubro de 2026.",
        ],
        "id": [
            "Halo CE Browser: Mainkan Halo: Combat Evolved di Browser Anda",
            "Halo CE Browser adalah port penggemar tidak resmi yang menjalankan Halo: Combat Evolved di tab browser: kampanye, co-op layar terbagi, dan ruang eksperimental 128 pemain.",
            "GAME BROWSER / SHOOTER ORANG PERTAMA",
            "Halo CE Browser: Halo: Combat Evolved di Satu Tab",
            "Halo CE Browser adalah proyek penggemar tidak resmi yang menjalankan Halo: Combat Evolved asli di tab browser. Tidak perlu installer atau launcher; halaman ini menjelaskan apa yang berfungsi, apa yang eksperimental, dan apa yang perlu diperhatikan.",
            [
                ["h2", "Apa itu Halo CE Browser?"],
                ["p", "Akhir September 2026, developer Mitch Hynes merilis port browser tidak resmi dari versi Xbox asli Halo: Combat Evolved. Port ini dibangun dari proyek dekompilasi Halo CE Universal dan bukan produk Microsoft. Laporan menyebut kampanye langsung dimuat di tab browser, tanpa instalasi atau launcher terpisah."],
                ["h2", "Apa yang bisa dilakukan di versi browser?"],
                ["ul", ["<b>Kampanye penuh</b> — mainkan kampanye asli di satu tab.", "<b>Co-op layar terbagi</b> — dilaporkan berfungsi.", "<b>Peta dan mode klasik</b> — peta seperti Blood Gulch, Battle Creek, dan Sidewinder; mode Slayer, Team Slayer, CTF, Oddball, King of the Hill, dan Race.", "<b>Ruang eksperimental 128 pemain</b> — ruang diikuti lewat tautan undangan dengan jaringan peer-to-peer. Batas 128 belum teruji, jadi perlakukan ruang besar sebagai eksperimental.", "<b>Kontrol</b> — mendukung mouse dan keyboard, plus tata letak ala Xbox."]],
                ["h2", "Cara bermain Halo CE di browser"],
                ["p", "Buka build browser di PC desktop, tunggu hingga dimuat, dan mulai bermain. Browser ponsel tidak disarankan: port ini dilaporkan berjalan buruk di iOS dan Android. Tergantung build-nya, Anda mungkin perlu file game sendiri—ikuti petunjuk terkini dari proyek."],
                ["p", "Artikel independen <a href=\"https://www.eteknix.com/unofficial-halo-combat-evolved-browser-port-arrives-with-split-screen-co-op-and-128-person-multiplayer/\">eTeknix</a> menautkan ke build browser yang bisa dimainkan; proyek dekompilasinya ada di repositori <a href=\"https://github.com/cybersecurity/halo-ce-universal\">Halo CE Universal</a> di GitHub. Kami tidak menghosting game ini."],
                ["h2", "Apakah Halo CE Browser resmi?"],
                ["p", "Bukan. Ini karya penggemar independen, tidak terkait Microsoft dan terpisah dari remake resmi mana pun. Ketersediaan dan performa bisa berubah kapan saja."],
                ["h2", "Game browser lain di situs ini"],
                ["p", "Lebih suka yang lebih ringan di tab? Mainkan <a href=\"/#game\">NoomiClone</a>, cek <a href=\"/lagos-life-game/\">game Lagos Life</a>, atau baca <a href=\"/freeze-tag-meaning/\">arti freeze tag dan aturannya</a>."],
            ],
            "Sumber: <a href=\"https://www.eteknix.com/unofficial-halo-combat-evolved-browser-port-arrives-with-split-screen-co-op-and-128-person-multiplayer/\">eTeknix</a> dan <a href=\"https://www.indiekings.com/2026/10/halo-combat-evolved-runs-in-browser.html\">Indie Kings</a>, diperiksa 10 Oktober 2026.",
        ],
    },
    "freeze-tag-meaning": {
        "ru": [
            "Freeze Tag: что это значит, правила и как играть",
            "Что означает freeze tag? Правила детской игры в догонялки: как «замерзают» пойманные, как их спасают и распространённые варианты.",
            "ИГРОВЫЕ ТЕРМИНЫ / КЛАССИКА ДВОРА",
            "Freeze Tag: значение, правила и как играть",
            "Freeze tag — детская игра в догонялки, в которой пойманный игрок замирает на месте, «замерзает», пока товарищ по команде не дотронется до него и не освободит. На этой странице — значение, правила и распространённые варианты.",
            [
                ["h2", "Что означает freeze tag?"],
                ["p", "Название описывает главное правило: когда «вода» догоняет и касается игрока, тот замирает на месте. Он не может двигаться, пока другой, ещё не пойманный игрок не коснётся его и не «разморозит». Игра заканчивается, когда замерли все, либо когда истекает время."],
                ["h2", "Основные правила"],
                ["ul", ["<b>Выберите «воду»</b> — один игрок начинает как ловящий.", "<b>Бегите и сальте</b> — «вода» догоняет и осаливает других.", "<b>Замёрз — значит замёрз</b> — пойманный стоит на месте, где его осалили.", "<b>Спасение касанием</b> — свободный товарищ размораживает замёрзшего, дотронувшись до него.", "<b>Условие победы</b> — «вода» выигрывает, когда все замерли; группа выигрывает, если кто-то остаётся свободным до конца времени."]],
                ["h2", "Распространённые варианты"],
                ["p", "Группы часто меняют правила: где-то игрок выбывает после трёх спасений, где-то добавляют «безопасную зону», где нельзя осалить, а где-то замёрзшие стоят с раскинутыми руками, чтобы их было видно. Похожие игры — stuck in the mud и shadow tag, где «замирание» работает иначе."],
                ["h2", "Почему игра так называется?"],
                ["p", "«Tag» — общее имя семейства игр в догонялки: один игрок догоняет и касается других. «Freeze» описывает наказание: пойманные стоят как статуи, пока их не спасут."],
                ["h2", "Ещё браузерные игры на этом сайте"],
                ["p", "Предпочитаете игры во вкладке браузера? Попробуйте <a href=\"/#game\">NoomiClone</a>, изучите <a href=\"/lagos-life-game/\">игру Lagos Life</a> или загляните в <a href=\"/halo-ce-browser/\">Halo CE Browser</a>."],
            ],
            None,
        ],
        "es": [
            "Freeze Tag: qué significa, reglas y cómo se juega",
            "¿Qué significa freeze tag? Las reglas de este juego infantil de persecución: cómo se congelan los atrapados, cómo se rescatan y las variantes comunes.",
            "TÉRMINOS DE JUEGO / CLÁSICOS DEL PATIO",
            "Freeze Tag: significado, reglas y cómo se juega",
            "Freeze tag es un juego infantil de persecución en el que el jugador tocado debe quedarse quieto, «congelado», hasta que un compañero lo toque para liberarlo. Esta página explica el significado, las reglas y las variantes más comunes.",
            [
                ["h2", "¿Qué significa freeze tag?"],
                ["p", "El nombre describe la regla principal: cuando el jugador que «la lleva» toca a alguien, ese jugador se congela en el sitio. No puede moverse hasta que otro jugador no tocado lo toque y lo descongele. La partida termina cuando todos están congelados o cuando se acaba el tiempo."],
                ["h2", "Reglas básicas"],
                ["ul", ["<b>Elegid quién la lleva</b> — un jugador empieza como perseguidor.", "<b>Corre y toca</b> — el perseguidor persigue y toca a los demás.", "<b>Congelado significa congelado</b> — el tocado se queda quieto donde lo tocaron.", "<b>Rescate con un toque</b> — un compañero libre descongela a un congelado tocándolo.", "<b>Condición de victoria</b> — el perseguidor gana si todos quedan congelados; el grupo gana si alguien queda libre hasta que acabe el tiempo."]],
                ["h2", "Variantes comunes"],
                ["p", "Los grupos suelen cambiar las reglas: algunos cuentan «tres rescates» antes de eliminar a alguien, otros añaden una zona segura donde no se puede tocar, y otros hacen que los congelados se queden con los brazos abiertos para que los rescates sean fáciles de ver. Juegos parecidos son stuck in the mud y shadow tag, donde el «congelamiento» funciona distinto."],
                ["h2", "¿Por qué se llama freeze tag?"],
                ["p", "«Tag» es el nombre de la familia de juegos de persecución: uno persigue y toca a los demás. «Freeze» describe el castigo: los tocados quedan como estatuas hasta que los rescatan."],
                ["h2", "Más juegos de navegador en este sitio"],
                ["p", "¿Prefieres juegos en una pestaña? Prueba <a href=\"/#game\">NoomiClone</a>, explora el <a href=\"/lagos-life-game/\">juego Lagos Life</a> o mira <a href=\"/halo-ce-browser/\">Halo CE Browser</a>."],
            ],
            None,
        ],
        "pt": [
            "Freeze Tag: o que significa, regras e como jogar",
            "O que significa freeze tag? As regras desse jogo infantil de pega-pega: como os pegos congelam, como são salvos e as variações comuns.",
            "TERMOS DE JOGO / CLÁSSICOS DO QUINTAL",
            "Freeze Tag: significado, regras e como jogar",
            "Freeze tag é um jogo infantil de pega-pega em que o jogador tocado deve parar no lugar, «congelado», até um colega tocá-lo para libertá-lo. Esta página explica o significado, as regras e as variações comuns.",
            [
                ["h2", "O que significa freeze tag?"],
                ["p", "O nome descreve a regra principal: quando o jogador que «pega» toca alguém, esse jogador congela na hora. Ele não pode se mover até outro jogador não tocado tocá-lo e descongelá-lo. A partida termina quando todos estão congelados ou quando o tempo acaba."],
                ["h2", "Regras básicas"],
                ["ul", ["<b>Escolham quem pega</b> — um jogador começa como o pegador.", "<b>Corra e pegue</b> — o pegador persegue e toca os outros.", "<b>Congelado é congelado</b> — o tocado fica parado onde foi tocado.", "<b>Salvamento por toque</b> — um colega livre descongela um congelado tocando nele.", "<b>Condição de vitória</b> — o pegador vence se todos congelarem; o grupo vence se alguém ficar livre até o tempo acabar."]],
                ["h2", "Variações comuns"],
                ["p", "Os grupos costumam mudar as regras: alguns contam «três salvamentos» antes de eliminar alguém, outros adicionam uma zona segura onde ninguém pode ser pego, e outros fazem os congelados ficarem com os braços abertos para facilitar o salvamento. Jogos parecidos são stuck in the mud e shadow tag, onde o «congelamento» funciona diferente."],
                ["h2", "Por que se chama freeze tag?"],
                ["p", "«Tag» é o nome da família de jogos de pega-pega: um jogador persegue e toca os outros. «Freeze» descreve a punição: os tocados ficam como estátuas até serem salvos."],
                ["h2", "Mais jogos de navegador neste site"],
                ["p", "Prefere jogos numa aba? Experimente <a href=\"/#game\">NoomiClone</a>, explore o <a href=\"/lagos-life-game/\">jogo Lagos Life</a> ou veja o <a href=\"/halo-ce-browser/\">Halo CE Browser</a>."],
            ],
            None,
        ],
        "id": [
            "Freeze Tag: Arti, Aturan, dan Cara Bermain",
            "Apa arti freeze tag? Pelajari aturan permainan kejar-kejaran anak ini, cara pemain beku diselamatkan, dan variasi umumnya.",
            "ISTILAH GAME / KLASIK HALAMAN RUMAH",
            "Freeze Tag: Arti, Aturan, dan Cara Bermain",
            "Freeze tag adalah permainan kejar-kejaran anak di mana pemain yang tertangkap harus berhenti di tempat, «membeku», sampai rekan menyentuhnya untuk membebaskannya. Halaman ini menjelaskan arti, aturan, dan variasi umumnya.",
            [
                ["h2", "Apa arti freeze tag?"],
                ["p", "Nama ini menggambarkan aturan utamanya: saat pemain yang «jadi» menyentuh seseorang, pemain itu langsung membeku di tempat. Ia tidak bisa bergerak sampai pemain lain yang belum tertangkap menyentuhnya dan mencairkannya. Permainan berakhir ketika semua pemain membeku, atau waktu habis."],
                ["h2", "Aturan dasar freeze tag"],
                ["ul", ["<b>Tentukan siapa yang jadi</b> — satu pemain memulai sebagai pengejar.", "<b>Lari dan sentuh</b> — pengejar mengejar dan menyentuh pemain lain.", "<b>Beku berarti beku</b> — pemain yang tersentuh diam di tempat ia disentuh.", "<b>Selamatkan dengan sentuhan</b> — rekan yang bebas mencairkan pemain beku dengan menyentuhnya.", "<b>Kondisi menang</b> — pengejar menang jika semua membeku; kelompok menang jika ada yang tetap bebas sampai waktu habis."]],
                ["h2", "Variasi umum freeze tag"],
                ["p", "Kelompok sering mengubah aturan: ada yang menghitung «tiga penyelamatan» sebelum pemain keluar, ada yang menambah zona aman tempat pemain tidak bisa disentuh, dan ada yang membuat pemain beku berdiri dengan tangan terbuka agar mudah terlihat. Permainan serupa termasuk stuck in the mud dan shadow tag, yang cara «membekukannya» berbeda."],
                ["h2", "Kenapa disebut freeze tag?"],
                ["p", "Kata «tag» adalah nama keluarga permainan kejar-kejaran: satu pemain mengejar dan menyentuh yang lain. «Freeze» menggambarkan hukumannya: pemain yang tersentuh menjadi patung sampai diselamatkan."],
                ["h2", "Game browser lain di situs ini"],
                ["p", "Lebih suka game yang bisa dimainkan di tab? Coba <a href=\"/#game\">NoomiClone</a>, jelajahi <a href=\"/lagos-life-game/\">game Lagos Life</a>, atau lihat <a href=\"/halo-ce-browser/\">Halo CE Browser</a>."],
            ],
            None,
        ],
    },
    "noomiclone-tips": {
        "ru": [
            "NoomiClone: советы по игре, качели и момент отпускания",
            "Советы по NoomiClone для браузерной версии: практикуйте прогиб, группировку и отпускание по одной переменной за раз, сначала наведите фокус на игру и сбрасывайте попытку клавишей R.",
            "ФИЗИЧЕСКИЙ ПЛЕЙБУК / ПРОДВИНУТАЯ ПРАКТИКА",
            "NoomiClone: советы — выше качели, точнее момент отпускания",
            "NoomiClone — физическая песочница на перекладине: вы прогибаетесь, группируетесь и отпускаете. Эти советы помогут практиковаться в браузерной версии, не выдумывая функций, которых в игре нет.",
            [
                ["h2", "Совет 1: сначала наведите фокус на игру"],
                ["p", "Откройте <a href=\"/#game\">плеер на главной странице</a> и сначала кликните внутри игровой области. Управление с клавиатуры — стрелка влево: прогиб, Space: группировка, стрелка вверх: отпустить, R: сброс — работает, только пока игра в фокусе."],
                ["h2", "Совет 2: меняйте одну переменную за раз"],
                ["p", "Повторите ту же последовательность, затем измените только одно: момент отпускания или то, как долго вы держите группировку. Сравнивать попытки гораздо проще, когда меняется одно решение."],
                ["h2", "Совет 3: следите за положением прогиба и группировки"],
                ["p", "Прежде чем добавлять следующее действие, посмотрите, где находится персонаж. Прогиб и группировка меняют форму тела во время качелей; заметить разницу — самый быстрый способ понять физику."],
                ["h2", "Совет 4: сделайте момент отпускания экспериментом"],
                ["p", "Слишком раннее или слишком позднее отпускание меняет траекторию. Сделайте момент отпускания главным экспериментом и сбрасывайте попытку клавишей R."],
                ["h2", "Совет 5: не ждите функций, которых нет в этой сборке"],
                ["p", "Браузерная версия — это оригинальный NoomiClone от jamesnorth. Мы не подтвердили для этой сборки выбор карт, клавишу повторного захвата или функции модов. Если в видео показано мобильное приложение или мод, не считайте, что браузерная версия это умеет. См. <a href=\"/controls/\">гид по управлению</a> и <a href=\"/guide/\">гид для новичков</a>."],
                ["h2", "Ещё браузерные игры на этом сайте"],
                ["p", "Хотите отдохнуть от перекладины? Изучите <a href=\"/lagos-life-game/\">игру Lagos Life</a>, <a href=\"/halo-ce-browser/\">Halo CE Browser</a> или почитайте про <a href=\"/freeze-tag-meaning/\">freeze tag</a>."],
            ],
            None,
        ],
        "es": [
            "Consejos de NoomiClone: mejora tu balanceo y el momento de soltar",
            "Consejos de NoomiClone para la versión de navegador: practica arquear, agrupar y soltar cambiando una variable a la vez, enfoca el juego primero y reinicia entre intentos.",
            "EL LIBRO DE FÍSICA / PRÁCTICA AVANZADA",
            "Consejos de NoomiClone: balancea más alto, suelta a tiempo",
            "NoomiClone es un patio de física en una barra: arqueas, agrupas y sueltas. Estos consejos te ayudan a practicar la versión de navegador sin inventar funciones que el juego no tiene.",
            [
                ["h2", "Consejo 1: enfoca el juego antes de pulsar teclas"],
                ["p", "Abre el <a href=\"/#game\">jugador de la página principal</a> y haz clic primero dentro del área del juego. Los controles de teclado — flecha izquierda para arquear, Espacio para agrupar, flecha arriba para soltar, R para reiniciar — solo funcionan mientras el juego tiene el foco."],
                ["h2", "Consejo 2: cambia una variable cada vez"],
                ["p", "Repite la misma secuencia y luego cambia solo una cosa: el momento de soltar o cuánto tiempo mantienes la agrupación. Comparar intentos es mucho más fácil cuando cambia una sola decisión."],
                ["h2", "Consejo 3: observa las posiciones de arquear y agrupar"],
                ["p", "Antes de añadir otra entrada, mira dónde está el personaje. Arquear y agrupar cambian la forma del cuerpo durante el balanceo; notar la diferencia es la forma más rápida de entender la física."],
                ["h2", "Consejo 4: trata el momento de soltar como el experimento"],
                ["p", "Soltar demasiado pronto o demasiado tarde cambia hacia dónde viajas. Haz del momento de soltar tu experimento principal y reinicia con R entre intentos."],
                ["h2", "Consejo 5: no esperes funciones que esta versión no tiene"],
                ["p", "La versión de navegador es el NoomiClone original de jamesnorth. No hemos verificado un selector de mapas, una tecla de reagarre ni funciones de mods para esta versión. Si un video muestra una app móvil o un mod, no asumas que la versión de navegador lo tiene. Consulta la <a href=\"/controls/\">guía de controles</a> y la <a href=\"/guide/\">guía para empezar</a>."],
                ["h2", "Más juegos de navegador en este sitio"],
                ["p", "¿Un descanso de la barra? Explora el <a href=\"/lagos-life-game/\">juego Lagos Life</a>, <a href=\"/halo-ce-browser/\">Halo CE Browser</a> o lee sobre <a href=\"/freeze-tag-meaning/\">freeze tag</a>."],
            ],
            None,
        ],
        "pt": [
            "Dicas de NoomiClone: melhore seu balanço e o momento de soltar",
            "Dicas de NoomiClone para a versão de navegador: pratique arquear, agrupar e soltar mudando uma variável por vez, foque o jogo primeiro e reinicie entre tentativas.",
            "O MANUAL DE FÍSICA / PRÁTICA AVANÇADA",
            "Dicas de NoomiClone: balance mais alto, solte na hora",
            "NoomiClone é um playground de física numa barra: você arqueia, agrupa e solta. Estas dicas ajudam a praticar a versão de navegador sem inventar recursos que o jogo não tem.",
            [
                ["h2", "Dica 1: foque o jogo antes de apertar teclas"],
                ["p", "Abra o <a href=\"/#game\">player da página inicial</a> e clique primeiro dentro da área do jogo. Os controles de teclado — seta esquerda para arquear, Espaço para agrupar, seta para cima para soltar, R para reiniciar — só funcionam enquanto o jogo está em foco."],
                ["h2", "Dica 2: mude uma variável por vez"],
                ["p", "Repita a mesma sequência e mude apenas uma coisa: o momento de soltar ou por quanto tempo você mantém a agrupação. Comparar tentativas fica muito mais fácil quando muda uma única decisão."],
                ["h2", "Dica 3: observe as posições de arquear e agrupar"],
                ["p", "Antes de adicionar outra entrada, veja onde o personagem está. Arquear e agrupar mudam o formato do corpo durante o balanço; notar a diferença é o jeito mais rápido de entender a física."],
                ["h2", "Dica 4: trate o momento de soltar como o experimento"],
                ["p", "Soltar cedo demais ou tarde demais muda para onde você vai. Faça do momento de soltar seu principal experimento e reinicie com R entre tentativas."],
                ["h2", "Dica 5: não espere recursos que esta versão não tem"],
                ["p", "A versão de navegador é o NoomiClone original de jamesnorth. Não confirmamos seletor de mapas, tecla de segurar de novo nem recursos de mods nesta versão. Se um vídeo mostra um app móvel ou um mod, não assuma que a versão de navegador tem. Veja o <a href=\"/controls/\">guia de controles</a> e o <a href=\"/guide/\">guia para começar</a>."],
                ["h2", "Mais jogos de navegador neste site"],
                ["p", "Quer uma pausa da barra? Explore o <a href=\"/lagos-life-game/\">jogo Lagos Life</a>, o <a href=\"/halo-ce-browser/\">Halo CE Browser</a> ou leia sobre <a href=\"/freeze-tag-meaning/\">freeze tag</a>."],
            ],
            None,
        ],
        "id": [
            "Tips NoomiClone: Tingkatkan Ayunan dan Waktu Lepas Anda",
            "Tips NoomiClone untuk versi browser: latih melengkung, menekuk, dan melepas satu variabel per kali, fokuskan game dulu, dan ulangi antar percobaan.",
            "BUKU FISIKA / LATIHAN LANJUT",
            "Tips NoomiClone: Ayun Lebih Tinggi, Lepas Tepat Waktu",
            "NoomiClone adalah taman bermain fisika di palang: Anda melengkung, menekuk, dan melepas. Tips ini membantu Anda berlatih versi browser tanpa mengarang fitur yang tidak ada di game.",
            [
                ["h2", "Tips 1: Fokuskan game sebelum menekan tombol"],
                ["p", "Buka <a href=\"/#game\">player di halaman utama</a> dan klik dulu di dalam area game. Kontrol keyboard—panah kiri untuk melengkung, Spasi untuk menekuk, panah atas untuk melepas, R untuk mengulang—hanya berfungsi saat game dalam fokus."],
                ["h2", "Tips 2: Ubah satu variabel setiap kali"],
                ["p", "Ulangi urutan input yang sama, lalu ubah hanya satu hal: waktu Anda melepas, atau berapa lama Anda menahan tekukan. Membandingkan percobaan jadi jauh lebih mudah ketika satu keputusan berubah."],
                ["h2", "Tips 3: Perhatikan posisi melengkung dan menekuk"],
                ["p", "Sebelum menambah input lain, lihat di mana karakter berada. Melengkung dan menekuk mengubah bentuk tubuh saat berayun; menyadari perbedaannya adalah cara tercepat memahami fisikanya."],
                ["h2", "Tips 4: Jadikan waktu lepas sebagai eksperimen"],
                ["p", "Melepas terlalu cepat atau terlalu lambat mengubah arah lompatan. Jadikan waktu lepas eksperimen utama Anda dan ulangi dengan R antar percobaan."],
                ["h2", "Tips 5: Jangan mengharapkan fitur yang tidak ada di build ini"],
                ["p", "Versi browser adalah NoomiClone asli karya jamesnorth. Kami belum memverifikasi pemilih peta, tombol pegang ulang, atau fitur mod untuk build ini. Jika video menampilkan aplikasi seluler atau mod, jangan anggap versi browser memilikinya. Lihat <a href=\"/controls/\">panduan kontrol</a> dan <a href=\"/guide/\">panduan memulai</a>."],
                ["h2", "Game browser lain di situs ini"],
                ["p", "Mau istirahat dari palang? Jelajahi <a href=\"/lagos-life-game/\">game Lagos Life</a>, <a href=\"/halo-ce-browser/\">Halo CE Browser</a>, atau baca tentang <a href=\"/freeze-tag-meaning/\">freeze tag</a>."],
            ],
            None,
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

def build_html(lang, slug, page):
    t, d, eyebrow, h1, intro, sections, fine = page
    L = LANGS.get(lang, EN)
    url = f"{SITE}/{slug}/" if lang == "en" else f"{SITE}/{lang}/{slug}/"
    local_path = f"/{slug}/" if lang == "en" else f"/{lang}/{slug}/"
    hreflangs = ""
    order = ["en", "ru", "es", "pt", "id"]
    for lo in order:
        href = f"{SITE}/{slug}/" if lo == "en" else f"{SITE}/{lo}/{slug}/"
        hreflangs += f'<link rel="alternate" hreflang="{lo}" href="{href}">\n'
    hreflangs += f'<link rel="alternate" hreflang="x-default" href="{SITE}/{slug}/">'
    langs_nav = ""
    for lo in order:
        href = f"/{slug}/" if lo == "en" else f"/{lo}/{slug}/"
        cur = ' aria-current="page"' if lo == lang else ""
        label = {"en": "English", "ru": "Русский", "es": "Español", "pt": "Português", "id": "Bahasa Indonesia"}[lo]
        langs_nav += f'<a href="{href}" lang="{lo}" hreflang="{lo}"{cur}>{label}</a>'
    header_nav = "".join(f'<a href="{h}">{txt}</a>' for txt, h in L["header_nav"])
    footer_nav = "".join(f'<a href="{h}">{txt}</a>' for txt, h in L["footer_nav"])
    name_ld = json.dumps(t, ensure_ascii=False)
    desc_ld = json.dumps(d, ensure_ascii=False)
    home_href = "/" if lang == "en" else f"/{lang}/"
    games_href = "/games/" if lang == "en" else f"/{lang}/games/"
    page_short = PAGE_SHORT[slug][lang]
    bread = json.dumps([
        {"@type": "ListItem", "position": 1, "name": "Noomicheems", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": L["games_name"], "item": f"{SITE}{games_href}"},
        {"@type": "ListItem", "position": 3, "name": page_short, "item": url},
    ], ensure_ascii=False)
    crumb_visible = (f'<nav class="breadcrumbs" aria-label="Breadcrumb">'
                     f'<a href="{home_href}">{L["home"]}</a><span aria-hidden="true">›</span>'
                     f'<a href="{games_href}">{L["games_name"]}</a><span aria-hidden="true">›</span>'
                     f'<span aria-current="page">{page_short}</span></nav>')
    fine_html = f'<p class="fine">{fine}</p>' if fine else ""
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="index,follow"><title>{esc(t)}</title><meta name="description" content="{esc(d)}"><meta name="theme-color" content="#171a1b"><link rel="icon" href="/favicon.svg"><link rel="stylesheet" href="/style.css?v=20261010"><script src="/app.js?v=20261010" defer></script><link rel="canonical" href="{url}">{hreflangs}<meta property="og:type" content="website"><meta property="og:title" content="{esc(t)}"><meta property="og:description" content="{esc(d)}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary"><script type="application/ld+json">{{"@context": "https://schema.org", "@type": "WebPage", "name": {name_ld}, "url": "{url}", "description": {desc_ld}, "inLanguage": "{lang}", "isPartOf": {{"@type": "WebSite", "name": "Noomicheems", "url": "{SITE}/"}}}}</script><script type="application/ld+json">{{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": {bread}}}</script><meta name="google-adsense-account" content="ca-pub-1284741242592931"><script src="/analytics.js?v=20261010" defer></script></head><body><a class="skip" href="#main">{L['skip']}</a><header><a class="brand" href="/{lang}/">n<span>↗</span> <b>noomicheems</b></a><nav aria-label="Main">{header_nav}</nav><a class="small" href="{L['small'][1]}">{L['small'][0]}</a></header><nav class="languages" aria-label="{L['lang_label']}">{langs_nav}</nav><main id="main"><article class="article">{crumb_visible}<p class="eyebrow">{esc(eyebrow)}</p><h1>{esc(h1)}</h1><p class="intro">{intro}</p>{render_sections(sections)}{fine_html}</article></main><footer><a class="brand" href="/{lang}/">noomicheems<span>↗</span></a><p>{L['footer_desc']}</p><nav aria-label="Footer">{footer_nav}</nav></footer></body></html>
"""

def build_games_html(lang):
    L = LANGS[lang] if lang != "en" else EN
    g = GAMES[lang]
    url = f"{SITE}/games/" if lang == "en" else f"{SITE}/{lang}/games/"
    hreflangs = ""
    order = ["en", "ru", "es", "pt", "id"]
    for lo in order:
        href = f"{SITE}/games/" if lo == "en" else f"{SITE}/{lo}/games/"
        hreflangs += f'<link rel="alternate" hreflang="{lo}" href="{href}">\n'
    hreflangs += f'<link rel="alternate" hreflang="x-default" href="{SITE}/games/">'
    langs_nav = ""
    for lo in order:
        href = "/games/" if lo == "en" else f"/{lo}/games/"
        cur = ' aria-current="page"' if lo == lang else ""
        label = {"en": "English", "ru": "Русский", "es": "Español", "pt": "Português", "id": "Bahasa Indonesia"}[lo]
        langs_nav += f'<a href="{href}" lang="{lo}" hreflang="{lo}"{cur}>{label}</a>'
    header_nav = "".join(f'<a href="{h}">{txt}</a>' for txt, h in L["header_nav"])
    footer_nav = "".join(f'<a href="{h}">{txt}</a>' for txt, h in L["footer_nav"])
    home_href = "/" if lang == "en" else f"/{lang}/"
    items_html = ""
    item_list = []
    for name, blurb, href, item_url in g["items"]:
        items_html += f'<li><h2><a href="{href}">{name}</a></h2><p>{blurb}</p></li>'
        item_list.append({"@type": "ListItem", "position": len(item_list) + 1,
                          "name": name, "url": item_url or (f"{SITE}{href}" if href.startswith("/") else href)})
    bread = json.dumps([
        {"@type": "ListItem", "position": 1, "name": "Noomicheems", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": L["games_name"], "item": url},
    ], ensure_ascii=False)
    name_ld = json.dumps(g["title"], ensure_ascii=False)
    desc_ld = json.dumps(g["desc"], ensure_ascii=False)
    item_ld = json.dumps({"@type": "ItemList", "itemListElement": item_list}, ensure_ascii=False)
    crumb_visible = (f'<nav class="breadcrumbs" aria-label="Breadcrumb">'
                     f'<a href="{home_href}">{L["home"]}</a><span aria-hidden="true">›</span>'
                     f'<span aria-current="page">{L["games_name"]}</span></nav>')
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="index,follow"><title>{esc(g['title'])}</title><meta name="description" content="{esc(g['desc'])}"><meta name="theme-color" content="#171a1b"><link rel="icon" href="/favicon.svg"><link rel="stylesheet" href="/style.css?v=20261010"><script src="/app.js?v=20261010" defer></script><link rel="canonical" href="{url}">{hreflangs}<meta property="og:type" content="website"><meta property="og:title" content="{esc(g['title'])}"><meta property="og:description" content="{esc(g['desc'])}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary"><script type="application/ld+json">{{"@context": "https://schema.org", "@type": "WebPage", "name": {name_ld}, "url": "{url}", "description": {desc_ld}, "inLanguage": "{lang}", "isPartOf": {{"@type": "WebSite", "name": "Noomicheems", "url": "{SITE}/"}}}}</script><script type="application/ld+json">{{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": {bread}}}</script><script type="application/ld+json">{item_ld}</script><meta name="google-adsense-account" content="ca-pub-1284741242592931"><script src="/analytics.js?v=20261010" defer></script></head><body><a class="skip" href="#main">{L['skip']}</a><header><a class="brand" href="/{lang}/">n<span>↗</span> <b>noomicheems</b></a><nav aria-label="Main">{header_nav}</nav><a class="small" href="{L['small'][1]}">{L['small'][0]}</a></header><nav class="languages" aria-label="{L['lang_label']}">{langs_nav}</nav><main id="main"><article class="article">{crumb_visible}<p class="eyebrow">{esc(g['eyebrow'])}</p><h1>{esc(g['h1'])}</h1><p class="intro">{g['intro']}</p><ul class="game-index">{items_html}</ul></article></main><footer><a class="brand" href="/{lang}/">noomicheems<span>↗</span></a><p>{L['footer_desc']}</p><nav aria-label="Footer">{footer_nav}</nav></footer></body></html>
"""

count = 0
for lang in ["ru", "es", "pt", "id"]:
    for slug, langs in PAGES.items():
        page = langs[lang]
        html = build_html(lang, slug, page)
        d = os.path.join(DEPLOY, lang, slug)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        count += 1
        print("wrote", lang, slug)

# Games index pages in all 5 languages.
for lang in ["en", "ru", "es", "pt", "id"]:
    html = build_games_html(lang)
    d = os.path.join(DEPLOY, "games") if lang == "en" else os.path.join(DEPLOY, lang, "games")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    count += 1
    print("wrote", lang, "games")

# Regenerate sitemap with the 5 games index pages (60 + 5 = 65).
slugs_old = ["about", "controls", "guide", "help", "privacy", "sources", "terms", "index"]
slugs_new = ["lagos-life-game", "halo-ce-browser", "freeze-tag-meaning", "noomiclone-tips", "games"]
lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for lang in ["en", "ru", "es", "pt", "id"]:
    for slug in slugs_old + slugs_new:
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
