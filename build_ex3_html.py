# -*- coding: utf-8 -*-
# Exam 3 (Gravitation, Oscillations, Waves, Sound) — same layout as ex2.html.
# Data: ex3_data/<Section>_problems.json  [n, q, ans, intro, steps]
#       ex3_data/<Section>_sections.json  topic tabs
#       ex3_data/figures.json             {n: "ex3_fig/<file>"}
import json
from pathlib import Path

from build_ex2 import CSS
import ex3_top_render as ex3_top

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "ex3_data"
BIG = [("Gravitation", "Гравитация"), ("Oscillations", "Колебания"),
       ("Waves", "Волны"), ("Sound", "Звук")]

problems, topics = [], []
for key, _ in BIG:
    problems += json.loads((DATA_DIR / f"{key}_problems.json").read_text(encoding="utf-8"))
    topics += json.loads((DATA_DIR / f"{key}_sections.json").read_text(encoding="utf-8"))
by_n = {p[0]: p for p in problems}
FIGS = {int(k): v for k, v in json.loads((DATA_DIR / "figures.json").read_text(encoding="utf-8")).items()}
RAW = {p["n"]: p for p in json.loads((DATA_DIR / "raw.json").read_text(encoding="utf-8"))}
# Badge always shows the official answer from the exam source.
for n, p in by_n.items():
    if RAW[n].get("answer"):
        p[2] = RAW[n]["answer"]
assert set(by_n) == set(RAW), sorted(set(RAW) ^ set(by_n))
ids = [t["id"] for t in topics]
assert len(ids) == len(set(ids)), ids
assert sorted(n for t in topics for n in t["nums"]) == sorted(RAW), "topic tabs must cover every problem once"

EXTRA_CSS = """
.back{display:inline-flex; align-items:center; gap:6px; color:var(--accent); text-decoration:none; font-weight:600; font-size:15px; margin-bottom:10px;}
.back:hover{text-decoration:underline;}
.fig{display:block; max-width:100%; max-height:320px; margin:0 auto 14px; border-radius:10px; background:#fff; padding:6px;}
"""


def prob_details(p):
    n, q, ans, intro, steps = p
    lis = "".join(
        f'<li><div class="eqwrap">\\({eq}\\)</div><div class="stepnote">{note}</div></li>'
        for eq, note in steps
    )
    fig = f'<img class="fig" loading="lazy" src="{FIGS[n]}" alt="Рисунок к P{n}"/>' if n in FIGS else ""
    return (
        f'<details class="prob" id="p{n}"><summary><span class="pn mono">P{n}</span>'
        f'<span class="ptext">{q}</span>'
        f'<span class="ans-badge mono">{ans}</span></summary>'
        f'<div class="solution">{fig}<p class="step-intro">{intro}</p>'
        f'<ol class="sol-steps">{lis}</ol></div></details>'
    )


sol = ['<p>Каждая задача свёрнута — нажми, чтобы увидеть шаги «как для ребёнка». Ответ в жёлтом бейдже справа. '
       'P87, P105, P106, P122, P125 убраны из экзамена — их здесь нет.</p>']
for key, title in BIG:
    nums = sorted(n for n, r in RAW.items() if r["section"] == key)
    sol.append(f'<div class="sec-divider"><h3>{title}</h3><span class="range mono">P{nums[0]}–P{nums[-1]}</span></div>')
    sol += [prob_details(by_n[n]) for n in nums]

