# -*- coding: utf-8 -*-
# Exam 4 (Temperature and heat, Kinetic theory, 1st and 2nd laws) — same layout as ex2.html.
# Data: ex4_data/<Section>_problems.json  [n, q, ans, intro, steps]
#       ex4_data/plan.json                {n: {given, find, formulas}}
#       ex4_data/<Section>_sections.json  topic tabs
#       ex4_data/figures.json             {n: "ex4_fig/<file>"}
import html
import json
from pathlib import Path

from build_ex2 import CSS
from pretty_text import pretty
import ex4_top_render as ex3_top
import ex4_nav

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "ex4_data"
BIG = [("Heat", "Температура и тепло"), ("Kinetic", "Кинетическая теория газов"),
       ("FirstLaw", "Первый закон термодинамики"), ("SecondLaw", "Второй закон термодинамики")]

problems, topics = [], []
for key, _ in BIG:
    problems += json.loads((DATA_DIR / f"{key}_problems.json").read_text(encoding="utf-8"))
    topics += json.loads((DATA_DIR / f"{key}_sections.json").read_text(encoding="utf-8"))
by_n = {p[0]: p for p in problems}
# Short restatements are plain text from the exam: render ^ and _ as real super/subscripts.
for _p in problems:
    if "<" not in _p[1]:
        _p[1] = pretty(_p[1])
FIGS = {int(k): v for k, v in json.loads((DATA_DIR / "figures.json").read_text(encoding="utf-8")).items()}
RAW = {p["n"]: p for p in json.loads((DATA_DIR / "raw.json").read_text(encoding="utf-8"))}
# Badge always shows the official answer from the exam source.
for n, p in by_n.items():
    if RAW[n].get("answer"):
        p[2] = pretty(RAW[n]["answer"])
assert set(by_n) == set(RAW), sorted(set(RAW) ^ set(by_n))
ids = [t["id"] for t in topics]
assert len(ids) == len(set(ids)), ids
assert sorted(n for t in topics for n in t["nums"]) == sorted(RAW), "topic tabs must cover every problem once"

# What the student sees before opening the solution: {n: {given, find, formulas}}.
PLANS = {int(k): v for k, v in json.loads((DATA_DIR / "plan.json").read_text(encoding="utf-8")).items()}
assert set(PLANS) == set(RAW), sorted(set(RAW) ^ set(PLANS))
# Plain-language explanations: {n: {kid, notes (one per solution step), check}}.
KID = {int(k): v for k, v in json.loads((DATA_DIR / "kid.json").read_text(encoding="utf-8")).items()}
assert set(KID) == set(RAW), sorted(set(RAW) ^ set(KID))
# Short routes: {n: {trick, given, find, formulas, steps: [[tex, kid_note]], kid, check}}.
# A problem listed here is shown with its short route instead of the long one.
_short_file = DATA_DIR / "short.json"
SHORT = {int(k): v for k, v in json.loads(_short_file.read_text(encoding="utf-8")).items()} if _short_file.exists() else {}
assert set(SHORT) <= set(RAW), sorted(set(SHORT) - set(RAW))

