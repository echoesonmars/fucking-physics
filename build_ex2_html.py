# -*- coding: utf-8 -*-
import json
from pathlib import Path

from build_ex2 import CSS

PROBLEMS = json.loads(Path(r"d:\phys161\_ex2_all.json").read_text(encoding="utf-8"))
by_n = {p[0]: p for p in PROBLEMS}

SECTIONS = [
    ("work", "Работа", "P1–P14", list(range(1, 15)),
     "Работа — это «сколько пользы принесла сила, пока что-то ехало».",
     [
         (r"W=F d\cos\theta", "Сила × путь × cos угла между ними. Если сила вдоль пути — cos=1."),
         (r"W_g=-mgh", "Гравитация: минус, если поднимаешь; плюс по модулю = mgh."),
         (r"W_{\text{spring}}=\tfrac12 kx^2", "Работа на растяжение/сжатие пружины из нуля."),
     ],
     """
  <p>Представь: ты толкаешь игрушечную машинку. <b>Работа</b> — это «насколько сильно» и «насколько далеко» ты её толкал, но только той частью силы, что смотрит <b>туда же, куда едет</b> машинка.</p>
  """ + '<div class="fbox"><div class="eqwrap">\\[W=F d\\cos\\theta\\]</div><div class="flegend"><b>F</b> — сила, <b>d</b> — путь, <b>θ</b> — угол между стрелкой силы и стрелкой пути.</div></div>' + """
  <div class="kid">Если сила смотрит ровно по пути — бери просто F×d. Если под углом — сначала «отрежь» кусочек F cosθ. Трение всегда против пути → работа с минусом.</div>
  <div class="warn"><b>⚠️ Ловушки:</b>
  <ul>
    <li>Масса НЕ нужна, если дают силу и путь напрямую (P1, P2, P12).</li>
    <li>На пандусе нормаль N = mg cosθ, не mg.</li>
    <li>см → м: дели на 100; г → кг: дели на 1000.</li>
  </ul></div>
  """),
    ("ke", "Кинетическая энергия", "P15–P25", list(range(15, 26)),
     "Кинетическая энергия — «энергия бега»: чем тяжелее и быстрее, тем её больше.",
     [
         (r"K=\tfrac12 mv^2", "Энергия движения."),
         (r"W_{\text{net}}=\Delta K", "Суммарная работа всех сил = изменение K."),
         (r"p=mv,\quad K=p^2/(2m)", "Связь импульса и кинетической энергии."),
     ],
     """
  <p>Если что-то разогнали — кто-то сделал работу, и эта работа «села» в <b>½mv²</b>.</p>
  <div class="kid">Одинаковая скорость → у кого масса больше, энергия больше. Одинаковый импульс → у кого масса больше, энергия МЕНЬШЕ (он медленнее).</div>
  """),
    ("power", "Мощность", "P26–P29", list(range(26, 30)),
     "Мощность — работа в секунду: «как быстро тратим/даём энергию».",
     [
         (r"P=F v", "При постоянной скорости."),
         (r"P=\dot m\, g h", "Водопад: сколько кг воды в секунду × gh."),
         (r"P=W/t", "Работа за время."),
     ],
     """
  <p>Мощность — это не «сколько всего», а «сколько в одну секунду».</p>
  <div class="kid">Сердце за день делает много работы, но в секунду — всего ~1.5 Вт: как очень слабая лампочка!</div>
  """),
    ("pe", "Потенциальная энергия", "P30–P35", list(range(30, 36)),
     "Потенциал U — «высота горки». Сила всегда толкает вниз с этой горки.",
     [
         (r"F=-dU/dx", "Сила = минус наклон графика U."),
         (r"W=-\Delta U", "Работа консервативной силы."),
         (r"\Delta U=-\int F\,dx", "Как найти U из силы."),
     ],
     """
  <p>Думай про U как про горку в игровой площадке: шарик сам катится туда, где U меньше.</p>
  """),
    ("econ", "Сохранение энергии", "P36–P59", list(range(36, 60)),
     "Энергия не пропадает: перетекает между K, U и работой трения.",
     [
         (r"K_i+U_i=K_f+U_f+W_{\text{friction}}", "Главный баланс."),
         (r"U_s=\tfrac12 kx^2", "Пружина."),
         (r"h_{\min}=\tfrac52 R", "Минимум для мёртвой петли."),
     ],
     """
  <p>Как копилка: сверху положил (потенциал), разогнался (кинетика), потёрся — часть ушла в тепло.</p>
  <div class="warn"><b>⚠️</b> Трение всегда «съедает» энергию: пиши его с минусом в балансе (или +W_fric в правой части).</div>
  """),
    ("impulse", "Импульс и удары", "P60–P71", list(range(60, 72)),
     "Импульс — «пинок»: J = F Δt = изменение mv.",
     [
         (r"J=F\Delta t=\Delta p", "Импульс силы."),
         (r"\Delta p=2mv", "Отскок с той же скоростью (лобовой)."),
         (r"\Delta p=mv", "Залипание / глина."),
     ],
     """
  <div class="kid">Отскочил как мячик — импульс изменился на <b>два</b> mv. Застрял в глине — только на <b>один</b> mv.</div>
  """),
    ("mom", "Сохранение импульса", "P72–P91", list(range(72, 92)),
     "Если снаружи никто не толкает — суммарный mv до = суммарный mv после.",
     [
         (r"m_1v_1=(m_1+m_2)V", "Неупругий (слиплись)."),
         (r"v_2=\dfrac{2m_1}{m_1+m_2}v_1", "Упругий, мишень покоилась."),
         (r"mv=(m+M)V,\ V=\sqrt{2gh}", "Баллистический маятник."),
     ],
     """
  <p>Два шага маятника: <b>удар</b> (импульс) → <b>взлёт</b> (энергия). Не смешивай!</p>
  """),
    ("rocket", "Ракеты", "P92–P93", list(range(92, 94)),
     "Ракета плюётся газом назад и едет вперёд.",
     [
         (r"\Delta v=v_e\ln(m_0/m_f)", "Формула Циолковского."),
     ],
     """
  <div class="kid">Чем больше топлива сжигаешь (меньше остаток m_f), тем быстрее конечная скорость.</div>
  """),
    ("inertia", "Момент инерции", "P94–P106", list(range(94, 107)),
     "I — «насколько трудно раскрутить». Как масса, только для вращения.",
     [
         (r"I_{\text{disk}}=\tfrac12 MR^2", "Диск/цилиндр около оси."),
         (r"I_{\text{rod,end}}=\tfrac13 ML^2", "Стержень около конца."),
         (r"I_{\text{rod,cm}}=\tfrac{1}{12}ML^2", "Стержень около центра."),
         (r"K=\tfrac12 I\omega^2", "Вращательная кинетическая."),
     ],
     """
  <p>Чем дальше масса от оси — тем больше I. Оболочка «труднее» крутится, чем сплошной шар той же массы.</p>
  """),
    ("rot", "Вращение", "P107–P118", list(range(107, 119)),
     "Те же формулы, что для обычного движения, только x→θ, v→ω, a→α.",
     [
         (r"\omega=\omega_0+\alpha t", "Как v=v0+at."),
         (r"\theta=\omega_0 t+\tfrac12\alpha t^2", "Как путь."),
         (r"\omega^2=\omega_0^2+2\alpha\theta", "Без времени."),
         (r"\omega=d\theta/dt,\ \alpha=d\omega/dt", "Из θ(t)."),
     ],
     """
  <div class="kid">Об/мин → рад/с: умножь на 2π и раздели на 60. Обороты = радианы / 2π.</div>
  """),
    ("torque", "Момент силы", "P119–P132", list(range(119, 133)),
     "Момент τ — «сила, которая крутит». τ = I α.",
     [
         (r"\tau=r F_\perp=I\alpha", "Главное уравнение вращения."),
         (r"\tau_{\text{fric}}=\mu_k N R", "Трение на ободе."),
     ],
     """
  <p>Чтобы раскрутить точильный камень, тебе нужно пересилить трение топора и подшипника.</p>
  """),
    ("angmom", "Угловой момент", "P133–P150", list(range(133, 151)),
     "L = Iω. Если никто снаружи не крутит — L сохраняется.",
     [
         (r"L=I\omega=mvr_\perp", "Угловой импульс."),
         (r"I_i\omega_i=I_f\omega_f", "Сохранение L."),
         (r"T=\dfrac{mv^2}{r}=\dfrac{\ell^2}{mr^3}", "Нить через дырку в столе."),
     ],
     """
  <div class="kid">Подошёл к центру карусели — крутишься быстрее (как фигурист прижимает руки). Это сохранение L!</div>
  """),
]

