import json
import os
import copy

base_dir = "/mnt/d/proyects/profile/i18n"
with open(os.path.join(base_dir, "es.json"), "r", encoding="utf-8") as f:
    es_data = json.load(f)

def make_lang_data(code):
    d = copy.deepcopy(es_data)
    d["_meta"] = {
        "machine_translated": True if code != "es" else False,
        "reviewed": True if code in ["es", "en"] else False
    }
    return d

translations = {
    "en": {
        "lang_name": "English",
        "title": "Manuel Vilcazan — Portfolio & Resume",
        "desc": "Cybersecurity Engineering student. CTFs, community labs, ESP32 hardware, and production software.",
        "identity_title": "Cybersecurity Engineering Student",
        "availability": "Available for internships and employment · On-site in Arequipa & Remote",
        "summary": "Cybersecurity Engineering student (4th semester, SENATI). I don't just solve challenges: I build hands-on labs for the community, microcontroller hardware, and software running in production for real businesses.",
        "nav": { "brand": ">_ mvilcazan", "about": "about", "education": "education", "experience": "experience", "projects": "projects", "competencies": "certifications & ctf", "stack": "stack", "contact": "contact", "download_cv": "Download CV (PDF)", "language_selector_aria": "Select language" },
        "actions": { "view_projects": "View projects", "github_btn": "GitHub ↗", "linkedin_btn": "LinkedIn ↗", "download_cv_btn": "Download CV (PDF)", "copy_email": "Copy email", "email_copied": "Copied!", "close_modal": "Close", "view_preview": "View evidence", "open_pdf": "Open PDF ↗", "view_original": "View full image ↗" },
        "filters": { "aria_label": "Filter projects", "all": "all", "sec": "security", "hw": "hardware", "sw": "software", "web": "web", "nasa": "nasa apps" },
        "badges": { "in_production": "live", "in_use": "in use", "featured": "Featured · Community", "prototype": "Prototype · NASA Space Apps 2026", "course": "Cisco Networking Academy Course", "badge_rank": "Rank", "todo_tag": "Pending confirmation" },
        "sections": {
            "about_title": "About me", "about_sub": "My profile is hybrid: I think like an attacker, build like a developer, and assemble my own hardware. I like completing the entire cycle, from initial concept until someone actually uses it.",
            "education_title": "Education", "education_sub": "Rigorous technical education in cybersecurity, combined with continuous self-learning and future university degree pathway.",
            "experience_title": "Experience", "experience_sub": "Practical enterprise experience and real production deployments, from computer vision to factory systems and web engineering.",
            "projects_title": "Projects", "projects_sub": "Production systems, security tooling, hardware developments, and space mission prototypes.",
            "competencies_title": "Certifications, CTFs & Courses", "competencies_sub": "Active participation in international cybersecurity competitions, structured training tracks, and technical labs.",
            "stack_title": "Stack", "stack_sub": "Tools, technologies, and environments I use for security analysis, development, and hardware.",
            "contact_title": "Let's build something", "contact_sub": "I'm looking for teams where I can break things, fix them, and ship them to production. The fastest way to reach me is on LinkedIn or via email.",
            "footer_copy": "© 2026 Manuel Vilcazan Mendoza", "ai_translation_notice": "AI-assisted translation"
        },
        "stats": [
            { "label": "HTB challenges documented with writeup" },
            { "label": "CTF categories: web, pwn, rev, crypto, forensics, blockchain" },
            { "label": "sites in production" },
            { "label": "end-to-end ESP32 prototypes built" }
        ],
        "pillars": [
            { "title": "Offensive & Defensive Security", "text": "I compete in Hack The Box CTFs with my team, progress through TryHackMe paths, and build custom defensive security tools." },
            { "title": "Software That Gets Used", "text": "Live websites for textile enterprises in Southern Peru and an industrial labeling system for factory floors." },
            { "title": "Hardware & IoT", "text": "ESP32 prototypes: biometric access control with 3D-modeled and printed enclosure, and factory floor intercoms." }
        ],
        "edu_senati": { "degree": "Cybersecurity Engineering (Technical Program)", "status": "Currently in 4th semester", "details": "Technical curriculum focused on network security, secure system administration, vulnerability analysis, and incident response." },
        "edu_transfer": { "institution": "Institution TBD (University Credit Transfer)", "degree": "Bachelor's Degree in Cybersecurity Engineering", "status": "TODO: Target institution and curriculum pending formal confirmation", "details": "Academic continuity pathway towards formal university professional degree." },
        "cisco_disclaimer": "Note: These records are Cisco Networking Academy Courses, not industry certifications.",
        "cisco_badges": "Module badges earned at Cisco Networking Academy (Nov 2025 & Oct 2026): System Safeguards, Threat Analysis, and Cybersecurity Administration.",
        "ctf_honesty": "Solved with AI assistance (Claude Code). Binary reverse engineering was performed exclusively via static analysis, without running untrusted executables.",
        "terminal": {
            "reply_whoami": "manuel · cybersecurity @ SENATI (4th semester)",
            "reply_ls": "shadowbytes/  htb-writeups/  esp32-biometric/\nindustrial-labeling/  intercom/  client-webs/  nasa-prototypes/",
            "reply_cat": "break → understand → build → ship"
        }
    },
    "pt": {
        "lang_name": "Português",
        "title": "Manuel Vilcazan — Portfólio e Currículo",
        "desc": "Estudante de Engenharia em Cibersegurança. CTFs, laboratórios para a comunidade, hardware com ESP32 e software em produção.",
        "identity_title": "Estudante de Engenharia em Cibersegurança",
        "availability": "Disponível para estágio e emprego · Presencial em Arequipa e Remoto",
        "summary": "Estudante de Engenharia em Cibersegurança (4.º ciclo, SENATI). Não fico apenas em resolver desafios: construo laboratórios práticos para a comunidade, hardware com microcontroladores e software em produção em empresas reais.",
        "nav": { "brand": ">_ mvilcazan", "about": "sobre mim", "education": "educação", "experience": "experiência", "projects": "projetos", "competencies": "certificações & ctf", "stack": "stack", "contact": "contato", "download_cv": "Baixar CV (PDF)", "language_selector_aria": "Selecionar idioma" },
        "actions": { "view_projects": "Ver projetos", "github_btn": "GitHub ↗", "linkedin_btn": "LinkedIn ↗", "download_cv_btn": "Baixar CV (PDF)", "copy_email": "Copiar e-mail", "email_copied": "Copiado!", "close_modal": "Fechar", "view_preview": "Ver evidência", "open_pdf": "Abrir PDF ↗", "view_original": "Ver imagem completa ↗" },
        "filters": { "aria_label": "Filtrar projetos", "all": "todos", "sec": "segurança", "hw": "hardware", "sw": "software", "web": "web", "nasa": "nasa apps" },
        "badges": { "in_production": "no ar", "in_use": "em uso", "featured": "Destaque · Comunidade", "prototype": "Protótipo · NASA Space Apps 2026", "course": "Curso de Cisco Networking Academy", "badge_rank": "Posição", "todo_tag": "Pendente de confirmação" },
        "sections": {
            "about_title": "Sobre mim", "about_sub": "Meu perfil é híbrido: penso como atacante, construo como desenvolvedor e monto meu próprio hardware. Gosto de fechar o ciclo completo, da ideia até que alguém a utilize.",
            "education_title": "Educação", "education_sub": "Formação técnica rigorosa em cibersegurança, aliada ao autoaprendizado contínuo e projeção universitária.",
            "experience_title": "Experiência", "experience_sub": "Prática aplicada em empresas e implantações reais em produção, de visão computacional a sistemas industriais e web.",
            "projects_title": "Projetos", "projects_sub": "Sistemas em produção, ferramentas de segurança, hardware e protótipos de missões espaciais.",
            "competencies_title": "Certificações, CTFs e Cursos", "competencies_sub": "Participação ativa em competições internacionais de cibersegurança, trilhas formativas e laboratórios técnicos.",
            "stack_title": "Stack", "stack_sub": "Ferramentas, tecnologias e ambientes que utilizo em análise de segurança, desenvolvimento e hardware.",
            "contact_title": "Vamos construir algo?", "contact_sub": "Busco equipes onde possa quebrar coisas, consertá-las e colocá-las em produção. O canal mais rápido é pelo LinkedIn ou por e-mail.",
            "footer_copy": "© 2026 Manuel Vilcazan Mendoza", "ai_translation_notice": "Tradução assistida por IA"
        },
        "stats": [
            { "label": "desafios de HTB documentados com writeup" },
            { "label": "categorias CTF: web, pwn, rev, crypto, forensics, blockchain" },
            { "label": "sites em produção" },
            { "label": "protótipos com ESP32 construídos de ponta a ponta" }
        ],
        "pillars": [
            { "title": "Segurança Ofensiva e Defensiva", "text": "Compito em CTFs de Hack The Box com minha equipe, avanço em trilhas do TryHackMe e construo ferramentas defensivas próprias." },
            { "title": "Software Que Funciona", "text": "Websites em produção para indústrias têxteis do sul do Peru e sistema de etiquetagem industrial para chão de fábrica." },
            { "title": "Hardware e IoT", "text": "Protótipos com ESP32: controle biométrico com case modelado e impresso em 3D, e intercomunicadores para fábrica." }
        ],
        "edu_senati": { "degree": "Engenharia em Cibersegurança (Programa Técnico)", "status": "Atualmente no 4.º ciclo", "details": "Formação técnica especializada em segurança de redes, administração segura de sistemas, análise de vulnerabilidades e resposta a incidentes." },
        "edu_transfer": { "institution": "Instituição a definir (Aproveitamento Universitário)", "degree": "Convalidação para Engenharia em Cibersegurança", "status": "TODO: Instituição e grade curricular pendentes de confirmação formal", "details": "Plano de continuidade acadêmica para obtenção do diploma universitário profissional." },
        "cisco_disclaimer": "Nota: Estes registros referem-se a Cursos da Cisco Networking Academy, não a certificações industriais.",
        "cisco_badges": "Insígnias de módulo obtidas na Cisco Networking Academy (nov. 2025 e out. 2026): System Safeguards, Threat Analysis e Cybersecurity Administration.",
        "ctf_honesty": "Resolvidos com assistência de IA (Claude Code). Engenharia reversa realizada exclusivamente via análise estática, sem executar binários não confiáveis.",
        "terminal": {
            "reply_whoami": "manuel · cibersegurança @ SENATI (4.º ciclo)",
            "reply_ls": "shadowbytes/  htb-writeups/  esp32-biometrico/\netiquetagem-industrial/  intercom/  webs-clientes/  nasa-prototypes/",
            "reply_cat": "quebrar → entender → construir → entregar"
        }
    },
    "fr": {
        "lang_name": "Français",
        "title": "Manuel Vilcazan — Portfolio & CV",
        "desc": "Étudiant en Ingénierie de Cybersécurité. CTFs, laboratoires pour la communauté, matériel ESP32 et logiciels en production.",
        "identity_title": "Étudiant en Ingénierie de Cybersécurité",
        "availability": "Disponible pour stage et emploi · En présentiel à Arequipa et à distance",
        "summary": "Étudiant en Ingénierie de Cybersécurité (4e semestre, SENATI). Je ne me contente pas de résoudre des défis : je conçois des laboratoires pratiques pour la communauté, du matériel à microcontrôleurs et des logiciels en production dans des entreprises réelles.",
        "nav": { "brand": ">_ mvilcazan", "about": "à propos", "education": "formation", "experience": "expérience", "projects": "projets", "competencies": "certifications & ctf", "stack": "stack", "contact": "contact", "download_cv": "Télécharger CV (PDF)", "language_selector_aria": "Choisir la langue" },
        "actions": { "view_projects": "Voir les projets", "github_btn": "GitHub ↗", "linkedin_btn": "LinkedIn ↗", "download_cv_btn": "Télécharger CV (PDF)", "copy_email": "Copier l'e-mail", "email_copied": "Copié !", "close_modal": "Fermer", "view_preview": "Voir la preuve", "open_pdf": "Ouvrir PDF ↗", "view_original": "Voir image complète ↗" },
        "filters": { "aria_label": "Filtrer les projets", "all": "tous", "sec": "sécurité", "hw": "matériel", "sw": "logiciel", "web": "web", "nasa": "nasa apps" },
        "badges": { "in_production": "en ligne", "in_use": "en service", "featured": "À la une · Communauté", "prototype": "Prototype · NASA Space Apps 2026", "course": "Cours Cisco Networking Academy", "badge_rank": "Rang", "todo_tag": "En attente de confirmation" },
        "sections": {
            "about_title": "À propos de moi", "about_sub": "Mon profil est hybride : je pense comme un attaquant, je construis comme un développeur et j'assemble mon propre matériel. J'aime mener à bien le cycle complet, de la conception à l'usage réel.",
            "education_title": "Formation", "education_sub": "Formation technique rigoureuse en cybersécurité, enrichie par l'auto-apprentissage permanent et une passerelle universitaire.",
            "experience_title": "Expérience", "experience_sub": "Pratique appliquée en entreprise et déploiements réels en production, de la vision par ordinateur aux systèmes d'usine et au web.",
            "projects_title": "Projets", "projects_sub": "Systèmes en production, outillage de sécurité, développements matériels et prototypes d'exploration spatiale.",
            "competencies_title": "Certifications, CTFs & Cours", "competencies_sub": "Participation active aux compétitions internationales de cybersécurité, parcours de formation et laboratoires techniques.",
            "stack_title": "Stack", "stack_sub": "Outils, technologies et environnements que j'emploie en analyse de sécurité, développement et électronique.",
            "contact_title": "Bâtissons un projet ensemble", "contact_sub": "Je recherche des équipes où je peux casser, réparer et déployer en production. Le moyen le plus direct est LinkedIn ou par e-mail.",
            "footer_copy": "© 2026 Manuel Vilcazan Mendoza", "ai_translation_notice": "Traduction assistée par IA"
        },
        "stats": [
            { "label": "défis HTB documentés avec writeup" },
            { "label": "catégories CTF : web, pwn, rev, crypto, forensics, blockchain" },
            { "label": "sites web en production" },
            { "label": "prototypes ESP32 conçus de bout en bout" }
        ],
        "pillars": [
            { "title": "Sécurité Offensive & Défensive", "text": "Je participe à des CTFs Hack The Box en équipe, progresse sur TryHackMe et développe des outils défensifs sur mesure." },
            { "title": "Logiciels Opérationnels", "text": "Sites web en production pour des entreprises textiles du sud du Pérou et système d'étiquetage industriel pour usine." },
            { "title": "Matériel & IoT", "text": "Prototypes ESP32 : contrôle biométrique avec boîtier modélisé et imprimé en 3D, et interphones pour atelier industriel." }
        ],
        "edu_senati": { "degree": "Ingénierie en Cybersécurité (Programme Technique)", "status": "Actuellement en 4e semestre", "details": "Cursus technique spécialisé en sécurité réseau, administration de systèmes sécurisés, analyse de vulnérabilités et réponse aux incidents." },
        "edu_transfer": { "institution": "Établissement à déterminer (Passerelle Universitaire)", "degree": "Équivalence Licence / Ingénieur en Cybersécurité", "status": "TODO : Établissement et programme en attente de confirmation formelle", "details": "Poursuite d'études académiques vers l'obtention du diplôme professionnel universitaire d'ingénieur." },
        "cisco_disclaimer": "Remarque : Ces attestations correspondent à des Cours de la Cisco Networking Academy, et non à des certifications industrielles.",
        "cisco_badges": "Badges de modules obtenus à la Cisco Networking Academy (nov. 2025 et oct. 2026) : System Safeguards, Threat Analysis et Cybersecurity Administration.",
        "ctf_honesty": "Résolus avec l'assistance d'IA (Claude Code). Le rétro-ingénierie a été mené exclusivement en analyse statique, sans exécution de fichiers binaires non fiables.",
        "terminal": {
            "reply_whoami": "manuel · cybersécurité @ SENATI (4e semestre)",
            "reply_ls": "shadowbytes/  htb-writeups/  esp32-biometrique/\netiquetage-industriel/  intercom/  sites-clients/  nasa-prototypes/",
            "reply_cat": "casser → comprendre → construire → déployer"
        }
    },
    "de": {
        "lang_name": "Deutsch",
        "title": "Manuel Vilcazan — Portfolio & Lebenslauf",
        "desc": "Student der Cybersicherheitstechnik. CTFs, Community-Labs, ESP32-Hardware und Software in Produktion.",
        "identity_title": "Student der Cybersicherheitstechnik",
        "availability": "Verfügbar für Praktika und Festanstellung · Vor Ort in Arequipa & Remote",
        "summary": "Student der Cybersicherheitstechnik (4. Semester, SENATI). Ich löse nicht nur Challenges: Ich baue praxisnahe Labs für die Community, Mikrocontroller-Hardware und Software, die in echten Unternehmen im Produktiveinsatz läuft.",
        "nav": { "brand": ">_ mvilcazan", "about": "über mich", "education": "ausbildung", "experience": "berufserfahrung", "projects": "projekte", "competencies": "zertifikate & ctf", "stack": "stack", "contact": "kontakt", "download_cv": "CV herunterladen (PDF)", "language_selector_aria": "Sprache wählen" },
        "actions": { "view_projects": "Projekte ansehen", "github_btn": "GitHub ↗", "linkedin_btn": "LinkedIn ↗", "download_cv_btn": "CV herunterladen (PDF)", "copy_email": "E-Mail kopieren", "email_copied": "Kopiert!", "close_modal": "Schließen", "view_preview": "Nachweis ansehen", "open_pdf": "PDF öffnen ↗", "view_original": "Vollbild ansehen ↗" },
        "filters": { "aria_label": "Projekte filtern", "all": "alle", "sec": "sicherheit", "hw": "hardware", "sw": "software", "web": "web", "nasa": "nasa apps" },
        "badges": { "in_production": "live", "in_use": "im einsatz", "featured": "Highlight · Community", "prototype": "Prototyp · NASA Space Apps 2026", "course": "Cisco Networking Academy Kurs", "badge_rank": "Platz", "todo_tag": "Bestätigung ausstehend" },
        "sections": {
            "about_title": "Über mich", "about_sub": "Mein Profil ist hybrid: Ich denke wie ein Angreifer, baue wie ein Entwickler und montiere meine eigene Hardware. Ich schließe gerne den gesamten Zyklus ab, von der Idee bis zur realen Nutzung.",
            "education_title": "Ausbildung", "education_sub": "Fundierte technische Ausbildung in Cybersicherheit, ergänzt durch kontinuierliches Selbststudium und universitären Weiterbildungsweg.",
            "experience_title": "Berufserfahrung", "experience_sub": "Praktische Unternehmenserfahrung und reale Produktivinstallationen, von Computer Vision über Fabriksysteme bis hin zur Webentwicklung.",
            "projects_title": "Projekte", "projects_sub": "Produktivsysteme, Sicherheitstools, Hardware-Entwicklungen und Raumfahrt-Prototypen.",
            "competencies_title": "Zertifikate, CTFs & Kurse", "competencies_sub": "Aktive Teilnahme an internationalen Cybersicherheitswettbewerben, strukturierten Ausbildungspfaden und technischen Labs.",
            "stack_title": "Stack", "stack_sub": "Werkzeuge, Technologien und Umgebungen, die ich in Sicherheitsanalyse, Entwicklung und Hardware einsetze.",
            "contact_title": "Lassen Sie uns etwas bauen", "contact_sub": "Ich suche Teams, in denen ich Dinge analysieren, reparieren und produktiv bereitstellen kann. Am schnellsten erreichen Sie mich via LinkedIn oder E-Mail.",
            "footer_copy": "© 2026 Manuel Vilcazan Mendoza", "ai_translation_notice": "KI-unterstützte Übersetzung"
        },
        "stats": [
            { "label": "HTB-Challenges mit Writeup dokumentiert" },
            { "label": "CTF-Kategorien: web, pwn, rev, crypto, forensics, blockchain" },
            { "label": "Websites im Produktiveinsatz" },
            { "label": "durchgängig gebaute ESP32-Prototypen" }
        ],
        "pillars": [
            { "title": "Offensive & Defensive Sicherheit", "text": "Ich nehme im Team an Hack The Box CTFs teil, absolviere TryHackMe-Pfade und entwickle eigene defensive Sicherheitstools." },
            { "title": "Software, die genutzt wird", "text": "Live-Websites für Textilunternehmen im Süden Perus und ein industrielles Etikettiersystem für Fertigungshallen." },
            { "title": "Hardware & IoT", "text": "ESP32-Prototypen: biometrische Zugangskontrolle mit 3D-modelliertem und gedrucktem Gehäuse sowie Industrie-Gegensprechanlagen." }
        ],
        "edu_senati": { "degree": "Cybersicherheitstechnik (Technisches Programm)", "status": "Derzeit im 4. Semester", "details": "Technischer Lehrplan mit Schwerpunkt auf Netzwerksicherheit, sichere Systemadministration, Schwachstellenanalyse und Incident Response." },
        "edu_transfer": { "institution": "Institution noch festzulegen (Universitätsanerkennung)", "degree": "Bachelor in Cybersicherheitstechnik", "status": "TODO: Zieluniversität und Studienplan stehen noch aus", "details": "Akademischer Fortführungsweg zum Erwerb des staatlich anerkannten Ingenieurabschlusses." },
        "cisco_disclaimer": "Hinweis: Diese Nachweise sind Kurse der Cisco Networking Academy, keine Industrie-Zertifizierungen.",
        "cisco_badges": "Modul-Badges der Cisco Networking Academy (Nov. 2025 & Okt. 2026): System Safeguards, Threat Analysis und Cybersecurity Administration.",
        "ctf_honesty": "Gelöst mit KI-Unterstützung (Claude Code). Reverse Engineering erfolgte ausschließlich über statische Analyse, ohne Ausführung nicht vertrauenswürdiger Binärdateien.",
        "terminal": {
            "reply_whoami": "manuel · cybersicherheit @ SENATI (4. semester)",
            "reply_ls": "shadowbytes/  htb-writeups/  esp32-biometrie/\nindustrie-etikettierung/  intercom/  kunden-webs/  nasa-prototypes/",
            "reply_cat": "aufbrechen → verstehen → bauen → shippen"
        }
    },
    "it": {
        "lang_name": "Italiano",
        "title": "Manuel Vilcazan — Portfolio & CV",
        "desc": "Studente di Ingegneria della Sicurezza Informatica. CTF, laboratori per la community, hardware ESP32 e software in produzione.",
        "identity_title": "Studente di Ingegneria della Sicurezza Informatica",
        "availability": "Disponibile per tirocini e lavoro · In presenza ad Arequipa e da remoto",
        "summary": "Studente di Ingegneria della Sicurezza Informatica (4° semestre, SENATI). Non mi limito a risolvere sfide: costruisco laboratori pratici per la community, hardware a microcontrollore e software attivo in produzione per aziende reali.",
        "nav": { "brand": ">_ mvilcazan", "about": "chi sono", "education": "istruzione", "experience": "esperienza", "projects": "progetti", "competencies": "certificazioni & ctf", "stack": "stack", "contact": "contatti", "download_cv": "Scarica CV (PDF)", "language_selector_aria": "Seleziona lingua" },
        "actions": { "view_projects": "Vedi progetti", "github_btn": "GitHub ↗", "linkedin_btn": "LinkedIn ↗", "download_cv_btn": "Scarica CV (PDF)", "copy_email": "Copia e-mail", "email_copied": "Copiato!", "close_modal": "Chiudi", "view_preview": "Vedi prova", "open_pdf": "Apri PDF ↗", "view_original": "Vedi immagine intera ↗" },
        "filters": { "aria_label": "Filtra progetti", "all": "tutti", "sec": "sicurezza", "hw": "hardware", "sw": "software", "web": "web", "nasa": "nasa apps" },
        "badges": { "in_production": "live", "in_use": "in uso", "featured": "In evidenza · Community", "prototype": "Prototipo · NASA Space Apps 2026", "course": "Corso Cisco Networking Academy", "badge_rank": "Posizione", "todo_tag": "In attesa di conferma" },
        "sections": {
            "about_title": "Chi sono", "about_sub": "Il mio profilo è ibrido: penso come un attaccante, costruisco come uno sviluppatore e assemblo il mio hardware. Amo completare l'intero ciclo, dall'idea fino all'utilizzo reale.",
            "education_title": "Istruzione", "education_sub": "Rigorosa formazione tecnica in sicurezza informatica, unita ad autoapprendimento continuo e percorso di laurea universitario.",
            "experience_title": "Esperienza", "experience_sub": "Pratica applicata in azienda e installazioni reali in produzione, dalla computer vision ai sistemi industriali e allo sviluppo web.",
            "projects_title": "Progetti", "projects_sub": "Sistemi in produzione, strumenti di sicurezza, progetti hardware e prototipi spaziali.",
            "competencies_title": "Certificazioni, CTF e Corsi", "competencies_sub": "Partecipazione attiva a competizioni internazionali di cybersecurity, percorsi formativi e laboratori tecnici.",
            "stack_title": "Stack", "stack_sub": "Strumenti, tecnologie e ambienti che impiego nell'analisi di sicurezza, nello sviluppo e nell'hardware.",
            "contact_title": "Costruiamo qualcosa?", "contact_sub": "Cerco team in cui poter analizzare, riparare e portare soluzioni in produzione. Il modo più rapido per contattarmi è via LinkedIn o per e-mail.",
            "footer_copy": "© 2026 Manuel Vilcazan Mendoza", "ai_translation_notice": "Traduzione assistita da IA"
        },
        "stats": [
            { "label": "sfide HTB documentate con writeup" },
            { "label": "categorie CTF: web, pwn, rev, crypto, forensics, blockchain" },
            { "label": "siti web in produzione" },
            { "label": "prototipi ESP32 costruiti end-to-end" }
        ],
        "pillars": [
            { "title": "Sicurezza Offensiva e Difensiva", "text": "Partecipo a CTF su Hack The Box con il mio team, avanzo nei percorsi di TryHackMe e sviluppo strumenti difensivi personalizzati." },
            { "title": "Software che viene utilizzato", "text": "Siti web attivi per aziende tessili del sud del Perù e un sistema di etichettatura industriale per stabilimenti." },
            { "title": "Hardware e IoT", "text": "Prototipi ESP32: controllo accessi biometrico con custodia modellata e stampata in 3D, e interfoni industriali per reparti." }
        ],
        "edu_senati": { "degree": "Ingegneria della Sicurezza Informatica (Programma Tecnico)", "status": "Attualmente al 4° semestre", "details": "Curriculum tecnico focalizzato su sicurezza delle reti, amministrazione sicura dei sistemi, analisi delle vulnerabilità e gestione degli incidenti." },
        "edu_transfer": { "institution": "Istituto da definire (Riconoscimento Universitario)", "degree": "Laurea in Ingegneria della Sicurezza Informatica", "status": "TODO: Istituto e piano didattico in attesa di conferma formale", "details": "Percorso accademico di continuità per il conseguimento del titolo professionale universitario." },
        "cisco_disclaimer": "Nota: Questi attestati corrispondono a Corsi della Cisco Networking Academy, non a certificazioni professionali.",
        "cisco_badges": "Badge di modulo ottenuti presso Cisco Networking Academy (nov 2025 e ott 2026): System Safeguards, Threat Analysis e Cybersecurity Administration.",
        "ctf_honesty": "Risolti con l'assistenza dell'IA (Claude Code). Il reverse engineering è stato eseguito esclusivamente tramite analisi statica, senza eseguire file binari non affidabili.",
        "terminal": {
            "reply_whoami": "manuel · sicurezza informatica @ SENATI (4° semestre)",
            "reply_ls": "shadowbytes/  htb-writeups/  esp32-biometrico/\netichettatura-industriale/  intercom/  siti-clienti/  nasa-prototypes/",
            "reply_cat": "rompere → comprendere → costruire → rilasciare"
        }
    },
    "zh": {
        "lang_name": "简体中文",
        "title": "Manuel Vilcazan — 个人作品集与简历",
        "desc": "网络安全工程学生。CTF竞赛、社区靶场、ESP32硬件开发与生产环境应用软件。",
        "identity_title": "网络安全工程专业在读学生",
        "availability": "寻找实习与工作机会 · 秘鲁阿雷基帕（现场）与远程均可",
        "summary": "网络安全工程学生（SENATI 第4学期在读）。我不只解决挑战：我为开源社区构建实战靶场，自主研发微控制器硬件，并为实体企业打造运行在生产环境中的软件系统。",
        "nav": { "brand": ">_ mvilcazan", "about": "关于我", "education": "教育经历", "experience": "工作经历", "projects": "项目展示", "competencies": "认证与CTF", "stack": "技术栈", "contact": "联系方式", "download_cv": "下载简历 (PDF)", "language_selector_aria": "选择语言" },
        "actions": { "view_projects": "查看项目", "github_btn": "GitHub ↗", "linkedin_btn": "LinkedIn ↗", "download_cv_btn": "下载简历 (PDF)", "copy_email": "复制邮箱", "email_copied": "已复制！", "close_modal": "关闭", "view_preview": "查看证明", "open_pdf": "打开 PDF ↗", "view_original": "查看原图 ↗" },
        "filters": { "aria_label": "筛选项目", "all": "全部", "sec": "安全", "hw": "硬件", "sw": "软件", "web": "Web", "nasa": "NASA挑战" },
        "badges": { "in_production": "运行中", "in_use": "使用中", "featured": "重点精选 · 社区", "prototype": "原型 · NASA Space Apps 2026", "course": "思科网络学院课程", "badge_rank": "名次", "todo_tag": "待确认" },
        "sections": {
            "about_title": "关于我", "about_sub": "我的技术背景兼具多面性：像攻击者一样思考，像开发者一样构建，亲手组装硬件。我喜欢打通从构思到用户实际使用的完整闭环。",
            "education_title": "教育经历", "education_sub": "扎实系统的网络安全技术教育，辅以持续自主学习与大学学位衔接规划。",
            "experience_title": "实践经历", "experience_sub": "企业真实生产环境实训与落地部署，涵盖计算机视觉、工厂物联网与工业Web系统开发。",
            "projects_title": "项目展示", "projects_sub": "生产级软件系统、网络安全防御工具、嵌入式硬件开发与深空探测原型项目。",
            "competencies_title": "认证、CTF与研修课程", "competencies_sub": "积极参与全球高水平网络安全竞技、系统化进阶训练与前沿安全实验室。",
            "stack_title": "技术栈", "stack_sub": "在安全分析、全栈开发及智能硬件中所使用的工具、语言与平台环境。",
            "contact_title": "探讨合作", "contact_sub": "我渴望加入能够深入排查问题、修复缺陷并高效上线交付的团队。最快捷的联系方式是通过 LinkedIn 或发送电子邮件。",
            "footer_copy": "© 2026 Manuel Vilcazan Mendoza", "ai_translation_notice": "AI辅助翻译"
        },
        "stats": [
            { "label": "附完整解题报告的HTB挑战" },
            { "label": "CTF攻防类别：Web、Pwn、逆向、密码学、取证、区块链" },
            { "label": "个正式上线运营的商业网站" },
            { "label": "款端到端自研的ESP32智能硬件原型" }
        ],
        "pillars": [
            { "title": "攻防兼备的安全视野", "text": "随队征战 Hack The Box CTF 赛事，精进 TryHackMe 实战路径，并自主开发防守型安全工具。" },
            { "title": "落地实用的生产级软件", "text": "为秘鲁南部纺织制造业搭建官方系统，并研发工厂车间工业级一体化贴标追踪系统。" },
            { "title": "硬件物联网与智能制造", "text": "基于 ESP32 的创新硬件：含 3D 建模与打印外壳的生物识别终端，以及车间对讲专用网络。" }
        ],
        "edu_senati": { "degree": "网络安全工程（专业技术培养项目）", "status": "当前第4学期在读", "details": "专注网络攻防架构、安全系统管理、漏洞扫描挖掘与网络安全事件应急响应等核心技能。" },
        "edu_transfer": { "institution": "待定学府（大学学位学分衔接）", "degree": "网络安全工程学士学位课程", "status": "TODO：目标院校及正式课程大纲待官方最终确认", "details": "专升本学术晋升培养路径，以取得国家认证的网络安全工程师专业学士学位。" },
        "cisco_disclaimer": "注：以上项目为思科网络学院（Cisco Networking Academy）结业课程，非行业职业资格认证证书。",
        "cisco_badges": "思科网络学院所获核心模块徽章（2025年11月及2026年10月）：System Safeguards、Threat Analysis 与 Cybersecurity Administration。",
        "ctf_honesty": "题目解析借助 AI（Claude Code）辅助。二进制逆向工程全部基于静态反编译与代码审计，未在宿主机执行任何不受信二进制程序。",
        "terminal": {
            "reply_whoami": "manuel · 网络安全 @ SENATI（第4学期）",
            "reply_ls": "shadowbytes/  htb-writeups/  esp32-biometrico/\netiquetado-industrial/  intercom/  webs-clientes/  nasa-prototypes/",
            "reply_cat": "解构 → 洞察 → 构建 → 交付"
        }
    },
    "ja": {
        "lang_name": "日本語",
        "title": "Manuel Vilcazan — ポートフォリオ・履歴書",
        "desc": "サイバーセキュリティ工学の学生。CTF、コミュニティラボ、ESP32ハードウェア、本番環境ソフトウェア開発。",
        "identity_title": "サイバーセキュリティ工学 専攻学生",
        "availability": "インターン・就職希望 · ペルー・アレキパ（対面）およびリモート勤務可能",
        "summary": "サイバーセキュリティ工学の学生（SENATI 4学期在学中）。問題を解くだけにとどまらず、コミュニティ向け実践ラボ、マイコンハードウェア、実企業で稼働する本番ソフトウェアを構築しています。",
        "nav": { "brand": ">_ mvilcazan", "about": "自己紹介", "education": "学歴", "experience": "実務経験", "projects": "プロジェクト", "competencies": "認定資格・CTF", "stack": "技術スタック", "contact": "連絡先", "download_cv": "履歴書をダウンロード (PDF)", "language_selector_aria": "言語を選択" },
        "actions": { "view_projects": "プロジェクトを見る", "github_btn": "GitHub ↗", "linkedin_btn": "LinkedIn ↗", "download_cv_btn": "履歴書をダウンロード (PDF)", "copy_email": "メールをコピー", "email_copied": "コピー完了！", "close_modal": "閉じる", "view_preview": "証明書を見る", "open_pdf": "PDFを開く ↗", "view_original": "原寸画像を表示 ↗" },
        "filters": { "aria_label": "プロジェクトを絞り込む", "all": "すべて", "sec": "セキュリティ", "hw": "ハードウェア", "sw": "ソフトウェア", "web": "Web", "nasa": "NASA Apps" },
        "badges": { "in_production": "稼働中", "in_use": "運用中", "featured": "注目 · コミュニティ", "prototype": "プロトタイプ · NASA Space Apps 2026", "course": "シスコ・ネットワーキング・アカデミー修了コース", "badge_rank": "順位", "todo_tag": "確認待ち" },
        "sections": {
            "about_title": "自己紹介", "about_sub": "攻撃者の視点で考え、開発者として構築し、自らハードウェアを組み立てるハイブリッドな技術基盤を持ち、着想から実際の運用まで完遂します。",
            "education_title": "学歴・教育", "education_sub": "サイバーセキュリティに関する厳格な専門技術教育に加え、継続的な独学と大学編入による学位取得を目指しています。",
            "experience_title": "実務経験", "experience_sub": "画像認識・AI監視から工場内システム、Web開発まで、実企業における本番導入実績。",
            "projects_title": "プロジェクト", "projects_sub": "本番稼働システム、セキュリティツール、独自ハードウェア開発、宇宙ミッションシミュレータ。",
            "competencies_title": "認定・CTF・受講コース", "competencies_sub": "国際的なサイバーセキュリティ競技会、体系的トレーニングパス、技術ラボへの積極的な挑戦実績。",
            "stack_title": "技術スタック", "stack_sub": "セキュリティ分析、開発、ハードウェア製作で日常的に活用しているツールおよび開発環境。",
            "contact_title": "共同開発・お問い合わせ", "contact_sub": "課題を発見・解決し、本番環境へと素早く届けるチームへの参画を希望しています。LinkedInまたはメールにてお気軽にご連絡ください。",
            "footer_copy": "© 2026 Manuel Vilcazan Mendoza", "ai_translation_notice": "AI支援による翻訳"
        },
        "stats": [
            { "label": "詳細解説付きHTBチャレンジ" },
            { "label": "CTFカテゴリ：Web、Pwn、リバース、暗号、フォレンジック、ブロックチェーン" },
            { "label": "件の本番運用中Webサイト" },
            { "label": "件のフルスクラッチESP32試作機" }
        ],
        "pillars": [
            { "title": "攻防両面のアプローチ", "text": "チームで Hack The Box CTF に参戦し、TryHackMe でスキルを磨き、独自の防御ツールを構築。" },
            { "title": "実社会で使われるソフトウェア", "text": "ペルー南部の繊維企業向け本番サイトや、工場向け工業用バーコード・ラベル発行管理システム。" },
            { "title": "ハードウェア & IoT", "text": "ESP32プロトタイプ：3D設計・出力筐体付き生体認証端末や、工場間通話インターホン網。" }
        ],
        "edu_senati": { "degree": "サイバーセキュリティ工学（専門技術課程）", "status": "第4セメスター在学中", "details": "ネットワークセキュリティ、安全なシステム管理、脆弱性評価、インシデントレスポンスに特化した技術教育。" },
        "edu_transfer": { "institution": "大学機関未定（大学編入プログラム）", "degree": "サイバーセキュリティ工学 学士課程編入", "status": "TODO: 対象大学および公式カリキュラムは確定待ち", "details": "正規の工学学士号取得に向けた学術継続パスウェイ。" },
        "cisco_disclaimer": "注：上記は Cisco Networking Academy の修了コースであり、ベンダー認定プロ資格ではありません。",
        "cisco_badges": "Cisco Networking Academy で獲得したモジュールバッジ（2025年11月・2026年10月）：System Safeguards、Threat Analysis、Cybersecurity Administration。",
        "ctf_honesty": "AI（Claude Code）の支援を受けて解法を導出。バイナリのリバースエンジニアリングは静的解析のみで実施し、信頼できない実行可能ファイルは一切起動していません。",
        "terminal": {
            "reply_whoami": "manuel · サイバーセキュリティ @ SENATI（4学期）",
            "reply_ls": "shadowbytes/  htb-writeups/  esp32-biometrico/\netiquetado-industrial/  intercom/  webs-clientes/  nasa-prototypes/",
            "reply_cat": "解体 → 理解 → 構築 → 出荷"
        }
    },
    "ko": {
        "lang_name": "한국어",
        "title": "Manuel Vilcazan — 포트폴리오 및 이력서",
        "desc": "사이버 보안 공학 전공 학생. CTF 대회, 커뮤니티 실습 랩, ESP32 임베디드 하드웨어 및 상용 소프트웨어 개발.",
        "identity_title": "사이버 보안 공학 전공 학생",
        "availability": "인턴십 및 채용 희망 · 페루 아레키파(대면) 및 원격 근무 가능",
        "summary": "사이버 보안 공학 전공 학생 (SENATI 4학기 재학 중). 단순한 문제 해결을 넘어 커뮤니티를 위한 실습 랩, 마이크로컨트롤러 하드웨어, 실제 기업의 프로덕션 환경에서 작동하는 소프트웨어를 직접 제작합니다.",
        "nav": { "brand": ">_ mvilcazan", "about": "소개", "education": "학력", "experience": "경력", "projects": "프로젝트", "competencies": "자격 및 CTF", "stack": "기술 스택", "contact": "연락처", "download_cv": "이력서 다운로드 (PDF)", "language_selector_aria": "언어 선택" },
        "actions": { "view_projects": "프로젝트 보기", "github_btn": "GitHub ↗", "linkedin_btn": "LinkedIn ↗", "download_cv_btn": "이력서 다운로드 (PDF)", "copy_email": "이메일 복사", "email_copied": "복사됨!", "close_modal": "닫기", "view_preview": "증빙자료 보기", "open_pdf": "PDF 열기 ↗", "view_original": "원본 이미지 보기 ↗" },
        "filters": { "aria_label": "프로젝트 필터", "all": "전체", "sec": "보안", "hw": "하드웨어", "sw": "소프트웨어", "web": "웹", "nasa": "NASA 앱" },
        "badges": { "in_production": "운영 중", "in_use": "실사용 중", "featured": "주목 · 커뮤니티", "prototype": "프로토타입 · NASA Space Apps 2026", "course": "시스코 네트워킹 아카데미 수료 과정", "badge_rank": "순위", "todo_tag": "확인 대기 중" },
        "sections": {
            "about_title": "소개", "about_sub": "공격자처럼 사고하고, 개발자처럼 구축하며, 하드웨어를 직접 조립하는 하이브리드 프로필을 바탕으로 아이디어에서 실제 사용자 배포까지 완결합니다.",
            "education_title": "학력", "education_sub": "사이버 보안 전문 기술 교육과 지속적인 자기주도 학습, 향후 대학 학위 연계 경로.",
            "experience_title": "경력", "experience_sub": "컴퓨터 비전 모니터링부터 공장 생산 현장 시스템 및 웹 개발에 이르는 기업 실무와 프로덕션 배포 경험.",
            "projects_title": "프로젝트", "projects_sub": "운영 중인 소프트웨어, 보안 도구, 하드웨어 개발물 및 우주 미션 시뮬레이터.",
            "competencies_title": "자격, CTF 및 수료 과정", "competencies_sub": "국제 사이버 보안 대회 참가, 체계적인 학습 트랙 및 기술 실습 랩 수행 내역.",
            "stack_title": "기술 스택", "stack_sub": "보안 분석, 소프트웨어 개발 및 하드웨어 제작에 사용하는 도구 및 환경.",
            "contact_title": "함께 프로젝트를 진행해 볼까요?", "contact_sub": "문제를 분석하고 해결하여 프로덕션에 성공적으로 배포할 수 있는 팀을 찾고 있습니다. LinkedIn 또는 이메일로 연락 부탁드립니다.",
            "footer_copy": "© 2026 Manuel Vilcazan Mendoza", "ai_translation_notice": "AI 번역 지원"
        },
        "stats": [
            { "label": "개 상세 풀이가 작성된 HTB 챌린지" },
            { "label": "개 CTF 분야: Web, Pwn, Rev, Crypto, Forensics, Blockchain" },
            { "label": "개 프로덕션 운영 웹사이트" },
            { "label": "개 엔드투엔드 자체 제작 ESP32 프로토타입" }
        ],
        "pillars": [
            { "title": "공격 및 방어 보안", "text": "팀과 함께 Hack The Box CTF 대회에 출전하고, TryHackMe 학습 트랙을 진행하며, 자체 방어 툴을 제작합니다." },
            { "title": "현장에서 쓰이는 소프트웨어", "text": "페루 남부 섬유 기업을 위한 운영 웹사이트와 제조 공장용 산업 라벨 및 바코드 관리 시스템." },
            { "title": "하드웨어 및 IoT", "text": "ESP32 프로토타입: 3D 모델링 및 출력 케이스가 적용된 생체인식 단말기와 공장 통신용 인터콤망." }
        ],
        "edu_senati": { "degree": "사이버 보안 공학 (전문 기술 과정)", "status": "현재 4학기 재학 중", "details": "네트워크 보안, 안전한 시스템 관리, 취약점 분석 및 침해 사고 대응에 집중된 전문 기술 커리큘럼." },
        "edu_transfer": { "institution": "기관 미정 (학점 인정 및 학사 편입)", "degree": "사이버 보안 공학 학사 편입 과정", "status": "TODO: 편입 대학 및 세부 커리큘럼 공식 확인 예정", "details": "공인 사이버 보안 공학 전문 학사 학위 취득을 위한 학업 연계 계획." },
        "cisco_disclaimer": "알림: 위 항목은 Cisco Networking Academy 수료 과정이며, 벤더 공인 자격증이 아닙니다.",
        "cisco_badges": "Cisco Networking Academy 취득 모듈 배지 (2025년 11월 및 2026년 10월): System Safeguards, Threat Analysis, Cybersecurity Administration.",
        "ctf_honesty": "AI(Claude Code)의 보조를 받아 해결함. 바이너리 리버싱은 비신뢰 바이너리 실행 없이 순수 정적 분석으로만 수행되었습니다.",
        "terminal": {
            "reply_whoami": "manuel · 사이버보안 @ SENATI (4학기)",
            "reply_ls": "shadowbytes/  htb-writeups/  esp32-biometrico/\netiquetado-industrial/  intercom/  webs-clientes/  nasa-prototypes/",
            "reply_cat": "분해 → 이해 → 제작 → 배포"
        }
    },
    "ru": {
        "lang_name": "Русский",
        "title": "Мануэль Вилькасан — Портфолио и Резюме",
        "desc": "Студент факультета кибербезопасности. CTF, практические лаборатории, аппаратные решения на ESP32 и боевое ПО.",
        "identity_title": "Студент факультета кибербезопасности",
        "availability": "Ищу стажировку или работу · Очно в Арекипе и удаленно",
        "summary": "Студент факультета кибербезопасности (4-й семестр, SENATI). Я не просто решаю задачи: я создаю практические лаборатории для сообщества, аппаратные устройства на микроконтроллерах и ПО, работающее в продакшене реальных предприятий.",
        "nav": { "brand": ">_ mvilcazan", "about": "обо мне", "education": "образование", "experience": "опыт", "projects": "проекты", "competencies": "сертификаты & ctf", "stack": "стек", "contact": "контакты", "download_cv": "Скачать резюме (PDF)", "language_selector_aria": "Выбрать язык" },
        "actions": { "view_projects": "Смотреть проекты", "github_btn": "GitHub ↗", "linkedin_btn": "LinkedIn ↗", "download_cv_btn": "Скачать резюме (PDF)", "copy_email": "Скопировать email", "email_copied": "Скопировано!", "close_modal": "Закрыть", "view_preview": "Посмотреть подтверждение", "open_pdf": "Открыть PDF ↗", "view_original": "Открыть оригинал ↗" },
        "filters": { "aria_label": "Фильтр проектов", "all": "все", "sec": "безопасность", "hw": "аппаратное", "sw": "софт", "web": "веб", "nasa": "nasa apps" },
        "badges": { "in_production": "в работе", "in_use": "эксплуатируется", "featured": "Главное · Сообщество", "prototype": "Прототип · NASA Space Apps 2026", "course": "Курс Cisco Networking Academy", "badge_rank": "Место", "todo_tag": "Ожидает подтверждения" },
        "sections": {
            "about_title": "Обо мне", "about_sub": "У меня гибридный профиль: мыслю как атакующий, разрабатываю как программист и самостоятельно собираю аппаратное обеспечение. Предпочитаю вести проект от идеи до реальной эксплуатации.",
            "education_title": "Образование", "education_sub": "Фундаментальная техническая подготовка в сфере кибербезопасности, непрерывное самообразование и траектория получения университетской степени.",
            "experience_title": "Опыт работы", "experience_sub": "Практика в реальных компаниях и внедрение систем в продакшен: от компьютерного зрения до заводской автоматизации и веб-сервисов.",
            "projects_title": "Проекты", "projects_sub": "Системы в эксплуатации, инструменты безопасности, микроэлектроника и прототипы космических миссий.",
            "competencies_title": "Сертификаты, CTF и Курсы", "competencies_sub": "Активное участие в международных CTF-соревнованиях по безопасности, профильные учебные треки и технические лаборатории.",
            "stack_title": "Стек технологий", "stack_sub": "Инструменты, технологии и окружение, которые я использую в анализе защищенности, разработке и электронике.",
            "contact_title": "Давайте сотрудничать", "contact_sub": "Ищу команду, где смогу исследовать системы, устранять уязвимости и доводить решения до продакшена. Связаться со мной проще всего через LinkedIn или по email.",
            "footer_copy": "© 2026 Мануэль Вилькасан Мендоса", "ai_translation_notice": "Перевод выполнен с помощью ИИ"
        },
        "stats": [
            { "label": "решенных тасок HTB с подробными райтапами" },
            { "label": "категорий CTF: web, pwn, rev, crypto, forensics, blockchain" },
            { "label": "сайта в промышленной эксплуатации" },
            { "label": "завершенных сквозных прототипа на базе ESP32" }
        ],
        "pillars": [
            { "title": "Наступательная и оборонительная безопасность", "text": "Участвую в турнирах Hack The Box CTF в составе команды, прохожу треки TryHackMe и создаю собственные защитные утилиты." },
            { "title": "Практическое программное обеспечение", "text": "Действующие сайты для текстильных фабрик юга Перу и промышленная система маркировки для производственных цехов." },
            { "title": "Аппаратные платформы и IoT", "text": "Прототипы на ESP32: биометрический контроль доступа в смоделированном и напечатанном на 3D-принтере корпусе, и цеховой интерком." }
        ],
        "edu_senati": { "degree": "Инженерия кибербезопасности (Техническая программа)", "status": "В настоящее время на 4-м семестре", "details": "Специализированная программа: сетевая безопасность, безопасное администрирование систем, анализ уязвимостей и реагирование на инциденты." },
        "edu_transfer": { "institution": "Вуз уточняется (Университетский перевод)", "degree": "Бакалавриат по специальности «Инженерия кибербезопасности»", "status": "TODO: Выбранный университет и учебный план на согласовании", "details": "Траектория академического продолжения обучения для получения диплома государственного инженера." },
        "cisco_disclaimer": "Примечание: Данные документы подтверждают прохождение курсов Cisco Networking Academy, а не сдачу промышленных сертификаций.",
        "cisco_badges": "Модульные бейджи Cisco Networking Academy (ноябрь 2025 и октябрь 2026): System Safeguards, Threat Analysis и Cybersecurity Administration.",
        "ctf_honesty": "Задачи решены при консультации ИИ (Claude Code). Реверс-инжиниринг бинарных файлов производился исключительно статическим анализом, без запуска недоверенного кода.",
        "terminal": {
            "reply_whoami": "мануэль · кибербезопасность @ SENATI (4-й семестр)",
            "reply_ls": "shadowbytes/  htb-writeups/  esp32-biometrico/\netiquetado-industrial/  intercom/  webs-clientes/  nasa-prototypes/",
            "reply_cat": "разобрать → понять → построить → задеплоить"
        }
    }
}

