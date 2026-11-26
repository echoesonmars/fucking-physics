# -*- coding: utf-8 -*-
"""Exam 4 page: full problems in every topic tab, one shared "solved" state, and navigation.

- Each topic tab gets copies of its problem cards from the "Все задачи" tab (same markup, so solutions work the same).
- The "Решил" checkbox is keyed by problem number: ticking it in any tab ticks every copy, and the
  progress bar, number grid and tab counters update together. Stored in localStorage 'ex4-solved'.
- Number grid at the top of each problem tab, a floating bar (go to P#, next unsolved, up),
  and the page remembers the tab + problem you were on ('ex4-where') and brings you back there.
"""

CSS = r"""
.pgrid{display:flex; flex-wrap:wrap; gap:6px; margin:10px 0 18px;}
.pgrid a{font-family:"IBM Plex Mono",monospace; font-size:13px; min-width:40px; text-align:center; padding:5px 6px;
  border:1px solid var(--rule); color:var(--ink-muted); text-decoration:none; background:transparent;}
.pgrid a:hover{border-color:#8c8c8c; color:var(--ink);}
.pgrid a.on{background:#ffffff; color:#0a0a0a; border-color:#ffffff;}
.pgrid .gl{width:100%; font-size:12px; letter-spacing:.06em; text-transform:uppercase; color:var(--ink-muted); margin-top:6px;}
.tab-btn .tcount{font-family:"IBM Plex Mono",monospace; font-size:11px; margin-left:6px; opacity:.7;}
.tab-btn .tcount.full{opacity:1;}
.topicprog{font-size:15px; color:var(--ink-muted); margin:18px 0 4px;}
.topicprog b{color:var(--ink);}
.navbar{position:fixed; right:14px; bottom:14px; z-index:50; display:flex; gap:6px; align-items:center;
  background:#121212; border:1px solid #3a3a3a; padding:6px; box-shadow:0 6px 24px rgba(0,0,0,.6);}
.navbar input{width:64px; background:#0a0a0a; color:#ededed; border:1px solid #3a3a3a; padding:7px 8px;
  font-family:"IBM Plex Mono",monospace; font-size:14px;}
.navbar button{background:#0a0a0a; color:#ededed; border:1px solid #3a3a3a; padding:7px 10px; font-size:14px; cursor:pointer;
  font-family:"IBM Plex Sans",system-ui,sans-serif;}
.navbar button:hover{border-color:#ffffff;}
.task.flash{outline:2px solid #ffffff; outline-offset:4px; transition:outline-color .6s;}
.toast{position:fixed; left:50%; bottom:70px; transform:translateX(-50%); z-index:60; background:#ffffff; color:#0a0a0a;
  padding:9px 14px; font-size:15px; font-weight:600; opacity:0; transition:opacity .3s; pointer-events:none;}
.toast.show{opacity:1;}
@media (max-width:640px){ .navbar{left:10px; right:10px; justify-content:space-between;} .navbar input{flex:1;} }
"""

