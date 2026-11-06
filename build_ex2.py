# -*- coding: utf-8 -*-
import json
from pathlib import Path

CSS = r"""
:root{
  --bg:#f2efe6; --surface:#ffffff; --ink:#23262b; --ink-muted:#63666f;
  --accent:#35625c; --accent-soft:#e3ebe7; --accent-2:#a9781f; --accent-2-soft:#f2e9d3;
  --rule:#ddd7c8; --story-bg:#fbf9f3; --warn:#a1432b; --warn-soft:#f6e6de;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#1b1d1f; --surface:#242729; --ink:#e8e6df; --ink-muted:#9a9d9f;
    --accent:#7bb0a5; --accent-soft:#26332f; --accent-2:#dcae54; --accent-2-soft:#33291a; --rule:#37393c; --story-bg:#20232a;
    --warn:#e08a6c; --warn-soft:#3a271f;
  }
}
:root[data-theme="dark"]{
  --bg:#1b1d1f; --surface:#242729; --ink:#e8e6df; --ink-muted:#9a9d9f;
  --accent:#7bb0a5; --accent-soft:#26332f; --accent-2:#dcae54; --accent-2-soft:#33291a; --rule:#37393c; --story-bg:#20232a;
  --warn:#e08a6c; --warn-soft:#3a271f;
}
*{box-sizing:border-box; -webkit-tap-highlight-color:transparent;}
html,body{margin:0; background:var(--bg); color-scheme:light dark;}
body{color:var(--ink); font-family:"IBM Plex Sans", system-ui, sans-serif; padding:0 18px; font-size:19px;}
.wrap{max-width:860px; margin:0 auto; padding-block:22px 80px; display:flex; flex-direction:column; gap:18px; width:100%;}
h1{font-family:"Fraunces", Georgia, serif; text-wrap:balance; margin:0; font-size:clamp(26px,5.5vw,34px); font-weight:700; line-height:1.2;}
h2{font-family:"Fraunces", Georgia, serif; margin:0; font-size:clamp(22px,5vw,28px); font-weight:600;}
h3{font-family:"Fraunces", Georgia, serif; margin:0; font-size:clamp(18px,4.2vw,21px); font-weight:600; color:var(--accent);}
.mono{font-family:"IBM Plex Mono", monospace;}
.eyebrow{font-family:"IBM Plex Mono",monospace; font-size:13px; letter-spacing:.1em; text-transform:uppercase; color:var(--accent); font-weight:500;}
.tabs{
  display:flex; gap:4px; overflow-x:auto; -webkit-overflow-scrolling:touch;
  position:sticky; top:0; background:var(--bg); padding:8px 0; z-index:5;
  border-bottom:1px solid var(--rule); margin:0 -18px; padding-inline:18px;
}
.tab-btn{
  font-family:"IBM Plex Sans",sans-serif; font-size:14px; font-weight:600; white-space:nowrap; flex:0 0 auto;
  padding:11px 13px; border:none; background:none; color:var(--ink-muted); cursor:pointer;
  border-bottom:2px solid transparent; margin-bottom:-1px; border-radius:8px 8px 0 0; min-height:44px;
}
.tab-btn .qn{font-family:"IBM Plex Mono",monospace; color:var(--accent); margin-right:5px; font-size:12px;}
.tab-btn.active{color:var(--accent); border-bottom-color:var(--accent); background:var(--accent-soft);}
.tab-panel{display:none; flex-direction:column; gap:16px; min-width:0;}
.tab-panel.active{display:flex;}
.story{
  background:var(--story-bg); border:1px solid var(--rule); border-radius:16px;
  padding:22px clamp(16px,4vw,28px); display:flex; flex-direction:column; gap:14px;
  font-size:18.5px; line-height:1.75; max-width:100%; min-width:0;
}
.story h3{margin-top:6px;}
.story p{margin:0;}
.story b{color:var(--accent);}
.kid{
  background:var(--accent-soft); border-radius:12px; padding:14px 16px; font-size:17.5px;
  border-left:4px solid var(--accent); line-height:1.65;
}
.warn{
  background:var(--warn-soft); border-radius:12px; padding:14px 16px; font-size:16.5px;
  border-left:4px solid var(--warn); line-height:1.65;
}
.warn b{color:var(--warn);}
.warn ul{margin:8px 0 0; padding-left:22px; display:flex; flex-direction:column; gap:6px;}
.story ol.steps{margin:0; padding-left:24px; display:flex; flex-direction:column; gap:8px; font-size:17.5px;}
.story ol.steps li::marker{color:var(--accent); font-weight:600;}
.refs{
  font-family:"IBM Plex Mono",monospace; font-size:13.5px; color:var(--accent-2);
  background:var(--accent-2-soft); display:inline-block; padding:4px 11px; border-radius:7px; margin-top:2px;
}
.fbox{
  background:var(--surface); border:1px solid var(--rule); border-radius:14px;
  padding:18px 14px 14px; margin:4px 0; min-width:0; max-width:100%;
}
.fbox .eqwrap{overflow-x:auto; overflow-y:hidden; padding-bottom:4px; -webkit-overflow-scrolling:touch;}
.fbox .eqwrap .katex-display{margin:4px 0;}
.fbox .eqwrap .katex{font-size:1.55em;}
.flegend{margin-top:12px; font-size:15.5px; color:var(--ink-muted); line-height:1.6; text-align:left;}
.flegend b{color:var(--ink);}
hr.soft{border:none; border-top:1px solid var(--rule); margin:4px 0;}
details.ref{border:1px solid var(--rule); border-radius:12px; background:var(--surface); overflow:hidden; min-width:0;}
.sec-divider{
  display:flex; align-items:baseline; gap:12px; margin:22px 0 10px; padding-bottom:8px;
  border-bottom:2px solid var(--accent-soft);
}
.sec-divider:first-of-type{margin-top:4px;}
.sec-divider h3{margin:0; font-size:20px;}
.sec-divider .range{color:var(--ink-muted); font-size:13.5px;}
details.prob{
  border:1px solid var(--rule); border-radius:12px; background:var(--surface);
  margin-bottom:9px; overflow:hidden; min-width:0;
}
details.prob > summary{
  list-style:none; cursor:pointer; padding:14px 16px; display:flex; align-items:baseline;
  gap:10px; flex-wrap:wrap; font-size:16.5px; line-height:1.45;
}
details.prob > summary::-webkit-details-marker{display:none;}
details.prob > summary::before{content:"▸"; color:var(--ink-muted); transition:transform .15s; flex:0 0 auto; font-size:18px;}
details.prob[open] > summary::before{transform:rotate(90deg);}
details.prob .pn{color:var(--accent); font-weight:700; font-size:15px; flex:0 0 auto;}
details.prob .ptext{flex:1 1 260px; min-width:0;}
details.prob .ans-badge{
  margin-left:auto; font-size:14px; color:var(--accent-2); background:var(--accent-2-soft);
  padding:4px 10px; border-radius:6px; flex:0 0 auto; font-weight:600;
}
.solution{padding:4px 18px 18px;}
.step-intro{margin:0 0 14px; font-size:17px; color:var(--ink); line-height:1.65; font-style:normal; background:var(--accent-soft); padding:12px 14px; border-radius:10px;}
ol.sol-steps{margin:0; padding-left:26px; display:flex; flex-direction:column; gap:14px;}
ol.sol-steps li{font-size:17px;}
ol.sol-steps li .eqwrap{overflow-x:auto; -webkit-overflow-scrolling:touch; margin-bottom:5px;}
ol.sol-steps li .eqwrap .katex{font-size:1.45em;}
ol.sol-steps li .stepnote{color:var(--ink-muted); font-size:15.5px; line-height:1.55;}
details.ref > summary{list-style:none; cursor:pointer; padding:14px 16px; font-weight:600; font-size:16px; display:flex; align-items:center; gap:8px;}
details.ref > summary::-webkit-details-marker{display:none;}
details.ref > summary::after{content:"▸"; margin-left:auto; color:var(--ink-muted); transition:transform .15s;}
details.ref[open] > summary::after{transform:rotate(90deg);}
.fbody{display:flex; flex-direction:column; gap:2px; padding:0 16px 16px;}
.frow{padding:12px 0; border-top:1px solid var(--rule); font-size:16.5px; min-width:0;}
.frow .eqwrap{overflow-x:auto; -webkit-overflow-scrolling:touch;}
.frow .eqwrap .katex{font-size:1.4em;}
.fbody .frow:first-of-type{border-top:none;}
.frow .note{font-size:15px; color:var(--ink-muted); margin-top:5px;}
.pbody{padding:0 16px 10px;}
ol.problems{list-style:none; margin:0; padding:0; display:flex; flex-direction:column;}
ol.problems li{display:grid; grid-template-columns:42px 1fr; gap:12px; padding:12px 0; border-top:1px solid var(--rule); font-size:16px; line-height:1.55;}
ol.problems li:first-child{border-top:none;}
ol.problems li .pn{font-family:"IBM Plex Mono",monospace; color:var(--accent); font-weight:700; font-size:14px;}
ol.problems li .ans{display:inline-block; margin-top:6px; font-family:"IBM Plex Mono",monospace; font-size:14px; color:var(--accent-2); background:var(--accent-2-soft); padding:3px 9px; border-radius:6px; font-weight:600;}
footer{color:var(--ink-muted); font-size:14px; text-align:center; padding-top:10px; border-top:1px solid var(--rule);}
@media (max-width:420px){
  body{font-size:17.5px;}
  .story{font-size:17px; padding:16px 13px;}
  .fbox .eqwrap .katex{font-size:1.25em;}
}
"""