def js_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)

def prob_details(p):
    n, q, ans, intro, steps = p
    lis = []
    for eq, note in steps:
        lis.append(
            f'<li><div class="eqwrap">\\({eq}\\)</div>'
            f'<div class="stepnote">{note}</div></li>'
        )
    return (
        f'<details class="prob"><summary><span class="pn mono">P{n}</span>'
        f'<span class="ptext">{q}</span>'
        f'<span class="ans-badge mono">{ans}</span></summary>'
        f'<div class="solution"><p class="step-intro">{intro}</p>'
        f'<ol class="sol-steps">{"".join(lis)}</ol></div></details>'
    )

# Build solutions story HTML (escaped for JS template literal carefully via JSON)
sol_parts = ['<p>Каждая задача свёрнута — нажми, чтобы увидеть шаги «как для ребёнка». Ответ в жёлтом бейдже справа.</p>']
sec_names = [
    (range(1, 15), "Работа"),
    (range(15, 26), "Кинетическая энергия"),
    (range(26, 30), "Мощность"),
    (range(30, 36), "Потенциальная энергия"),
    (range(36, 60), "Сохранение энергии"),
    (range(60, 72), "Импульс и удары"),
    (range(72, 92), "Сохранение импульса"),
    (range(92, 94), "Ракеты"),
    (range(94, 107), "Момент инерции"),
    (range(107, 119), "Вращение"),
    (range(119, 133), "Момент силы"),
    (range(133, 151), "Угловой момент"),
]
for rng, title in sec_names:
    nums = list(rng)
    sol_parts.append(
        f'<div class="sec-divider"><h3>{title}</h3>'
        f'<span class="range mono">P{nums[0]}–P{nums[-1]}</span></div>'
    )
    for n in nums:
        sol_parts.append(prob_details(by_n[n]))

