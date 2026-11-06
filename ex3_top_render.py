# -*- coding: utf-8 -*-
# Renders the "Top 15 formulas" tab in English and Russian with a language switch.
# Formula data and problem tags live in ex3_top.py; English text lives here in EN.
import ex3_top as T

EN = {
    "vlf": dict(
        title="Wave speed = wavelength × frequency",
        legend="<b>v</b> — wave speed (m/s), <b>λ</b> — wavelength (m), <b>f</b> — frequency (Hz).",
        triggers="“wavelength”, “frequency”, “speed of sound”, “Hz”, any wave or sound.",
        how=["Write down the two of the three you know (v, λ, f).", "Get the third from v = λf.",
             "Sound in air: v ≈ 343–344 m/s (use whatever the problem gives)."],
        trap="kHz → Hz: ×1000. Convert lengths in cm to metres.",
        ex_intro="In one period a wave moves exactly one wavelength, so λ = speed / frequency.",
        ex_notes=["the basic relation", "a low sound has a very long wavelength"]),
    "spring": dict(
        title="Spring: ω, period, frequency",
        legend="<b>k</b> — spring constant (N/m), <b>m</b> — mass (kg), <b>ω</b> — angular frequency (rad/s).",
        triggers="“spring”, “oscillates”, “period”, “frequency of oscillation”, a mass on a spring, a car on its springs, a bucket on a spring.",
        how=["Find k (often from k = mg/d — see Hooke's law).", "Compute ω = √(k/m).",
             "Need the period → T = 2π/ω; the frequency → f = ω/2π."],
        trap="Grams → kg. If something sticks on or passengers get in, use the TOTAL mass.",
        ex_intro="Both masses now hang on the spring, 2m = 32 kg. The impact speed changes the amplitude, not the period.",
        ex_notes=["period"]),
    "harm": dict(
        title="Standing waves: strings and pipes",
        tex=r"\text{string / open pipe: } f_n=\dfrac{nv}{2L},\qquad \text{closed pipe: } f_n=\dfrac{nv}{4L},\ n=1,3,5\dots",
        legend="n = 1 is the fundamental. “First overtone” = 2nd harmonic (3rd for a closed pipe), “second overtone” = 3rd harmonic (5th for a closed pipe).",
        triggers="“fundamental”, “harmonic”, “overtone”, “organ pipe”, “open / closed / stopped pipe”, “fixed at both ends”.",
        how=["Pick the type: string or open pipe — every n; pipe closed at one end — odd n only.",
             "Two neighbouring harmonics: their difference Δf = f₁ for an open pipe, 2f₁ for a closed one.",
             "String fundamental: λ = 2L → v = 2Lf."],
        trap="Overtone ≠ harmonic! The second overtone of a string is the third harmonic (n = 3).",
        ex_intro="The closed end is a node, the open end an antinode. In the fundamental a quarter wavelength fits in the pipe: λ = 4L.",
        ex_notes=["a quarter wave in the pipe", "plug in"]),
    "newton": dict(
        title="Newton's law of gravitation and g",
        legend="<b>G</b> = 6.67·10⁻¹¹, <b>r</b> — distance between the CENTRES, <b>R</b> — planet radius.",
        triggers="“gravitational force”, “gravitational acceleration”, “weight on a planet”, “altitude”, two masses.",
        how=["Measure distance centre to centre (R + h above the surface).",
             "Plug into F = GMm/r² (or g = GM/R²).",
             "“How many times” → take a ratio: g ∝ M/R²."],
        trap="h in km → ×1000. With several masses, add the forces as VECTORS.",
        ex_intro="Straight Newton's law of gravitation, F = GMm/R².",
        ex_notes=["plug in", "result"]),
    "shmmax": dict(
        title="Simple harmonic motion: max speed and acceleration",
        legend="<b>A</b> — amplitude (largest displacement), <b>x</b> — current displacement.",
        triggers="“maximum speed”, “maximum acceleration”, “amplitude”, “passes equilibrium”, “does not slip / leave the platform”.",
        how=["Find ω (from k/m, from f, or read it off x = A cos(ωt)).",
             "Max speed is at the centre: v = Aω. Max acceleration is at the ends: a = Aω².",
             "Something resting on top must not slip / lift off → a_max = μg or a_max = g."],
        trap="Amplitude in cm/mm → m. “Released from x₀” means A = x₀.",
        ex_intro="Released from rest, so 0.02 m is the amplitude. The block is fastest at the centre, where all the spring energy has become kinetic.",
        ex_notes=["spring energy = kinetic energy at the centre", "answer"]),
    "string": dict(
        title="Wave speed on a string",
        legend="<b>F_T</b> — tension (N), <b>μ</b> — mass of one metre of string (kg/m).",
        triggers="“string”, “wire”, “cable”, “tension”, “linear mass density”, “pulse travels”.",
        how=["Compute μ = m/L (mass of the whole string / its length).", "v = √(F/μ).",
             "Need the tension → F = μv². Pulse travel time → t = L/v."],
        trap="m in grams → kg; L in cm → m. Given a diameter: μ = ρ·π d²/4.",
        ex_intro="Wave speed on a string: v = √(T/μ), where μ is the mass per metre.",
        ex_notes=["linear density (grams to kg!)", "speed"]),
    "genergy": dict(
        title="Gravitational energy and escape speed",
        legend="High above a planet mgh does NOT work — only −GMm/r.",
        triggers="“launched”, “escape speed”, “how high”, “comet”, “far from Earth”, “released from rest in deep space”.",
        how=["Write K + U at the start and at the end.", "U = −GMm/r (r from the centre!).", "Solve for the unknown (v or r)."],
        trap="“Very far away” means U = 0. Two free masses → total momentum is also 0.",
        ex_intro="Energy is conserved: all the kinetic energy at launch goes into raising U up to the height where the speed is zero.",
        ex_notes=["energy at the top = energy at the bottom", "solve"]),
    "echo": dict(
        title="Distance = speed × time, echoes",
        tex=r"d=vt,\qquad \text{echo: } t=\dfrac{2d}{v}",
        legend="An echo travels THERE and BACK — hence 2d.",
        triggers="“echo”, “sonar”, “returns”, “how long does it take”, “pulse travels”, “hears two sounds”.",
        how=["Find the speed (given, or v = λf, or v = √(F/μ), or √(B/ρ)).", "t = d/v. For an echo, t = 2d/v."],
        trap="The easiest points on the exam — just don't forget the 2 for an echo.",
        ex_intro="v = fλ, t = d/v. The amplitude is not needed.",
        ex_notes=["speed", "time"]),
    "orbit": dict(
        title="Circular orbits and Kepler's law",
        legend="Gravity supplies the centripetal force. Artificial gravity: a = ω²r.",
        triggers="“orbit”, “satellite”, “period of orbit”, “binary stars”, “space station rotates”.",
        how=["Set GM/r² equal to v²/r (or ω²r).", "Need the period → T = 2π√(r³/GM); the radius → r = (GMT²/4π²)^(1/3)."],
        trap="Periods in days/hours → seconds. Altitude = r − R.",
        ex_intro="Kepler's third law again, this time solved for T.",
        ex_notes=["period formula", "compute (≈36.6 days)"]),
    "doppler": dict(
        title="Doppler effect",
        legend="<b>v_o</b> — listener speed, <b>v_s</b> — source speed. Moving closer → top signs, HIGHER pitch.",
        triggers="“moving toward / away”, “train whistle”, “siren”, “bat”, “approaching”, “receding”.",
        how=["Decide who moves: the source (denominator) or the listener (numerator).",
             "Approaching → frequency goes up; receding → it goes down. Choose the signs so that happens.",
             "Reflection off a moving wall → apply Doppler TWICE."],
        trap="v is the speed of sound (≈ 343–344 m/s), not the speed of the car.",
        ex_intro="The source is at rest and the listener moves away — fewer wave crests reach them each second, so the pitch is lower.",
        ex_notes=["listener moving away: minus", "solve", "answer"]),
    "hooke": dict(
        title="Hooke's law: find the spring constant",
        legend="A hanging mass stretches the spring by d → its weight is balanced by the spring force.",
        triggers="“stretches by”, “compresses by”, “spring balance”, “car sinks by”, “hangs at rest”.",
        how=["k = mg/d (d in metres).", "Usually next → ω = √(k/m) or T = 2π√(m/k)."],
        trap="This is almost always step one of a spring problem. d in cm → ÷100.",
        ex_intro="When the mass hangs at rest, the spring force equals the weight: kx = mg.",
        ex_notes=["equilibrium", "g → kg, cm → m"]),
    "damp": dict(
        title="Damped oscillations",
        legend="The amplitude decays exponentially; the energy decays as its square, even faster.",
        triggers="“damping”, “amplitude decreases”, “loses energy”, “each cycle”, “b =”.",
        how=["If each cycle multiplies the amplitude by r → the energy is multiplied by r².", "Take logs: t = ln(…)/(b/2m) or N = ln(p)/(2 ln r)."],
        trap="Don't mix up amplitude and energy — energy ∝ A².",
        ex_intro="Same idea: each cycle multiplies the energy by 0.94². The period (0.7 s) is not needed — they ask for the number of cycles.",
        ex_notes=["energy after n cycles", "take logarithms"]),
    "beats": dict(
        title="Beats",
        legend="Two close frequencies → the loudness “pulses” at their difference frequency.",
        triggers="“beats”, “beat frequency”, “out of tune”, “hears beats”.",
        how=["Find both frequencies (often from f = v/λ or f = v/4L).", "Subtract: f_beat = |f₁ − f₂|."],
        trap="When finding a frequency from beats, it can be either above or below the reference.",
        ex_intro="Find both frequencies f = v/λ (cm → m!) and subtract.",
        ex_notes=["frequencies", "beats = difference of frequencies"]),
    "pend": dict(
        title="Simple pendulum",
        legend="The bob's mass does NOT matter! Only the length and g.",
        triggers="“pendulum”, “swings”, “length of string”, “unknown planet”.",
        how=["N full oscillations in time t → T = t/N.", "T = 2π√(L/g) → solve for L or g.",
             "In an accelerating rocket: g → g + a."],
        trap="“From one side to the other” is HALF a period.",
        ex_intro="Pendulum frequency: f = (1/2π)√(g/L). Centimetres → metres.",
        ex_notes=["plug in"]),
    "db": dict(
        title="Decibels and intensity",
        tex=r"\beta=10\log_{10}\dfrac{I}{I_0},\quad I_0=10^{-12}\,\tfrac{\text{W}}{\text{m}^2},\quad I=\dfrac{P}{4\pi r^2},\quad I=\dfrac{p_{\max}^2}{2\rho v}",
        legend="Twice as far → a quarter of the intensity → about 6 dB less.",
        triggers="“sound level”, “dB”, “intensity”, “pressure amplitude”, “at what distance”.",
        how=["From dB to intensity: I = I₀·10^(β/10).",
             "Distance changes: β₂ = β₁ − 20 log(r₂/r₁).", "Pressure → intensity: I = p²/(2ρv)."],
        trap="log means log₁₀, not ln.",
        ex_intro="Intensity of a sound wave from its pressure amplitude: more pressure → louder (as the square).",
        ex_notes=["formula", "plug in"]),
}