EXTRA_CSS = """
.back{display:inline-flex; align-items:center; gap:6px; color:var(--accent); text-decoration:none; font-weight:600; font-size:15px; margin-bottom:10px;}
.back:hover{text-decoration:underline;}
.fig{display:block; max-width:100%; max-height:320px; margin:0 auto 14px; border-radius:10px; background:#fff; padding:6px;}
.task{border:1px solid var(--rule); border-radius:14px; background:var(--surface); padding:16px; display:flex; flex-direction:column; gap:14px; min-width:0; scroll-margin-top:12px; margin-bottom:14px;}
.task.solved{opacity:.6;}
.task-head{display:flex; align-items:center; gap:10px;}
.task-head .pn{color:var(--accent); font-weight:700; font-size:16px;}
.done{margin-left:auto; display:inline-flex; align-items:center; gap:6px; font-size:15px; cursor:pointer; user-select:none; padding:4px 10px; border:1px solid var(--rule); border-radius:999px;}
.done input{width:18px; height:18px; accent-color:var(--accent); margin:0;}
.task.solved .done{border-color:var(--accent); color:var(--accent); font-weight:600;}
.stmt{font-size:17px; line-height:1.6;}
.plan{display:grid; gap:12px;}
.pl{background:var(--story-bg); border:1px solid var(--rule); border-radius:10px; padding:10px 14px; min-width:0;}
.pl .lbl{font-weight:700; font-size:13px; letter-spacing:.06em; text-transform:uppercase; color:var(--accent); margin-bottom:6px;}
.pl ul, .pl ol{margin:0; padding:0; list-style:none; display:flex; flex-direction:column; gap:12px;}
.pl li{min-width:0;}
.pl .f{overflow-x:auto; -webkit-overflow-scrolling:touch; padding:2px 0;}
.pl .f .katex{font-size:1.3em;}
.pl .why{color:#bdbdbd; font-size:15.5px; line-height:1.45; margin-top:2px;}
.pl.find{background:var(--accent-2-soft);}
.pl.formulas li{border-top:1px solid var(--rule); padding-top:10px;}
.pl.formulas li:first-child{border-top:none; padding-top:0;}
.pl .stepno{font-family:"IBM Plex Mono",monospace; font-size:12px; letter-spacing:.06em; text-transform:uppercase; color:var(--ink-muted); margin-bottom:4px;}
.pl.formulas .f .katex{font-size:1.35em;}
.pl .f .katex, .pl .f .katex-html{white-space:nowrap;}
@media (max-width:520px){ .task{padding:12px;} .pl{padding:10px;} .stmt{font-size:16px;} }
details.reveal{border:2px dashed var(--accent); border-radius:12px; overflow:hidden;}
details.reveal > summary{list-style:none; cursor:pointer; padding:12px 16px; font-weight:700; color:var(--accent); text-align:center;}
details.reveal > summary::-webkit-details-marker{display:none;}
details.reveal[open] > summary{border-bottom:1px dashed var(--accent);}
details.reveal[open] > summary .show{display:none;}
details.reveal:not([open]) > summary .hide{display:none;}
.ansline{margin-top:14px; font-size:17px;}
.kidbox{font-size:17px; line-height:1.65; background:var(--story-bg); border-left:2px solid #ffffff; padding:12px 14px;}
.trick{font-size:16px; line-height:1.6; padding:12px 14px; border:1px solid #ffffff; margin-top:10px;}
.derive{margin-top:8px; padding:8px 10px; border-left:2px solid #8c8c8c; background:#0f0f0f;}
.derive .dl{font-size:12px; letter-spacing:.06em; text-transform:uppercase; color:var(--ink-muted); margin-bottom:4px;}
.derive .dline{display:flex; flex-wrap:wrap; align-items:baseline; gap:4px 12px; padding:3px 0;}
.derive .dline .f{overflow-x:auto; max-width:100%;}
.derive .dn{font-size:14px; color:#bdbdbd;}
.trick .lbl{font-weight:700; font-size:13px; letter-spacing:.06em; text-transform:uppercase; margin-bottom:6px;}
.kidbox .lbl{font-weight:700; font-size:13px; letter-spacing:.06em; text-transform:uppercase; margin-bottom:6px;}
.checkline{margin-top:12px; font-size:16px; line-height:1.55; color:#d0d0d0;}
ol.sol-steps{list-style:none; padding-left:0 !important;}
ol.sol-steps .stepno{font-family:"IBM Plex Mono",monospace; font-size:12px; letter-spacing:.06em; text-transform:uppercase; color:var(--ink-muted); margin-bottom:4px;}
ol.sol-steps li .stepnote{color:#cfcfcf !important; font-size:16.5px !important; line-height:1.6 !important;}
.progress{position:sticky; top:0; z-index:5; background:var(--bg); padding:10px 0; display:flex; align-items:center; gap:12px;}
.progress .pbar{flex:1; height:10px; border-radius:5px; background:var(--accent-soft); overflow:hidden;}
.progress .pbar i{display:block; height:100%; width:0; background:var(--accent); transition:width .3s;}
.progress b{font-family:"IBM Plex Mono",monospace; font-size:15px; white-space:nowrap;}
"""

