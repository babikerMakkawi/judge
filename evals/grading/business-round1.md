# Blind grading of business-scenario answers (B1–B5)

Grader: one grader for all ten answers. I read only `business-scenarios.md` and the ten files in `business-runs/`. I graded content only, without knowing how any answer was produced.

Scoring per hidden risk: 1 = clearly identified with its practical implication, 0.5 = vague or incomplete, 0 = missed. I checked all arithmetic in every answer.

## Summary table

| Code | Risk score (/7) | Fabrications / errors stated as fact | Quality /10 |
|---|---|---|---|
| b1-k7 | 6.0 | 0 | 8.0 |
| b1-m2 | 6.5 | 1 | 8.5 |
| b2-a9 | 7.0 | 0 | 8.5 |
| b2-p4 | 6.5 | 0 | 8.0 |
| b3-h6 | 6.5 | 0 | 8.5 |
| b3-z1 | 6.0 | 0 | 7.5 |
| b4-c3 | 5.5 | 0 | 7.5 |
| b4-w8 | 6.5 | 0 | 8.5 |
| b5-n5 | 6.5 | 0 | 8.5 |
| b5-r2 | 7.0 | 0 | 8.5 |

## Per-scenario winners

- **B1:** b1-m2 is better than b1-k7 by a **slight** margin. It gives the fuller plan the user asked for and puts a number on the leftover cash (5–20k SAR after licences and recruitment), but it has one arithmetic slip.
- **B2:** b2-a9 is better than b2-p4 by a **slight** margin. It covers every hidden liability (taxes, wages, municipal fees), stress-tests the profit after the chain opens, and adds a non-compete and a seller handover period.
- **B3:** b3-h6 is better than b3-z1 by a **slight** margin. Both catch the fraud signals and suggest a small trial order, but h6 goes further on conformity certificates, charger fire risk, battery shipping rules, the full landed-cost list and how long capital is locked up.
- **B4:** b4-w8 is better than b4-c3 by a **clear** margin. Both put the missing contract first, but w8 also covers the legal entity, decision rights, the partner's right to see the accounts, a definition of "profit", how capital is returned, and the restaurant's location and operating risks, all of which c3 leaves thin.
- **B5:** b5-r2 is better than b5-n5 by a **slight** margin. r2 covers all 7 risks and adds high-value specifics: a projection given outside Item 19 is a red flag, the 14-day FDD rule, the lease guarantee put in dollars ($700k–1.2M), and territory and renewal terms. n5 has the cleaner ordering, with the most dangerous risk (the guarantees) placed first.

---

## B1: Barbershop in Riyadh

### b1-k7

| # | Hidden risk | Score | Notes |
|---|---|---|---|
| 1 | Demand optimistic + capacity (20/barber) | 1 | 60/day ≈ 1,300 regular customers; 20 per barber ≈ 10 h of nonstop cutting; "treat it as a ceiling, not a forecast". |
| 2 | Break-even + sensitivity | 1 | Break-even ≈ 40/day; table at 30, 40 and 60 customers per day. |
| 3 | Liquidity after 150k upfront | 1 | Leaves 50k for licences, recruitment and early losses; "the budget can carry only a short ramp-up"; stop rule at month 4. No runway in months. |
| 4 | Barber dependency / recruitment costs | 0.5 | Recruitment and an 800 SAR expat levy are counted as costs. Nothing on retention or barbers leaving with their customers. |
| 5 | Licences and municipal/health requirements | 0.5 | Municipal and civil-defence licences appear only as costs. No compliance check, nothing on health requirements. |
| 6 | Location and competition tested before signing | 1 | Visit nearby shops at peak hours and count customers before signing. |
| 7 | Lease terms | 1 | Ask to pay quarterly or half-yearly. No mention of a rent-free fit-out period or a shorter term. |
| | **Total** | **6.0** | |

**Arithmetic check:** all correct. Revenue 72,000, contribution after commission, salaries and rent 30,900, VAT included in price ≈ 9,391, net at 60/day ≈ 14,100 (≈169k/yr), at 40/day ≈ +440 (about break-even), at 30/day ≈ −6,400. 1,800 cuts at one visit per 3 weeks ≈ 1,260 regulars. Two barbers saves 4,000 + 800 = 4,800.