def esc(s):
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

def fbox(latex, legend):
    return f'<div class="fbox"><div class="eqwrap">\\\\[{latex}\\\\]</div><div class="flegend">{legend}</div></div>'

def prob_html(n, q, ans, intro, steps):
    lis = []
    for eq, note in steps:
        lis.append(
            f'<li><div class="eqwrap">\\\\({eq}\\\\)</div><div class="stepnote">{note}</div></li>'
        )
    return (
        f'<details class="prob"><summary><span class="pn mono">P{n}</span>'
        f'<span class="ptext">{q}</span><span class="ans-badge mono">{ans}</span></summary>'
        f'<div class="solution"><p class="step-intro">{intro}</p>'
        f'<ol class="sol-steps">{"".join(lis)}</ol></div></details>'
    )

# (n, q, ans, intro, [(eq, note), ...])
PROBLEMS = []

def add(n, q, ans, intro, steps):
    PROBLEMS.append((n, q, ans, intro, steps))

# ========== WORK ==========
add(1, "Determine the work necessary to push (not pull) a mass of 66.5 kg horizontally at a distance of 2.6 m by a force of 73.8 N on a horizontal frictionless surface.", "191.88 J",
    "Представь: ты толкаешь коробку ровно вперёд. Сила смотрит туда же, куда едет коробка — значит вся сила «работает». Масса тут вообще не нужна: трения нет, угол = 0°.",
    [(r"W=F\,d=73.8\times 2.6=191.88\ \text{J}", "работа = сила × путь, потому что cos0°=1")])

