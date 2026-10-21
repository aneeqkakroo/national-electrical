"""Builds the National Electrical Ltd website into ../site/.

    python build.py

Edit content.py for words, assets/site.css for styling. Every page is plain static HTML,
so ../site/ can be uploaded to any host (Netlify, Cloudflare Pages, cPanel...).
"""
import json, shutil
from urllib.parse import quote
from datetime import date
from html import escape as e
from pathlib import Path

from content import BUSINESS as B, DRAFT_NOTE, GROUPS, SERVICES, SECTORS, AREAS, FAQS_GENERAL

HERE = Path(__file__).parent
OUT = HERE.parent / "site"
SVC = {s["slug"]: s for s in SERVICES}
SEC = {s["slug"]: s for s in SECTORS}
PAGES = []  # paths for sitemap

# ------------------------------------------------------------------ pieces
ICONS = {
    "install": '<path d="M3 12h4l2-5 4 10 2-5h6"/>',
    "testing": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16l2 2 4-4"/>',
    "design": '<path d="M3 21h18M5 21V9l7-5 7 5v12"/><path d="M9 21v-6h6v6"/>',
    "repairs": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.5-.5-.5-2.5z"/>',
    "renew": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    "safety": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
    "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
}
def icon(key, color="#FFFFFF"):
    return (f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[key]}</svg>')

SPRITE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="mark" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#0A2A52"/><path d="M19 47V17M45 47V17" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" fill="none"/><path d="M19 17L29 31L35 31L45 47" stroke="#F2B321" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="19" cy="47" r="4.5" fill="#F2B321"/><circle cx="45" cy="17" r="4.5" fill="#F2B321"/></symbol>
<symbol id="tick" viewBox="0 0 16 16"><circle cx="8" cy="8" r="8" fill="#F2B321"/><path d="M4.5 8.2l2.3 2.3 4.7-4.9" stroke="#0A2A52" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></symbol>
</defs></svg>'''

LOGO = ('<svg viewBox="0 0 440 96" role="img" aria-label="National Electrical Ltd"><use href="#mark" x="0" y="8" width="80" height="80"/>'
        '<text x="100" y="50" font-family="Archivo, Arial Narrow, sans-serif" font-weight="800" font-size="38" font-stretch="85%" style="fill:var(--ink)" letter-spacing="1">NATIONAL</text>'
        '<text x="100" y="82" font-family="Archivo, Arial Narrow, sans-serif" font-weight="600" font-size="22" style="fill:var(--blue)" letter-spacing="6.2">ELECTRICAL LTD</text></svg>')

TICK = '<svg width="16" height="16" aria-hidden="true"><use href="#tick"/></svg>'
PHONE = f'<a href="tel:{B["phone_tel"]}">{B["phone"]}</a>'
WA_ICON = ('<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round">'
           '<path d="M3.6 20.4l1.2-4A8.6 8.6 0 1 1 8 19.3z"/>'
           '<path d="M9.2 7.8c-.4 3 2.8 6.9 6.6 7.2l1-1.5-2-1.1-1 .8c-1.1-.5-2.3-1.7-2.8-2.8l.8-1-1-2z" fill="currentColor" stroke="none"/></svg>')
def lc(name):
    """Lower-case a service name for use mid-sentence, keeping acronyms like EICR, PAT, EV, CCTV."""
    return " ".join(w if w.isupper() else w.lower() for w in name.split())

def wa(text="Hi National Electrical, I'd like a quote please."):
    return f"https://wa.me/{B['whatsapp']}?text={quote(text)}"
def wa_btn(text=None, label="WhatsApp us", cls="btn btn-wa"):
    href = wa(text) if text else wa()
    return f'<a href="{href}" class="{cls}" target="_blank" rel="noopener">{WA_ICON}<span>{label}</span></a>'
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Public+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap">')

def svc_url(r, slug): return f"{r}services/{slug}.html"
def area_url(r, slug): return f"{r}areas/{slug}.html"
def sec_url(r, slug): return f"{r}customers/{slug}.html"
def home_url(r): return r or "./"

def head(title, desc, path, r, jsonld=None, artifact=False):
    canon = B["url"] + "/" + ("" if path == "index.html" else path)
    meta = (f'<meta name="claude:viewport-fit-sides" content="cover">'
            f'<meta name="description" content="{e(desc)}">'
            f'<link rel="canonical" href="{canon}">'
            f'<meta property="og:type" content="website"><meta property="og:title" content="{e(title)}">'
            f'<meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canon}">'
            f'<meta property="og:site_name" content="{e(B["name"])}"><meta property="og:locale" content="en_GB">'
            f'<meta property="og:image" content="{B["url"]}/assets/og-image.jpg"><meta property="og:image:secure_url" content="{B["url"]}/assets/og-image.jpg">'
            f'<meta property="og:image:type" content="image/jpeg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
            f'<meta property="og:image:alt" content="National Electrical Ltd branded van with phone number {B["phone"]}">'
            f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{B["url"]}/assets/og-image.jpg">'
            f'<link rel="apple-touch-icon" href="{r}assets/apple-touch-icon.png">'
            f'<meta name="theme-color" content="#0A2A52">'
            f'<link rel="icon" href="{r}assets/favicon.svg" type="image/svg+xml">'
            f'{FONTS}<link rel="stylesheet" href="{r}assets/site.css">')
    if jsonld:
        meta += f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>'
    if artifact:
        return f"<title>{e(title)}</title>{meta}"
    return (f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            f'<title>{e(title)}</title>{meta}</head><body>')

def header(r, active=""):
    def cur(k): return ' aria-current="page"' if k == active else ""
    groups = ""
    for gk, glabel, _ in GROUPS:
        links = "".join(f'<li><a href="{svc_url(r, s["slug"])}">{e(s["name"])}</a></li>' for s in SERVICES if s["group"] == gk)
        groups += f"<div><h4>{e(glabel)}</h4><ul>{links}</ul></div>"
    secs = "".join(f'<li><a href="{sec_url(r, s["slug"])}">{e(s["name"])}</a></li>' for s in SECTORS)
    draft = f'<div class="draft"><div class="wrap"><b>Draft.</b> {e(DRAFT_NOTE.replace("Draft website. ", ""))}</div></div>' if DRAFT_NOTE else ""
    return f'''<a class="skip" href="#main">Skip to content</a>{SPRITE}{draft}