UI = {
    "ru": dict(problems="задач", spot="Как узнать задачу", solve="Как решать", example="Разбор на реальной задаче",
               answer="Ответ", all="Все задачи на эту формулу (нажми — откроется решение)",
               intro=lambda total: f"""<p>Я прошёлся по всем <b>{total}</b> задачам третьей мидки и для каждой отметил, какие формулы нужны для решения.
Ниже — сколько задач держится на каждой формуле. В одной задаче бывает 2–3 формулы, поэтому проценты в сумме больше 100.</p>""",
               s5="задач ({p}%) — хотя бы одна из 5 главных формул", s15="задач ({p}%) — покрывают все 15",
               seasy="задач решаются ОДНОЙ формулой — начни с них",
               plan="<b>План, если времени мало:</b> выучи 5 формул сверху → на экзамене ищи слова из «Как узнать задачу» → решай по шагам «Как решать». Сначала бери задачи из списка «лёгкие» в самом низу.",
               h5="🔥 5 обязательных формул", h10="⭐ Ещё 10 важных",
               heasy="✅ Лёгкие задачи — одна формула, один шаг",
               peasy="Если надо решить хоть что-то — начни с этих. Нажми номер, откроется решение.",
               units="""<b>⚠️ Единицы — главная причина ошибок:</b>
<ul><li>г → кг ÷1000, см → м ÷100, мм → м ÷1000, км → м ×1000</li>
<li>кГц → Гц ×1000; часы → секунды ×3600; сутки → ×86400</li>
<li>«Second overtone» струны — это n = 3, а не n = 2</li></ul>"""),
    "en": dict(problems="problems", spot="How to spot it", solve="How to solve it", example="Worked example",
               answer="Answer", all="Every problem that uses it (tap to open the solution)",
               intro=lambda total: f"""<p>I went through all <b>{total}</b> Exam 3 problems and marked which formulas each one needs.
Below is how many problems rely on each formula. A problem often needs 2–3 formulas, so the percentages add up to more than 100.</p>""",
               s5="problems ({p}%) use at least one of the top 5", s15="problems ({p}%) are covered by all 15",
               seasy="problems take just ONE formula — start there",
               plan="<b>Short on time?</b> Learn the top 5 → on the exam, look for the words under “How to spot it” → follow “How to solve it”. Start with the easy problems listed at the very bottom.",
               h5="🔥 The 5 must-know formulas", h10="⭐ 10 more important ones",
               heasy="✅ Easy problems — one formula, one step",
               peasy="If you need to solve at least something, start here. Tap a number to open its solution.",
               units="""<b>⚠️ Units are the #1 source of mistakes:</b>
<ul><li>g → kg ÷1000, cm → m ÷100, mm → m ÷1000, km → m ×1000</li>
<li>kHz → Hz ×1000; hours → seconds ×3600; days → ×86400</li>
<li>The “second overtone” of a string is n = 3, not n = 2</li></ul>"""),
}

