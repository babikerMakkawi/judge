# Evaluation records

This folder holds the test scenarios, pass criteria, raw model answers and grading behind the claims in the main README. It is published so anyone can check the evidence or rerun the tests.

**Read this first: what these tests are and are not**

- They are qualitative, small-sample tests: **one run per case**, mostly on Claude models (Opus, Sonnet, Haiku), in simulated chats run by subagents.
- Differences of half a point are within grader noise. In one case two blind graders gave the *same* text 6.5 and 5.5.
- They support "this behaves well in these situations", not "this is X% more accurate".
- GPT and Gemini were **not tested**.
- Most scenario files, gradings and notes are in **Arabic**, because the skill was developed with an Arabic-speaking owner. Several scenarios themselves are in English.

## Method

1. **Pre-registered criteria.** Each scenario's success and failure conditions were written *before* any run (`scenarios/`).
2. **Skill vs baseline.** Each scenario was run in a fresh, isolated context twice: once with the skill's instructions loaded, once without (baseline). Same model, same prompt.
3. **Blind grading.** Answers were relabeled with random codes, such as `b1-k7`, and graded against the criteria by graders who did not know which answer used the skill. In round 0 two graders saw the pair in opposite orders, to cancel position bias. The code-to-condition mapping is in `runs/blinding-key.txt`.
4. **Hidden-risk checklists.** Each business scenario has 7 risks the user did not mention (for example cash runway, fraud signals, key-person loss). Graders scored how many each answer caught.
5. **Tool safety.** Purchase-authorization tests used a local mock purchasing tool (`tools/mock_shop.py`, no network, no payments). Its first call times out, to test whether the model checks state before retrying instead of ordering twice.

To save cost, some later rounds were graded by one blind grader or by the developer directly. Each results file says which.

## Version history

The release went through several internal drafts. File names refer to these drafts:

| Draft | What it was |
|---|---|
| original draft | The owner's first version, before this testing (it was also labeled "1.0.0" at the time) |
| v1.1 | First revision: routes, warmer personal answers, idea lists, purchase authorization |
| v1.2 | Shortened to under 8,000 characters, plus the 10-category risk scan |
| v1.3 | Fixes for cash-runway math and for "only"/"best" claims, plus the rule for unworkable and joke ideas |
| **release 1.0.0** | v1.3 plus final-check wording, a standalone light edition, and README and metadata cleanup (**these last edits were not re-tested**) |

## Results by round

| Round | Draft and models | What was tested | Result | File |
|---|---|---|---|---|
| 0 | original draft: Opus, Haiku, some Sonnet | 21 core scenarios, 41 blind comparisons | **No net benefit:** skill 17, baseline 17, ties 7. The draft won open decisions, constraint-heavy comparisons, code review and purchase confirmation. It lost on idea lists, emotional decisions, simple facts and practical tips. | `results/round0-original-draft-report.md` |
| 1 | v1.1: same models | The 7 losing scenarios, plus a regression round | All 7 improved; regressions checked | `results/round1-v1.1-retest.md` |
| 2 | v1.1: Sonnet | 5 business projects (barbershop, supermarket, importing, restaurant partnership, gym franchise) | **Lost 5 of 5.** Hidden risks: 30.5 of 35 vs baseline 33.5, because secondary risks were dropped to stay short. Fix: the systematic risk scan. A recheck of the two worst cases won narrowly. | `results/round2-business-v1.1.md` |
| 3 | v1.2: Sonnet (business), Haiku (core) | 5 business projects plus 10 core behaviors | **Won 4 of 5.** Hidden risks: 34 vs 33.5 of 35 (about even); quality 8.6 vs 8.0. Errors found: a cash-runway mistake in B1 and an "only option within budget" slip in S13. | `results/round3-v1.2.md` |
| 4 | v1.3: full and light editions | Rechecks of B1, B3, B4 and S13 | Both errors fixed; fraud signals in B3 caught by both editions. Graded by the developer, not blind. | `runs/v1.3-rechecks/` |
| 5 | v1.3: full and light, EN and AR, Opus and Haiku | 6 unworkable or joke ideas (X1–X6), 9 runs | All 6 flagged as unworkable up front, with a realistic nearby niche and a cheap test. Humor matched in the joke cases, and no invented numbers. On X3 the skill beat the baseline, which invented cost figures. One run still added an unneeded "nothing has been executed" line; the final check was tightened afterwards (not re-tested). | `runs/absurd-ideas/`, `scenarios/absurd-scenarios.md` |

## Folder map

```
evals/
├── scenarios/            # pre-registered scenarios and pass criteria
│   ├── core-scenarios.md        # S01–S21: pushback, bias, scoring, purchases...
│   ├── business-scenarios.md    # B1–B5 with 7 hidden risks each
│   └── absurd-scenarios.md      # X1–X6 unworkable / joke ideas
├── results/              # round summaries (see table above)
├── grading/              # blind graders' detailed scoring
├── runs/                 # raw model answers, by round
│   └── blinding-key.txt         # which code was skill vs baseline
└── tools/mock_shop.py    # local mock purchasing tool used in S21
```

Local file paths in the records have been replaced with `<workdir>/`.

## Rerunning

1. Pick a scenario from `scenarios/` and copy its user turns.
2. Run it in a fresh chat with the skill installed, and in another fresh chat without it, on the same model.
3. Hide which answer is which, then grade both against the pre-registered criteria.
4. Run each case several times. One run per case, as here, cannot measure variance.

Results from other models, especially GPT and Gemini, are welcome as issues or pull requests.

---

## ملخص بالعربية

يحتوي هذا المجلد على السيناريوهات، ومعايير النجاح المكتوبة قبل التشغيل، والردود الخام، والتقييمات العمياء، حتى يمكن لأي شخص التحقق من النتائج أو إعادة الاختبار.

- **المسودة الأصلية:** بلا فائدة صافية، 17 فوزًا مقابل 17 خسارة في 41 مقارنة عمياء.
- **بعد التعديلات:**
  - تحسنت السيناريوهات الخاسرة كلها.
  - فاز الإصدار 1.2 في 4 من 5 مشاريع تجارية.
  - صُحح خطأ حساب السيولة وخطأ وصف «الخيار الوحيد».
  - حكمت المهارة على الأفكار الست غير القابلة للتطبيق بذلك من البداية، دون اختلاق أرقام.
- **الحدود:**
  - تشغيل واحد لكل حالة، على نماذج Claude فقط.
  - بعض الجولات قيّمها المطوّر لا محكّم أعمى.
  - آخر التعديلات قبل الإصدار 1.0.0 لم يُعَد اختبارها.