<div class="topbar"><div class="wrap"><span>Covering <b>{e(B["region_line"])}</b></span>
<span class="em"><span class="dot"></span> Call us: {PHONE} <span aria-hidden="true">·</span> <a href="{wa()}" target="_blank" rel="noopener">WhatsApp</a></span></div></div>
<header class="site-head"><div class="wrap">
<a class="brand" href="{home_url(r)}" aria-label="National Electrical Ltd home">{LOGO}</a>
<button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav class="nav" id="nav" aria-label="Main">
<div class="dd"><a href="{r}services/index.html"{cur("services")}>Services</a><div class="dd-panel">{groups}</div></div>
<div class="dd"><a href="{r}customers/index.html"{cur("customers")}>Who we help</a><div class="dd-panel" style="grid-template-columns:1fr;width:260px"><div><ul>{secs}</ul></div></div></div>
<a href="{r}areas/index.html"{cur("areas")}>Areas</a>
<a href="{r}about.html"{cur("about")}>About</a>
<a href="{r}faq.html"{cur("faq")}>FAQs</a>
<a href="{r}contact.html" class="btn btn-primary">Get a free quote</a>
</nav></div></header>
<main id="main">'''

def footer(r):
    svc = "".join(f'<li><a href="{svc_url(r, s)}">{e(SVC[s]["name"])}</a></li>' for s in
                  ["rewiring", "consumer-unit-upgrades", "eicr", "landlord-certificates", "ev-chargers", "emergency-electrician"])
    secs = "".join(f'<li><a href="{sec_url(r, s["slug"])}">{e(s["name"])}</a></li>' for s in SECTORS)
    areas = "".join(f'<li><a href="{area_url(r, a["slug"])}">{e(a["name"])}</a></li>' for a in AREAS)
    return f'''</main>
<footer><div class="wrap"><div class="foot-grid">
<div class="foot-brand">{LOGO}<p>Electrical installation, design and testing for homes, landlords and businesses across {e(B["region_line"])}.</p></div>
<div><h4>Services</h4><ul>{svc}<li><a href="{r}services/index.html">All services</a></li></ul></div>
<div><h4>Who we help</h4><ul>{secs}</ul></div>
<div><h4>Areas</h4><ul>{areas}</ul></div>
<div><h4>Contact</h4><ul><li>{PHONE}</li><li><a href="{wa()}" target="_blank" rel="noopener">WhatsApp us</a></li><li><a href="mailto:{B["email"]}">{B["email"]}</a></li><li>{e(B["hours"])}</li><li><a href="{r}contact.html">Get a free quote</a></li></ul></div>
</div>
<div class="legal"><span>© {date.today().year} {e(B["name"])}. Registered in England &amp; Wales{f", company no. {e(B['company_no'])}" if B["company_no"] else ""}{f". Registered office: {e(B['registered_office'])}" if B["registered_office"] else ""}.</span>
<span><a href="{r}privacy.html">Privacy policy</a> · <a href="{r}faq.html">FAQs</a></span></div></div></footer>
<div class="callbar"><a class="btn btn-amber" href="tel:{B["phone_tel"]}">Call</a>{wa_btn(label="WhatsApp")}<a class="btn btn-primary" href="{r}contact.html">Quote</a></div>
<a class="wa-float" href="{wa()}" target="_blank" rel="noopener" aria-label="Message us on WhatsApp">{WA_ICON}<span>WhatsApp us</span></a>
<script src="{r}assets/site.js"></script>'''

def page(path, title, desc, body, active="", jsonld=None, artifact=False):
    r = "../" * path.count("/")
    html = head(title, desc, path, r, jsonld, artifact) + header(r, active) + body(r) + footer(r)
    if not artifact:
        html += "</body></html>"
    return html

def write(path, title, desc, body, active="", jsonld=None):
    out = OUT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(path, title, desc, body, active, jsonld), encoding="utf-8")
    if path not in ("404.html", "thanks.html"):
        PAGES.append(path)

def crumbs(r, items):
    parts = [f'<a href="{home_url(r)}">Home</a>']
    for label, href in items:
        parts.append('<span aria-hidden="true">/</span>')
        parts.append(f'<a href="{href}">{e(label)}</a>' if href else f'<span>{e(label)}</span>')
    return f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'

def page_hero(r, eyebrow, h1, lead, crumb_items, ctas=True, quote_hash="", wa_text=None):
    c = (f'<div class="ctas"><a href="{r}contact.html{quote_hash}" class="btn btn-amber">Get a free quote</a>'
         f'{wa_btn(wa_text)}<a href="tel:{B["phone_tel"]}" class="btn btn-ghost">Call {B["phone"]}</a></div>') if ctas else ""
    return f'''<section class="page-hero"><div class="wrap">{crumbs(r, crumb_items)}