add(2, "Determine the work necessary to push a mass of 25 kg a distance of 3.4 m along a horizontal frictionless surface by a force of 73 N directed at an angle of 20° below the horizontal.", "233.232 J",
    "Сила смотрит чуть вниз. Только «горизонтальный кусочек» силы толкает коробку вперёд. Этот кусочек = F cos20°.",
    [(r"W=F\cos 20^\circ\cdot d=73\cos 20^\circ\cdot 3.4\approx 233.232\ \text{J}", "берём только часть силы вдоль пути")])

add(3, "Find the magnitude of work to be done lifting the mass of 1.5 kg from height 0.3 m up to 1.4 m. g=9.8 m/s².", "16.17 J",
    "Ты поднимаешь игрушку выше. Насколько выше? На Δh. Работа против гравитации = вес × подъём.",
    [(r"\Delta h=1.4-0.3=1.1\ \text{m}", "на сколько подняли"),
     (r"|W|=mg\Delta h=1.5\times 9.8\times 1.1=16.17\ \text{J}", "сила тяжести × высота подъёма")])

add(4, "A small particle of mass 400 g is pulled to the top of a frictionless half-cylinder of radius 1 m by a cord at constant speed. Find the work done by F. g=9.8.", "3.92 J",
    "Скорость постоянная → кинетическая энергия не меняется. Значит работа силы F ровно отменяет работу тяжести. Частица поднялась на высоту R (с низа полукруга на верх).",
    [(r"m=0.4\ \text{kg}", "граммы → килограммы"),
     (r"W_F=-W_g=mgR=0.4\times 9.8\times 1=3.92\ \text{J}", "F делает положительную работу, равную mgR")])