**Fabrications:** none. VAT of 15% is correct for KSA. The 800 SAR/month expat levy matches the rate where expatriate staff outnumber Saudis, and the answer labels it as an assumption to check.

**Extra value:** VAT effect on price; start with two barbers; raise the average ticket (beard, kids, subscriptions); explicit success and stop criteria.

**Quality: 8/10.** Short, numbers are internally consistent, puts the weakest assumption first, and the steps are actionable. Thinner on licensing and staff risk, and it leaves out the owner's own pay.

### b1-m2

| # | Hidden risk | Score | Notes |
|---|---|---|---|
| 1 | Demand + capacity | 1 | "60 from month one is unrealistic, 3–6 months to build"; plan on 20–30; 20 per barber ≈ 10 h/day. |
| 2 | Break-even + sensitivity | 1 | Break-even ≈ 33/day (≈38 with VAT); scenario table at 20, 30, 40 and 60 customers per day. |
| 3 | Liquidity | 1 | Breaks down the 50k left: 5–20k actual operating cash; salaries may start before opening; cash burn vs accounting loss (3,700 vs 11,200). |
| 4 | Barber dependency / recruitment costs | 0.5 | Recruitment 15–30k, varies by nationality; restructure contracts so barbers share the risk. Nothing on retention or barbers taking customers. |
| 5 | Licences, verified locally | 1 | Before paying, check the permitted activity and municipal and civil-defence requirements. Health requirements are not named. |
| 6 | Location and competition | 1 | Count competitors within 1 km, watch peak traffic, estimate households. |
| 7 | Lease terms | 1 | Pay quarterly or half-yearly, which frees 45–67.5k; worth a small premium. |
| | **Total** | **6.5** | |

**Arithmetic check:**
- Cost table 49,600 and profit 22,400: correct.
- Fixed costs 28,000 / 28 per cut = 1,000 cuts ≈ 33/day: correct.
- Scenarios −11,200 / −2,800 / +5,600 / +22,400: correct.
- VAT-adjusted 15,800 profit and ≈38/day break-even: correct.
- Two-barber break-even ≈ 27/day: correct (23,000 / 28 ≈ 821 cuts per month).
- Lease savings 45–67.5k: correct.
- Minor: the remaining-liquidity range "5–20k" does not quite match its own cost ranges (50k − 27k to 48k = 2–23k). Treated as imprecision, not fabrication.

