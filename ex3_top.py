# -*- coding: utf-8 -*-
# "Топ-15 формул" tab for ex3.html.
# nums = the Exam 3 problems that need the formula, tagged by hand from each problem's
# answer expression in content/sets/phys161-exam3/scenarios (omgaXD/pt-nu-phys161).

TOP5 = [
    dict(
        id="vlf", title="Скорость волны = длина × частота",
        tex=r"v=\lambda f,\qquad \lambda=\dfrac{v}{f},\qquad T=\dfrac1f",
        legend="<b>v</b> — скорость волны (м/с), <b>λ</b> — длина волны (м), <b>f</b> — частота (Гц).",
        triggers="«wavelength», «frequency», «speed of sound», «Hz», любая волна или звук.",
        how=["Выпиши две величины из трёх (v, λ, f).", "Третью найди из v = λf.",
             "Звук в воздухе без данных: v ≈ 343–344 м/с (смотри, что дали в условии)."],
        trap="кГц → Гц: ×1000. Длину в см переведи в метры.",
        nums=[80, 81, 82, 83, 84, 88, 89, 94, 95, 96, 98, 99, 100, 101, 103, 109, 112, 114,
              117, 118, 137, 138, 139, 146],
        example=117,
    ),
    dict(
        id="spring", title="Пружина: ω, период, частота",
        tex=r"\omega=\sqrt{\dfrac{k}{m}},\qquad T=2\pi\sqrt{\dfrac{m}{k}},\qquad f=\dfrac1T=\dfrac{\omega}{2\pi}",
        legend="<b>k</b> — жёсткость (Н/м), <b>m</b> — масса (кг), <b>ω</b> — угловая частота (рад/с).",
        triggers="«spring», «oscillates», «period», «frequency of oscillation», груз на пружине, машина на рессорах, ведро на пружине.",
        how=["Найди k (часто через k = mg/d — см. формулу №9).", "Посчитай ω = √(k/m).",
             "Нужен период → T = 2π/ω; частота → f = ω/2π."],
        trap="Масса в граммах → кг. Если что-то прилипло или сели пассажиры — бери СУММАРНУЮ массу.",
        nums=[39, 40, 43, 44, 46, 48, 49, 50, 51, 54, 55, 57, 63, 65, 66, 67, 69, 70, 71, 73, 75, 76, 77],
        example=65,
    ),
    dict(
        id="newton", title="Закон всемирного тяготения и g",
        tex=r"F=\dfrac{GMm}{r^2},\qquad g=\dfrac{GM}{R^2},\qquad g(h)=g\left(\dfrac{R}{R+h}\right)^2",
        legend="<b>G</b> = 6.67·10⁻¹¹, <b>r</b> — расстояние между ЦЕНТРАМИ, <b>R</b> — радиус планеты.",
        triggers="«gravitational force», «gravitational acceleration», «weight on planet», «altitude», две массы.",
        how=["Расстояние — от центра до центра (R + h, если над поверхностью).",
             "Подставь в F = GMm/r² (или g = GM/R²).",
             "Если «во сколько раз» — бери отношение: g ∝ M/R²."],
        trap="h в км → ×1000. Если масс несколько — силы складываются как ВЕКТОРЫ.",
        nums=[1, 2, 3, 7, 8, 9, 10, 11, 12, 17, 19, 20, 21, 25, 28, 29, 30, 31, 61],
        example=21,
    ),
    dict(
        id="shmmax", title="Гармонические колебания: max скорость и ускорение",
        tex=r"v_{\max}=A\omega,\qquad a_{\max}=A\omega^2,\qquad v=\omega\sqrt{A^2-x^2},\qquad E=\tfrac12 kA^2",
        legend="<b>A</b> — амплитуда (самое большое отклонение), <b>x</b> — текущее смещение.",
        triggers="«maximum speed», «maximum acceleration», «amplitude», «passes equilibrium», «does not slip / leave the platform».",
        how=["Найди ω (из k/m, из f, или дана в x = A cos(ωt)).",
             "Max скорость — в центре: v = Aω. Max ускорение — на краях: a = Aω².",
             "Что-то лежит сверху и не должно соскользнуть / оторваться → a_max = μg или a_max = g."],
        trap="Амплитуда в см/мм → м. «Released from x₀» значит A = x₀.",
        nums=[40, 45, 52, 53, 54, 55, 57, 58, 59, 60, 63, 64, 98, 99, 100],
        example=40,
    ),
    dict(
        id="string", title="Скорость волны на струне",
        tex=r"v=\sqrt{\dfrac{F_T}{\mu}},\qquad \mu=\dfrac{m}{L}",
        legend="<b>F_T</b> — натяжение (Н), <b>μ</b> — масса одного метра струны (кг/м).",
        triggers="«string», «wire», «cable», «tension», «linear mass density», «pulse travels».",
        how=["Посчитай μ = m/L (масса всей струны / длина).", "v = √(F/μ).",
             "Нужно натяжение → F = μv². Время пробега импульса → t = L/v."],
        trap="m в граммах → кг; L в см → м. Если дан диаметр: μ = ρ·π d²/4.",
        nums=[90, 91, 92, 93, 96, 97, 101, 104, 107, 108, 112, 114, 142, 143],
        example=90,
    ),
]