add(5, "A small particle of mass 0.6 kg is pulled at constant speed to the top of a frictionless half-cylinder of radius 1.55 m. Find the work done by gravity. g=9.8.", "−9.114 J",
    "Гравитация всегда тянет вниз, а частица едет вверх — значит гравитация «мешает» и делает отрицательную работу.",
    [(r"W_g=-mgR=-0.6\times 9.8\times 1.55=-9.114\ \text{J}", "минус, потому что сила и путь «в разные стороны» по высоте")])

add(6, "When a 4.5 kg object is hung on a spring, it stretches 1.5 cm. If removed, how much work must an external agent do to stretch the same spring 4.5 cm from unstretched? g=9.8.", "2.97675 J",
    "Сначала по весу находим «жёсткость» пружины k (как тугая резинка). Потом работа на растяжение = ½kx².",
    [(r"x_1=0.015\ \text{m},\quad mg=kx_1\Rightarrow k=\dfrac{4.5\times 9.8}{0.015}=2940\ \text{N/m}", "вес растянул пружину — нашли k"),
     (r"W=\tfrac12 k x_2^2=\tfrac12\cdot 2940\cdot(0.045)^2=2.97675\ \text{J}", "работа внешней силы на растяжение")])

add(7, "A woman steps on a bathroom scale. Spring compressed 1 cm, total work on the spring is 3.1 J. Find her mass. g=9.8.", "63.265306122449 kg",
    "Работа на сжатие пружины = ½kx². Из неё находим k, потом из равновесия mg=kx находим массу.",
    [(r"W=\tfrac12 kx^2\Rightarrow k=\dfrac{2W}{x^2}=\dfrac{2\cdot 3.1}{(0.01)^2}=62000\ \text{N/m}", "из работы → k"),
     (r"m=\dfrac{kx}{g}=\dfrac{62000\cdot 0.01}{9.8}\approx 63.265\ \text{kg}", "в равновесии вес = сила пружины")])

add(8, "A woman of mass 80.5 kg steps on a scale. Spring compressed 1.35 cm. Find total work done on the spring. g=9.8.", "5.32508 J",
    "Сначала k из равновесия, потом работа ½kx².",
    [(r"k=\dfrac{mg}{x}=\dfrac{80.5\times 9.8}{0.0135}\approx 58437\ \text{N/m}", "нашли жёсткость"),
     (r"W=\tfrac12 kx^2\approx 5.32508\ \text{J}", "работа сжатия пружины")])

add(9, "Farmer pulls a sled 20 m. Tractor force 4700 N at 34.2° above horizontal, friction 3400 N. Find total work by all forces.", "9745.5739818088 J",
    "Сложи работы всех сил. Вес и нормаль перпендикулярны пути → их работа 0. Остаются трактор и трение.",
    [(r"W_F=F\cos\theta\cdot d=4700\cos 34.2^\circ\cdot 20", "горизонтальная часть силы трактора"),
     (r"W_f=-f d=-3400\cdot 20", "трение против движения"),
     (r"W_\text{tot}=W_F+W_f\approx 9745.57\ \text{J}", "сумма работ = полная работа")])

add(10, "Farmer pulls sled 19.5 m. Friction 3750 N opposing. Find work done by friction.", "−73125 J",
    "Трение всегда против пути. Работа = − (сила трения)×путь.",
    [(r"W_f=-f d=-3750\times 19.5=-73125\ \text{J}", "минус обязателен")])