<div class="eyebrow">{e(eyebrow)}</div><h1>{h1}</h1><p class="lead">{lead}</p>{c}</div></section>'''

def cta_band(r, title="Need an electrician?", text=None):
    text = text or f"Free, fixed-price quotes across {B['region_line']}."
    return f'''<section class="cta-band"><div class="wrap"><div><h2>{e(title)}</h2><p>{e(text)}</p></div>
<div class="ctas" style="margin:0"><a href="{r}contact.html" class="btn btn-amber">Get a free quote</a>{wa_btn()}<a href="tel:{B["phone_tel"]}" class="btn btn-ghost">Call {B["phone"]}</a></div></div></section>'''

def quote_card(r, hash_="", wa_text=None):
    return f'''<div class="quote-card"><h3>Get a free quote</h3><p>Tell us about the job and we'll reply within one working day.</p>
<div class="phone"><small>Call us</small>{PHONE}</div>
<a href="{r}contact.html{hash_}" class="btn btn-amber">Request a quote</a>{wa_btn(wa_text, "Message us on WhatsApp")}</div>'''

def side_list(title, links):
    lis = "".join(f'<li><a href="{h}">{e(t)}</a></li>' for t, h in links)
    return f'<div class="side-list"><h3>{e(title)}</h3><ul>{lis}</ul></div>'

def checklist(items):
    return '<ul class="checklist">' + "".join(f"<li>{TICK}<span>{e(i)}</span></li>" for i in items) + "</ul>"

def faq_block(faqs, heading="Questions"):
    d = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in faqs)
    return f'<section><h2>{e(heading)}</h2><div class="faq">{d}</div></section>'

def service_cards(r, slugs):
    return '<div class="cards">' + "".join(
        f'<a class="card" href="{svc_url(r, s)}"><h3>{e(SVC[s]["name"])}</h3><p>{e(SVC[s]["short"])}</p><span class="more">Find out more →</span></a>'
        for s in slugs) + "</div>"

CODES = '''<div class="codes">
<div class="code"><div class="tag t-c1">C1</div><div><b>Danger present</b><span>Risk of injury. We make it safe straight away, before we leave.</span></div></div>
<div class="code"><div class="tag t-c2">C2</div><div><b>Potentially dangerous</b><span>Needs urgent repair. The report is unsatisfactory until it's fixed.</span></div></div>
<div class="code"><div class="tag t-fi">FI</div><div><b>Further investigation</b><span>Something needs checking more closely without delay.</span></div></div>
<div class="code"><div class="tag t-c3">C3</div><div><b>Improvement recommended</b><span>Not dangerous, but bringing it up to date would improve safety.</span></div></div>
</div>'''

INTERVALS = '''<div class="table-card"><h3>How often to test</h3><p>Maximum time between inspections, based on IET guidance.</p>
<table><tbody>
<tr><td>Rented homes (legal requirement)</td><td>5 years</td></tr>
<tr><td>Owner-occupied homes</td><td>10 years</td></tr>
<tr><td>Offices, shops &amp; commercial</td><td>5 years</td></tr>
<tr><td>Industrial premises</td><td>3 years</td></tr>
<tr><td>Swimming pools &amp; saunas</td><td>1 year</td></tr>
<tr><td>Construction sites</td><td>3 months</td></tr>
</tbody></table><p class="note">Also when you buy or sell a home, or at a change of tenancy.</p></div>'''

STEPS = '''<ol class="steps">
<li><h3>Tell us what you need</h3><p>Call or send the form. We'll ask a few questions and arrange a visit if needed.</p></li>
<li><h3>Free, fixed quote</h3><p>A clear written price with no hidden extras, usually within 48 hours.</p></li>
<li><h3>The work, done properly</h3><p>Qualified electricians, on time and tidy, with dust sheets down.</p></li>
<li><h3>Tested &amp; certified</h3><p>Every job is tested and you get the certificate. Part P work is registered for you.</p></li>
</ol>'''

def trust_strip():
    return f'''<div class="trust" aria-label="Accreditations"><div class="wrap">
{f'<div class="trust-item"><div class="badge">✓</div><div><b>{e(B["scheme"])}</b><span>Competent person scheme</span></div></div>' if B["scheme"] else '<div class="trust-item"><div class="badge">FREE</div><div><b>Free, fixed quotes</b><span>No call-out charge to quote</span></div></div>'}
<div class="trust-item"><div class="badge">7671</div><div><b>BS 7671 qualified</b><span>IET Wiring Regulations</span></div></div>
<div class="trust-item"><div class="badge">P</div><div><b>Part P notified</b><span>Building Regulations sign-off</span></div></div>
<div class="trust-item"><div class="badge">£</div><div><b>Public liability insured</b><span>Covered on every job</span></div></div>
</div></div>'''

def quote_form(r):
    opts = "".join(f'<option data-slug="{s["slug"]}">{e(s["name"])}</option>' for s in SERVICES)
    types = "".join(f"<option>{e(s['name'])}</option>" for s in SECTORS)
    return f'''<form class="form" id="quoteForm" name="quote" method="POST" action="{r}thanks.html" data-netlify="true" netlify-honeypot="website" novalidate>
