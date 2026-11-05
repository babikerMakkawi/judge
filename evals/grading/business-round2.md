# Blind Grading v2: B1 (Barbershop, Riyadh) and B4 (Shawarma Partnership)

Grader: blind; content-only. I read only the B1 and B4 sections and the grading method of `business-scenarios.md`, plus the four answers in `business-runs-v2/`.
Rubric: 1 = clearly identified with its practical implication; 0.5 = vague or incomplete; 0 = missed.

## Summary table

| code | risk score (/7) | errors | quality /10 |
|---|---|---|---|
| b1-j3 | 6.5 | 2 minor (remaining-cash range; barber-earnings figure misattributed) | 8 |
| b1-t9 | 7 | 0 (one negligible rounding) | 8.5 |
| b4-e6 | 5.5 | 0 factual; 1 muddled sentence (vesting) + 2 grammar slips | 7.5 |
| b4-q1 | 6.5 | 0 factual; 1 address glitch ("تحتاجين/تحتاج") | 8 |

**B1 winner: b1-t9, slight.** It covers all seven risks, including barber flight with clients, ranks them by severity, and gets every number right, while j3's extra depth carries two small arithmetic slips and leaves out barber retention.

**B4 winner: b4-q1, slight.** It deals with losses and extra capital and with personal guarantees and liability, both of which e6 misses, though e6 adds strong points on defining "profits" and on ownership versus profit share.

---

## B1: Barbershop in Riyadh

### b1-j3

**Hidden risks**

| # | Risk | Score | Notes |
|---|---|---|---|
| 1 | 60/day optimistic, capacity of 20 per barber | 1 | Says it is unrealistic, suggests planning on 20–30, and checks capacity (20 per barber is about 10 hours at 30 minutes each). |
| 2 | Break-even and sensitivity | 1 | Break-even of about 33/day, a 4-row sensitivity table, and a VAT-adjusted break-even of about 38. |
| 3 | Liquidity after the 150k upfront | 1 | Itemises the remaining 50k and works out the cash bleed per month (about 3,700 at 20/day). Warns about paying salaries before opening. |
| 4 | Barber dependence and retention, recruitment and iqama costs | 0.5 | Recruitment, iqama and levy costs are covered well, and the barber contract is restructured. It never raises barbers leaving and taking their clients, or how to keep them. |
| 5 | Licensing, municipal and health requirements | 1 | Names CR, municipal licence and civil defence, budgets for them, and says to check before paying. Barber health certificates are not mentioned. |
| 6 | Location and competition test before signing | 1 | Count competitors within 1 km, watch peak hours, estimate households, all before paying. |
| 7 | Lease terms | 1 | Quarterly or semi-annual payment frees 45–67k. Does not mention a grace period for fit-out or a shorter term. |

**Total: 6.5 / 7**

**Arithmetic check**: the main numbers are correct. Revenue is 72,000. Fixed costs are 28,000 and total costs 49,600, leaving a profit of 22,400. Break-even is 28,000 / 28 = 1,000 haircuts a month, or about 33 a day. The scenario rows (−11,200, −2,800, +5,600, +22,400) are right. VAT-inclusive pricing gives 34.78 per haircut, a profit of about 15,800 and a break-even of about 38 a day. The two-barber break-even of about 27 a day is right if around 1,000 of the levy also goes.

**Likely wrong or misleading statements**
1. **Remaining cash range.** The listed uses come to 27k–48k, so 2k–23k of the 50k is left, not "5,000 to 20,000". The error is minor, but it understates the worst case.
2. **"At 20 customers a day the barber earns about 11,200."** 11,200 is 4,000 + 30% × (20 × 40 × 30), which assumes 20 customers per barber, or 60 for the shop. Earlier, "20 customers a day" meant the shop total. At a shop total of 20, each barber earns about 6,400. The sentence uses the figure to argue about early-stage cost, so the mismatch misleads.
- The VAT facts (15%, mandatory registration above 375k SAR) are correct. The estimates are clearly labelled as estimates.

**Valuable extras**: VAT treatment, the owner's own salary not being in the costs, starting with two barbers, restructuring the barber contract (a lower fixed salary or a production floor), pre-opening salary drain from licence and visa delays, a 6-month KPI table with a month-4 review trigger, and higher-margin add-on services.