for code, tr in translations.items():
    lang_obj = make_lang_data(code)
    
    # Meta
    lang_obj["meta"]["title"] = tr["title"]
    lang_obj["meta"]["description"] = tr["desc"]
    lang_obj["meta"]["og_title"] = tr["title"]
    lang_obj["meta"]["og_description"] = tr["desc"]
    
    # Identity
    lang_obj["identity"]["title"] = tr["identity_title"]
    lang_obj["identity"]["availability"] = tr["availability"]
    lang_obj["identity"]["summary"] = tr["summary"]
    
    # Stats
    for idx, st in enumerate(tr["stats"]):
        lang_obj["identity"]["stats"][idx]["label"] = st["label"]
        
    # UI
    lang_obj["ui"]["nav"] = tr["nav"]
    lang_obj["ui"]["actions"] = tr["actions"]
    lang_obj["ui"]["filters"] = tr["filters"]
    lang_obj["ui"]["badges"] = tr["badges"]
    for k, v in tr["sections"].items():
        lang_obj["ui"]["sections"][k] = v
        
    # Pillars
    for idx, pil in enumerate(tr["pillars"]):
        lang_obj["about_pillars"][idx]["title"] = pil["title"]
        lang_obj["about_pillars"][idx]["text"] = pil["text"]
        
    # Education
    lang_obj["education"][0]["degree"] = tr["edu_senati"]["degree"]
    lang_obj["education"][0]["status"] = tr["edu_senati"]["status"]
    lang_obj["education"][0]["details"] = tr["edu_senati"]["details"]
    
    lang_obj["education"][1]["institution"] = tr["edu_transfer"]["institution"]
    lang_obj["education"][1]["degree"] = tr["edu_transfer"]["degree"]
    lang_obj["education"][1]["status"] = tr["edu_transfer"]["status"]
    lang_obj["education"][1]["details"] = tr["edu_transfer"]["details"]
    
    # Cisco
    lang_obj["competencies"]["cisco_courses"]["disclaimer"] = tr["cisco_disclaimer"]
    lang_obj["competencies"]["cisco_courses"]["badges_summary"] = tr["cisco_badges"]
    
    # CTF Honesty
    lang_obj["competencies"]["ctf_writeups"]["honesty_note"] = tr["ctf_honesty"]
    
    # Terminal
    lang_obj["terminal"]["whoami_reply"] = tr["terminal"]["reply_whoami"]
    lang_obj["terminal"]["ls_reply"] = tr["terminal"]["reply_ls"]
    lang_obj["terminal"]["cat_reply"] = tr["terminal"]["reply_cat"]
    
    out_file = os.path.join(base_dir, f"{code}.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(lang_obj, f, indent=2, ensure_ascii=False)
    print(f"Generated {code}.json")

print("All translations generated successfully.")