<input type="hidden" name="form-name" value="quote"><p hidden><label>Leave blank <input name="website"></label></p>
<div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required></div>
<div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required></div>
<div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email"></div>
<div class="field"><label for="f-pc">Postcode</label><input id="f-pc" name="postcode" autocomplete="postal-code" placeholder="e.g. CB1 2AB"></div>
<div class="field"><label for="f-type">I am a</label><select id="f-type" name="customer">{types}</select></div>
<div class="field"><label for="f-svc">Service</label><select id="f-svc" name="service">{opts}<option>Something else</option></select></div>
<div class="field full"><label for="f-msg">About the job</label><textarea id="f-msg" name="message" placeholder="What needs doing, property type and size, any deadlines"></textarea></div>
<p class="consent full">We'll only use your details to reply to this enquiry. See our <a href="{r}privacy.html">privacy policy</a>.</p>
<div class="full"><button class="btn btn-primary" type="submit" style="width:100%">Send my enquiry</button></div>
<div class="form-msg" id="formMsg" role="status" hidden></div></form>'''

def contact_section(r, heading="Tell us about your job"):
    return f'''<section class="band contact" id="contact"><div class="wrap contact-grid"><div>
<div class="eyebrow">Get a free quote</div><h2 style="margin-top:12px">{e(heading)}</h2>
<p class="lead" style="margin-top:12px">We reply to every enquiry within one working day. For emergencies, please call.</p>
<div class="direct"><div><small>Phone</small>{PHONE}</div>
<div><small>WhatsApp</small><a href="{wa()}" target="_blank" rel="noopener">Message us on WhatsApp</a></div>
<div><small>Email</small><a href="mailto:{B["email"]}">{B["email"]}</a></div>
<div><small>Hours</small><b style="font-size:1.05rem">{e(B["hours"])}</b></div></div></div>
{quote_form(r)}</div></section>'''

def areas_grid(r):
    out = ""
    for a in AREAS:
        towns = [t for g in a["towns"].values() for t in g][:7]
        lis = "".join(f"<li>{e(t)}</li>" for t in towns)
        tag = "<small>BASE</small>" if a.get("home") else ""
        out += f'<div class="county{" home" if a.get("home") else ""}"><h3><a href="{area_url(r, a["slug"])}">{e(a["name"])}</a> {tag}</h3><ul>{lis}</ul></div>'
    pcs = sorted({p for a in AREAS for p in a["postcodes"]})
    return f'<div class="areas-grid">{out}</div><div class="pc" aria-label="Postcode areas covered">' + "".join(f"<span>{p}</span>" for p in pcs) + "</div>"

def local_business_schema():
    return {
        "@context": "https://schema.org", "@type": "Electrician", "name": B["name"], "url": B["url"],
        "telephone": B["phone_tel"], "email": B["email"], "logo": B["url"] + "/assets/favicon.svg",
        "openingHours": B["hours_schema"],
        "areaServed": [{"@type": "AdministrativeArea", "name": a["name"]} for a in AREAS],
        "address": {"@type": "PostalAddress", "addressRegion": "Cambridgeshire", "addressCountry": "GB"},
    }

# ------------------------------------------------------------------ pages
def home_body(r):
    tabs, panels = "", ""
    for i, s in enumerate(SECTORS):
        sel = "true" if i == 0 else "false"
        tabs += f'<button class="tab" role="tab" id="tab-{s["slug"]}" aria-controls="p-{s["slug"]}" aria-selected="{sel}"{"" if i == 0 else " tabindex=\"-1\""}>{e(s["tab"])}</button>'
        pills = "".join(f'<li><a href="{svc_url(r, sl)}">{e(SVC[sl]["name"])}<small>{e(note)}</small></a></li>' for sl, note in s["pills"])
        panels += (f'<div class="panel" role="tabpanel" id="p-{s["slug"]}" aria-labelledby="tab-{s["slug"]}"{"" if i == 0 else " hidden"}>'
                   f'<div><h3>For {e(s["name"].lower())}</h3><p>{e(s["intro"])}</p>'
                   f'<a href="{sec_url(r, s["slug"])}" class="btn btn-primary">{e(s["cta"])}</a></div>'
                   f'<ul class="pill-list">{pills}</ul></div>')
    groups = ""
    for gk, glabel, ik in GROUPS:
        items = [s for s in SERVICES if s["group"] == gk]
        lis = "".join(f'<li><a href="{svc_url(r, s["slug"])}">{e(s["name"])}</a></li>' for s in items)
        blurb = items[0]["short"] if len(items) == 1 else {
            "install": "New wiring and upgrades for homes, commercial and industrial buildings.",
            "testing": "Certificates and reports for safety, insurance, sales and lettings.",
            "repairs": "Fast fault finding, and an electrician to make it safe when things go wrong.",
            "renew": "Lower bills and cleaner energy for homes and fleets.",
            "safety": "Systems that protect people and property and keep you connected.",
        }.get(gk, "")
        groups += (f'<article class="svc"><div class="svc-head"><div class="svc-icon">{icon(ik)}</div><h3>{e(glabel)}</h3></div>'
                   f'<p>{e(blurb)}</p><ul>{lis}</ul></article>')
    return f'''<section class="hero"><div class="wrap"><div>