PROGRESS_JS = r"""
(function(){
  var KEY = 'ex4-solved';
  var done = {};
  try { (JSON.parse(localStorage.getItem(KEY) || '[]')).forEach(function(n){ done[n] = true; }); } catch(e) {}
  var boxes = document.querySelectorAll('.done input');
  function paint(){
    var c = 0;
    boxes.forEach(function(b){
      var on = !!done[b.dataset.n];
      b.checked = on;
      b.closest('.task').classList.toggle('solved', on);
      if (on) c++;
    });
    document.querySelectorAll('.progress b').forEach(function(el){ el.textContent = c + ' / ' + boxes.length; });
    document.querySelectorAll('.progress .pbar i').forEach(function(el){ el.style.width = (100 * c / boxes.length) + '%'; });
  }
  boxes.forEach(function(b){
    b.addEventListener('change', function(){
      if (b.checked) done[b.dataset.n] = true; else delete done[b.dataset.n];
      try { localStorage.setItem(KEY, JSON.stringify(Object.keys(done))); } catch(e) {}
      paint();
    });
  });
  paint();
})();
"""


def derive_html(lines):
    """'Откуда взялась': the base formula this one comes from and what was done to it."""
    if not lines:
        return ""
    rows = "".join(f'<div class="dline"><span class="f">\\({t}\\)</span><span class="dn">{note}</span></div>' for t, note in lines)
    return f'<div class="derive"><div class="dl">Откуда взялась</div>{rows}</div>'


def statement(n):
    """Full problem text from the exam, without the official answer in parentheses at the end."""
    t = RAW[n]["text"].strip()
    if t.endswith(")"):
        depth = 0
        for i in range(len(t) - 1, -1, -1):
            depth += {")": 1, "(": -1}.get(t[i], 0)
            if depth == 0:
                t = t[:i].rstrip()
                break
    return pretty(t)


def prob_details(p):
    n, q, ans, intro, steps = p
    plan = PLANS[n]
    kid = KID[n]
    assert len(kid["notes"]) == len(steps), n
    pairs = [(eq, note) for (eq, _), note in zip(steps, kid["notes"])]
    trick = ""
    if n in SHORT:
        s = SHORT[n]
        plan = {"given": s["given"], "find": s["find"], "formulas": s["formulas"]}
        kid = {"kid": s["kid"], "check": s["check"]}
        pairs = [tuple(x) for x in s["steps"]]
        trick = f'<div class="trick"><div class="lbl">⚡ Короткий путь</div>{s["trick"]}</div>'
    lis = "".join(
        f'<li><div class="stepno">Шаг {i}</div><div class="eqwrap">\\({eq}\\)</div><div class="stepnote">{note}</div></li>'
        for i, (eq, note) in enumerate(pairs, 1)
    )
    given = "".join(f'<li><div class="f">\\({s}={v}\\)</div><div class="why">{why}</div></li>' for s, v, why in plan["given"])
    find = "".join(f'<li><div class="f">\\({s}\\)</div><div class="why">{why}</div></li>' for s, why in plan["find"])
    derive = SHORT.get(n, {}).get("derive", {})
    forms = "".join(f'<li><div class="stepno">Шаг {i}</div><div class="f">\\(\\displaystyle {f}\\)</div><div class="why">{why}</div>'
                    f'{derive_html(derive.get(str(i - 1)))}</li>'
                    for i, (f, why) in enumerate(plan["formulas"], 1))
    fig = f'<img class="fig" loading="lazy" src="{FIGS[n]}" alt="Рисунок к P{n}"/>' if n in FIGS else ""
    return (
        f'<div class="task" id="p{n}">'
        f'<div class="task-head"><span class="pn mono">P{n}</span>'
        f'<label class="done"><input type="checkbox" data-n="{n}"/> Решил</label></div>'
        f'{fig}<div class="stmt">{statement(n)}</div>'
        f'<div class="kidbox"><div class="lbl">🧸 Простыми словами</div>{kid["kid"]}</div>'
        f'{trick}<div class="plan">'
        f'<div class="pl given"><div class="lbl">Дано</div><ul>{given}</ul></div>'
        f'<div class="pl find"><div class="lbl">Найти</div><ul>{find}</ul></div>'
        f'<div class="pl formulas"><div class="lbl">Формулы по порядку</div><ol>{forms}</ol></div>'
        f'</div>'
        f'<details class="reveal"><summary><span class="show">👀 Показать решение</span><span class="hide">Скрыть решение</span></summary>'
        f'<div class="solution"><ol class="sol-steps">{lis}</ol>'
        f'<div class="ansline">Ответ: <span class="ans-badge mono">{ans}</span></div>'
        f'<div class="checkline">🔎 <b>Проверь себя:</b> {kid["check"]}</div></div></details>'
        f'</div>'
    )