add(11, "Two forces of equal magnitude 7 N move an object on a horizontal surface a distance d=8.5 m. Determine the work required.", "84.1457 J",
    "На картинке обычно две одинаковые силы под углом 45° к пути (или симметрично). В работу идёт только часть вдоль пути: каждая даёт F cos45°.",
    [(r"W=2\cdot F\cdot d\cdot\cos 45^\circ=2\cdot 7\cdot 8.5\cdot\dfrac{\sqrt2}{2}\approx 84.1457\ \text{J}", "две силы, у каждой «полезная» часть F/√2")])

add(12, "Luggage handler pulls 24-kg suitcase up ramp 29° by force F=165 N parallel to ramp, μk=0.36, distance 3.1 m. Work by F?", "511.5 J",
    "Сила F параллельна пандусу — значит угол с путём 0°. Работа силы F просто F×d. Трение и масса для ЭТОГО вопроса не нужны!",
    [(r"W_F=F d=165\times 3.1=511.5\ \text{J}", "сила вдоль пути → просто умножь")])

add(13, "18-kg suitcase up ramp 28°, F=195 N parallel, μk=0.35, travels 3.5 m. Work by friction? g=9.8.", "−190.796 J",
    "Трение = μk × N. На пандусе N = mg cosθ (не весь вес!). Работа трения отрицательная.",
    [(r"N=mg\cos 28^\circ", "нормаль на наклонной"),
     (r"f=\mu_k N=0.35\cdot 18\cdot 9.8\cos 28^\circ", "сила трения"),
     (r"W_f=-f d\approx -190.796\ \text{J}", "против движения → минус")])

add(14, "18-kg suitcase up ramp 31°, travels 4.1 m. Magnitude of work by gravity? g=9.8.", "372.49613729795 J",
    "Гравитация меняет только высоту. Высота = d sinθ. |W_g|=mgh.",
    [(r"h=d\sin 31^\circ=4.1\sin 31^\circ", "насколько поднялись"),
     (r"|W_g|=mgh=18\times 9.8\times h\approx 372.496\ \text{J}", "magnitude = без знака минус")])

# ========== KINETIC ENERGY ==========
add(15, "In a gun, 11 g bullet accelerated from rest to 751 m/s over 37 cm. Magnitude of average net force?", "8383.7986486486 N",
    "Пуля получает кинетическую энергию. Эта энергия = работа силы = F×d. Значит F = K/d.",
    [(r"m=0.011\ \text{kg},\ d=0.37\ \text{m}", "в СИ"),
     (r"K=\tfrac12 mv^2=\tfrac12\cdot 0.011\cdot 751^2", "энергия пули"),
     (r"F=\dfrac{K}{d}\approx 8383.80\ \text{N}", "работа = сила × путь")])

add(16, "17.5 g bullet from rest to 756 m/s over 61.5 cm. Time inside the gun?", "0.00162698 s",
    "Разгон равномерный: средняя скорость = v/2. Время = путь / средняя скорость.",
    [(r"d=0.615\ \text{m}", "см → м"),
     (r"t=\dfrac{d}{v/2}=\dfrac{2d}{v}=\dfrac{2\cdot 0.615}{756}\approx 0.001627\ \text{s}", "из покоя средняя скорость половина")])

add(17, "11 g bullet from rest to 754 m/s. Work done on the bullet?", "3126.84 J",
    "Работа = прирост кинетической энергии. Было 0, стало ½mv².",
    [(r"W=\tfrac12 mv^2=\tfrac12\cdot 0.011\cdot 754^2=3126.84\ \text{J}", "теорема о кинетической энергии")])

add(18, "Meteor mass 1.6×10⁸ kg hits at 12 km/s. Kinetic energy delivered?", "1.152E+16 J",
    "Просто ½mv², но скорость в м/с: 12 км/с = 12000 м/с.",
    [(r"v=12000\ \text{m/s}", "км/с → м/с"),
     (r"K=\tfrac12\cdot 1.6\times 10^8\cdot 12000^2=1.152\times 10^{16}\ \text{J}", "огромная энергия")])