<div class="eyebrow">Installation · Design · Testing</div>
<h1>Safe, certified electrical work across <em>London &amp; the East of England</em></h1>
<p class="lead">Qualified electricians for homes, landlords and businesses across Cambridgeshire, the East of England and Greater London. We install, design and test to BS 7671 and give you the right certificate for every job.</p>
<div class="ctas"><a href="{r}contact.html" class="btn btn-amber">Get a free quote</a>{wa_btn()}<a href="tel:{B["phone_tel"]}" class="btn btn-ghost">Call {B["phone"]}</a></div>
<ul class="hero-points"><li>{TICK}Free, fixed-price quotes</li><li>{TICK}Certificate with every job</li><li>{TICK}Domestic, commercial &amp; industrial</li><li>{TICK}Fully insured</li></ul></div>
<figure class="cert" aria-label="Example electrical installation condition report">
<div class="cert-top"><b>Electrical Installation Condition Report</b><span>Example</span></div>
<div class="cert-meta"><div><small>Property</small><strong>3-bed rental, Cambridge CB1</strong></div><div><small>Standard</small><strong>BS 7671 (IET Wiring Regs)</strong></div></div>
<div class="scroll"><table><thead><tr><th>Circuit</th><th>Zs (Ω)</th><th>IR (MΩ)</th><th>RCD (ms)</th><th>Result</th></tr></thead><tbody>
<tr><td>1 Sockets ring</td><td>0.42</td><td>&gt;999</td><td>18</td><td class="pass">✓</td></tr>
<tr><td>2 Lighting dn</td><td>0.88</td><td>&gt;999</td><td>21</td><td class="pass">✓</td></tr>
<tr><td>3 Cooker</td><td>0.31</td><td>450</td><td>19</td><td class="pass">✓</td></tr>
<tr><td>4 Shower</td><td>0.27</td><td>&gt;999</td><td>17</td><td class="pass">✓</td></tr>
</tbody></table></div>
<div class="cert-foot"><small>Next inspection due in 5 years</small><span class="stamp">SATISFACTORY</span></div></figure>
</div></section>
{trust_strip()}
<section class="band" id="who"><div class="wrap"><div class="band-head"><div class="eyebrow">Who we work for</div><h2>Electrical services for every kind of property</h2></div>
<div class="tabs" role="tablist" aria-label="Customer type">{tabs}</div>{panels}</div></section>
<section class="band band-alt" id="services"><div class="wrap"><div class="band-head"><div class="eyebrow">Our services</div>
<h2>Everything electrical, from design to certificate</h2><p class="lead">One team for the whole job. We can design the installation, fit it, test it and certify it.</p></div>
<div class="svc-grid">{groups}</div>
<div class="ctas"><a href="{r}services/index.html" class="btn btn-primary">See all services</a></div></div></section>
<section class="band" id="testing"><div class="wrap"><div class="band-head"><div class="eyebrow">Testing &amp; EICR</div><h2>What your electrical report means</h2>
<p class="lead">An Electrical Installation Condition Report (EICR) checks wiring, sockets, protective devices and earthing against the current wiring regulations. Anything we find is given one of four codes.</p></div>
<div class="test-grid">{CODES}{INTERVALS}</div></div></section>
<section class="band band-sky"><div class="wrap"><div class="band-head"><div class="eyebrow">How we work</div><h2>From first call to certificate</h2></div>{STEPS}</div></section>
<section class="band" id="areas"><div class="wrap"><div class="band-head"><div class="eyebrow">Areas we cover</div>
<h2>Based in Cambridgeshire, working across the East of England and London</h2><p class="lead">Can't see your town? We cover most of the region, so just ask.</p></div>{areas_grid(r)}</div></section>
{contact_section(r)}'''

def service_body(s):
    def body(r):
        g = next(gl for gk, gl, _ in GROUPS if gk == s["group"])
        secs = "".join(f"<section><h2>{e(h)}</h2><p>{e(p)}</p></section>" for h, p in s["sections"])
        codes = (f'<section><h2>Understanding your report</h2><p>Every issue on an EICR is given a code. Here\'s what they mean.</p>{CODES}</section>'
                 f'<section>{INTERVALS}</section>') if s.get("codes") else ""
        callout = f'<div class="callout"><b>{e(s["callout"][0])}</b><span>{e(s["callout"][1])}</span></div>' if s.get("callout") else ""
        rel = [(SVC[x]["name"], svc_url(r, x)) for x in s["related"]]
        areas = [(a["name"], area_url(r, a["slug"])) for a in AREAS]
        return (page_hero(r, g, s["h1"], e(s["intro"]), [("Services", f"{r}services/index.html"), (s["name"], None)], quote_hash="#" + s["slug"], wa_text=f"Hi National Electrical, I'd like a quote for {lc(s['name'])}.") +
                f'''<section class="band"><div class="wrap layout"><div class="prose">