cheat_story = r"""
  <p>Открой перед экзаменом. Подробные формулы — во вкладках, тут самое нужное.</p>
  <h3>Константы</h3>
  <div class="kid">G = 6.67·10⁻¹¹ Н·м²/кг². g = 9.8 м/с². Звук в воздухе ≈ 343 м/с. I₀ = 10⁻¹² Вт/м². км → м: <b>×1000</b>. см → м: <b>÷100</b>.</div>
  <h3>Гравитация</h3>
  <div class="fbox"><div class="eqwrap">\[F=\dfrac{GMm}{r^2},\quad g=\dfrac{GM}{R^2},\quad U=-\dfrac{GMm}{r}\]</div><div class="flegend">Сила, ускорение на поверхности, потенциальная энергия (всегда с минусом).</div></div>
  <div class="fbox"><div class="eqwrap">\[v_{\text{orb}}=\sqrt{\dfrac{GM}{r}},\quad v_{\text{esc}}=\sqrt{\dfrac{2GM}{R}},\quad T^2=\dfrac{4\pi^2 r^3}{GM}\]</div><div class="flegend">Орбита, вторая космическая, закон Кеплера.</div></div>
  <h3>Колебания</h3>
  <div class="fbox"><div class="eqwrap">\[\omega=\sqrt{\dfrac{k}{m}},\quad T=2\pi\sqrt{\dfrac{L}{g}},\quad x=A\cos(\omega t+\varphi)\]</div><div class="flegend">Пружина, маятник, закон движения. v_max = Aω, a_max = Aω².</div></div>
  <h3>Волны</h3>
  <div class="fbox"><div class="eqwrap">\[v=\lambda f,\quad v=\sqrt{\dfrac{T}{\mu}},\quad y=A\sin(kx-\omega t),\ k=\dfrac{2\pi}{\lambda}\]</div><div class="flegend">Скорость волны, струна, уравнение бегущей волны.</div></div>
  <h3>Звук</h3>
  <div class="fbox"><div class="eqwrap">\[\beta=10\log_{10}\dfrac{I}{I_0},\quad I=\dfrac{P}{4\pi r^2},\quad f'=f\,\dfrac{v\pm v_o}{v\mp v_s}\]</div><div class="flegend">Децибелы, интенсивность от точечного источника, Доплер (сближение → частота выше).</div></div>
  <div id="allformulas"></div>
"""

data_items = [
    {"id": "cheat", "title": "Шпаргалка", "range": "все формулы", "isCheatSheet": True,
     "formulas": [], "problems": [], "story": cheat_story},
    {"id": "top", "title": "Top 15 formulas", "range": "ranked by frequency · 145 problems", "isTop": True,
     "formulas": [], "problems": [], "story": ex3_top.build_story(by_n)},
    {"id": "solutions", "title": "Все решения", "range": f"{len(problems)} задач · P1–P150", "isSolutionsTab": True,
     "formulas": [], "problems": [], "story": "".join(sol)},
]
for t in topics:
    data_items.append({
        "id": t["id"], "title": t["title"], "range": t["range"],
        "formulas": t["formulas"], "story": t["story"],
        "problems": [[n, by_n[n][1], by_n[n][2]] for n in t["nums"] if n in by_n],
    })

data_js = json.dumps(data_items, ensure_ascii=False).replace("</", "<\\/")

template = (ROOT / "build_ex2_html.py").read_text(encoding="utf-8")
# Reuse the ex2 page script verbatim: everything between "<script>\nconst DATA" and "</script>".
js_start = template.index("const tabs = document.getElementById('tabs');")
js_end = template.index("</script>\n</body>")
page_js = template[js_start:js_end].replace("{{", "{").replace("}}", "}").replace("\\\\", "\\")

page_js = page_js.replace("if(sec.isSolutionsTab) qn = '✓';",
                          "if(sec.isSolutionsTab) qn = '✓';\n  if(sec.isTop) qn = '🔥';")
assert "sec.isTop" in page_js

html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>PHYS161 · Exam 3</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="vendor/katex/katex.min.css"/>
<script defer src="vendor/katex/katex.min.js"></script>
<script defer src="vendor/katex/auto-render.min.js"></script>
<style>
{CSS}
{EXTRA_CSS}
{ex3_top.CSS}
</style>
</head>
<body>
<div class="wrap">
  <div>
    <a class="back" href="index.html">← Все мидки</a>
    <div class="eyebrow">PHYS161 · Exam 3 · Конспект как для ребёнка</div>
    <h1>Гравитация, колебания, волны, звук — каждая задача по шагам</h1>
  </div>
  <div class="tabs" id="tabs"></div>
  <div id="panels"></div>
  <footer>Источник: PHYS161_Exam3 (omgaXD/pt-nu-phys161) · {len(problems)} задач разобраны по шагам</footer>
</div>
<script>
const DATA = {data_js};

{page_js}
{ex3_top.JS}
</script>
</body>
</html>
"""

out = ROOT / "ex3.html"
out.write_text(html, encoding="utf-8")
print("Wrote", out, out.stat().st_size, "bytes;", len(problems), "problems,", len(topics), "topic tabs")
