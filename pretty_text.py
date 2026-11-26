# -*- coding: utf-8 -*-
"""Turn the plain-text notation of the exam sources into readable HTML.

    m/s^2 -> m/s<sup>2</sup>      6.022×10^23 -> 6.022×10<sup>23</sup>
    10^-23, 10^-^7 -> 10<sup>−23</sup>, 10<sup>−7</sup>
    N_2, c_lead, v_rms -> N<sub>2</sub>, c<sub>lead</sub>, v<sub>rms</sub>

Input is plain text; it is HTML-escaped first, so the result is safe to drop into a page.
Text that already contains KaTeX delimiters is left alone apart from escaping.
"""
import html
import re

_EXP = re.compile(r"\^\s*(?:\{([^{}]*)\}|(-?\^?-?\d+(?:\.\d+)?))")
_SUB = re.compile(r"(?<=[A-Za-zρΔ])_(?:\{([^{}]*)\}|([A-Za-z0-9]+))")


def _exp(m):
    v = (m.group(1) or m.group(2)).replace("^", "")
    return "<sup>" + v.replace("-", "−") + "</sup>"


def pretty(text):
    s = html.escape(text, quote=False)
    if "\\(" in s or "\\[" in s:
        return s
    s = _EXP.sub(_exp, s)
    s = _SUB.sub(lambda m: "<sub>" + (m.group(1) or m.group(2)) + "</sub>", s)
    return s


if __name__ == "__main__":
    for t in ["c_lead = 128 J/(kg·°C)", "g = 9.8 m/s^2.", "1.38×10^-23 J/K", "4.7×10^-^7", "M_N2 = 28 g/mol", "0.0242 m^3"]:
        print(t, "->", pretty(t))