sol = ['<p>У каждой задачи сразу видно, что <b>дано</b>, что <b>найти</b> и какие <b>формулы</b> нужны по порядку. '
       'Попробуй решить сам, а потом нажми «Показать решение» и сверься. Решил — ставь галочку, прогресс сохраняется в браузере.</p>'
       '<div class="progress"><span>Решено</span><div class="pbar"><i></i></div><b>0 / 150</b></div>']
for key, title in BIG:
    nums = sorted(n for n, r in RAW.items() if r["section"] == key)
    sol.append(f'<div class="sec-divider"><h3>{title}</h3><span class="range mono">P{nums[0]}–P{nums[-1]}</span></div>')
    sol += [prob_details(by_n[n]) for n in nums]

cheat_story = r"""
  <p>Открой перед экзаменом. Подробные формулы — во вкладках, тут самое нужное.</p>
  <h3>Константы и единицы</h3>
  <div class="kid">R = 8.314 Дж/(моль·К). k = 1.38·10⁻²³ Дж/К. N_A = 6.022·10²³. σ = 5.67·10⁻⁸ Вт/(м²·К⁴). 1 атм = 101325 Па. 1 л = 10⁻³ м³. <b>T в кельвинах: T = t°C + 273.15</b>.</div>
  <h3>Температура и тепло</h3>
  <div class="fbox"><div class="eqwrap">\[Q=mc\Delta T,\quad Q=mL,\quad \Delta L=\alpha L_0\Delta T,\quad \sum Q=0\]</div><div class="flegend">Нагрев, плавление/кипение, расширение, смешивание (сколько отдал горячий — столько получил холодный).</div></div>
  <div class="fbox"><div class="eqwrap">\[H=\dfrac{kA\,\Delta T}{L},\quad P=e\sigma A T^4\]</div><div class="flegend">Теплопроводность и излучение (T в кельвинах!).</div></div>
  <h3>Газы</h3>
  <div class="fbox"><div class="eqwrap">\[pV=nRT=Nk_BT,\quad \overline{K}=\tfrac32 k_B T,\quad v_{\text{rms}}=\sqrt{\dfrac{3RT}{M}}\]</div><div class="flegend">Уравнение газа, средняя кинетическая энергия молекулы, среднеквадратичная скорость (M в кг/моль).</div></div>
  <h3>Первый закон</h3>
  <div class="fbox"><div class="eqwrap">\[\Delta U=Q-W,\quad W=p\Delta V,\quad W_{T}=nRT\ln\dfrac{V_2}{V_1},\quad \Delta U=nC_V\Delta T\]</div><div class="flegend">Энергия, работа при p = const, при T = const, внутренняя энергия.</div></div>
  <div class="fbox"><div class="eqwrap">\[C_V=\tfrac32R,\quad C_p=\tfrac52R,\quad \Delta U=\tfrac32\,nR\,\Delta T,\quad Q_V=\tfrac32\,nR\,\Delta T,\quad Q_p=\tfrac52\,nR\,\Delta T\]</div><div class="flegend"><b>Одноатомный газ</b> (гелий, неон, аргон). Двухатомный (O₂, N₂, воздух): C<sub>V</sub> = 5/2·R, C<sub>p</sub> = 7/2·R.</div></div>
  <div class="fbox"><div class="eqwrap">\[V=\text{const}:\ W=0,\ Q=\Delta U\qquad T=\text{const}:\ \Delta U=0,\ Q=W\qquad \text{адиабата}:\ Q=0,\ \Delta U=-W\qquad \text{цикл}:\ \Delta U=0\]</div><div class="flegend">Какой процесс — то и обнуляется. Закрытый сосуд = объём не меняется = работы нет, всё тепло идёт на нагрев.</div></div>
  <div class="fbox"><div class="eqwrap">\[pV^{\gamma}=\text{const},\quad TV^{\gamma-1}=\text{const},\quad \gamma=\tfrac53\ (\text{одноатомный}),\ \gamma=1.4\ (\text{двухатомный})\]</div><div class="flegend">Адиабата (тепло не входит и не выходит). Выучи как правило.</div></div>
  <h3>Второй закон</h3>
  <div class="fbox"><div class="eqwrap">\[e=\dfrac{W}{Q_h}=1-\dfrac{Q_c}{Q_h},\quad e_{\text{Carnot}}=1-\dfrac{T_c}{T_h},\quad \Delta S=\dfrac{Q}{T}\]</div><div class="flegend">КПД двигателя, КПД Карно, энтропия.</div></div>
  <div class="fbox"><div class="eqwrap">\[K=\dfrac{Q_c}{W},\quad K_{\text{Carnot}}=\dfrac{T_c}{T_h-T_c},\quad Q_h=Q_c+W,\quad \Delta S=mc\ln\dfrac{T_2}{T_1},\quad Q=mL_c\]</div><div class="flegend">Холодильник (K — сколько тепла забрал на 1 Дж работы), энергия цикла, энтропия при нагреве, тепло сгорания топлива (L<sub>c</sub> — сколько Дж даёт 1 кг).</div></div>
  <h3>Вспомогательные формулы (механика, геометрия, моли)</h3>
  <div class="kid">Они не про тепло, но встречаются внутри задач. Их тоже надо знать.</div>
  <div class="fbox"><div class="eqwrap">\[A=\pi r^2=\dfrac{\pi d^2}{4},\quad V_{\text{шар}}=\tfrac43\pi r^3,\quad V_{\text{куб}}=a^3,\quad V_{\text{цилиндр}}=A\cdot h\]</div><div class="flegend">Площадь круга (r — радиус, d — диаметр), объём шара, куба, цилиндра. Размеры в метрах.</div></div>
  <div class="fbox"><div class="eqwrap">\[F_g=mg,\quad p=\dfrac{F}{A}\ \ (\text{поршень: } pA=mg),\quad p=p_0+\rho g h\]</div><div class="flegend">Вес; давление = сила ÷ площадь (поршень держит груз, когда сила газа pA равна весу mg); давление на глубине h под водой.</div></div>
  <div class="fbox"><div class="eqwrap">\[\rho=\dfrac{m}{V},\quad E_{\text{пот}}=mgh,\quad E_{\text{кин}}=\dfrac{mv^2}{2},\quad E=P\cdot t\]</div><div class="flegend">Плотность; энергия падения и движения; энергия = мощность × время (Вт × с = Дж).</div></div>
  <div class="fbox"><div class="eqwrap">\[n=\dfrac{m}{M},\quad N=n\cdot N_A,\quad m_0=\dfrac{M}{N_A}\]</div><div class="flegend">Моли из массы (M — молярная масса), число молекул, масса одной молекулы.</div></div>
  <div id="allformulas"></div>
"""