TOP10 = [
    dict(
        id="harm", title="Стоячие волны: струна и трубы",
        tex=r"\text{струна / открытая труба: } f_n=\dfrac{nv}{2L},\qquad \text{закрытая труба: } f_n=\dfrac{nv}{4L},\ n=1,3,5\dots",
        legend="n = 1 — основной тон. «First overtone» = 2-я гармоника (у закрытой — 3-я), «second overtone» = 3-я (у закрытой — 5-я).",
        triggers="«fundamental», «harmonic», «overtone», «organ pipe», «open / closed / stopped pipe», «fixed at both ends».",
        how=["Определи тип: струна/открытая — все n; закрытая с одной стороны — только нечётные.",
             "Две соседние гармоники: разность Δf = f₁ у открытой, 2f₁ у закрытой.",
             "Основной тон струны: λ = 2L → v = 2Lf."],
        trap="Overtone ≠ harmonic! Second overtone струны = третья гармоника (n = 3).",
        nums=[92, 93, 94, 95, 96, 101, 102, 103, 108, 112, 113, 114, 121, 123, 124, 126, 130, 131, 142, 143],
        example=131,
    ),
    dict(
        id="genergy", title="Энергия в гравитации и вторая космическая",
        tex=r"U=-\dfrac{GMm}{r},\qquad \tfrac12 mv_1^2-\dfrac{GMm}{r_1}=\tfrac12 mv_2^2-\dfrac{GMm}{r_2},\qquad v_{\text{esc}}=\sqrt{\dfrac{2GM}{R}}",
        legend="Высоко над планетой mgh НЕ работает — только −GMm/r.",
        triggers="«launched», «escape speed», «how high», «comet», «far from Earth», «released from rest in deep space».",
        how=["Запиши K + U в начале и в конце.", "U = −GMm/r (r от центра!).", "Реши относительно неизвестной (v или r)."],
        trap="«Very far away» значит U = 0. Две свободные массы → ещё и импульс = 0.",
        nums=[6, 13, 14, 15, 16, 18, 24, 26, 27, 32, 33],
        example=14,
    ),
    dict(
        id="echo", title="Путь = скорость × время, эхо",
        tex=r"d=vt,\qquad \text{эхо: } t=\dfrac{2d}{v}",
        legend="Эхо проходит путь ТУДА и ОБРАТНО — поэтому 2d.",
        triggers="«echo», «sonar», «returns», «how long does it take», «pulse travels», «hears two sounds».",
        how=["Найди скорость (дана, или v = λf, или v = √(F/μ), или √(B/ρ)).", "t = d/v. Для эха — t = 2d/v."],
        trap="Самые лёгкие баллы на экзамене — не забудь множитель 2 у эха.",
        nums=[86, 88, 89, 91, 97, 104, 107, 109, 140, 141, 147],
        example=109,
    ),
    dict(
        id="orbit", title="Круговая орбита и закон Кеплера",
        tex=r"\dfrac{GM}{r^2}=\dfrac{v^2}{r}=\left(\dfrac{2\pi}{T}\right)^2 r\ \Rightarrow\ v=\sqrt{\dfrac{GM}{r}},\quad T^2=\dfrac{4\pi^2 r^3}{GM}",
        legend="Гравитация работает как центростремительная сила. Искусственная гравитация: a = ω²r.",
        triggers="«orbit», «satellite», «period of orbit», «binary stars», «space station rotates».",
        how=["Приравняй GM/r² к v²/r (или ω²r).", "Нужен период → T = 2π√(r³/GM); радиус → r = (GMT²/4π²)^(1/3)."],
        trap="Период в днях/часах → секунды. Высота = r − R.",
        nums=[4, 5, 11, 12, 17, 22, 23, 29, 30, 36],
        example=23,
    ),
    dict(
        id="doppler", title="Эффект Доплера",
        tex=r"f'=f\,\dfrac{v\pm v_o}{v\mp v_s}",
        legend="<b>v_o</b> — скорость слушателя, <b>v_s</b> — источника. Сближаются → верхние знаки, частота ВЫШЕ.",
        triggers="«moving toward / away», «train whistle», «siren», «bat», «approaching», «receding».",
        how=["Определи, кто движется: источник (знаменатель) или слушатель (числитель).",
             "Сближение → частота растёт; удаление → падает. Подбери знаки так, чтобы так и вышло.",
             "Отражение от движущейся стенки — Доплер ДВА раза."],
        trap="v — скорость звука (≈ 343–344 м/с), а не скорость машины.",
        nums=[115, 116, 132, 133, 134, 135, 148, 149, 150],
        example=134,
    ),
    dict(
        id="hooke", title="Закон Гука: найти жёсткость",
        tex=r"F=kx,\qquad k=\dfrac{mg}{d}",
        legend="Груз повис и растянул пружину на d → сила тяжести уравновесилась силой пружины.",
        triggers="«stretches by», «compresses by», «spring balance», «car sinks by», «hangs at rest».",
        how=["k = mg/d (d в метрах).", "Дальше обычно → ω = √(k/m) или T = 2π√(m/k)."],
        trap="Почти всегда это первый шаг задачи на пружину. d в см → ÷100.",
        nums=[39, 43, 46, 47, 50, 51, 70, 71],
        example=47,
    ),
    dict(
        id="damp", title="Затухающие колебания",
        tex=r"A(t)=A_0e^{-\frac{b}{2m}t},\qquad E\propto A^2,\qquad \omega'=\sqrt{\dfrac{k}{m}-\left(\dfrac{b}{2m}\right)^2}",
        legend="Амплитуда тает экспоненциально, энергия — в квадрате быстрее.",
        triggers="«damping», «amplitude decreases», «loses energy», «each cycle», «b =».",
        how=["Если за цикл амплитуда × r → энергия × r².", "Логарифмируй: t = ln(…)/(b/2m) или N = ln(p)/(2 ln r)."],
        trap="Не путай амплитуду и энергию — энергия ∝ A².",
        nums=[41, 42, 72, 73, 74, 78],
        example=42,
    ),
    dict(
        id="beats", title="Биения",
        tex=r"f_{\text{beat}}=|f_1-f_2|",
        legend="Две близкие частоты → громкость «пульсирует» с разностной частотой.",
        triggers="«beats», «beat frequency», «out of tune», «hears beats».",
        how=["Найди обе частоты (часто через f = v/λ или f = v/4L).", "Вычти: f_beat = |f₁ − f₂|."],
        trap="Если надо найти частоту по биениям — не забудь, что она может быть и выше, и ниже.",
        nums=[116, 130, 132, 137, 138, 142],
        example=137,
    ),
    dict(
        id="pend", title="Математический маятник",
        tex=r"T=2\pi\sqrt{\dfrac{L}{g}},\qquad f=\dfrac{1}{2\pi}\sqrt{\dfrac{g}{L}}",
        legend="Масса шарика НЕ важна! Только длина и g.",
        triggers="«pendulum», «swings», «length of string», «unknown planet».",
        how=["N полных колебаний за t → T = t/N.", "T = 2π√(L/g) → выражай L или g.",
             "В ускоряющейся ракете: g → g + a."],
        trap="«From one side to the other» — это ПОЛ-периода.",
        nums=[37, 38, 56, 61, 62],
        example=56,
    ),
    dict(
        id="db", title="Децибелы и интенсивность",
        tex=r"\beta=10\log_{10}\dfrac{I}{I_0},\quad I_0=10^{-12}\,\tfrac{\text{Вт}}{\text{м}^2},\quad I=\dfrac{P}{4\pi r^2},\quad I=\dfrac{p_{\max}^2}{2\rho v}",
        legend="В 2 раза дальше → интенсивность в 4 раза меньше → минус ~6 дБ.",
        triggers="«sound level», «dB», «intensity», «pressure amplitude», «at what distance».",
        how=["Из дБ в интенсивность: I = I₀·10^(β/10).",
             "Расстояние меняется: β₂ = β₁ − 20 log(r₂/r₁).", "Давление → интенсивность: I = p²/(2ρv)."],
        trap="log — десятичный (log₁₀), не ln.",
        nums=[119, 120, 127, 128, 129],
        example=120,
    ),
]

