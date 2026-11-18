# -*- coding: utf-8 -*-
# Renders the "Top 15 formulas" tab in English and Russian with a language switch.
# Formula data and problem tags live in ex4_top.py; English text lives here in EN.
import ex4_top as T

EN = T.EN

UI = {
    "ru": dict(problems="задач", spot="Как узнать задачу", solve="Как решать", example="Разбор на реальной задаче",
               answer="Ответ", all="Все задачи на эту формулу (нажми — откроется решение)",
               intro=lambda total: f"""<p>Я прошёлся по всем <b>{total}</b> задачам четвёртой мидки и для каждой отметил, какие формулы нужны для решения.
Ниже — сколько задач держится на каждой формуле. В одной задаче бывает 2–3 формулы, поэтому проценты в сумме больше 100.</p>""",
               s5="задач ({p}%) — хотя бы одна из 5 главных формул", s15="задач ({p}%) — покрывают все 15",
               seasy="задач решаются ОДНОЙ формулой — начни с них",
               plan="<b>План, если времени мало:</b> выучи 5 формул сверху → на экзамене ищи слова из «Как узнать задачу» → решай по шагам «Как решать». Сначала бери задачи из списка «лёгкие» в самом низу.",
               h5="🔥 5 обязательных формул", h10="⭐ Ещё 10 важных",
               heasy="✅ Лёгкие задачи — одна формула, один шаг",
               peasy="Если надо решить хоть что-то — начни с этих. Нажми номер, откроется решение.",
               units=T.UNITS_RU),
    "en": dict(problems="problems", spot="How to spot it", solve="How to solve it", example="Worked example",
               answer="Answer", all="Every problem that uses it (tap to open the solution)",
               intro=lambda total: f"""<p>I went through all <b>{total}</b> Exam 4 problems and marked which formulas each one needs.
Below is how many problems rely on each formula. A problem often needs 2–3 formulas, so the percentages add up to more than 100.</p>""",
               s5="problems ({p}%) use at least one of the top 5", s15="problems ({p}%) are covered by all 15",
               seasy="problems take just ONE formula — start there",
               plan="<b>Short on time?</b> Learn the top 5 → on the exam, look for the words under “How to spot it” → follow “How to solve it”. Start with the easy problems listed at the very bottom.",
               h5="🔥 The 5 must-know formulas", h10="⭐ 10 more important ones",
               heasy="✅ Easy problems — one formula, one step",
               peasy="If you need to solve at least something, start here. Tap a number to open its solution.",
               units=T.UNITS_EN),
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
    try { localStorage.setItem('ex4-top-lang', l); } catch(e) {}
  }
  var saved = null;
  try { saved = localStorage.getItem('ex4-top-lang'); } catch(e) {}
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
