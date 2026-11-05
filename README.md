<div align="center">

<img src="assets/logo.png" alt="judge logo" width="140">

# judge

**Clear decisions. Less noise. · قرارات أوضح، وكلام أقل.**

An AI skill that compares options, evaluates projects, finds the risks and gives an honest recommendation, in your language.

`v1.0.0` · MIT License · **[English](#english)** · **[العربية](#arabic)**

</div>

---

<a id="english"></a>

## 🚀 Quick start (any AI chat, no install)

> Sending the GitHub link alone won't work. Paste the instructions yourself.

1. Open [this file](https://github.com/babikerMakkawi/judge/blob/main/skills/en/judge-flash/SKILL.md) and click 📋 **Copy raw file**.
2. In a new chat (ChatGPT, Gemini, Claude...), type `Follow these instructions in every reply:`, paste the text, then add your question.
3. Keep using the same chat. In a new chat, paste again.

## What it does

- Gives a clear verdict first, then the reasons, the main risk and the next step.
- For a business or other costly decision, it checks ten risk areas and ranks them by severity.
- Says plainly when an idea can't work, then suggests a realistic alternative.
- Never invents prices, numbers or sources.
- Never buys, sends or deletes anything unless you explicitly tell it to.

## Permanent setup

| Where | How |
|---|---|
| ChatGPT (Custom GPT or Project) · Gemini (Gem) | Paste `judge-flash/SKILL.md` into **Instructions** |
| Claude apps | Download a zip from [Releases](https://github.com/babikerMakkawi/judge/releases), then **Settings → Capabilities → Skills → Upload** |
| Claude Code · Codex | Copy `skills/en/judge` into your skills folder, then use `/judge` or `$judge` |

`judge-flash` is the light edition (under 8,000 characters, works on its own). `judge` is the full edition.

## Example request

```text
judge: Evaluate my project honestly and rank its risks.
Idea: ...   Location: ...   Budget: ...   My goal: ...
```

If you don't know a detail, write "assume and proceed".

## Limits

Tested on Claude models only, one run per case ([test records](evals/)). It supports your decision; it is not professional legal, medical or financial advice.

[MIT License](LICENSE) © 2026 Babiker Makkawi

---

<a id="arabic"></a>

<div dir="rtl" align="right">

## 🚀 ابدأ هنا (أي محادثة، بدون تثبيت)

> إرسال رابط GitHub وحده لا يكفي، الصق التعليمات بنفسك.

1. افتح [هذا الملف](https://github.com/babikerMakkawi/judge/blob/main/skills/ar/judge-flash/SKILL.md) واضغط 📋 **Copy raw file**.
2. في محادثة جديدة (ChatGPT أو Gemini أو Claude...) اكتب: «اتبع هذه التعليمات في كل ردودك:»، ثم الصق النص، ثم اكتب سؤالك.
3. أكمل في المحادثة نفسها. وفي أي محادثة جديدة، الصق النص مرة أخرى.

## ماذا تفعل؟

- تعطيك الحكم أولًا، ثم الأسباب، وأهم خطر، والخطوة التالية.
- في المشاريع والقرارات المكلفة، تفحص عشرة أنواع من المخاطر وترتبها حسب خطورتها.
- تقول بصراحة إن كانت الفكرة غير قابلة للتطبيق، ثم تقترح بديلًا واقعيًا.
- لا تختلق أسعارًا أو أرقامًا أو مصادر.
- لا تشتري ولا ترسل ولا تحذف شيئًا إلا بأمر صريح منك.

## الإعداد الدائم

| أين | كيف |
|---|---|
| ChatGPT (Custom GPT أو Project) · Gemini (Gem) | الصق محتوى `judge-flash/SKILL.md` في خانة **Instructions** |
| تطبيقات Claude | نزّل ملف zip من [الإصدارات](https://github.com/babikerMakkawi/judge/releases)، ثم **Settings ← Capabilities ← Skills ← Upload** |
| Claude Code · Codex | انسخ مجلد `skills/ar/judge` إلى مجلد المهارات، ثم استخدم `/judge` أو `$judge` |

`judge-flash` هي النسخة الخفيفة (أقل من 8,000 حرف، وتعمل وحدها)، و`judge` هي النسخة الكاملة.

## مثال على الطلب

```text
judge: قيّم مشروعي بصراحة، ورتّب مخاطره حسب خطورتها.
الفكرة: ...   المكان: ...   الميزانية: ...   هدفي: ...
```

وإن لم تعرف معلومة، فاكتب «افترض وأكمل».

## الحدود

اختُبرت على نماذج Claude فقط، بتشغيل واحد لكل حالة ([سجلات الاختبار](evals/)). وهي مساعدة على اتخاذ القرار، لا استشارة قانونية أو طبية أو مالية متخصصة.

[ترخيص MIT](LICENSE) © 2026 Babiker Makkawi

</div>