add(19, "Proton mass = 1836 × electron mass. Electron KE = 3.55×10⁻¹⁶ J. Proton same speed — its KE?", "6.5178E-13 J",
    "Одинаковая скорость → кинетическая энергия пропорциональна массе. Протон тяжелее в 1836 раз → энергия больше в 1836 раз.",
    [(r"K_p=1836\cdot K_e=1836\cdot 3.55\times 10^{-16}=6.5178\times 10^{-13}\ \text{J}", "K ∝ m при одном v")])

add(20, "Proton mass = 1836 × electron. Electron KE = 4.3×10⁻¹⁶ J. Same momentum — proton KE?", "2.34205e-19 J",
    "Одинаковый импульс p. Но K=p²/(2m). Протон тяжелее → при том же p энергия МЕНЬШЕ в 1836 раз.",
    [(r"K=\dfrac{p^2}{2m}\Rightarrow K_p=\dfrac{K_e}{1836}\approx 2.342\times 10^{-19}\ \text{J}", "тяжелее → медленнее при том же p")])

add(21, "Proton speed 1×10⁶ m/s. Electron same KE — what speed?", "42848570.57 m/s",
    "½ m_e v_e² = ½ m_p v_p² → v_e = v_p √(m_p/m_e) = v_p √1836.",
    [(r"v_e=v_p\sqrt{1836}=10^6\sqrt{1836}\approx 4.285\times 10^7\ \text{m/s}", "электрон легче → должен лететь быстрее")])

add(22, "Proton speed 5.5×10⁴ m/s. Electron same momentum — speed?", "1.0098e+08 m/s",
    "m_e v_e = m_p v_p → v_e = v_p × 1836.",
    [(r"v_e=1836\cdot 5.5\times 10^4\approx 1.0098\times 10^8\ \text{m/s}", "тот же импульс, масса крошечная → огромная скорость")])

add(23, "4 kg object velocity (2î+2ĵ) → (8î+5ĵ) m/s. Net work?", "162 J",
    "Работа = изменение кинетической энергии. Считай K до и K после (скорость = длина вектора).",
    [(r"v_i^2=2^2+2^2=8,\quad v_f^2=8^2+5^2=89", "квадрат скорости = сумма квадратов компонент"),
     (r"W=\Delta K=\tfrac12 m(v_f^2-v_i^2)=\tfrac12\cdot 4\cdot(89-8)=162\ \text{J}", "теорема работ-энергии")])

add(24, "2 kg object (2î+1ĵ) → (7î+8ĵ) m/s. Magnitude of change in momentum?", "17.2047 kg m/s",
    "Импульс p=mv. Изменение Δp = m(v_f − v_i). Потом длина этого вектора.",
    [(r"\Delta\vec v=(5\hat i+7\hat j)\ \text{m/s}", "разность скоростей"),
     (r"|\Delta p|=m\sqrt{5^2+7^2}=2\sqrt{74}\approx 17.205\ \text{kg·m/s}", "модуль изменения импульса")])

add(25, "Professor+chair 87 kg pushed 2.6 m up 26° ramp by horizontal 500 N. Bottom speed 2.4 m/s. Speed at top? Frictionless. g=9.8.", "3.206 m/s",
    "Энергия: работа студентов = прирост K + прирост U. Сила горизонтальная, путь по наклонной → угол между ними = 26°.",
    [(r"W=F\cos 26^\circ\cdot d", "работа горизонтальной силы на наклонном пути"),
     (r"W=\Delta K+\Delta U=\tfrac12 m(v^2-v_0^2)+mg(d\sin 26^\circ)", "куда ушла работа"),
     (r"v\approx 3.206\ \text{m/s}", "решаем уравнение относительно v")])

# ========== POWER ==========
add(26, "Electric engine pulls 1800 kg block at constant 2.86 m/s up 21° incline, μk=0.69. Power? g=9.8.", "50578.47 W",
    "Скорость постоянная → сила двигателя = сила «мешалки» (тяжесть вдоль склона + трение). Мощность = F×v.",
    [(r"F=mg\sin\theta+\mu_k mg\cos\theta", "сила вверх по склону"),
     (r"P=Fv\approx 50578\ \text{W}", "мощность при постоянной скорости")])