<section><h2>What's included</h2>{checklist(s["includes"])}</section>{callout}{secs}{codes}{faq_block(s["faqs"])}
<section><h2>Related services</h2>{service_cards(r, s["related"])}</section></div>
<aside class="aside">{quote_card(r, "#" + s["slug"], f"Hi National Electrical, I'd like a quote for {lc(s['name'])}.")}{side_list("Areas we cover", areas)}</aside></div></section>''' +
                cta_band(r, f"Need {lc(s['name'])}?"))
    return body

def services_index(r):
    out = ""
    for gk, glabel, ik in GROUPS:
        items = [s["slug"] for s in SERVICES if s["group"] == gk]
        out += (f'<section class="band{" band-alt" if len(out) % 2 else ""}" style="padding-block:48px"><div class="wrap">'
                f'<div class="svc-head" style="margin-bottom:20px"><div class="svc-icon">{icon(ik)}</div><h2 style="font-size:1.6rem">{e(glabel)}</h2></div>'
                f'{service_cards(r, items)}</div></section>')
    return page_hero(r, "Our services", "Every electrical service, <em>one team</em>",
                     "Installation, design, testing, repairs, renewables and safety systems for homes, landlords and businesses.",
                     [("Services", None)]) + out + cta_band(r)

def customers_index(r):
    cards = "".join(f'<a class="card" href="{sec_url(r, s["slug"])}"><h3>{e(s["name"])}</h3><p>{e(s["intro"][:150].rsplit(" ", 1)[0])}…</p><span class="more">See how we help →</span></a>' for s in SECTORS)
    return (page_hero(r, "Who we help", "Electricians for <em>homes, landlords and businesses</em>",
                      "Every kind of customer has different needs. Choose yours to see the services we recommend.", [("Who we help", None)]) +
            f'<section class="band"><div class="wrap"><div class="cards">{cards}</div></div></section>' + cta_band(r))

def sector_body(s):
    def body(r):
        pts = "".join(f'<div class="value"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in s["points"])
        return (page_hero(r, "Who we help", s["h1"], e(s["intro"]), [("Who we help", f"{r}customers/index.html"), (s["name"], None)]) +
                f'<section class="band"><div class="wrap"><div class="values">{pts}</div></div></section>'
                f'<section class="band band-alt"><div class="wrap"><div class="band-head"><div class="eyebrow">Recommended services</div><h2>What we do for {e(s["name"].lower())}</h2></div>{service_cards(r, s["services"])}</div></section>'
                f'<section class="band band-sky"><div class="wrap"><div class="band-head"><div class="eyebrow">How we work</div><h2>From first call to certificate</h2></div>{STEPS}</div></section>' +
                contact_section(r, s["cta"]))
    return body

def areas_index(r):
    return (page_hero(r, "Areas we cover", "Electricians across <em>London &amp; the East of England</em>",
                      "Based in Cambridgeshire, we cover Suffolk, Norfolk, Essex, Hertfordshire, Bedfordshire and Greater London.", [("Areas", None)]) +
            f'<section class="band"><div class="wrap">{areas_grid(r)}</div></section>' + cta_band(r, "Not sure if we cover you?", "Call or send us your postcode and we'll let you know."))

def area_body(a):
    def body(r):
        groups = "".join(f'<div class="town-group"><h3>{e(g)}</h3><ul>' + "".join(f"<li>{e(t)}</li>" for t in ts) + "</ul></div>" for g, ts in a["towns"].items())
        pcs = "".join(f"<span>{p}</span>" for p in a["postcodes"])
        others = [(x["name"], area_url(r, x["slug"])) for x in AREAS if x["slug"] != a["slug"]]
        return (page_hero(r, "Areas we cover", f'Electricians in <em>{e(a["name"])}</em>', e(a["intro"]), [("Areas", f"{r}areas/index.html"), (a["name"], None)], wa_text=f"Hi National Electrical, I need an electrician in {a['name']}.") +
                f'''<section class="band"><div class="wrap layout"><div class="prose">
