# Using judge 1.0.0 / استخدام judge 1.0.0

## English

- **Packages.** `judge` is the full version (all details). `judge-flash` is the light version (under 8,000 characters), for hosts with tight limits such as Custom GPTs or Gems. Each comes with English instructions or Arabic instructions; the two languages say the same thing. Install only one package per host: two same-name or overlapping skills compete for activation.
- **Language.** Every package replies in the user's language and dialect, whatever the language of its instructions. Choose Arabic instructions only if you want to read or edit them in Arabic.
- **Invocation.** Use the host's supported mechanism: `/judge` in Claude Code, `$judge` in Codex/ChatGPT, or automatic selection from the description where the host supports it. `judge: ...` is a semantic shortcut, not a universal loader.
- **Plain chat without a skill loader.** Paste the chosen `SKILL.md` as instructions; add the relevant reference contents if possible. If bundled files cannot be read, do not claim to have loaded them; use the available instructions.
- **Capabilities.** Tools, accounts, external actions, persistence and background execution depend on the actual host and authorization. judge installs no connectors. Coordinate with specialist workflows for documents, code and media.
- **Workers.** When inheritance is unavailable, give workers the skill path or the needed instructions plus task-local context. The coordinator integrates and verifies results.
- **Commands** such as `plan`, `compare 7`, `ideas`, `audit`, `debate only`, `execute B` and `handoff` describe behavior; natural-language equivalents work too. Execution still needs the actual target, authorization and capabilities.
- **Examples:** `judge: Compare these options under my budget.` · `judge: Ask the next essential question.` · `judge: Audit this plan; separate confirmed defects from untested risks.` · `judge: Execute the approved option and verify the result.`
- **Limits.** Testing so far covered Claude models (Opus, Sonnet, Haiku) in simulated chats, with one run per case. It does not establish universal compatibility or guaranteed accuracy. Licensing is the owner's decision.

## العربية

- **الحزم.** `judge` هي النسخة الكاملة (بكل التفاصيل). و`judge-flash` هي النسخة الخفيفة (أقل من 8,000 حرف)، للبيئات ذات الحدود الضيقة مثل Custom GPTs أو Gems. وتأتي كل منهما بتعليمات إنجليزية أو عربية، واللغتان تقولان الشيء نفسه. ثبّت حزمة واحدة فقط في كل بيئة: المهارتان المتشابهتان في الاسم أو العمل تتنافسان على التفعيل.
- **اللغة.** كل حزمة تجيب بلغة المستخدم ولهجته، أيًا كانت لغة تعليماتها. اختر التعليمات العربية فقط إن أردت قراءتها أو تعديلها بالعربية.
- **الاستدعاء.** استخدم الطريقة التي تدعمها البيئة: `/judge` في Claude Code، و`$judge` في Codex/ChatGPT، أو الاختيار التلقائي من الوصف حيث تدعمه البيئة. أما `judge: ...` فاختصار دلالي، لا آلية تحميل عامة.
- **دردشة بلا محمّل مهارات.** الصق ملف `SKILL.md` المختار كتعليمات، وأضف محتوى المراجع ذات الصلة إن أمكن. وإذا تعذرت قراءة الملفات المرفقة، فلا تدّعِ تحميلها؛ استخدم التعليمات المتاحة.
- **القدرات.** تعتمد الأدوات والحسابات والأفعال الخارجية والاستمرار والعمل الخلفي على البيئة والتفويض الفعليين. ولا تثبّت judge أي موصلات. تعاون مع الإجراءات المتخصصة للمستندات والكود والوسائط.
- **العمال.** عند غياب التوريث، أعطِ العمال مسار المهارة أو التعليمات اللازمة مع سياق المهمة. ويتولى المنسق دمج النتائج والتحقق منها.
- **الأوامر** مثل `ابدأ التخطيط` و`قارن 7` و`أفكار` و`راجع` و`مداولة فقط` و`نفّذ B` و`حزمة تسليم` تصف السلوك، وتعمل مكافئاتها الطبيعية أيضًا. ويبقى التنفيذ مرتبطًا بالهدف والتفويض والقدرات الفعلية.
- **أمثلة:** `judge: قارن البدائل ضمن ميزانيتي.` · `judge: اسألني السؤال الضروري التالي.` · `judge: راجع الخطة وافصل العيوب المؤكدة عن المخاطر غير المختبرة.` · `judge: نفّذ الخيار المعتمد وتحقق من النتيجة.`
- **الحدود.** شملت الاختبارات حتى الآن نماذج Claude (Opus وSonnet وHaiku) في محادثات محاكاة، بتشغيل واحد لكل حالة. وهذا لا يثبت توافقًا عامًا أو دقة مضمونة. والترخيص قرار المالك.