JS = r"""
(function(){
  var KEY = 'ex4-solved', WHERE = 'ex4-where';
  var TOPICS = window.EX4_TOPICS || [];   // [{id, nums}]
  var done = {};
  try { (JSON.parse(localStorage.getItem(KEY) || '[]')).forEach(function(n){ done[n] = true; }); } catch(e) {}

  var solPanel = document.getElementById('panel-solutions');
  var ALL = [];
  solPanel.querySelectorAll('.task').forEach(function(t){ ALL.push(+t.id.slice(1)); });

  function gridHtml(nums, groups){
    var out = '';
    (groups || [{title: '', nums: nums}]).forEach(function(g){
      if (g.title) out += '<div class="gl">' + g.title + '</div>';
      out += g.nums.map(function(n){ return '<a href="#p' + n + '" data-go="' + n + '">' + n + '</a>'; }).join('');
    });
    return '<div class="pgrid">' + out + '</div>';
  }

  // 1. Topic tabs: copy the full problem cards in, with a number grid and a progress line.
  TOPICS.forEach(function(t){
    var panel = document.getElementById('panel-' + t.id);
    if (!panel) return;
    var box = document.createElement('div');
    box.innerHTML = '<div class="topicprog">Задачи темы: решено <b class="tp">0</b> из ' + t.nums.length + '</div>' + gridHtml(t.nums);
    t.nums.forEach(function(n){
      var src = document.getElementById('p' + n);
      if (!src) return;
      var c = src.cloneNode(true);
      c.id = 'p' + n + '-' + t.id;
      c.dataset.n = n;
      box.appendChild(c);
    });
    panel.appendChild(box);
  });

  // Grid in "Все задачи", grouped by section dividers.
  var groups = [], cur = null;
  Array.prototype.forEach.call(solPanel.querySelectorAll('.sec-divider, .task'), function(el){
    if (el.classList.contains('sec-divider')) { cur = {title: el.querySelector('h3').textContent, nums: []}; groups.push(cur); }
    else if (cur) cur.nums.push(+el.id.slice(1));
  });
  var prog = solPanel.querySelector('.progress');
  if (prog) prog.insertAdjacentHTML('afterend', gridHtml(ALL, groups));

  // 2. Shared solved state.
  function paint(){
    document.querySelectorAll('.done input').forEach(function(b){
      var on = !!done[b.dataset.n];
      b.checked = on;
      b.closest('.task').classList.toggle('solved', on);
    });
    var c = ALL.filter(function(n){ return done[n]; }).length;
    document.querySelectorAll('.progress b').forEach(function(el){ el.textContent = c + ' / ' + ALL.length; });
    document.querySelectorAll('.progress .pbar i').forEach(function(el){ el.style.width = (100 * c / ALL.length) + '%'; });
    document.querySelectorAll('.pgrid a').forEach(function(a){ a.classList.toggle('on', !!done[a.dataset.go]); });
    TOPICS.forEach(function(t){
      var k = t.nums.filter(function(n){ return done[n]; }).length;
      var btn = document.querySelector('.tab-btn[data-tab="' + t.id + '"]');
      if (btn) {
        var s = btn.querySelector('.tcount');
        if (!s) { s = document.createElement('span'); s.className = 'tcount'; btn.appendChild(s); }
        s.textContent = k + '/' + t.nums.length;
        s.classList.toggle('full', k === t.nums.length);
      }
      var tp = document.querySelector('#panel-' + t.id + ' .tp');
      if (tp) tp.textContent = k;
    });
    var sb = document.querySelector('.tab-btn[data-tab="solutions"]');
    if (sb) {
      var s2 = sb.querySelector('.tcount');
      if (!s2) { s2 = document.createElement('span'); s2.className = 'tcount'; sb.appendChild(s2); }
      s2.textContent = c + '/' + ALL.length;
    }
  }
  document.addEventListener('change', function(e){
    var b = e.target;
    if (!b.matches || !b.matches('.done input')) return;
    if (b.checked) done[b.dataset.n] = true; else delete done[b.dataset.n];
    try { localStorage.setItem(KEY, JSON.stringify(Object.keys(done))); } catch(err) {}
    paint();
  });
  paint();

  // 3. Navigation.
  function activePanel(){ return document.querySelector('.tab-panel.active'); }
  function openTab(id){
    var btn = document.querySelector('.tab-btn[data-tab="' + id + '"]');
    if (btn && !btn.classList.contains('active')) btn.click();
  }
  function cardIn(panel, n){
    return panel && (panel.querySelector('.task[data-n="' + n + '"]') || (panel.id === 'panel-solutions' && document.getElementById('p' + n)));
  }
  function go(n, smooth){
    n = +n;
    if (ALL.indexOf(n) < 0) { toast('Нет задачи P' + n); return; }
    var el = cardIn(activePanel(), n);
    if (!el) { openTab('solutions'); el = document.getElementById('p' + n); }
    el.scrollIntoView({block: 'start', behavior: smooth === false ? 'auto' : 'smooth'});
    el.classList.add('flash');
    setTimeout(function(){ el.classList.remove('flash'); }, 1200);
  }
  window.ex4Go = go;
  var toastEl = document.createElement('div'); toastEl.className = 'toast'; document.body.appendChild(toastEl);
  var tt;
  function toast(msg){ toastEl.textContent = msg; toastEl.classList.add('show'); clearTimeout(tt); tt = setTimeout(function(){ toastEl.classList.remove('show'); }, 2200); }

  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('.pgrid a');
    if (!a) return;
    e.preventDefault();
    go(a.dataset.go);
  });

  var bar = document.createElement('div');
  bar.className = 'navbar';
  bar.innerHTML = '<input type="number" min="1" max="150" placeholder="P№" aria-label="Номер задачи"/>' +
                  '<button data-a="go">Перейти</button><button data-a="next">Нерешённая ▶</button><button data-a="up">↑</button>';
  document.body.appendChild(bar);
  var inp = bar.querySelector('input');
  inp.addEventListener('keydown', function(e){ if (e.key === 'Enter' && inp.value) go(inp.value); });
  bar.addEventListener('click', function(e){
    var a = e.target.dataset && e.target.dataset.a;
    if (a === 'go' && inp.value) go(inp.value);
    if (a === 'up') window.scrollTo({top: 0, behavior: 'smooth'});
    if (a === 'next') {
      var panel = activePanel();
      var list = Array.prototype.map.call(panel.querySelectorAll('.task'), function(t){ return +(t.dataset.n || t.id.slice(1)); });
      if (!list.length) { openTab('solutions'); list = ALL; panel = activePanel(); }
      var here = currentN();
      var after = list.filter(function(n){ return !done[n] && (here == null || list.indexOf(n) > list.indexOf(here)); });
      var any = list.filter(function(n){ return !done[n]; });
      var n = after[0] || any[0];
      if (n == null) toast('Тут всё решено 🎉'); else go(n);
    }
  });

  // Remember where you are: the first problem card whose bottom is below the top of the screen.
  function currentN(){
    var panel = activePanel();
    if (!panel) return null;
    var cards = panel.querySelectorAll('.task');
    for (var i = 0; i < cards.length; i++) {
      var r = cards[i].getBoundingClientRect();
      if (r.bottom > 90) return r.top < window.innerHeight ? +(cards[i].dataset.n || cards[i].id.slice(1)) : null;
    }
    return null;
  }
  var st;
  window.addEventListener('scroll', function(){
    clearTimeout(st);
    st = setTimeout(function(){
      var p = activePanel();
      if (!p) return;
      var w = {tab: p.id.replace('panel-', ''), n: currentN(), y: window.scrollY};
      try { localStorage.setItem(WHERE, JSON.stringify(w)); } catch(e) {}
    }, 250);
  }, {passive: true});
  document.querySelectorAll('.tab-btn').forEach(function(b){
    b.addEventListener('click', function(){
      try { localStorage.setItem(WHERE, JSON.stringify({tab: b.dataset.tab, n: null, y: 0})); } catch(e) {}
    });
  });

  // Coming back: link #p34 wins, otherwise the saved place.
  var saved = null;
  try { saved = JSON.parse(localStorage.getItem(WHERE) || 'null'); } catch(e) {}
  var hash = location.hash.match(/^#p(\d+)$/);
  function restore(first){
    if (hash) { go(hash[1], false); return; }
    var w = saved;
    if (!w || !w.tab) return;
    openTab(w.tab);
    if (w.n != null) {
      var el = cardIn(activePanel(), w.n);
      if (el) { el.scrollIntoView({block: 'start'}); if (first) toast('Продолжаем с P' + w.n); }
    } else if (w.y) window.scrollTo(0, w.y);
    try { localStorage.setItem(WHERE, JSON.stringify(w)); } catch(e) {}
  }
  // KaTeX changes heights, so place once now and again after maths has rendered (unless you already scrolled).
  restore(true);
  var moved = false;
  window.addEventListener('wheel', function(){ moved = true; }, {passive: true, once: true});
  window.addEventListener('touchmove', function(){ moved = true; }, {passive: true, once: true});
  window.addEventListener('load', function(){ setTimeout(function(){ if (!moved) restore(false); }, 400); });
})();
"""