EASY = [117, 118, 47, 21, 56, 131, 40, 109, 7, 19, 23, 85]

CSS = """
.statgrid{display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:10px; margin:4px 0 6px;}
.stat{background:var(--surface); border:1px solid var(--rule); border-radius:12px; padding:12px 14px;}
.stat b{display:block; font-family:"Fraunces",Georgia,serif; font-size:28px; color:var(--accent); line-height:1.1;}
.stat span{font-size:14px; color:var(--ink-muted);}
.fcard{border:1px solid var(--rule); border-radius:14px; background:var(--surface); padding:16px 16px 14px; display:flex; flex-direction:column; gap:10px; min-width:0;}
.fcard.must{border:2px solid var(--accent);}
.fhead{display:flex; align-items:baseline; gap:10px; flex-wrap:wrap;}
.frank{font-family:"Fraunces",Georgia,serif; font-weight:700; font-size:22px; color:var(--accent);}
.fhead h4{margin:0; font-size:18px; flex:1 1 200px;}
.fcount{font-family:"IBM Plex Mono",monospace; font-size:13px; color:var(--accent-2); white-space:nowrap;}
.bar{height:6px; border-radius:3px; background:var(--accent-soft); overflow:hidden;}
.bar i{display:block; height:100%; background:var(--accent);}
.fcard .eqwrap{overflow-x:auto; -webkit-overflow-scrolling:touch;}
.fcard .eqwrap .katex-display{margin:4px 0;}
.fcard .eqwrap .katex{font-size:1.3em;}
.fcard .legend{font-size:15px; color:var(--ink-muted);}
.fcard .lbl{font-weight:600; font-size:14px; color:var(--accent); text-transform:uppercase; letter-spacing:.04em;}
.fcard ol{margin:2px 0 0; padding-left:22px; font-size:16px;}
.fcard .trapline{font-size:15px; background:var(--warn-soft); color:var(--ink); border-radius:8px; padding:8px 10px;}
.chips{display:flex; flex-wrap:wrap; gap:6px;}
a.pchip{font-family:"IBM Plex Mono",monospace; font-size:13px; padding:3px 8px; border-radius:999px; border:1px solid var(--rule); color:var(--ink); text-decoration:none; background:var(--story-bg);}
a.pchip:hover{border-color:var(--accent); color:var(--accent);}
a.pchip.ex{border-color:var(--accent-2); color:var(--accent-2); font-weight:600;}
.excase{border-left:3px solid var(--accent-2); padding:6px 0 6px 12px; display:flex; flex-direction:column; gap:8px;}
.excase .q{font-size:15.5px;}
.excase ol{font-size:15.5px;}
.excase .eqwrap .katex{font-size:1.15em;}
.excase .ans{font-family:"IBM Plex Mono",monospace; font-weight:600; color:var(--accent-2);}
details.prob.flash{outline:3px solid var(--accent-2); outline-offset:2px;}
"""

JS = r"""
document.addEventListener('click', function(e){
  var a = e.target.closest && e.target.closest('a.pchip');
  if (!a) return;
  e.preventDefault();
  var btn = document.querySelector('.tab-btn[data-tab="solutions"]');
  if (btn) btn.click();
  var d = document.getElementById('p' + a.dataset.p);
  if (!d) return;
  d.open = true;
  renderMath();
  d.scrollIntoView({block:'start', behavior:'smooth'});
  d.classList.add('flash');
  setTimeout(function(){ d.classList.remove('flash'); }, 1600);
});
"""


def chip(n, ex=False):
    return f'<a class="pchip{" ex" if ex else ""}" href="#p{n}" data-p="{n}">P{n}</a>'