add(27, "Waterfall 62 m high, water rate 5.4×10⁵ kg/s. Electrical power if all PE converted? g=9.8.", "328104000 W",
    "Каждый килограмм воды «приносит» энергию mgh. За секунду приходит (dm/dt)·gh ватт.",
    [(r"P=\dot m\, g h=5.4\times 10^5\cdot 9.8\cdot 62=3.28104\times 10^8\ \text{W}", "мощность = энергия в секунду")])

add(28, "Waterfall 81 m produces 43 MW. Average water rate? g=9.8.", "54169.8 kg/s",
    "Наоборот: из P = ṁgh находим ṁ.",
    [(r"\dot m=\dfrac{P}{gh}=\dfrac{43\times 10^6}{9.8\cdot 81}\approx 54169.8\ \text{kg/s}", "сколько кг воды в секунду")])

add(29, "Heart pumps 7450 liters/day of blood, lift height 1.77 m, density 1.05×10³ kg/m³. Power in watts? g=9.8. 1 L=0.001 m³.", "1.571 W",
    "Сначала масса крови за день, потом работа mgh, потом делим на секунды в сутках.",
    [(r"V=7450\times 0.001=7.45\ \text{m}^3,\ m=\rho V", "объём → масса"),
     (r"W=mgh,\quad P=\dfrac{W}{86400}\approx 1.571\ \text{W}", "работа за день / 86400 с")])

# ========== POTENTIAL ENERGY ==========
add(30, "U(x)=α x⁴, α=2.7 J/m⁴. Force magnitude at x=−0.2 m?", "0.0864 N",
    "Сила = минус производная потенциальной энергии. Как горка: сила толкает «вниз с горки».",
    [(r"F=-\dfrac{dU}{dx}=-4\alpha x^3", "правило: F = −dU/dx"),
     (r"|F|=4\cdot 2.7\cdot(0.2)^3=0.0864\ \text{N}", "подставили x=−0.2, взяли модуль")])

add(31, "U(x)=α x⁴, α=2.6. Work by this force from x=1.3 m to x=0.2 m?", "7.4217 J",
    "Для консервативной силы работа = −ΔU = U_начало − U_конец.",
    [(r"W=U(1.3)-U(0.2)=\alpha(1.3^4-0.2^4)\approx 7.4217\ \text{J}", "спустились по «горке» U — сила сделала положительную работу")])

add(32, "F=(2x+6) N on 5 kg particle, x=1→8 m. Change in potential energy?", "−105 J",
    "ΔU = −W = −∫F dx. Сила положительная и толкает в сторону движения → потенциал падает.",
    [(r"\Delta U=-\int_1^8(2x+6)\,dx=-\big[x^2+6x\big]_1^8=-105\ \text{J}", "интеграл силы со знаком минус")])

add(33, "F=(2x+4) N, x=2.5→9.5 m. Work by this force?", "112 J",
    "Работа = ∫F dx (без минуса — просят именно работу силы).",
    [(r"W=\int_{2.5}^{9.5}(2x+4)\,dx=\big[x^2+4x\big]_{2.5}^{9.5}=112\ \text{J}", "площадь под графиком F(x)")])

add(34, "F(x)=1.3x²+4x. Find U(x) at x=8 m, U(0)=0.", "−349.867 J",
    "U(x)= −∫F dx от 0 до x.",
    [(r"U(8)=-\int_0^8(1.3x^2+4x)\,dx=-\big[0.4333x^3+2x^2\big]_0^8\approx -349.867\ \text{J}", "потенциал падает, если сила толкает в +x")])

add(35, "F(x)=1.5x²+3x. Magnitude of force at x=7 m?", "94.5 N",
    "Просто подставь x=7 в формулу силы. Никакой энергии тут нет.",
    [(r"F(7)=1.5\cdot 49+3\cdot 7=73.5+21=94.5\ \text{N}", "подстановка в F(x)")])

if __name__ == "__main__":
    print("work-KE-power-PE:", len(PROBLEMS))
    Path(r"d:\phys161\_ex2_part1.json").write_text(
        json.dumps(PROBLEMS, ensure_ascii=False), encoding="utf-8"
    )
    print("saved part1", len(PROBLEMS))