CSS = T.CSS + """
.langbar{display:flex; gap:6px; align-self:flex-start;}
.langbar button{font:inherit; font-size:14px; font-weight:600; padding:6px 14px; border-radius:999px; border:1px solid var(--rule); background:var(--surface); color:var(--ink); cursor:pointer;}
.langbar button.on{background:var(--accent); border-color:var(--accent); color:var(--bg);}
.topwrap{display:flex; flex-direction:column; gap:16px;}
.topwrap[data-lang="en"] .lang-ru, .topwrap[data-lang="ru"] .lang-en{display:none;}
"""

JS = T.JS + r"""
(function(){
  var w = document.querySelector('.topwrap');
  if (!w) return;
  function set(l){
    w.dataset.lang = l;
    w.querySelectorAll('.langbar button').forEach(function(b){ b.classList.toggle('on', b.dataset.lang === l); });
    try { localStorage.setItem('ex3-top-lang', l); } catch(e) {}
  }
  var saved = null;
  try { saved = localStorage.getItem('ex3-top-lang'); } catch(e) {}
  if (saved === 'ru' || saved === 'en') set(saved);
  w.querySelectorAll('.langbar button').forEach(function(b){
    b.addEventListener('click', function(){ set(b.dataset.lang); });
  });
})();
"""


