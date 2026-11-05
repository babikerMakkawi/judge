<div align="center">

# ⚖️ judge

**Clear decisions. Less noise.**

An Agent Skill that helps an AI assistant compare options, evaluate projects, surface risks and give an honest recommendation — in the user's own language and dialect.

`v1.0.0` · English & Arabic instructions · Full and light editions

[English](#english) · [العربية](#العربية)

</div>

---

<a id="english"></a>

## What it does

`judge` turns a fuzzy question ("which is better?", "should I open this shop?", "is this plan sound?") into a practical, defensible decision — or an honest statement that the evidence does not support one yet.

- **Picks the right depth automatically.** A quick question gets a short answer; a costly or hard-to-reverse decision (savings, lease, loan, partnership, starting a business) gets a full risk scan.
- **Risk scan for real projects.** Ten categories: demand, cash runway, unit economics and break-even (with a low / expected / high table), contracts and tax, fraud signals, key people, competition, supply and regulation, currency and price shocks, and exit terms. Risks are ranked by severity, and each comes with a check or a mitigation.
- **Honest about bad ideas.** If an idea cannot work as stated, it says so in the first lines and gives the decisive reason. Then it looks for the useful core: a real niche nearby, what would have to be true, and the cheapest test.
- **Never invents.** No made-up prices, buyers, sources or statistics. Assumptions are labeled.
- **Choosing is not authorizing.** "Sounds good, let's go with A" is a choice, not an order. The skill never buys, sends, publishes or deletes anything without an explicit instruction for that action.
- **Disagreement is not evidence.** It holds its assessment unless you bring new facts, while making clear the decision is yours.
- **Fair comparisons.** The same criteria apply to every option. Polish, order and authorship are not merits, and people are never judged on name, gender, age, nationality, religion or looks.
- **Speaks your language.** It replies in the user's language, dialect and register, matching grammatical gender when that is evident.

## Editions

| Edition | Folder | Size | Best for |
|---|---|---|---|
| **judge** (full) | `skills/en/judge` · `skills/ar/judge` | ~18k chars (EN) · ~16k (AR) | Claude Code, Claude apps, Codex and other hosts with skill support |
| **judge-flash** (light) | `skills/en/judge-flash` · `skills/ar/judge-flash` | < 8,000 chars | Custom GPTs, Gemini Gems and hosts with tight instruction limits |

The English and Arabic instructions say the same thing. Every edition **replies in the user's language** whichever instruction language you install, so pick Arabic instructions only if you want to read or edit them in Arabic.

> **Install only one edition per host.** Two similar skills compete for activation.

## Repository layout

```
skills/
├── en/
│   ├── judge/                  # full edition, English instructions
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml  # Codex / ChatGPT metadata
│   │   ├── assets/icon.svg
│   │   └── references/
│   │       ├── edge-cases.md        # ties, stakeholders, portfolios...
│   │       ├── runtime-protocol.md  # tools, delegation, handoff
│   │       └── usage.md
│   └── judge-flash/            # light edition, same structure
└── ar/
    ├── judge/                  # full edition, Arabic instructions
    └── judge-flash/            # light edition, Arabic instructions
```

## Installation

**Claude Code**: copy one skill folder into your skills directory, then invoke it with `/judge` (or let Claude pick it up automatically).

```bash
cp -r skills/en/judge ~/.claude/skills/judge
```

Use `.claude/skills/judge` inside a project instead to scope it to that project.

**Claude apps (claude.ai, desktop, mobile)**: zip one skill folder (for example `judge/`) and upload it under Settings → Capabilities → Skills. Menu names may change over time.

**Codex**: copy the folder into your Codex skills directory and invoke it with `$judge`. The `agents/openai.yaml` file provides the display name, icon and default prompt.

```bash
cp -r skills/en/judge ~/.codex/skills/judge
```

**Custom GPTs, Gemini Gems or any plain chat**: paste the contents of `judge-flash/SKILL.md` into the instructions field. If the host accepts knowledge files, also upload the files in `references/`. Otherwise the skill works from its main instructions alone.

## How to use it

Just ask naturally ("which is better", "should I", "is it worth it", "قارن", "هل يستحق"), or use a shortcut:

| Shortcut | What it does |
|---|---|
| `judge: ...` | Run any request through the skill |
| `compare 7` | Compare up to 7 options |
| `ideas` | 10–20 varied ideas in groups instead of a single verdict |
| `plan` | Ask only the next essential question |
| `audit` | Separate confirmed defects from untested risks |
| `debate only` | Arguments for and against, with no verdict |
| `execute B` | Act on an approved option (requires a real tool and your authorization) |
| `handoff` | Package the decision for another person or agent |

### Recommended prompt for evaluating a project

```text
judge: Evaluate my project honestly and list its weaknesses and risks ranked by severity.

Idea: [e.g. a men's barbershop]
Location: [city and neighborhood]
Available budget: [amount, and how much is a loan or a partner's money]
Known costs: [rent, equipment, salaries...]
Expected income: [customers or sales per day, and price]
My experience: [have you worked in this field?]
My goal: [side income, full-time, experiment...]
Non-negotiables: [e.g. no more than 50k, no loans]
Maximum loss I can absorb: [amount]

I want: go or no-go, the break-even point, a low / expected / high table,
and the cheapest test before I pay anything.
```

Real numbers matter more than descriptions. If you don't know something, write **"assume and proceed"** and the skill will label its assumptions and keep going.

## Testing and limitations

The skill was developed through blind A/B tests against the same models without the skill. Rubrics were written before each run, judges did not know which answer came from the skill, and the answer order was swapped between judges. The tests covered:

- core and regression scenarios: options, scoring formulas, multi-turn decisions, pushback, purchase authorization with a simulated tool timeout;
- real-world business cases: barbershop, supermarket, importing goods and more complex ventures. In the final round the skill won 4 of the 5 business cases and caught 34 of 35 hidden risks;
- unworkable and joke ideas: the skill flagged all six as unworkable up front, offered a realistic niche and a cheap test each time, and invented no numbers.

**Limits:**

- Tests ran on Claude models (Opus, Sonnet, Haiku) in simulated chats, with one run per case.
- GPT and Gemini are untested.
- None of this guarantees accuracy. The skill gives decision support, not professional legal, medical or financial advice.
- Tools, accounts, external actions and background execution depend on the host and your authorization. The skill installs no connectors.

## Version

See [CHANGELOG.md](CHANGELOG.md). Current release: **1.0.0**.

## License

No license has been chosen yet. Until one is added, all rights are reserved by the author.

---

<a id="العربية"></a>

<div dir="rtl">

## العربية

### ما هي judge؟

مهارة (Agent Skill) تساعد المساعد الذكي على مقارنة الخيارات وتقييم المشاريع وكشف مخاطرها، ثم إعطاء توصية صريحة بلغة المستخدم ولهجته.

- **تختار العمق المناسب تلقائيًا:** السؤال البسيط يأخذ ردًا قصيرًا. أما القرار المكلف أو الصعب التراجع عنه، كالمدخرات أو الإيجار أو القرض أو الشراكة أو بدء مشروع، فيأخذ فحصًا كاملًا للمخاطر.
- **فحص مخاطر للمشاريع الحقيقية:** عشر فئات، منها:
  - الطلب، والسيولة، وتكلفة الوحدة.
  - نقطة التعادل، مع جدول للحالات المتشائمة والمتوقعة والمتفائلة.
  - العقود والضرائب، وإشارات الاحتيال، والأشخاص الأساسيون.
  - المنافسة، والتوريد، والعملة، وشروط الخروج.

  وترتّب المخاطر حسب خطورتها، مع فحص أو حل لكل خطر.
- **صريحة مع الأفكار غير القابلة للتطبيق:** تقول ذلك في أول سطر مع السبب الحاسم. ثم تبحث عن الجانب المفيد: حاجة حقيقية قريبة من الفكرة، وما يجب أن يتحقق لتنجح، وأرخص اختبار.
- **لا تختلق** أسعارًا أو مشترين أو مصادر أو أرقامًا، وتوضّح افتراضاتها.
- **الاختيار ليس إذنًا بالتنفيذ:** لا تشتري ولا ترسل ولا تنشر ولا تحذف شيئًا إلا بأمر صريح.
- **الاعتراض ليس دليلًا:** تحافظ على تقييمها ما لم تأتِ بمعلومة جديدة، والقرار في النهاية قرارك.
- **عادلة:** معايير واحدة لكل الخيارات، ولا حكم على الأشخاص بالاسم أو الجنس أو العمر أو الجنسية أو الدين أو المظهر.

### النسخ

| النسخة | المجلد | الحجم | الأنسب لـ |
|---|---|---|---|
| **judge** (الكاملة) | `skills/ar/judge` · `skills/en/judge` | نحو 16 ألف حرف (عربي) و18 ألفًا (إنجليزي) | Claude Code وتطبيقات Claude وCodex |
| **judge-flash** (الخفيفة) | `skills/ar/judge-flash` · `skills/en/judge-flash` | أقل من 8,000 حرف | Custom GPTs وGemini Gems والمنصات ذات الحدود الضيقة |

التعليمات العربية والإنجليزية متطابقتان في المعنى. **كل النسخ تجيب بلغة المستخدم ولهجته** أيًا كانت لغة التعليمات. ثبّت **نسخة واحدة فقط** في كل منصة.

### التثبيت

- **Claude Code:** انسخ مجلد المهارة إلى `~/.claude/skills/judge`، ثم استدعها بـ `/judge`.
- **تطبيقات Claude:** اضغط مجلد المهارة في ملف zip، ثم ارفعه من الإعدادات ← Capabilities ← Skills.
- **Codex:** انسخ المجلد إلى `~/.codex/skills/judge`، ثم استدعها بـ `$judge`.
- **Custom GPTs وGems وأي محادثة عادية:** الصق محتوى `judge-flash/SKILL.md` في خانة التعليمات، وارفع ملفات `references/` إن أمكن.

### الطلب المقترح لتقييم مشروع

</div>

```text
judge: قيّم مشروعي بصراحة، واذكر العيوب والمخاطر مرتبة حسب خطورتها.

الفكرة: [مثال: محل حلاقة رجالي]
المكان: [المدينة والحي]
الميزانية المتاحة: [المبلغ، وكم منه قرض أو مال شريك]
التكاليف المعروفة: [إيجار، معدات، رواتب...]
الدخل المتوقع: [عدد الزبائن أو المبيعات يوميًا، والسعر]
خبرتي: [هل عملت في هذا المجال؟]
هدفي: [دخل إضافي، تفرغ كامل، تجربة...]
ما لا أقبل التنازل عنه: [مثال: لا أتجاوز 50 ألف، لا قروض]
أقصى خسارة أتحملها: [المبلغ]

أريد: هل أبدأ أم لا، ونقطة التعادل، وجدول للحالات المتشائمة والمتوقعة والمتفائلة، وأرخص اختبار قبل أن أدفع.
```

<div dir="rtl">

**صيغ أقصر:**
- `judge: قارن بين هذه الخيارات ضمن ميزانيتي: ...`
- `judge: راجع خطتي وافصل العيوب المؤكدة عن المخاطر غير المختبرة: ...`
- `judge: أعطني أفكار مشاريع بميزانية ... في ...`
- `judge: هل هذه الفكرة قابلة للتطبيق أصلًا؟ ...`

الأرقام الحقيقية أهم من الوصف. وإن لم تعرف معلومة، فاكتب **«افترض وأكمل»**.

### الاختبار والحدود

طُوّرت المهارة باختبارات مقارنة عمياء ضد النموذج نفسه بدون المهارة. شملت الاختبارات:

- **المقارنات والقرارات متعددة الرسائل وتفويض الشراء.**
- **مشاريع حقيقية:** محل حلاقة، وسوبرماركت، واستيراد بضائع. فازت المهارة في 4 من 5 مشاريع في الجولة الأخيرة، والتقطت 34 من 35 خطرًا مخفيًا.
- **أفكار غير قابلة للتطبيق أو مزاح:** حكمت المهارة على الأفكار الست بأنها غير قابلة للتطبيق من البداية، دون اختلاق أرقام.

**الحدود:**
- الاختبارات أُجريت على نماذج Claude فقط، بتشغيل واحد لكل حالة.
- لم تُختبر على GPT وGemini بعد.
- المهارة دعم للقرار، لا استشارة قانونية أو طبية أو مالية متخصصة.

### الترخيص

لم يُحدد الترخيص بعد، وجميع الحقوق محفوظة للمؤلف إلى أن يُضاف ترخيص.

</div>
