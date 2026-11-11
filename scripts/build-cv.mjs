import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');
const cvDir = path.resolve(rootDir, 'cv');
const i18nDir = path.resolve(rootDir, 'i18n');

if (!fs.existsSync(cvDir)) {
  fs.mkdirSync(cvDir, { recursive: true });
}

// Read config
const config = JSON.parse(fs.readFileSync(path.join(i18nDir, 'config.json'), 'utf-8'));
const allLangs = config.languages.map(l => l.code);

// Parse CLI args: node scripts/build-cv.mjs [--lang=es]
let targetLangs = allLangs;
for (const arg of process.argv.slice(2)) {
  if (arg.startsWith('--lang=')) {
    const val = arg.split('=')[1].trim();
    if (val && val !== 'all') {
      targetLangs = [val];
    }
  }
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function renderCvHtml(lang, data) {
  const email = `${data.identity.email_user}@${data.identity.email_domain}`;
  const template = fs.readFileSync(path.join(rootDir, 'cv-template.html'), 'utf-8');

  // Labels by lang
  const sectionLabels = {
    es: { profile: "Perfil Profesional", edu: "Educación", exp: "Experiencia Laboral", proj: "Proyectos Destacados", ctf: "CTF y Competencias de Ciberseguridad", cisco: "Cursos — Cisco Networking Academy", skills: "Habilidades Técnicas", langs: "Idiomas" },
    en: { profile: "Professional Summary", edu: "Education", exp: "Work Experience", proj: "Key Projects", ctf: "CTFs & Cybersecurity Competitions", cisco: "Courses — Cisco Networking Academy", skills: "Technical Skills", langs: "Languages" },
    pt: { profile: "Resumo Profissional", edu: "Educação", exp: "Experiência Profissional", proj: "Projetos em Destaque", ctf: "CTFs e Competições de Cibersegurança", cisco: "Cursos — Cisco Networking Academy", skills: "Habilidades Técnicas", langs: "Idiomas" },
    fr: { profile: "Profil Professionnel", edu: "Formation", exp: "Expérience Professionnelle", proj: "Projets Notables", ctf: "CTFs & Compétitions de Cybersécurité", cisco: "Cours — Cisco Networking Academy", skills: "Compétences Techniques", langs: "Langues" },
    de: { profile: "Kurzprofil", edu: "Ausbildung", exp: "Berufserfahrung", proj: "Ausgewählte Projekte", ctf: "CTF & Cybersicherheits-Wettbewerbe", cisco: "Kurse — Cisco Networking Academy", skills: "Fachliche Kompetenzen", langs: "Sprachen" },
    it: { profile: "Profilo Professionale", edu: "Istruzione", exp: "Esperienza Lavorativa", proj: "Progetti in Evidenza", ctf: "CTF & Competizioni di Cybersecurity", cisco: "Corsi — Cisco Networking Academy", skills: "Competenze Tecniche", langs: "Lingue" },
    zh: { profile: "个人简介", edu: "教育背景", exp: "项目与工作经历", proj: "重点技术项目", ctf: "CTF竞赛与网络安全竞技", cisco: "研修课程 — 思科网络学院", skills: "专业技术栈", langs: "语言能力" },
    ja: { profile: "概要・プロフィール", edu: "学歴", exp: "実務経験・職歴", proj: "主要プロジェクト", ctf: "CTF・サイバーセキュリティ競技会", cisco: "修了コース — Cisco Networking Academy", skills: "技術スキル", langs: "言語" },
    ko: { profile: "소개 및 요약", edu: "학력", exp: "실무 및 프로젝트 경험", proj: "주요 프로젝트", ctf: "CTF 및 사이버 보안 대회", cisco: "수료 과정 — Cisco Networking Academy", skills: "기술 역량", langs: "언어" },
    ru: { profile: "О себе", edu: "Образование", exp: "Опыт работы", proj: "Ключевые проекты", ctf: "CTF и соревнования по кибербезопасности", cisco: "Курсы — Cisco Networking Academy", skills: "Технические навыки", langs: "Языки" }
  };

  const lbl = sectionLabels[lang] || sectionLabels.es;

  // Selected featured projects for CV
  const featuredProjects = data.projects.filter(p =>
    ['shadowbytes', 'firecal-global', 'base-sandbox', 'htb-resolution', 'its-4-s3cr3-t', 'esp32-biometrico'].includes(p.id)
  );

  const content = `
    <header>
      <div class="header-top">
        <h1>${escapeHtml(data.identity.name)}</h1>
        <div style="font-size: 8pt; color: #64748b; font-weight: 500;">${escapeHtml(data.identity.location)}</div>
      </div>
      <div class="cv-title">${escapeHtml(data.identity.title)}</div>
      <div class="contact-line">
        <span>📧 <a href="mailto:${email}">${email}</a></span>
        <span>🔗 <a href="${data.identity.links.linkedin}" target="_blank">LinkedIn</a></span>
        <span>💻 <a href="${data.identity.links.github}" target="_blank">GitHub</a></span>
        <span>🛡️ <a href="${data.identity.links.tryhackme}" target="_blank">TryHackMe</a></span>
        <span>🚩 <a href="${data.identity.links.hackthebox}" target="_blank">Hack The Box</a></span>
        <span style="color: #0d9488;">· ${escapeHtml(data.identity.availability)}</span>
      </div>
    </header>

    <section>
      <h2>${lbl.profile}</h2>
      <p class="summary-text">${escapeHtml(data.identity.summary)}</p>
    </section>

    <section>
      <h2>${lbl.edu}</h2>
      ${data.education.map(ed => `
        <div class="item">
          <div class="item-header">
            <span>${escapeHtml(ed.institution)}</span>
            <span class="item-period">${escapeHtml(ed.period)}</span>
          </div>
          <div class="item-sub">
            <span>${escapeHtml(ed.degree)}</span>
            <span style="font-weight: 400; color: #475569;">${escapeHtml(ed.status)}</span>
          </div>
          ${ed.details ? `<p style="font-size: 7.8pt; color: #475569; margin: 1px 0 2px;">${escapeHtml(ed.details)}</p>` : ''}
        </div>
      `).join('')}
    </section>

    <section>
      <h2>${lbl.exp}</h2>
      ${data.experience.map(exp => `
        <div class="item">
          <div class="item-header">
            <span>${escapeHtml(exp.role)} · <strong>${escapeHtml(exp.company)}</strong></span>
            <span class="item-period">${escapeHtml(exp.period)}</span>
          </div>
          <ul class="bullets">
            ${exp.bullets.map(b => `<li>${escapeHtml(b)}</li>`).join('')}
          </ul>
        </div>
      `).join('')}
    </section>

    <section>
      <h2>${lbl.proj}</h2>
      <div class="two-col">
        ${featuredProjects.map(p => `
          <div class="item" style="margin-bottom: 4px;">
            <div class="item-header" style="font-size: 8.5pt;">
              <span>${escapeHtml(p.title)}</span>
              <span class="tag-badge">${escapeHtml(p.kind)}</span>
            </div>
            <p style="font-size: 7.8pt; color: #334155; margin: 1px 0 2px;">${escapeHtml(p.description)}</p>
            <div>
              ${(p.tags || []).slice(0, 4).map(t => `<span class="tech-pill">${escapeHtml(t)}</span>`).join('')}
            </div>
          </div>
        `).join('')}
      </div>
    </section>

    <section>
      <h2>${lbl.ctf}</h2>
      <ul class="ctf-list">
        ${data.competencies.ctf_competitions.map(c => `
          <li>
            <strong>${escapeHtml(c.name)}</strong>: ${escapeHtml(c.official_event)} — 
            <span class="tag-badge">${escapeHtml(c.badge)}</span>
            <span style="color: #64748b;">(${escapeHtml(c.date)})</span>.
            ${escapeHtml(c.description)}
          </li>
        `).join('')}
        <li style="margin-top: 3px;">
          <strong>${escapeHtml(data.competencies.platforms.portswigger.title)}</strong>:
          <span style="color: #047857; font-weight: 600;">${escapeHtml(data.competencies.platforms.portswigger.stat)}</span>.
          ${escapeHtml(data.competencies.platforms.portswigger.topics)}
          <em>${escapeHtml(data.competencies.platforms.portswigger.tools)}</em>
        </li>
      </ul>
      <div class="note-box">${escapeHtml(data.competencies.ctf_writeups.honesty_note)}</div>
    </section>

    <section>
      <h2>${lbl.cisco}</h2>
      <div style="font-size: 7.5pt; color: #475569; margin-bottom: 3px; font-weight: 500;">
        ${escapeHtml(data.competencies.cisco_courses.disclaimer)}
      </div>
      <div class="two-col">
        <ul class="cisco-list">
          ${data.competencies.cisco_courses.items.slice(0, 4).map(it => `
            <li>• ${escapeHtml(it.title)} <span style="color: #64748b;">(${escapeHtml(it.date)})</span></li>
          `).join('')}
        </ul>
        <ul class="cisco-list">
          ${data.competencies.cisco_courses.items.slice(4).map(it => `
            <li>• ${escapeHtml(it.title)} <span style="color: #64748b;">(${escapeHtml(it.date)})</span></li>
          `).join('')}
        </ul>
      </div>
      <div class="note-box" style="margin-top: 3px;">
        ${escapeHtml(data.competencies.cisco_courses.badges_summary)}
      </div>
    </section>

    <section>
      <h2>${lbl.skills} & ${lbl.langs}</h2>
      <div class="skills-block">
        ${data.stack.map(st => `
          <div style="margin-bottom: 2px;">
            <strong>${escapeHtml(st.category)}:</strong>
            ${st.tags.map(t => `<span class="tech-pill">${escapeHtml(t)}</span>`).join('')}
          </div>
        `).join('')}
        <div style="margin-top: 3px;">
          <strong>${lbl.langs}:</strong>
          ${data.identity.languages.map(l => `${escapeHtml(l.name)} (${escapeHtml(l.level)})`).join(' · ')}
        </div>
      </div>
    </section>
  `;

  return template
    .replace('<html lang="es">', `<html lang="${lang}">`)
    .replace('<div class="cv-container" id="cv-root">', `<div class="cv-container" id="cv-root">${content}`);
}

async function buildCvForLang(lang) {
  const langFile = path.join(i18nDir, `${lang}.json`);
  if (!fs.existsSync(langFile)) {
    console.error(`Language file not found: ${langFile}`);
    return;
  }
  const data = JSON.parse(fs.readFileSync(langFile, 'utf-8'));
  const renderedHtml = renderCvHtml(lang, data);
  const tempHtmlPath = path.join(cvDir, `temp-${lang}.html`);
  const outPdfPath = path.join(cvDir, `Manuel-Vilcazan-CV-${lang}.pdf`);

  fs.writeFileSync(tempHtmlPath, renderedHtml, 'utf-8');

  // Method 1: Playwright (if installed)
  let generated = false;
  try {
    const { chromium } = await import('playwright');
    // Try msedge or chrome channel
    const browser = await chromium.launch({
      channel: 'msedge',
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
    }).catch(() => chromium.launch({
      channel: 'chrome',
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
    })).catch(() => chromium.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
    }));

    const page = await browser.newPage();
    await page.goto(`file://${tempHtmlPath}`, { waitUntil: 'networkidle' });
    await page.pdf({
      path: outPdfPath,
      format: 'A4',
      printBackground: true,
      margin: { top: '10mm', right: '12mm', bottom: '10mm', left: '12mm' }
    });
    await browser.close();
    generated = true;
    console.log(`[Playwright] Generated: cv/Manuel-Vilcazan-CV-${lang}.pdf`);
  } catch (err) {
    // Playwright failed or not installed, fallback to native msedge binary
  }

  // Method 2: Fallback to Windows Microsoft Edge binary via WSL
  if (!generated) {
    const edgePaths = [
      '/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
      '/mnt/c/Program Files/Microsoft/Edge/Application/msedge.exe',
      '/mnt/c/Program Files/Google/Chrome/Application/chrome.exe'
    ];
    let edgeBinary = edgePaths.find(p => fs.existsSync(p));

    if (edgeBinary) {
      // In WSL, convert Linux paths to Windows format for edge.exe
      let winHtml = tempHtmlPath;
      let winPdf = outPdfPath;
      try {
        winHtml = execFileSync('wslpath', ['-w', tempHtmlPath]).toString().trim();
        winPdf = execFileSync('wslpath', ['-w', outPdfPath]).toString().trim();
      } catch (e) {
        // keep as is
      }

      execFileSync(edgeBinary, [
        '--headless',
        '--disable-gpu',
        '--no-pdf-header-footer',
        `--print-to-pdf=${winPdf}`,
        winHtml
      ], { stdio: 'pipe' });

      console.log(`[Edge Headless] Generated: cv/Manuel-Vilcazan-CV-${lang}.pdf`);
      generated = true;
    } else {
      console.error(`Could not generate PDF for ${lang}: No browser found.`);
    }
  }

  // Clean up temp html
  if (fs.existsSync(tempHtmlPath)) {
    fs.unlinkSync(tempHtmlPath);
  }
}

async function main() {
  console.log(`Building CV for languages: ${targetLangs.join(', ')}`);
  for (const lang of targetLangs) {
    await buildCvForLang(lang);
  }
  console.log('All CV generation complete.');
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