solutions_html = "".join(sol_parts)

cheat_story = r"""
  <p>Открой перед экзаменом. Крупные формулы — ниже во вкладках, тут самое нужное.</p>
  <h3>Единицы (самое частое)</h3>
  <div class="kid">г → кг: <b>÷1000</b>. см → м: <b>÷100</b>. км/с → м/с: <b>×1000</b>. об/мин → рад/с: <b>×2π/60</b>.</div>
  <h3>Три главные формулы энергии</h3>
  <div class="fbox"><div class="eqwrap">\[K=\tfrac12 mv^2,\quad U=mgh,\quad U_s=\tfrac12 kx^2\]</div><div class="flegend">Бег, высота, пружина.</div></div>
  <h3>Работа и мощность</h3>
  <div class="fbox"><div class="eqwrap">\[W=Fd\cos\theta,\quad P=Fv\]</div><div class="flegend">Работа — «польза силы». Мощность — «польза в секунду».</div></div>
  <h3>Импульс</h3>
  <div class="fbox"><div class="eqwrap">\[J=F\Delta t=\Delta p,\quad \sum mv=\text{const}\]</div><div class="flegend">Пинок меняет mv. Если снаружи никто не толкает — сумма mv не меняется.</div></div>
  <h3>Вращение</h3>
  <div class="fbox"><div class="eqwrap">\[\tau=I\alpha,\quad L=I\omega,\quad K=\tfrac12 I\omega^2\]</div><div class="flegend">Момент крутит, L сохраняется, энергия вращения — ½Iω².</div></div>
  <div id="allformulas"></div>
"""

