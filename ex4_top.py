# -*- coding: utf-8 -*-
# "Top 15 formulas" data for ex4.html.
# Which formulas each problem needs: ex4_data/tags.json {n: [key, ...]}, tagged while writing the solutions.
# Card texts (RU and EN): ex4_data/top_text.json {key: {...}}.
# Ranking, problem lists, worked examples and the easy list are all computed from the tags.
import json
from pathlib import Path

from ex3_top import CSS, JS, chip  # noqa: F401  (same look and click behaviour as Exam 3)

DATA = Path(__file__).resolve().parent / "ex4_data"
TAGS = {int(k): v for k, v in json.loads((DATA / "tags.json").read_text(encoding="utf-8")).items()}
STEPS = {}
for key in ["Heat", "Kinetic", "FirstLaw", "SecondLaw"]:
    for p in json.loads((DATA / f"{key}_problems.json").read_text(encoding="utf-8")):
        STEPS[p[0]] = len(p[4])


def rank():
    """Formula keys by how many problems use them, most first."""
    count = {}
    for n, keys in TAGS.items():
        for k in set(keys):
            count.setdefault(k, []).append(n)
    return sorted(count.items(), key=lambda kv: (-len(kv[1]), kv[0]))


def simplest(nums):
    """The easiest problem in a list: fewest formulas, then fewest steps, then lowest number."""
    return min(nums, key=lambda n: (len(TAGS[n]), STEPS[n], n))


RANKED = rank()[:15]
TOP_KEYS = [k for k, _ in RANKED]
EXAMPLES = {}
for k, nums in RANKED:  # a different worked example for every card where possible
    free = [n for n in nums if n not in EXAMPLES.values()] or nums
    EXAMPLES[k] = simplest(free)

if (DATA / "top_text.json").exists():
    TEXT = json.loads((DATA / "top_text.json").read_text(encoding="utf-8"))
    ALL = [dict(id=k, nums=sorted(nums), example=EXAMPLES[k], **TEXT[k]["ru"]) for k, nums in RANKED]
    TOP5, TOP10 = ALL[:5], ALL[5:]
    EN = {k: TEXT[k]["en"] for k in TOP_KEYS}
    UNITS_RU = TEXT["_units"]["ru"]
    UNITS_EN = TEXT["_units"]["en"]

# One formula, one or two steps: the problems to try first.
# Take them round-robin across formulas so the list is not all one topic.
_pool = {k: sorted((n for n, keys in TAGS.items() if set(keys) == {k} and STEPS[n] <= 2), key=lambda n: (STEPS[n], n))
         for k in TOP_KEYS}
EASY = []
while len(EASY) < 12 and any(_pool.values()):
    for k in TOP_KEYS:
        if _pool[k] and len(EASY) < 12:
            EASY.append(_pool[k].pop(0))
EASY.sort()