data_items = [
    {"id": "cheat", "title": "Шпаргалка", "range": "все формулы", "isCheatSheet": True,
     "formulas": [], "problems": [], "story": cheat_story},
    {"id": "top", "title": "Top 15 formulas", "range": f"ranked by frequency · {len(problems)} problems", "isTop": True,
     "formulas": [], "problems": [], "story": ex3_top.build_story(by_n)},
    {"id": "solutions", "title": "Все задачи", "range": f"{len(problems)} задач · P1–P150", "isSolutionsTab": True,
     "formulas": [], "problems": [], "story": "".join(sol)},
]
def topic_story(nums):
    """The formulas the problems of this topic actually use (from their 'Формулы по порядку'), most used first."""
    seen = {}
    for n in nums:
        src = SHORT.get(n) or PLANS[n]
        der = src.get("derive", {})
        for i, (tex, note) in enumerate(src["formulas"]):
            key = tex.replace(" ", "")
            if key not in seen:
                seen[key] = {"tex": tex, "note": note, "nums": [], "der": der.get(str(i))}
            if n not in seen[key]["nums"]:
                seen[key]["nums"].append(n)
    items = sorted(seen.values(), key=lambda x: -len(x["nums"]))
    boxes = "".join(
        f'<div class="fbox"><div class="eqwrap">\\[{x["tex"]}\\]</div>'
        f'<div class="flegend">{x["note"]} <span class="mono" style="opacity:.7">· задачи: '
        + ", ".join(f"P{n}" for n in x["nums"]) + '</span></div>' + derive_html(x["der"]) + '</div>'
        for x in items
    )
    return ('<p><b>Все формулы, которые нужны в задачах этой темы</b> — ровно те, что стоят в «Формулах по порядку». '
            'Сверху самые частые. Больше ничего не нужно.</p>' + boxes)