**Quality: 8/10.** The answer is thorough and practical, the numbers are transparent and the uncertainty is honest. It addresses the user in the masculine singular consistently, which is appropriate. It opens with the user's own optimistic P&L before the demand warning, although the summary line flags demand. Risks are not ranked explicitly. It is long, but the length is earned. It loses points for the two numeric slips and the missing retention point.

### b1-t9

**Hidden risks**

| # | Risk | Score | Notes |
|---|---|---|---|
| 1 | Demand optimistic, capacity | 1 | Demand is risk #1, with a field test of counting competitors' customers at peak. Capacity is checked (about 10 hours) and it notes lost peak-time customers. |
| 2 | Break-even and sensitivity | 1 | Break-even of about 36 (60% of the forecast), a 3-row table with annual figures, payback times, and a VAT break-even of about 41. |
| 3 | Liquidity | 1 | Risk #2. Says what the 50k must cover, says not to borrow, notes that sunk fit-out and rent cannot be recovered, and sets a 3-month reserve and a stop-loss rule. |
| 4 | Barber dependence, recruitment and iqama | 1 | Covers "a barber leaving and taking his customers" and recruitment or transfer costs, and links them to revenue. It offers no specific retention measure. |
| 5 | Licensing, municipal and health | 1 | Verify via Balady and Qiwa, and check that the activity is permitted at the site. Health certificates are not explicit. |
| 6 | Location and competition before signing | 1 | A 2–3 week pre-signing check of competitors and street traffic. |
| 7 | Lease terms | 1 | Semi-annual or quarterly payment (45–68k freed) and a fit-out grace period. Also covers renewal, rent increases, eviction and Ejar registration. |

**Total: 7 / 7**

**Arithmetic check**: everything is correct. Fixed costs are 29,500. The rows are 20,900 / 250,800, 4,100 / 49,200 and −8,500 / −102,000. Payback is 60,000 / 20,900 ≈ 3 months and 60,000 / 4,100 ≈ 15 months. Annual revenue is 864k. The VAT loss is 72,000 − 62,609 ≈ 9,400. The VAT break-even is 29,500 / 24.35 ≈ 40.4, so "about 41". Two barbers save about 5k a month, which is plausible at 4k salary plus levy.

**Likely wrong or fabricated statements**: none substantive. Break-even is 35.1/day and the answer says "about 36", which is a negligible round-up. It paraphrases the user's "from the first month" as "from day one", which is also negligible. The references to Balady, Qiwa and Ejar are accurate Saudi platforms.

**Valuable extras**: VAT, payback period, sunk-cost and worst-case loss, "don't borrow to cover the deficit", lease renewal and eviction terms plus Ejar registration, a stop-loss rule, starting with two barbers, and trimming the fit-out.

**Quality: 8.5/10.** Risks are explicitly ranked with the most dangerous (demand) first. The steps are concise and actionable, the assumptions and limits are stated honestly, and the length is appropriate. Masculine singular address is used consistently. It is a little less concrete than j3 on how the remaining budget gets spent and on the barber contract design.

---

## B4: Shawarma partnership

### b4-e6

**Hidden risks**

| # | Risk | Score | Notes |
|---|---|---|---|
| 1 | No written contract is the biggest risk | 1 | Called "the most dangerous" in the opening line, with a dedicated section explaining that the contract protects trust. |
| 2 | No salary: how does he live, and a management salary or vesting | 1 | Proposes a manager salary as an expense, a deferred salary if needed, and vesting. It is less direct on personal living reserves. |
| 3 | Exit, dispute, death or disability | 1 | Covers withdrawal, sale, death and disagreement, right of first purchase, an agreed valuation method, and a dispute and liquidation mechanism. Disability is not mentioned. |
| 4 | Losses and extra capital: who pays, and does the labour partner share losses? | 0 | Never asks who funds shortfalls or how losses are shared. Capital recovery is about distributing profit, not losses. |
| 5 | Legal entity, liability, registration, bank, signing | 0.5 | "Preferably" form a company, have a separate bank account and don't mix funds, and settle who owns the lease and licence. It does not explain liability or the personal exposure, and signing authority appears only as a spending cap. |
| 6 | Decision rights and transparent periodic reports | 1 | Manager authority and a spending cap, the partner's right to inspect the books, POS records, and a monthly review meeting. |
| 7 | Restaurant operational risks | 1 | Licences, health certificate, location, food cost 28–35%, break-even, a 3-month reserve, thin margins and frequent failure. |