<section><h2>Where we work in {e(a["name"])}</h2><div class="town-groups">{groups}</div><div class="pc" style="margin-top:4px">{pcs}</div></section>
<section><h2>Local work</h2><p>{e(a["local"])}</p></section>
<section><h2>Popular services in {e(a["name"])}</h2>{service_cards(r, a["services"])}</section>
<section><h2>Every job tested and certified</h2>{checklist(["Free, fixed-price quotes", "Qualified to BS 7671", "Part P notification handled", "Certificate with every job", "Domestic, commercial & industrial", "Fully insured"])}</section>
</div><aside class="aside">{quote_card(r, "", f"Hi National Electrical, I need an electrician in {a['name']}.")}{side_list("Other areas", others)}</aside></div></section>''' + cta_band(r, f"Need an electrician in {a['name']}?"))
    return body

def about_body(r):
    return (page_hero(r, "About us", f'About <em>{e(B["name"])}</em>',
                      "An electrical contractor based in Cambridgeshire, providing installation, design and testing for homes, landlords and businesses across the East of England and Greater London.",
                      [("About", None)]) +
            f'''<section class="band"><div class="wrap layout"><div class="prose">
<section><h2>Who we are</h2><p>{e(B["name"])} was set up to offer one dependable team for every electrical job, from a landlord's EICR to the design and installation of a commercial fit-out. We test and certify everything we do, and we explain what we've found in plain English.</p>
<p>We're based in Cambridgeshire and work across the East of England and Greater London, for homeowners, landlords, letting agents, businesses and main contractors. Whatever the size of the job, you deal with qualified electricians who take pride in safe, tidy work.</p></section>
<section><h2>What we stand for</h2><div class="values">
<div class="value"><h3>Safety first</h3><p>Every installation is designed and tested to BS 7671. If we find something dangerous, we tell you and make it safe.</p></div>
<div class="value"><h3>Honest advice</h3><p>We'll tell you if you don't need the work, and we'll always explain the options and the prices before we start.</p></div>
<div class="value"><h3>Tidy, reliable work</h3><p>We turn up when we say we will, protect your property and leave it clean.</p></div>
<div class="value"><h3>Proper paperwork</h3><p>The right certificate for every job, and Part P notification handled for you.</p></div></div></section>
<section><h2>Qualifications and accreditation</h2>{checklist(["Qualified to the current IET Wiring Regulations (BS 7671)", "Inspection and testing qualified", "Part P notification for Building Regulations", "Public liability insurance"] + ([B["scheme"]] if B["scheme"] else []))}</section>
<section><h2>How we work</h2>{STEPS}</section>
</div><aside class="aside">{quote_card(r)}{side_list("Who we help", [(s["name"], sec_url(r, s["slug"])) for s in SECTORS])}</aside></div></section>''' + cta_band(r))

def faq_body(r):
    return (page_hero(r, "FAQs", "Frequently asked <em>questions</em>", "Answers to the questions we're asked most often. Can't find yours? Just call us.", [("FAQs", None)]) +
            f'''<section class="band"><div class="wrap layout"><div class="prose">{faq_block(FAQS_GENERAL, "General")}
{faq_block([q for s in SERVICES if s["group"] == "testing" for q in s["faqs"]], "Testing and EICRs")}
{faq_block([q for s in SERVICES if s["group"] in ("install", "renew") for q in s["faqs"]][:6], "Installation, EV and solar")}
<section><h2>What the EICR codes mean</h2>{CODES}</section></div>
<aside class="aside">{quote_card(r)}</aside></div></section>''' + cta_band(r))

def contact_body(r):
    return (page_hero(r, "Contact", "Get a <em>free quote</em>", f"Call {B['phone']} or send us the details below. We reply to every enquiry within one working day.", [("Contact", None)], ctas=False) +
            contact_section(r) +
            f'<section class="band"><div class="wrap"><div class="band-head"><div class="eyebrow">Areas we cover</div><h2>Where we work</h2></div>{areas_grid(r)}</div></section>')

def thanks_body(r):
    return (page_hero(r, "Enquiry sent", "Thanks, we've got your <em>enquiry</em>",
                      f"We'll be in touch within one working day. If it's urgent, call us on {B['phone']}.", [("Thank you", None)], ctas=False) +
            f'<section class="band"><div class="wrap"><a href="{home_url(r)}" class="btn btn-primary">Back to the homepage</a></div></section>')

def privacy_body(r):
    return (page_hero(r, "Privacy", "Privacy <em>policy</em>", "How we collect and use your personal information.", [("Privacy policy", None)], ctas=False) +
            f'''<section class="band"><div class="wrap"><div class="legal-text">