HOWTO = {
    "firstlaw_cycle": """
<div class="trick"><div class="lbl">🧭 Как понять, какую формулу брать</div>
<p><b>Работа = сколько газ толкал поршень.</b> Объём растёт — работа плюс, объём уменьшается — минус, объём не меняется — работа 0.</p>
<p><b>1. Есть график с числами на осях p и V → считай площадь фигуры</b> (P90, P91, P92). Треугольник: ½ × основание × высота.
Прямоугольник: ширина × высота. Основание = изменение V, высота = изменение p. По часовой стрелке — плюс, против — минус.
атм·л × 101,3 = Дж.</p>
<p><b>2. Вместо графика — температуры и названия участков → считай каждый участок и сложи</b> (P93):
изобара (p не меняется): W = nRΔT · изохора (V не меняется): W = 0 · адиабата (Q = 0): W = −nC<sub>V</sub>ΔT ·
изотерма (T не меняется): W = nRT·ln(V₂/V₁).</p></div>""",
}

_howto_file = DATA_DIR / "howto.json"
if _howto_file.exists():
    for _id, _html in json.loads(_howto_file.read_text(encoding="utf-8")).items():
        HOWTO.setdefault(_id, '<div class="trick"><div class="lbl">🧭 Как понять, какую формулу брать</div>' + _html + '</div>')

for t in topics:
    nums_in = [n for n in t["nums"] if n in by_n]
    data_items.append({
        "id": t["id"], "title": t["title"], "range": t["range"],
        "formulas": [], "story": HOWTO.get(t["id"], "") + topic_story(nums_in),
        # Full problem cards are copied into the tab by ex4_nav.JS, so no short answer list here.
        "problems": [],
    })

data_js = json.dumps(data_items, ensure_ascii=False).replace("</", "<\\/")
topics_js = json.dumps([{"id": t["id"], "nums": [n for n in t["nums"] if n in by_n]} for t in topics])

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
<title>PHYS161 · Exam 4</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="vendor/katex/katex.min.css"/>
<script defer src="vendor/katex/katex.min.js"></script>
<script defer src="vendor/katex/auto-render.min.js"></script>
<style>
{CSS}
{EXTRA_CSS}
{ex4_nav.CSS}
{ex3_top.CSS}
</style>
<link rel="stylesheet" href="theme.css"/>
</head>
<body>
<div class="wrap">
  <div>
    <a class="back" href="index.html">← Все мидки</a>
    <div class="eyebrow">PHYS161 · Exam 4 · Конспект как для ребёнка</div>
    <h1>Тепло, газы, законы термодинамики — каждая задача по шагам</h1>
  </div>
  <div class="tabs" id="tabs"></div>
  <div id="panels"></div>
  <footer>Источник: PHYS161_Exam4 (omgaXD/pt-nu-phys161) · {len(problems)} задач разобраны по шагам</footer>
</div>
<script>
const DATA = {data_js};

{page_js}
{ex3_top.JS}
window.EX4_TOPICS = {topics_js};
{ex4_nav.JS}
</script>
</body>
</html>
"""

out = ROOT / "ex4.html"
out.write_text(html, encoding="utf-8")
print("Wrote", out, out.stat().st_size, "bytes;", len(problems), "problems,", len(topics), "topic tabs")