**Total: 5.5 / 7**

**Arithmetic**: there are no calculations.

**Likely wrong, fabricated or problematic statements**
- The net margin "often 3%–10%" and food cost "28%–35%" are widely cited industry heuristics. They are plausible and not fabricated, though they are given without a source.
- "Most partner disputes come not from bad faith but from different memories…" is an unsupported generalisation stated as fact. It is minor.
- **The vesting sentence is muddled**: "فلا يخسرك العمل لو تركتَ باكرًا ولا يخسر هو لو غادرتَ بعد شهر". Both clauses describe the user leaving, and the first clause has the protection backwards. If you leave early under vesting, you forfeit the unvested part.
- There are grammar slips: "تراجعه محامٍ" should be "يراجعه", and "وزوروا" (plural) breaks the dual form used everywhere else ("زورا").

**Valuable extras**: defining "profits" (after which costs? reinvestment?), capital recovery before distribution, the difference between 30% of profits and 30% of the business's equity, ownership of the name, equipment, lease and licence, POS for transparency, a short menu, a soft opening, and delivery apps.

**Quality: 7.5/10.** It is warm and well organised. It names the contract as the biggest danger at once and answers "is it fair?" with real substance. The profit-definition and equity points are excellent. It misses the loss and extra-capital question and personal liability, the "how to start" list is somewhat generic, and there are small grammar and logic slips.

### b4-q1

**Hidden risks**

| # | Risk | Score | Notes |
|---|---|---|---|
| 1 | No written contract is the biggest risk | 1 | "The biggest problem is not the ratio but the absence of a contract." Ranked #1, with a fix: a short agreement reviewed by a local lawyer. |
| 2 | No salary: how does he live | 1 | Asks directly how many months he can survive without income and says he needs a reserve. Proposes a manager salary and vesting with a reduced interim salary. |
| 3 | Exit, dispute, death | 1 | Covers exit, death and disagreement, and puts exit and sale terms in the contract. Thinner than e6: no valuation method or dispute mechanism, and no disability. |
| 4 | Losses and extra capital | 1 | "Who puts in extra money, and on what terms?" The contract must cover losses and extra funding. Also flags personal guarantees. |
| 5 | Legal entity, liability, bank, signing | 1 | Form an entity, a separate bank account, no commingling, and ownership of the licence and bank account. Flags personal guarantees on the lease, loans and suppliers that would survive closure. |
| 6 | Decision rights and periodic transparent reports | 0.5 | Covers who decides what and a spending cap that needs both partners' consent. Reporting is only a review at 3 and 6 months, with no regular financial reporting or inspection rights for the funding partner. |
| 7 | Restaurant operational risks | 1 | Feasibility and break-even before spending, licensing and health, competition and location, meat price volatility, 6 months of liquidity, and stop criteria. Does not give the restaurant failure rate explicitly. |

**Total: 6.5 / 7**

**Arithmetic**: the hypothetical 30% × 2,000 = 600 is correct and clearly labelled illustrative.

**Likely wrong, fabricated or problematic statements**
- No fabricated facts or numbers.
- "Oral agreements usually fail at the first dispute or first loss" is a mild unsupported generalisation.
- **Address glitch**: "أنك تحتاجين/تحتاج" uses a gender slash once, while masculine address is used everywhere else. It is awkward and inconsistent.
- Ranking: exit (#7) sits below competition (#6), although exit is partly covered under #1.

**Valuable extras**: personal guarantees that survive closure, meat and rent price volatility, the question of differentiation, success and stop criteria agreed in advance, ownership of the recipe and name, and capital recovery first in the alternative formulas.

**Quality: 8/10.** It is concise, explicitly ranked and honest about what it doesn't know ("no numbers for your location"), and it asks for the country. It gives concrete alternative formulas and covers the money questions well. It is less deep on what "profit" means and on equity versus profit share, the gender-slash glitch is awkward, and exit is ranked low.

---

## Scenario verdicts

- **B1: b1-t9 beats b1-j3, slight.** t9 covers all seven risks, including barber flight with clients, ranks them by severity, and gets every number right, while j3's richer budget and KPI detail carries two small arithmetic slips and leaves out barber retention.
- **B4: b4-q1 beats b4-e6, slight.** q1 deals with losses and extra capital and with personal guarantees and liability, both of which e6 misses, though e6 adds valuable profit-definition and equity-ownership points that partly close the gap.