<p>{e(B["name"])} ("we", "us") is the data controller for personal information collected through this website. Contact us at {B["email"]} or {B["phone"]} with any questions.</p>
<h2>What we collect</h2><ul><li>Details you send through our quote form or by email or phone: name, phone number, email address, postcode and details of the job.</li><li>Details needed to carry out work: property address, access arrangements and, for landlords, tenant contact details you give us.</li></ul>
<h2>How we use it</h2><p>We use your information to reply to your enquiry, quote for and carry out work, issue certificates and invoices, and remind you when testing is due if you've asked us to. Our lawful bases are taking steps to enter a contract with you, our legitimate interests in running the business, and legal obligations such as keeping certificates and tax records.</p>
<h2>Who we share it with</h2><p>We only share your information where needed to do the work: for example, with Building Control or our competent person scheme for Part P notification, your network operator for EV charger or solar registration, and our accountant. We never sell your data.</p>
<h2>How long we keep it</h2><p>Enquiries that don't go ahead are deleted after 12 months. Job records, certificates and invoices are kept for at least six years.</p>
<h2>Your rights</h2><p>You can ask to see, correct or delete the information we hold about you, or object to how we use it. If you're unhappy with how we've handled your data, you can complain to the Information Commissioner's Office at ico.org.uk.</p>
<h2>Cookies</h2><p>This website doesn't use advertising or tracking cookies. Fonts are loaded from Google Fonts.</p>
<p><small>Last updated {date.today().strftime("%B %Y")}.</small></p>
</div></div></section>''')

def notfound_body(r):
    return (page_hero(r, "Page not found", "We can't find <em>that page</em>", "It may have moved. Try one of these instead.", [("Not found", None)], ctas=False) +
            f'<section class="band"><div class="wrap">{service_cards(r, ["eicr", "rewiring", "consumer-unit-upgrades", "emergency-electrician"])}</div></section>')

# ------------------------------------------------------------------ build
def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    for f in (HERE / "assets").iterdir():
        shutil.copy(f, OUT / "assets" / f.name)
    shutil.copy(HERE / "_headers", OUT / "_headers")

    region = "Cambridgeshire, East of England & London"
    write("index.html", f"Electricians in {region} | {B['name']}",
          f"Electrical installation, design and testing for homes, landlords and businesses across {B['region_line']}. Free quotes: {B['phone']}.",
          home_body, jsonld=local_business_schema())
    write("services/index.html", f"Electrical services | {B['name']}", "All our electrical services: installation, rewiring, EICR testing, design, EV chargers, solar, fire alarms and emergency repairs.", services_index, "services")
    for s in SERVICES:
        write(f"services/{s['slug']}.html", f"{s['name']} | {B['name']}", s["meta"], service_body(s), "services")
    write("customers/index.html", f"Who we help | {B['name']}", "Electrical services for homeowners, landlords, businesses and industrial customers.", customers_index, "customers")
    for s in SECTORS:
        write(f"customers/{s['slug']}.html", f"Electricians for {lc(s['name'])} | {B['name']}", s["meta"], sector_body(s), "customers")
    write("areas/index.html", f"Areas we cover | {B['name']}", f"Electricians covering {B['region_line']}.", areas_index, "areas")
    for a in AREAS:
        write(f"areas/{a['slug']}.html", f"Electricians in {a['name']} | {B['name']}", a["meta"], area_body(a), "areas")
    write("about.html", f"About us | {B['name']}", f"About {B['name']}, electrical contractors in {B['region_line']}.", about_body, "about")
    write("faq.html", f"FAQs | {B['name']}", "Answers to common questions about electrical work, EICRs, certificates and quotes.", faq_body, "faq",
          jsonld={"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
              {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS_GENERAL]})
    write("contact.html", f"Contact us | {B['name']}", f"Get a free electrical quote. Call {B['phone']} or send us your job details.", contact_body, "contact", jsonld=local_business_schema())
    write("thanks.html", f"Thank you | {B['name']}", "Thanks for your enquiry.", thanks_body)
    write("privacy.html", f"Privacy policy | {B['name']}", f"Privacy policy for {B['name']}.", privacy_body)
    write("404.html", f"Page not found | {B['name']}", "Page not found.", notfound_body)

    today = date.today().isoformat()
    urls = "".join(f"<url><loc>{B['url']}/{'' if p == 'index.html' else p}</loc><lastmod>{today}</lastmod></url>" for p in PAGES if p != "privacy.html")
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>', encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {B['url']}/sitemap.xml\n", encoding="utf-8")

    # Preview entry for the Claude artifact (same home page, without the document wrapper)
    (HERE.parent / "preview-home.html").write_text(
        page("index.html", B["name"], "Electricians in Cambridgeshire, the East of England and Greater London.", home_body, artifact=True),
        encoding="utf-8")
    print(f"Built {len(PAGES) + 2} pages into {OUT}")

if __name__ == "__main__":
    main()