# Build DATA array as JS
data_items = []

# cheat
data_items.append({
    "id": "cheat",
    "title": "Шпаргалка",
    "range": "все формулы",
    "isCheatSheet": True,
    "formulas": [],
    "problems": [],
    "story": cheat_story,
})

# solutions first-ish after cheat for urgency? Keep like exam1: cheat then sections then solutions
# Actually exam1 has solutions as a tab - put it first after cheat for easy access
data_items.append({
    "id": "solutions",
    "title": "Все решения",
    "range": "P1–P150",
    "isSolutionsTab": True,
    "formulas": [],
    "problems": [],
    "story": solutions_html,
})

for sid, title, rng, nums, blurb, formulas, story in SECTIONS:
    probs = [[n, by_n[n][1], by_n[n][2]] for n in nums]
    data_items.append({
        "id": sid,
        "title": title,
        "range": rng,
        "formulas": formulas,
        "problems": probs,
        "story": story,
    })

# Emit JS: use JSON for structured fields, but story has HTML - embed via JSON.stringify of whole DATA
data_js = json.dumps(data_items, ensure_ascii=False)
# In browser JSON is fine; stories contain backslashes for LaTeX - JSON escapes them properly

html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>PHYS161 · Exam 2 · как для ребёнка</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="vendor/katex/katex.min.css"/>
<script defer src="vendor/katex/katex.min.js"></script>
<script defer src="vendor/katex/auto-render.min.js"></script>
<style>
{CSS}
</style>
</head>
<body>
<div class="wrap">
  <div>
    <div class="eyebrow">PHYS161 · Exam 2 · Конспект как для ребёнка</div>
    <h1>Каждая задача — простыми словами, с крупными формулами</h1>
  </div>
  <div class="tabs" id="tabs"></div>
  <div id="panels"></div>
  <footer>Источник: EX2.pdf · Все 150 задач разобраны по шагам</footer>
</div>
<script>
const DATA = {data_js};

const tabs = document.getElementById('tabs');
const panels = document.getElementById('panels');

DATA.forEach((sec,i)=>{{
  const btn = document.createElement('button');
  btn.className = 'tab-btn' + (i===0?' active':'');
  btn.dataset.tab = sec.id;
  let qn = '§'+(i);
  if(sec.isCheatSheet) qn = '★';
  if(sec.isSolutionsTab) qn = '✓';
  btn.innerHTML = '<span class="qn">'+qn+'</span>'+sec.title;
  tabs.appendChild(btn);

  const panel = document.createElement('div');
  panel.className = 'tab-panel' + (i===0?' active':'');
  panel.id = 'panel-'+sec.id;

  const h = document.createElement('div');
  h.innerHTML = '<div class="eyebrow mono">'+sec.range+'</div><h2>'+sec.title+'</h2>';
  panel.appendChild(h);

  const story = document.createElement('div');
  story.className = 'story';
  story.innerHTML = sec.story;
  panel.appendChild(story);

  if(sec.formulas && sec.formulas.length){{
    const fref = document.createElement('details');
    fref.className = 'ref';
    fref.innerHTML = '<summary>Формулы раздела — коротко</summary>';
    const fbody = document.createElement('div');
    fbody.className = 'fbody';
    fbody.innerHTML = sec.formulas.map(function(pair){{
      return '<div class="frow"><div class="eqwrap">\\\\('+pair[0]+'\\\\)</div><div class="note">'+pair[1]+'</div></div>';
    }}).join('');
    fref.appendChild(fbody);
    panel.appendChild(fref);
  }}

  if(sec.problems && sec.problems.length){{
    const pref = document.createElement('details');
    pref.className = 'ref';
    pref.innerHTML = '<summary>Все задачи раздела с ответами ('+sec.problems.length+')</summary>';
    const pbody = document.createElement('div');
    pbody.className = 'pbody';
    const ol = document.createElement('ol');
    ol.className = 'problems';
    sec.problems.forEach(function(p){{
      const li = document.createElement('li');
      li.innerHTML = '<span class="pn mono">P'+p[0]+'</span><span>'+p[1]+'<br><span class="ans">'+p[2]+'</span></span>';
      ol.appendChild(li);
    }});
    pbody.appendChild(ol);
    pref.appendChild(pbody);
    panel.appendChild(pref);
  }}

  panels.appendChild(panel);
}});