def card(rank, f, by_n, total, must, lang):
    u = UI[lang]
    t = dict(f, **EN[f["id"]]) if lang == "en" else f
    n_ex = f["example"]
    p = by_n[n_ex]
    if lang == "en":
        notes = EN[f["id"]]["ex_notes"]
        assert len(notes) == len(p[4]), (f["id"], len(notes), len(p[4]))
        intro = EN[f["id"]]["ex_intro"]
    else:
        notes = [s[1] for s in p[4]]
        intro = p[3]
    steps = "".join(f'<li><div class="eqwrap">\\({eq}\\)</div><div class="stepnote">{note}</div></li>'
                    for (eq, _), note in zip(p[4], notes))
    pct = round(100 * len(f["nums"]) / total)
    how = "".join(f"<li>{h}</li>" for h in t["how"])
    chips = "".join(T.chip(n, n == n_ex) for n in f["nums"])
    return f"""
<div class="fcard{' must' if must else ''}">
  <div class="fhead"><span class="frank">#{rank}</span><h4>{t['title']}</h4><span class="fcount">{len(f['nums'])} {u['problems']} · {pct}%</span></div>
  <div class="bar"><i style="width:{min(100, pct * 4)}%"></i></div>
  <div class="eqwrap">\\[{t['tex']}\\]</div>
  <div class="legend">{t['legend']}</div>
  <div><div class="lbl">{u['spot']}</div>{t['triggers']}</div>
  <div><div class="lbl">{u['solve']}</div><ol>{how}</ol></div>
  <div class="trapline">⚠️ {t['trap']}</div>
  <details class="ref"><summary>{u['example']}: P{n_ex}</summary>
    <div class="fbody"><div class="excase">
      <div class="q">{p[1]}</div>
      <div>{intro}</div>
      <ol class="sol-steps">{steps}</ol>
      <div>{u['answer']}: <span class="ans">{p[2]}</span></div>
    </div></div>
  </details>
  <div><div class="lbl">{u['all']}</div><div class="chips">{chips}</div></div>
</div>"""