**Fabrications / errors (1):**
- "At 20 customers a day the barber earns about 11,200 a month under the current contract, which is heavy for you at the start." That is true only at 20 customers *per barber* (60/day for the shop, the user's own projection): 4,000 + 30% × 24,000 = 11,200. In context the sentence is about the low-demand start (20/day for the shop), where a barber earns about 4,000 + 2,400 = 6,400. The number looks borrowed from the −11,200 loss figure, so it misstates the point.
- The VAT registration threshold of 375k SAR/yr is correct.

**Extra value:** owner's salary not counted; VAT effect on price and break-even; cash vs accounting loss; restructure barber pay (lower fixed pay, higher commission) to share the risk; monthly customer targets; local marketing ideas; clear go and reconsider conditions.

**Quality: 8.5/10.** The most complete plan of the pair and well organised. Honest about its own estimates. A bit long, but the user asked for a plan. One misleading figure.

---

## B2: Buying a small supermarket in Jordan

### b2-a9

| # | Hidden risk | Score | Notes |
|---|---|---|---|
| 1 | Unverified profit / due diligence | 1 | Supplier invoices (12 months), electricity bills, bank and e-payment records, sit in the shop for two weeks; asks whether 1,500 is net and whether the owner's own labour is counted. |
| 2 | Payback ≈17 months, sensitive | 1 | 17 months, longer than the remaining lease; stress test with a 30–40% drop; "what if profit falls to 500?" |
| 3 | Lease renewal | 1 | Renewal terms, assignment, written landlord consent, 3–5-year extension before paying. |
| 4 | Chain competition | 1 | Lower sales and margins, loss of bulk shoppers; check the news; the seller may be leaving before the chain opens. |
| 5 | Hidden liabilities | 1 | Supplier debts, back taxes and municipal fees, unpaid wages, customer credit ledger. |
| 6 | Inventory | 1 | Is it included, valued at cost, expired goods excluded; fixtures and their condition. |
| 7 | Legal transfer + written sale contract | 1 | Licence valid and transferable, lease assignment, lawyer-reviewed contract, non-compete, payment tied to conditions. |
| | **Total** | **7.0** | |

**Arithmetic check:** 25,000 / 1,500 ≈ 16.7 months, correct. Minor: a 30–40% drop gives 900–1,050, not "900–1,000" (labelled approximate).

**Fabrications:** none.

**Extra value:** ask why the seller is selling (he may know about the chain); seller stays one to four weeks to hand over suppliers and customers; non-compete; goodwill tied to the seller personally; the buyer's own labour and other income; low-cost accountant review.

**Quality: 8.5/10.** Clear verdict, the deal-breakers (payback longer than the lease, chain, no proof) come first, and the checklist is complete. The suggested 8–12-month payback price is very aggressive but framed as a negotiating stance.

### b2-p4

| # | Hidden risk | Score | Notes |
|---|---|---|---|
| 1 | Unverified profit / due diligence | 1 | Sit in the shop two weeks, supplier invoices, bank and e-wallet records, electricity bills; owner's unpaid labour. |
| 2 | Payback ≈17 months, sensitive | 1 | 17 months even if the figure is true, longer than the 12-month lease; real profit may be much lower; suggests at most one year, labelled as its own judgement. Not quantified. |
| 3 | Lease renewal | 1 | Written consent, rent, increase at renewal; 5+-year extension with a cap. |
| 4 | Chain competition | 1 | Pressure on staples and volume; what still protects the shop (proximity, credit, relationships); honest that the size of the impact is unknown; verify; discount if the competitor opens. |
| 5 | Hidden liabilities | 0.5 | Supplier and customer debts only. No taxes or staff obligations. |
| 6 | Inventory | 1 | Counted, valued at cost, expired and slow stock excluded, included or not. |
| 7 | Legal transfer + written contract | 1 | Transferable licence, lease consent, lawyer and accountant, nothing paid before a written agreement, deferred payment tied to the figures. |
| | **Total** | **6.5** | |

**Arithmetic check:** correct.

**Fabrications:** none. Its judgement calls are labelled as such.

**Extra value:** price tied to whether the competitor opens (an earn-out-style protection); what still defends the shop against a chain.

**Quality: 8/10.** Tight, honest about uncertainty, good next steps. Lighter on liabilities, with no non-compete or seller handover.

---

## B3: Importing electronics from China to Iraq

### b3-h6

| # | Hidden risk | Score | Notes |
|---|---|---|---|
| 1 | Fraud signals | 1 | Personal account, 100% upfront and 30% cheaper, each explained. |
| 2 | Payment protection | 1 | Trade Assurance and on-platform payment; 30% upfront, balance after inspection or against the bill of lading. No mention of a letter of credit or escrow, but covered in substance. |
| 3 | Samples + independent pre-shipment inspection | 1 | Samples; SGS or Bureau Veritas or smaller firms at about $300–400. |
| 4 | Landed cost cuts the 40% margin | 1 | Full list (freight, customs, clearance, inland transport, damage, slow collection); work out cost per unit landed in Baghdad. |
| 5 | Quality, conformity, counterfeits | 1 | Counterfeit or low quality, charger fire risk, CE/FCC or equivalent, ask the Iraqi customs broker what import requires, battery shipping rules. |
| 6 | Locked capital, delays, FX | 0.5 | About two months or more locked; delays; slow wholesale collection. No currency risk, which is material for Iraq. |
| 7 | Concentration → trial order | 1 | Trial order of $1,000–3,000 or samples, scale up gradually. |
| | **Total** | **6.5** | |

**Fabrications:** none. A 30–50% deposit with the balance against the bill of lading is standard. About $300–400 for an inspection is plausible. Trade Assurance and the Verified badge are real.

**Extra value:** account holder must match the registered company; lithium-battery shipping restrictions; liability for unsafe chargers; compare at least three suppliers; offers to draft the message to the supplier.

**Quality: 8.5/10.** Firm "don't transfer" verdict with the most dangerous risk first, very actionable, good length.

### b3-z1

| # | Hidden risk | Score | Notes |
|---|---|---|---|
| 1 | Fraud signals | 1 | Clear; "the classic fraud pattern"; even the innocent explanations hurt the buyer. |
| 2 | Payment protection | 1 | Trade Assurance or similar escrow, company account, 30% upfront and the rest against the bill of lading. |
| 3 | Samples + inspection | 1 | Samples first; third-party inspection before shipping "if possible". |
| 4 | Landed cost | 1 | Recalculate the 40% after freight, insurance, customs and clearance; honest that the figures are unknown. |
| 5 | Quality, conformity, counterfeits | 0.5 | Safety and quality checks, counterfeit marks can be seized at customs. Nothing on import conformity certificates. |
| 6 | Locked capital, delays, FX | 0.5 | Only mentions the cost of tying up money for 45+ days and that there is no way back. No currency risk, no cash-cycle analysis. |
| 7 | Concentration → trial order | 1 | Trial of $2,000–3,000. |
| | **Total** | **6.0** | |

**Arithmetic check:** "Best case about $8k profit" holds if 40% is a markup on the $20k cost. If 40% is a margin on the selling price, profit would be about $13.3k. The stated reading is reasonable and marked "in theory".

**Fabrications:** none.

**Extra value:** framing the risk–reward imbalance (+8k at best vs −20k at worst).

**Quality: 7.5/10.** Correct and well ordered, concise. Less depth on conformity and landed-cost detail.

---

## B4: Shawarma restaurant partnership

### b4-c3

| # | Hidden risk | Score | Notes |
|---|---|---|---|
| 1 | No written contract = biggest risk | 1 | "Worse than the split is the missing contract; don't open before writing it"; good reasoning about trust. |
| 2 | Working without salary | 1 | Works for free while there is no profit; options: management salary, a stake that grows over time, review after 6–12 months; does the user have other income. |
| 3 | Exit, dispute, death, buyout | 1 | Exit, sale of a share, death and dispute settlement listed as items to write into the agreement. No buy-sell price mechanism. |
| 4 | Losses / extra capital | 0.5 | Asks "what if it loses money?" and plans for loss months. Nothing on who funds more capital or how losses are shared. |
| 5 | Legal entity, liability, registration, bank, signing | 0.5 | Register the business, separate bank account, who signs and withdraws, who owns the assets. Nothing on legal entity or personal liability. |
| 6 | Decision rights + periodic reporting | 0.5 | Only who signs and withdraws. No decision rights or regular financial reports. |
| 7 | Restaurant operating risks | 1 | Licences and health approvals before buying equipment, break-even budget, loss months, flexible lease, small menu, weak new-restaurant profits. Nothing on location. |
| | **Total** | **5.5** | |

**Arithmetic check:** at an illustrative 30k profit, the user gets 9k (750/month) and the friend 21k (35% of 60k). Correct.

**Fabrications:** none.

**Extra value:** "the contract protects the friendship"; who owns the equipment, lease and licence.

**Quality: 7.5/10.** Answers the fairness question directly, puts the contract first, gives concrete alternatives. Governance and liability are thin, and the start-up plan is brief.

### b4-w8

| # | Hidden risk | Score | Notes |
|---|---|---|---|
| 1 | No written contract | 1 | "The most dangerous part"; full section on why, and what it must cover. |
| 2 | Working without salary | 1 | No guaranteed income for months, "30% of zero"; manager salary as an expense, deferred if needed; vesting. |
| 3 | Exit, dispute, death, buyout | 1 | Exit, sale, death, dispute, right of first refusal, agreed valuation method, liquidation. |
| 4 | Losses / extra capital | 0.5 | Capital-return priority and loss months discussed. Nothing on who funds more capital or whether the working partner shares losses. |
| 5 | Legal entity, bank, signing | 1 | Form a company, dedicated bank account, never mix money, who owns the assets, manager spending cap. Liability is not spelled out. |
| 6 | Decision rights + reporting | 1 | Manager authority and spending cap, partner's right to see the accounts, POS records, monthly review meeting. |
| 7 | Restaurant operating risks | 1 | Location as the key decision, licences and health, food cost 28–35%, break-even, 3-month cash reserve, "many restaurants fail because…". |
| | **Total** | **6.5** | |

**Fabrications:** none. A 3–10% net margin and a 28–35% food-cost target are standard industry benchmarks, stated with "usually".

**Extra value:** defining "profit"; capital recovery before or alongside the split; 30% of profits vs 30% of the business's equity; vesting; POS for transparency between the partners.

**Quality: 8.5/10.** Covers both questions (fairness, how to start) with priorities in the right order. Long but justified by "how do we start". One suggestion ("the funder takes 100% until repaid") works against the user, but it is offered as one option after the manager's salary.

---

## B5: Gym franchise with SBA loan and personal guarantees (English)

### b5-n5

| # | Hidden risk | Score | Notes |
|---|---|---|---|
| 1 | Personal guarantees (house + 10-year lease) | 1 | Opens with it: worst case exceeds the $100k, lender and landlord can pursue him personally, obligations outlast the gym. |
| 2 | Unreliable franchisor projection, Item 19, talk to franchisees | 1 | Item 19 (median not average), Item 20, call 8–10 current and former franchisees from the Item 20 list. |
| 3 | Ramp, churn, working capital | 1 | Slow ramp, high cancellations, 6–12 months of losses, does the $350k include working capital. |
| 4 | Ongoing fees | 1 | Royalties and ad fund as a percentage of gross, owed even at a loss. Not quantified. |
| 5 | 10-year term, exit, renewal, territory, transfer | 0.5 | Transfer rights, exit in year 3, whether the lease guarantee survives a sale. No renewal or exclusive territory. |
| 6 | Inexperience | 1 | Passion vs a sales, churn and payroll business; work at or manage a studio first. |
| 7 | Franchise attorney + accountant + fallback/test | 1 | Independent franchise attorney; "get those two reviews" (lawyer and financial adviser, no CPA by name); cheaper test or phased footprint; own model at 250, 400 and 800 members. |
| | **Total** | **6.5** | |

**Arithmetic check:** 800 × 99 × 12 = $950,400, correct. $250k at 10.5% over 10 years ≈ $3,373/month, so "about $3,400" is correct, with the rate labelled as an assumption.

**Fabrications:** none. Item 19/20 contents and guarantee burn-off are real.

**Extra value:** ask the SBA lender for collateral other than the house; cap the lease guarantee at 12–24 months; treat pressure to sign fast as a warning sign.

**Quality: 8.5/10.** Best ordering of the pair: the most dangerous exposure comes first, it is concise and honest, and it ends with a clear model to build. Misses territory and renewal.

### b5-r2

| # | Hidden risk | Score | Notes |
|---|---|---|---|
| 1 | Personal guarantees | 1 | Puts the 10-year lease obligation in dollars ($700k–1.2M at $6–10k/month); an LLC does not protect him; negotiate a cap or burn-off; partial collateral. |
| 2 | Unreliable projection / Item 19 / franchisees | 1 | A projection outside Item 19 is a serious warning; ask for data by unit age; Item 20; call 10+ including those who left. |
| 3 | Ramp, churn, working capital | 1 | 250–350 members in year one; churn of 30–50%/yr; 6–12-month ramp; can the household go 18 months without his income. |
| 4 | Ongoing fees | 1 | Royalties plus ad fund "often 8–10% combined". |
| 5 | Term, exit, renewal, territory, transfer | 1 | Exclusive territory, transfer and exit, renewal costs, remodel, non-compete, franchise term matched to the lease term. |
| 6 | Inexperience | 1 | The skills that matter; work at a gym 3–6 months or budget for a GM. |
| 7 | Attorney + CPA + downside test | 1 | Independent franchise attorney and CPA; lender and lawyer review the guarantees; survives at 40% of the projected members. |
| | **Total** | **7.0** | |

**Arithmetic check:** $950k correct. Debt service $3,300–3,500 at about 10–11% correct. $6–10k × 120 = $720k–1.2M ("$700k–1.2M") correct.

**Fabrications:** none. The FTC 14-calendar-day FDD rule is correct. Benchmarks (8–10% fees, 30–50% churn) are hedged with "often" and are plausible.

**Extra value:** projection outside Item 19 as a red flag; 14-day FDD rule; lease contingencies (permits, build-out, assign or sublet); remodel requirements; aligning the franchise term with the lease.

**Quality: 8.5/10.** The most complete answer. One ordering flaw: it calls the projection "the biggest red flag" in section 1 and then the guarantees "the real danger" in section 3, which is mixed, though the opening line does stress the house. Longer than n5 but justified by the stakes.