const allf = document.getElementById('allformulas');
if(allf){{
  allf.innerHTML = DATA.filter(function(s){{ return s.formulas && s.formulas.length; }}).map(function(s,idx){{
    const rows = s.formulas.map(function(pair){{
      return '<div class="frow"><div class="eqwrap">\\\\('+pair[0]+'\\\\)</div><div class="note">'+pair[1]+'</div></div>';
    }}).join('');
    return '<details class="ref" style="margin-bottom:8px;"><summary>'+s.title+' <span class="mono" style="color:var(--ink-muted); font-weight:400; margin-left:6px;">'+s.range+'</span></summary><div class="fbody">'+rows+'</div></details>';
  }}).join('');
}}

document.querySelectorAll('.tab-btn').forEach(function(btn){{
  btn.addEventListener('click', function(){{
    document.querySelectorAll('.tab-btn').forEach(function(b){{ b.classList.remove('active'); }});
    document.querySelectorAll('.tab-panel').forEach(function(p){{ p.classList.remove('active'); }});
    btn.classList.add('active');
    document.getElementById('panel-'+btn.dataset.tab).classList.add('active');
    btn.scrollIntoView({{block:'nearest', inline:'center', behavior:'smooth'}});
    renderMath();
  }});
}});

function renderMath(){{
  if (!window.renderMathInElement) return false;
  renderMathInElement(document.body, {{
    delimiters: [
      {{left: "\\\\[", right: "\\\\]", display: true}},
      {{left: "\\\\(", right: "\\\\)", display: false}}
    ],
    throwOnError: false,
    ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"]
  }});
  return true;
}}
function bootMath(){{
  if (renderMath()) return;
  var n = 0;
  var t = setInterval(function(){{
    n++;
    if (renderMath() || n > 40) clearInterval(t);
  }}, 100);
}}
document.addEventListener('DOMContentLoaded', bootMath);
window.addEventListener('load', bootMath);
document.addEventListener('toggle', function(e){{
  if (e.target && e.target.tagName === 'DETAILS') renderMath();
}}, true);
</script>
</body>
</html>
"""

# Fix: in the f-string above I doubled braces for JS, but LaTeX in data_js is already fine.
# Problem: in the HTML template, `\\(` became wrong. In an f-string:
# `\\\\(` → `\\(` in output which is correct for JS string in .map
# Wait - the formulas in DATA come from JSON and when we do pair[0] in JS we wrap with \\( \\)
# In the generated file we need the JS source to contain: '\\(' + pair[0] + '\\)'
# In Python f-string: to get \\\\( in output we need... 
# Actually looking at my code: `'\\\\('+pair[0]+'\\\\)'` inside f-string with doubled {{ 
# The f-string processes \\ → \, so `\\\\(` → `\\(` in the .py output file. Good for JS.

out = Path(r"d:\phys161\ex2.html")
out.write_text(html, encoding="utf-8")
print("Wrote", out, "bytes", out.stat().st_size)
print("problems", len(PROBLEMS))
