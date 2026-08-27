#!/usr/bin/env python3
"""
Builds Ankur Chandrakar's product portfolio page as a single static HTML file,
using the copy pulled from Notion_Page_Content.md (Home / Resume / Case Studies Gallery).

Run:  python3 build_portfolio.py
Output: ./dist/index.html
"""

import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "index.html")

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ankur Chandrakar — Product Portfolio</title>
<meta name="description" content="Ankur Chandrakar — QA Lead transitioning to Product Management. Case studies in retention strategy, growth prioritization, PRD authorship and market sizing.">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

<style>
  :root{
    --bg-deep:#050B18;
    --bg-mid:#0A1B37;
    --bg-blue:#123B6E;
    --panel:#0D2244;
    --panel-line:rgba(148,180,224,0.16);
    --accent:#4FD6FF;
    --accent-dim:#2E7DA8;
    --amber:#FFB347;
    --icon-envelope:#123B6E;
    --text-primary:#F4F8FD;
    --text-secondary:#AFC3E3;
    --text-muted:#7C93BD;
    --mono:'JetBrains Mono', ui-monospace, monospace;
    --display:'Space Grotesk', sans-serif;
    --body:'Inter', sans-serif;
    --maxw:1120px;
  }

  *{ box-sizing:border-box; }
  html{ scroll-behavior:smooth; }
  ::selection{ background:var(--accent); color:var(--bg-deep); }

  body{
    margin:0;
    font-family:var(--body);
    color:var(--text-primary);
    background:
      radial-gradient(1100px 620px at 82% -8%, rgba(79,214,255,0.12), transparent 60%),
      linear-gradient(150deg, var(--bg-blue) 0%, var(--bg-mid) 42%, var(--bg-deep) 100%);
    background-attachment:fixed;
    line-height:1.6;
    -webkit-font-smoothing:antialiased;
  }

  a{ color:inherit; }
  img{ max-width:100%; display:block; }

  .wrap{ max-width:var(--maxw); margin:0 auto; padding:0 28px; }

  /* Focus visibility */
  a:focus-visible, button:focus-visible{
    outline:2px solid var(--accent);
    outline-offset:3px;
    border-radius:4px;
  }

  @media (prefers-reduced-motion: reduce){
    *{ animation-duration:0.001ms !important; animation-iteration-count:1 !important; transition-duration:0.001ms !important; scroll-behavior:auto !important; }
  }

  /* ---------- NAV ---------- */
  header.nav{
    position:sticky; top:0; z-index:50;
    backdrop-filter:blur(14px);
    background:rgba(5,11,24,0.72);
    border-bottom:1px solid var(--panel-line);
  }
  .nav-inner{
    display:flex; align-items:center; justify-content:space-between;
    padding:16px 28px; max-width:var(--maxw); margin:0 auto;
  }
  .logo{
    font-family:var(--mono); font-size:14px; letter-spacing:0.14em;
    color:var(--accent); text-decoration:none; font-weight:600;
    border:1px solid var(--accent-dim); padding:6px 10px; border-radius:6px;
  }
  .nav-links{ display:flex; gap:28px; list-style:none; margin:0; padding:0; }
  .nav-links a{
    text-decoration:none; color:var(--text-secondary); font-size:14px; font-weight:500;
    transition:color .2s ease;
  }
  .nav-links a:hover{ color:var(--accent); }
  .nav-toggle{ display:none; }

  @media (max-width:720px){
    .nav-links{ display:none; }
  }

  /* ---------- HERO ---------- */
  .hero{ padding:96px 0 64px; position:relative; }
  .eyebrow{
    font-family:var(--mono); font-size:12.5px; letter-spacing:0.16em; text-transform:uppercase;
    color:var(--amber); display:flex; align-items:center; gap:10px; margin-bottom:22px;
  }
  .eyebrow::before{
    content:''; width:7px; height:7px; background:var(--amber); border-radius:50%;
    box-shadow:0 0 0 4px rgba(255,179,71,0.18);
  }
  h1.name{
    font-family:var(--display); font-weight:700;
    font-size:clamp(2.6rem, 6vw, 4.4rem);
    line-height:1.02; margin:0 0 14px; letter-spacing:-0.01em;
  }
  .subtitle{
    font-family:var(--display); font-weight:500;
    font-size:clamp(1.1rem, 2.4vw, 1.5rem);
    color:var(--accent); margin:0 0 34px;
  }

  .positioning{
    max-width:780px; border-left:2px solid var(--accent-dim);
    padding:4px 0 4px 24px; margin-bottom:46px;
  }
  .positioning p{ margin:0 0 16px; color:var(--text-secondary); font-size:1.05rem; }
  .positioning p:last-child{ margin-bottom:0; }
  .positioning strong{ color:var(--text-primary); font-weight:600; }

  .quicklinks{ display:flex; flex-wrap:wrap; gap:14px; }
  .qlink{
    display:inline-flex; align-items:center; gap:9px;
    padding:12px 20px; border-radius:8px; text-decoration:none;
    font-weight:600; font-size:14.5px; font-family:var(--body);
    border:1px solid var(--panel-line); color:var(--text-primary);
    background:rgba(255,255,255,0.03);
    transition:border-color .2s ease, transform .18s ease, background .2s ease;
  }
  .qlink:hover{ border-color:var(--accent); transform:translateY(-2px); background:rgba(79,214,255,0.08); }
  .qlink.primary{ background:var(--accent); color:var(--bg-deep); border-color:var(--accent); }
  .qlink.primary:hover{ background:#7EE3FF; }

  /* ---------- SECTION SCAFFOLD ---------- */
  section{ padding:76px 0; border-top:1px solid var(--panel-line); }
  .section-head{ margin-bottom:44px; max-width:640px; }
  .section-tag{
    font-family:var(--mono); font-size:12px; letter-spacing:0.16em; text-transform:uppercase;
    color:var(--accent); margin:0 0 12px;
  }
  h2{
    font-family:var(--display); font-weight:700; font-size:clamp(1.7rem, 3.4vw, 2.4rem);
    margin:0 0 12px; letter-spacing:-0.01em;
  }
  .section-desc{ color:var(--text-secondary); font-size:1.02rem; margin:0; }

  /* ---------- SKILLS ---------- */
  .skills-grid{ display:grid; grid-template-columns:repeat(auto-fit, minmax(230px,1fr)); gap:1px; background:var(--panel-line); border:1px solid var(--panel-line); border-radius:14px; overflow:hidden; }
  .skill-cat{ background:var(--panel); padding:26px 24px; }
  .skill-cat h3{
    font-family:var(--mono); font-size:12.5px; letter-spacing:0.1em; text-transform:uppercase;
    color:var(--amber); margin:0 0 16px;
  }
  .pill-row{ display:flex; flex-wrap:wrap; gap:8px; }
  .pill{
    font-size:12.8px; padding:6px 11px; border-radius:100px;
    border:1px solid var(--panel-line); color:var(--text-secondary);
    background:rgba(255,255,255,0.02);
  }

  /* ---------- CASE STUDIES : TEST-CASE LEDGER ---------- */
  .gallery-intro{
    max-width:760px; color:var(--text-secondary); font-size:1.02rem; margin:0 0 46px;
    padding:20px 22px; border-radius:10px; background:rgba(79,214,255,0.05);
    border:1px solid var(--panel-line);
  }
  .ledger{ display:flex; flex-direction:column; gap:18px; }
  .ticket{
    border:1px solid var(--panel-line); border-radius:14px; background:var(--panel);
    padding:28px 30px; position:relative; overflow:hidden;
    transition:border-color .22s ease, transform .22s ease;
  }
  .ticket::before{
    content:''; position:absolute; left:0; top:0; bottom:0; width:3px;
    background:var(--accent); opacity:0.55;
  }
  .ticket:hover{ border-color:var(--accent-dim); transform:translateY(-3px); }
  .ticket-head{
    display:flex; align-items:center; flex-wrap:wrap; gap:14px 18px; margin-bottom:16px;
  }
  .tc-id{
    font-family:var(--mono); font-size:12.5px; color:var(--text-muted); letter-spacing:0.06em;
  }
  .tc-status{
    font-family:var(--mono); font-size:11.5px; letter-spacing:0.08em; text-transform:uppercase;
    padding:4px 10px; border-radius:5px; font-weight:600;
  }
  .status-shipped{ background:rgba(79,214,255,0.14); color:var(--accent); border:1px solid rgba(79,214,255,0.35); }
  .status-verified{ background:rgba(140,255,170,0.1); color:#8CFFAA; border:1px solid rgba(140,255,170,0.3); }
  .status-scoped{ background:rgba(255,179,71,0.12); color:var(--amber); border:1px solid rgba(255,179,71,0.32); }
  .status-sized{ background:rgba(200,160,255,0.12); color:#C8A0FF; border:1px solid rgba(200,160,255,0.32); }

  .ticket h3{
    font-family:var(--display); font-weight:600; font-size:1.32rem; margin:0 0 12px;
  }
  .ticket p.blurb{ color:var(--text-secondary); margin:0 0 16px; font-size:0.99rem; }
  .north-star{
    display:flex; align-items:baseline; gap:10px; flex-wrap:wrap;
    padding-top:16px; margin-top:2px; border-top:1px solid var(--panel-line);
  }
  .north-star .ns-label{
    font-family:var(--mono); font-size:11px; letter-spacing:0.1em; text-transform:uppercase;
    color:var(--amber); white-space:nowrap;
  }
  .north-star .ns-value{ font-size:0.96rem; color:var(--text-primary); font-weight:600; }
  /* ---------- RESUME ---------- */
  .resume-card{
    border:1px solid var(--panel-line); border-radius:14px; background:var(--panel);
    padding:34px 36px;
  }
  .resume-top{ display:flex; justify-content:space-between; align-items:flex-start; gap:24px; flex-wrap:wrap; margin-bottom:26px; }
  .resume-top p{ color:var(--text-secondary); margin:0; max-width:520px; }
  .btn-download{
    font-family:var(--mono); font-size:13px; letter-spacing:0.04em; font-weight:600;
    padding:12px 22px; border-radius:8px; text-decoration:none; white-space:nowrap;
    background:var(--accent); color:var(--bg-deep);
    transition:background .2s ease;
  }
  .btn-download:hover{ background:#7EE3FF; }

  .resume-block{ margin-bottom:30px; }
  .resume-block:last-child{ margin-bottom:0; }
  .resume-block h4{
    font-family:var(--mono); font-size:12.5px; letter-spacing:0.14em; text-transform:uppercase;
    color:var(--amber); margin:0 0 16px; padding-bottom:10px; border-bottom:1px solid var(--panel-line);
  }
  .resume-block p{ color:var(--text-secondary); margin:0 0 18px; }

  .job{ margin-bottom:22px; }
  .job:last-child{ margin-bottom:0; }
  .job-row{ display:flex; justify-content:space-between; gap:16px; flex-wrap:wrap; margin-bottom:6px; }
  .job-title{ font-weight:600; color:var(--text-primary); font-size:1rem; }
  .job-meta{ font-family:var(--mono); font-size:12px; color:var(--text-muted); text-align:right; }
  .job p{ margin:0; color:var(--text-secondary); font-size:0.96rem; }

  .edu-row{ display:flex; justify-content:space-between; gap:16px; flex-wrap:wrap; padding:10px 0;
    border-bottom:1px solid var(--panel-line); }
  .edu-row:last-child{ border-bottom:none; }
  .edu-name{ color:var(--text-primary); font-weight:500; font-size:0.96rem; }
  .edu-year{ font-family:var(--mono); font-size:12px; color:var(--text-muted); }

  /* ---------- CONTACT / FOOTER ---------- */
  .contact-card{
    display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:26px;
    padding:44px 40px; border-radius:16px;
    background:linear-gradient(120deg, rgba(79,214,255,0.10), rgba(18,59,110,0.5));
    border:1px solid var(--panel-line);
  }
  .contact-card h2{ margin:0 0 10px; }
  .contact-card p{ margin:0; color:var(--text-secondary); }
  .contact-links{ display:flex; gap:14px; flex-wrap:wrap; }

  footer{ padding:36px 0 60px; }
  .foot-row{ display:flex; justify-content:flex-end; align-items:center; flex-wrap:wrap; gap:12px; }
  .back-top{ color:var(--text-muted); font-size:13px; text-decoration:none; }
  .back-top:hover{ color:var(--accent); }

  @media (max-width:640px){
    .hero{ padding:72px 0 48px; }
    section{ padding:56px 0; }
    .ticket{ padding:22px 20px; }
    .resume-card{ padding:26px 22px; }
    .contact-card{ padding:32px 24px; flex-direction:column; align-items:flex-start; }
  }
</style>
</head>
<body>

<header class="nav">
  <div class="nav-inner">
    <a class="logo" href="#top">AC</a>
    <ul class="nav-links">
      <li><a href="#case-studies">Case Studies</a></li>
      <li><a href="#skills">Skills</a></li>
      <li><a href="#resume">Resume</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </div>
</header>

<main id="top" class="wrap">

  <!-- HERO -->
  <section class="hero" style="border-top:none;">
    <p class="eyebrow">Open to Product Management roles</p>
    <h1 class="name">Ankur Chandrakar</h1>
    <p class="subtitle">QA Lead transitioning to Product Management</p>

    <div class="positioning">
      <p>I've spent <strong>9+ years</strong> making sure products work for every user, including the ones most teams forget. I'm now applying that same discipline to deciding what gets built, not just verifying that it was built right.</p>
      <p>That shift shows up in hands-on PM case studies across <strong>FinTech, Consumer, and B2C/B2B SaaS</strong> — RICE prioritization, OKR design, TAM/SAM/SOM market sizing, and full PRD authorship, backed by working knowledge of SQL, Python, and Tableau for data-informed decisions.</p>
    </div>

    <div class="quicklinks">
      <a class="qlink primary" href="#case-studies">📂 Case Studies</a>
      <a class="qlink" href="#resume">📄 Resume</a>
      <a class="qlink" href="#contact"><svg width="14" height="14" viewBox="0 0 20 20" style="vertical-align:-2px;margin-right:2px;" xmlns="http://www.w3.org/2000/svg"><rect x="1.5" y="4" width="17" height="12" rx="1.6" style="fill:var(--icon-envelope)"/><path d="M2 5L10 11L18 5" stroke="var(--bg-deep)" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg> Contact</a>
    </div>
  </section>

  <!-- CASE STUDIES -->
  <section id="case-studies">
    <div class="section-head">
      <p class="section-tag">Case Studies · 04 Tickets Closed</p>
      <h2>Four case studies, four different PM muscles</h2>
      <p class="section-desc">From deep retention strategy to 0-to-1 market sizing to growth prioritization to PRD authorship and MVP scoping. Each one includes the actual research, trade-offs, and metrics behind the decisions — not just the polished outcome.</p>
    </div>

    <div class="ledger">

      <article class="ticket">
        <div class="ticket-head">
          <span class="tc-id">TC-01 · RETENTION</span>
          <span class="tc-status status-shipped">+₹18Cr Projected</span>
        </div>
        <h3>Stable Money — Phase 1 Retention Initiative</h3>
        <p class="blurb">A Phase 1 retention initiative for Stable Money's first-time FD investors, where only 20% rebook within 90 days. 75% of users said a pre-maturity reminder would help. 23 of them also warned me not to push them toward reinvesting. I had to design a feature that satisfied both — and it's projected to unlock ₹18 crore in revenue without a single sales CTA.</p>
        <div class="north-star"><span class="ns-label">North Star Metric</span><span class="ns-value">90-Day Repeat Investment Rate — 20% → 35%</span></div>
      </article>

      <article class="ticket">
        <div class="ticket-head">
          <span class="tc-id">TC-02 · GROWTH</span>
          <span class="tc-status status-verified">+15–20% AOV Target</span>
        </div>
        <h3>Zepto — Lifting Average Order Value</h3>
        <p class="blurb">A growth case study on lifting Zepto's Average Order Value, where 67% of users are stuck in a ₹200–400 band well below break-even. The data pointed to one solution as the clear winner. I recommended a different one instead — and the reasoning had nothing to do with the numbers everyone was looking at.</p>
        <div class="north-star"><span class="ns-label">North Star Metric</span><span class="ns-value">Average Order Value — +15–20% Uplift</span></div>
      </article>

      <article class="ticket">
        <div class="ticket-head">
          <span class="tc-id">TC-03 · PRD / MVP</span>
          <span class="tc-status status-scoped">25% MAU Target</span>
        </div>
        <h3>VitaFit Engage — Gamification &amp; Community PRD</h3>
        <p class="blurb">A gamification &amp; community PRD for VitaFit, built to fix a 60% user drop-off in the first 2–4 sessions. Most retention features launch to everyone and hope for the best. I deliberately launched this one first to the exact users most likely to churn — before it ever reached anyone else.</p>
        <div class="north-star"><span class="ns-label">North Star Metric</span><span class="ns-value">DAU/MAU — 15% → 25%</span></div>
      </article>

      <article class="ticket">
        <div class="ticket-head">
          <span class="tc-id">TC-04 · MARKET SIZING</span>
          <span class="tc-status status-sized">260M Underserved</span>
        </div>
        <h3>Google Maps — The Parking Gap</h3>
        <p class="blurb">A market-sizing case study on a feature Google Maps doesn't have: parking discovery. 260 million people in India have a phone in their pocket with zero tool to solve a problem they face every single day. I sized the opportunity, and the number surprised even me.</p>
        <div class="north-star"><span class="ns-label">North Star Metric</span><span class="ns-value">Serviceable Obtainable Market — ₹49 Cr in 3–5 Years</span></div>
      </article>

    </div>
  </section>

  <!-- CORE SKILLS -->
  <section id="skills">
    <div class="section-head">
      <p class="section-tag">Coverage Map</p>
      <h2>Core skills</h2>
      <p class="section-desc">The same rigor QA demands of a release checklist, now applied to product decisions.</p>
    </div>

    <div class="skills-grid">
      <div class="skill-cat">
        <h3>Product</h3>
        <div class="pill-row">
          <span class="pill">Product Strategy</span>
          <span class="pill">Roadmapping</span>
          <span class="pill">PRD Writing</span>
          <span class="pill">RICE Framework</span>
          <span class="pill">User Research</span>
          <span class="pill">Market Sizing (TAM/SAM/SOM)</span>
          <span class="pill">SaaS Product Management</span>
          <span class="pill">Gamification</span>
        </div>
      </div>
      <div class="skill-cat">
        <h3>Analytics</h3>
        <div class="pill-row">
          <span class="pill">AARRR Funnel</span>
          <span class="pill">A/B Testing</span>
          <span class="pill">Retention Metrics</span>
          <span class="pill">Cohort Analysis</span>
          <span class="pill">KPI Definition</span>
          <span class="pill">Google Analytics</span>
        </div>
      </div>
      <div class="skill-cat">
        <h3>UX</h3>
        <div class="pill-row">
          <span class="pill">UX/UI Evaluation</span>
          <span class="pill">Usability Testing</span>
          <span class="pill">Figma</span>
          <span class="pill">Wireframing</span>
          <span class="pill">Accessibility Testing</span>
        </div>
      </div>
      <div class="skill-cat">
        <h3>Data</h3>
        <div class="pill-row">
          <span class="pill">Tableau</span>
          <span class="pill">Power BI</span>
          <span class="pill">SQL</span>
          <span class="pill">Python</span>
          <span class="pill">Advanced Excel</span>
        </div>
      </div>
      <div class="skill-cat">
        <h3>Tools</h3>
        <div class="pill-row">
          <span class="pill">JIRA</span>
          <span class="pill">Bugzilla</span>
          <span class="pill">Survey Monkey</span>
          <span class="pill">Google Forms</span>
          <span class="pill">Stakeholder Management</span>
        </div>
      </div>
    </div>
  </section>

  <!-- RESUME -->
  <section id="resume">
    <div class="section-head">
      <p class="section-tag">Resume</p>
      <h2>9+ years, one clear pivot</h2>
      <p class="section-desc">Full resume below — download for the complete version, or scroll for a quick read.</p>
    </div>

    <div class="resume-card">
      <div class="resume-top">
        <p>Full resume below — download for the complete version, or scroll for a quick read.</p>
        <a class="btn-download" href="Ankur_Chandrakar_Resume_Updated.docx" download>↓ Download Resume</a>
      </div>

      <div class="resume-block">
        <h4>Professional Summary</h4>
        <p>Product-minded QA Lead with 9+ years delivering WCAG 2.1 AA-compliant SaaS eLearning platforms for US enterprise clients. Transitioning to Product Management via the Airtribe PM Program, with case studies spanning RICE prioritisation, OKR design, market sizing (TAM/SAM/SOM), and full PRD authoring across B2C and B2B/SaaS. Brings compliance-driven product discipline and working knowledge of Tableau, SQL, and Python to support data-informed decisions.</p>
      </div>

      <div class="resume-block">
        <h4>Work Experience</h4>

        <div class="job">
          <div class="job-row">
            <span class="job-title">Quality Analyst Team Lead — Focus Digital Labs (Freelance)</span>
            <span class="job-meta">Bangalore · Nov 2025 – Present</span>
          </div>
          <p>Owned end-to-end product quality for ADA compliance deliverables across 3+ concurrent client projects, ensuring 80–90% of deliverables shipped on schedule with zero client-reported ADA defects post-delivery.</p>
        </div>

        <div class="job">
          <div class="job-row">
            <span class="job-title">Quality Analyst Team Lead — NuAge Edtech Pvt. Ltd.</span>
            <span class="job-meta">Bangalore · Mar 2022 – Oct 2025</span>
          </div>
          <p>Drove product quality strategy for a portfolio of 10+ WCAG 2.1 AA-compliant SaaS eLearning products serving US K-12 clients; aligned a 16-person QA team to business, regulatory, and accessibility outcomes.</p>
        </div>

        <div class="job">
          <div class="job-row">
            <span class="job-title">Senior Quality Analyst — NuAge Edtech Pvt. Ltd.</span>
            <span class="job-meta">Bangalore · Feb 2021 – Feb 2022</span>
          </div>
          <p>Acted as quality owner for new product launches, partnering with Product Development on release-readiness criteria against US client requirements.</p>
        </div>

        <div class="job">
          <div class="job-row">
            <span class="job-title">Quality Analyst — Focus Edtumatics Pvt. Ltd.</span>
            <span class="job-meta">Bangalore · Mar 2017 – Jan 2021</span>
          </div>
          <p>Delivered WCAG 2.1-compliant QA for the San Francisco Department of Public Health (SFDPH) platform, shaping UI and content decisions through user-impact-prioritised recommendations.</p>
        </div>
      </div>

      <div class="resume-block">
        <h4>Education</h4>
        <div class="edu-row">
          <span class="edu-name">PG Diploma in Data Science — IIIT Bangalore</span>
          <span class="edu-year">2022</span>
        </div>
        <div class="edu-row">
          <span class="edu-name">B.E. in Computer Science — CMRIT College, Bangalore</span>
          <span class="edu-year">2015</span>
        </div>
        <div class="edu-row">
          <span class="edu-name">Airtribe PM Program — B2C and B2B/SaaS Case Studies</span>
          <span class="edu-year">2026</span>
        </div>
      </div>
    </div>
  </section>

  <!-- CONTACT -->
  <section id="contact">
    <div class="contact-card">
      <div>
        <h2>Let's talk product.</h2>
        <p>Based in Bengaluru, India · Open to Product Management roles</p>
      </div>
      <div class="contact-links">
        <a class="qlink primary" href="mailto:ankur.c2208@gmail.com"><svg width="15" height="15" viewBox="0 0 20 20" style="vertical-align:-2px;margin-right:4px;" xmlns="http://www.w3.org/2000/svg"><rect x="1.5" y="4" width="17" height="12" rx="1.6" style="fill:var(--icon-envelope)"/><path d="M2 5L10 11L18 5" stroke="var(--bg-deep)" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg> ankur.c2208@gmail.com</a>
        <a class="qlink" href="https://www.linkedin.com/in/ankur-chandrakar-4675483b/" target="_blank" rel="noopener">LinkedIn ↗</a>
        <a class="qlink" href="https://github.com/ankurc123" target="_blank" rel="noopener">GitHub ↗</a>
      </div>
    </div>
  </section>

</main>

<footer>
  <div class="wrap foot-row">
    <a class="back-top" href="#top">Back to top ↑</a>
  </div>
</footer>

</body>
</html>
"""

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(HTML)
    print(f"Wrote {OUTPUT_FILE} ({len(HTML):,} characters)")

if __name__ == "__main__":
    main()