def lang_block(lang, top5, top10, by_n, total, cov5, cov15):
    u = UI[lang]
    parts = [f"""<div class="lang-{lang} topwrap-inner" lang="{lang}" style="display:flex; flex-direction:column; gap:16px;">
{u['intro'](total)}
<div class="statgrid">
  <div class="stat"><b>{len(cov5)}</b><span>{u['s5'].format(p=round(100*len(cov5)/total))}</span></div>
  <div class="stat"><b>{len(cov15)}</b><span>{u['s15'].format(p=round(100*len(cov15)/total))}</span></div>
  <div class="stat"><b>{len(T.EASY)}</b><span>{u['seasy']}</span></div>
</div>
<div class="kid">{u['plan']}</div>
<h3>{u['h5']}</h3>"""]
    parts += [card(i + 1, f, by_n, total, True, lang) for i, f in enumerate(top5)]
    parts.append(f"<h3>{u['h10']}</h3>")
    parts += [card(i + 6, f, by_n, total, False, lang) for i, f in enumerate(top10)]
    easy = "".join(T.chip(n) for n in T.EASY)
    parts.append(f"""<h3>{u['heasy']}</h3>
<p>{u['peasy']}</p>
<div class="chips">{easy}</div>
<div class="warn">{u['units']}</div>
</div>""")
    return "".join(parts)


def build_story(by_n):
    total = len(by_n)
    allf = sorted(T.TOP5 + T.TOP10, key=lambda f: -len(f["nums"]))  # rank by frequency
    assert set(EN) == {f["id"] for f in allf}
    for f in allf:
        missing = [n for n in f["nums"] + [f["example"]] if n not in by_n]
        assert not missing, (f["id"], missing)
        assert f["example"] in f["nums"], f["id"]
    top5, top10 = allf[:5], allf[5:]
    cov5 = {n for f in top5 for n in f["nums"]}
    cov15 = {n for f in allf for n in f["nums"]}
    return (f"""<div class="topwrap" data-lang="en">
<div class="langbar"><button type="button" data-lang="en" class="on">English</button><button type="button" data-lang="ru">Русский</button></div>
{lang_block('en', top5, top10, by_n, total, cov5, cov15)}
{lang_block('ru', top5, top10, by_n, total, cov5, cov15)}
</div>""")
