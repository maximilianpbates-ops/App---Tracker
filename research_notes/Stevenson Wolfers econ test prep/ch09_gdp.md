# Chapter 9, "Sizing Up the Economy Using GDP" (slide deck title: "GDP and the Macroeconomy"), Stevenson & Wolfers, *Principles of Macroeconomics*, 2nd ed. (Worth/Macmillan Learning, ©2023): checking the slides against BEA and academic sources, with a full catalogue of calculation methods

Textbook identification (corrected by the coordinator): the book is **Betsey Stevenson & Justin Wolfers, *Principles of Macroeconomics*, 2nd ed., ©2023**, not Goolsbee/Levitt/Syverson. Macmillan Learning's table of contents lists:
- Part III, "Macroeconomic Foundations and the Long Run": **Ch. 9 "Sizing Up the Economy Using GDP"**, Ch. 10 "Economic Growth", Ch. 11 "Unemployment", Ch. 12 "Inflation and Money"
- **Ch. 17 "Tracking the Business Cycle"**, where recession dating is probably treated in more depth

The same page notes a 3rd edition scheduled for Dec 19, 2025. — [Macmillan Learning, *Principles of Macroeconomics* 2e](https://store.macmillanlearning.com/Us/product/Principles-of-Macroeconomics/p/1319432085)

Data note: all U.S. figures below were pulled from FRED/ALFRED on 2026-10-14. That vintage already includes BEA's September 30, 2026 release (the Q2 2026 third estimate), which also carried the 2026 annual update covering 2021Q1–2026Q1. Shares and growth rates marked "computed" are my own arithmetic from the cited FRED levels, checked in Python.

---

## Key Question 1: Latest BEA figures (2024, 2025, latest 2026 quarter), shares of C/I/G/NX, and the 2021 figure on the slides

### Takeaway
U.S. nominal GDP was **$29.38T in 2024** and **$30.86T in 2025**. Real growth was **+2.9% in 2024** and **+2.3% in 2025**. In the latest quarter (Q2 2026, third estimate released Sept 30, 2026), real GDP grew **2.2% at an annual rate** and nominal GDP stood at an annualized **$32.56T**. Expenditure shares hardly move from year to year: C ≈ 67–68%, I ≈ 18%, G ≈ 17–17.5%, NX ≈ −3%.

The slides' "2021 GDP = $23 trillion" figure matches BEA's **original** January 2022 estimate of **$22.99T**. Revisions have since raised 2021 GDP to $23.32T (2022 vintage), $23.59T (2023), and **$23.75T** (current). "~$23.3T" was the published value only between late 2022 and the 2023 comprehensive update.

### Cited Findings

**Latest quarter (Q2 2026)**
- BEA third estimate (released Sept 30, 2026): "Real gross domestic product (GDP) increased at an annual rate of 2.2 percent in the second quarter of 2026." It was revised up 0.7 pp from the second estimate (1.5%). Q1 2026 was revised to 2.5% (from 2.1%). — [BEA news release, Q2 2026 third estimate](https://www.bea.gov/news/2026/gdp-third-estimate-industries-corporate-profits-state-gdp-and-state-personal-income-2nd); [BEA GDP page](https://www.bea.gov/data/gdp/gross-domestic-product)
- Same release:
  - Current-dollar GDP rose 8.5% at an annual rate in Q2 2026.
  - The PCE price index rose 5.0%, and 3.3% excluding food and energy.
  - The gross domestic purchases price index rose 5.6%.
  - Real GDI rose 2.6%, and the average of real GDP and real GDI rose 2.4%.
  - Growth came from consumer spending, investment, and exports. Imports (a subtraction) increased.
  - The release incorporates the 2026 annual update, which "covered the first quarter of 2021 through the first quarter of 2026". The reference year for chained dollars remains 2017.

  — [BEA Q2 2026 third estimate](https://www.bea.gov/news/2026/gdp-third-estimate-industries-corporate-profits-state-gdp-and-state-personal-income-2nd)
- Q2 2026 nominal GDP (SAAR) was **$32,563.0B**; Q1 2026 was $31,906.3B. — [FRED GDP](https://fred.stlouisfed.org/series/GDP)
- Q2 2026 real GDP was **$24,408.0B** (chained 2017 $, SAAR); Q1 2026 was $24,274.4B. Computed annualized growth = 2.22%, which matches BEA's 2.2%. — [FRED GDPC1](https://fred.stlouisfed.org/series/GDPC1)
- Q2 2026 nominal GDP per capita was **$95,005** (SAAR). — [FRED A939RC0Q052SBEA](https://fred.stlouisfed.org/series/A939RC0Q052SBEA)
- Q2 2026 real GDP per capita was **$71,212** (chained 2017 $). — [FRED A939RX0Q048SBEA](https://fred.stlouisfed.org/series/A939RX0Q048SBEA)
- Q2 2026 implicit price deflator was 133.411 (2017=100), against 131.440 in Q1 2026. Computed annualized rise ≈ 6.1%. — [FRED GDPDEF](https://fred.stlouisfed.org/series/GDPDEF)
- A search summary of the BEA release lists the next release, "GDP (Advance Estimate), 3rd Quarter 2026", for **October 29, 2026**. A BEA taxonomy page in the same results carried a "lapse in appropriations" notice. — [BEA Q2 2026 third estimate](https://bea.gov/news/2026/gdp-third-estimate-industries-corporate-profits-state-gdp-and-state-personal-income-2nd) (see Gaps)

**Annual figures (current vintage)**

| Year | Nominal GDP ($B) | Real GDP (chained 2017 $B) | Real growth | Nominal growth | Nominal GDP per capita | Population (BEA, thousands) |
|---|---|---|---|---|---|---|
| 2021 | 23,745.8 | 21,556.0 | — | — | $71,416 | 332,503 |
| 2022 | 26,059.7 | 22,079.7 | 2.4% | 9.7% | $77,941 | 334,350 |
| 2023 | 27,825.9 | 22,724.1 | 2.9% | 6.8% | $82,548 | 337,087 |
| 2024 | **29,381.0** | 23,394.9 | **2.95%** | 5.6% | **$86,390** | 340,095 |
| 2025 | **30,861.3** | 23,943.3 | **2.34%** | 5.0% | **$90,252** | 341,944 |

Sources for the table: [FRED GDPA](https://fred.stlouisfed.org/series/GDPA); [FRED GDPCA](https://fred.stlouisfed.org/series/GDPCA); [FRED A939RC0A052NBEA (GDP per capita)](https://fred.stlouisfed.org/series/A939RC0A052NBEA); [FRED B230RC0A052NBEA (population)](https://fred.stlouisfed.org/series/B230RC0A052NBEA). Growth rates are computed.

- Annual real GDP per capita for 2025 ≈ **$70,021** (chained 2017 $), computed as 23,943.3B / 341.944M. The four quarterly values for 2025 (69,278; 69,881; 70,469; 70,453) average to the same number. Real GDP per capita grew 1.79% in 2025 while population grew 0.54% (computed). — [FRED A939RX0Q048SBEA](https://fred.stlouisfed.org/series/A939RX0Q048SBEA); [FRED GDPCA](https://fred.stlouisfed.org/series/GDPCA)
- Before the September 2026 annual update, 2025 nominal GDP was $30,762.1B and 2025 real growth was ≈2.1% (June 2026 vintage: 23,850.4 / 23,358.4). Any source printed before October 2026 will therefore show slightly different numbers. — [ALFRED GDPA vintages](https://alfred.stlouisfed.org/series?seid=GDPA); [ALFRED GDPCA vintages](https://alfred.stlouisfed.org/series?seid=GDPCA)

**Shares of GDP (computed from FRED levels: PCEC, GPDI, GCE, NETEXP, EXPGS, IMPGS)**

| Period | C (PCE) | I (gross private domestic investment) | G (gov't consumption + gross investment) | NX | Exports | Imports |
|---|---|---|---|---|---|---|
| 2021 | 67.9% | 17.9% | 17.8% | −3.5% | 10.8% | 14.4% |
| 2024 | 67.5% | 18.1% | 17.5% | −3.0% | 11.0% | 14.0% |
| 2025 | 67.6% ($20,870B) | 18.0% ($5,557B) | 17.4% ($5,355B) | −3.0% (−$921B) | 10.8% ($3,341B) | 13.8% ($4,262B) |
| Q2 2026 (SAAR) | 67.5% ($21,993B) | 17.9% ($5,823B) | 17.3% ($5,627B) | −2.7% (−$880B) | 11.7% ($3,795B) | 14.4% ($4,675B) |

Sources: [FRED PCEC](https://fred.stlouisfed.org/series/PCEC); [FRED GPDI](https://fred.stlouisfed.org/series/GPDI); [FRED GCE](https://fred.stlouisfed.org/series/GCE); [FRED NETEXP](https://fred.stlouisfed.org/series/NETEXP); [FRED EXPGS](https://fred.stlouisfed.org/series/EXPGS); [FRED IMPGS](https://fred.stlouisfed.org/series/IMPGS). Annual values are the average of the four quarterly SAAR values. 2025 check: 67.6 + 18.0 + 17.4 − 3.0 = 100.0.

**Checking the slide's 2021 figures**
- BEA's original release (Jan 27, 2022): "Current-dollar GDP increased 10.0 percent, or $2.10 trillion, in 2021 to a level of $22.99 trillion" and "Real GDP increased 5.7 percent in 2021." — [BEA Q4 & year 2021 advance estimate](https://www.bea.gov/news/2022/gross-domestic-product-fourth-quarter-and-year-2021-advance-estimate)
- How 2021 nominal GDP changed across ALFRED vintages:
  - $22,993.5B (Feb 2022)
  - **$23,315.1B** (Oct 2022 and June 2023 vintages)
  - $23,594.0B (Oct 2023, after the 2023 comprehensive update)
  - $23,681.2B (Oct 2024)
  - $23,725.6B (Oct 2025)
  - **$23,745.8B** (Oct 13, 2026)

  — [ALFRED GDPA](https://alfred.stlouisfed.org/series?seid=GDPA)
- Slide per-capita check: $23.0T ÷ 332.2M = **$69,235**, consistent with the slide's "$69,200". With the original $22.99T, the result is $69,216 (computed). BEA's current 2021 population is 332.503M, and its current 2021 nominal per-capita GDP is **$71,416**. — [FRED A939RC0A052NBEA](https://fred.stlouisfed.org/series/A939RC0A052NBEA); [FRED B230RC0A052NBEA](https://fred.stlouisfed.org/series/B230RC0A052NBEA)

### Inferences
- The slides are internally consistent ($23T ÷ 332.2M ≈ $69,200) and match the data available when the book went to press. For an exam, "$23 trillion" is the expected answer. A student quoting today's numbers should say about **$31 trillion (2025)** and about **$90,000 per person**.
- Q2 2026 nominal growth (8.5%) was far above real growth (2.2%), so roughly 6 percentage points of the nominal increase was price change. This is a live illustration of why the slides insist on real GDP.
- C ≈ two-thirds of GDP is the single most stable fact in the table, and makes a good multiple-choice anchor. NX has been negative every year shown (the U.S. runs a trade deficit), so for the U.S., GDP < C + I + G.

### Gaps
- I could not confirm whether the Oct 29, 2026 Q3 advance release will go out on schedule. One BEA page showed a "lapse in appropriations" banner, and it was unclear whether that was current or cached from a past shutdown.
- I did not retrieve BEA's own NIPA Table 1.1.10 (percentage shares). The shares above are computed from FRED levels, so BEA's published shares may differ by ±0.1 pp because of rounding.
- I could not identify the exact population source behind the slide's 332.2M figure. It is close to Census resident-population estimates but differs from BEA's 332.5M.

---

## Key Question 2: BEA definitions: investment components, G vs. transfers, imports, owner-occupied imputed rent, GDP vs. GNP/GNI, plus traps such as used goods, existing homes, and stocks

### Takeaway
BEA's *NIPA Handbook* backs up every slide definition, with a few nuances that hard exams like to test:
1. **Investment** includes **intellectual property products** (R&D, software, entertainment originals) as well as new housing and inventory change.
2. **Transfers** (Social Security, Medicare and similar benefits) "are not counted as production" and are excluded from G.
3. The **largest exception** to "market transactions only" is **imputed rent on owner-occupied housing** (≈8% of GDP).
4. In a used-good or existing-home sale, the **dealer's margin / broker's commission IS counted**, even though the item itself is not.
5. **GNP = GDP + income receipts from the rest of the world − income payments to the rest of the world.**

### Cited Findings

**GDP definition and the three approaches**
- BEA's definition: "GDP is defined as the market value of the goods, services, and structures produced by the economy in a given period. Conceptually, this measure can be arrived at by three separate means: as the sum of goods and services sold to final users, as the sum of income payments and other costs incurred in the production of goods and services, and as the sum of the value added at each stage of production." The three "may not result in identical estimates … because of differences in data sources, timing, and estimation techniques." — [BEA NIPA Handbook ch. 2, Fundamental Concepts](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)

**Expenditure components**
- **Personal consumption expenditures (PCE)** = goods and services "purchased by, or on the behalf of, persons." — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- **Gross private fixed investment** covers "additions and replacements to the stock of private fixed assets without deduction of depreciation." It has two parts:
  - Nonresidential: "investment by businesses and nonprofit institutions in nonresidential structures, equipment, and intellectual property products."
  - Residential: "investment by businesses and households in residential structures and equipment, primarily new construction of single-family and multifamily units."

  — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- **R&D counts as investment:** "Private investment in research and development and in entertainment originals, along with that in software (which has been treated as a fixed asset since the 1999 comprehensive NIPA revision), is now shown in the NIPAs in the subcategory 'intellectual property products' in nonresidential fixed investment." — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- **Change in private inventories** "measures the value of the change in the physical volume of inventories owned by private business over a specified period, valued in the average prices of that period." — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- **Net exports** = exports − imports. In BEA's words: "imports offset the non-U.S. production that is included in the other final-expenditure components. For example, PCE includes expenditures on imported cars as well as on domestically produced cars; thus … the sales of foreign-produced cars that are included in PCE are offset by a comparable entry in the imports." Footnote 20: "the domestic value-added (such as the margin provided by domestic dealerships) on imported cars … is included in GDP." — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- **Government consumption expenditures and gross investment (G):**
  - "Current consumption expenditures consists of the spending by general government in order to produce and provide goods and services to the public." "Gross investment consists of spending … for fixed assets (structures, equipment, and intellectual property products)." — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
  - BEA glossary: "The value of services produced by government, measured as the purchases made by government on inputs of labor, intermediate goods and services, and investment expenditures." — [BEA glossary](https://www.bea.gov/help/glossary/government-consumption-expenditures-and-gross-investment)

**Transfers are excluded from G**
- BEA describes G as spending "to produce and provide services to the public, such as national defense and public school education," plus investment "such as highway construction." It treats social benefits separately: governments "also provide social benefits, such as social security and Medicare, to households." — [BEA NIPA Handbook ch. 9, Government](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-09.pdf)
- "current transfer payments, which account for a significant part of the federal budget, are not counted as production and are therefore excluded from the NIPA measures of consumption expenditures." — [BEA NIPA Handbook ch. 9](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-09.pdf)
- Government consumption is "valued at their cost of production." This is why the vaccines and public schools on the slides enter at cost even though they are not sold at a market price. — [BEA NIPA Handbook ch. 9, Table 9.1 note](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-09.pdf)

**Imputations: the exception to "market value"**
- "In the NIPAs, a number of imputations for own-use and nonmarket transactions are made in order to include in the accounts the value of certain goods and services that have no observable price." — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- "**The largest NIPA imputation** is that made to approximate the value of the services provided by owner-occupied housing … thereby keeping GDP invariant as to whether a house is owned or rented … the purchase of a new house (excluding the value of the unimproved land) is treated as an investment, the ownership of the home is treated as a productive enterprise … the value of this service is measured as the income the homeowner could have received if the house had been rented to a tenant." — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- Owner-occupied imputed rent "accounts for about 8 percent of GDP." — [BEA Working Paper WP2017-7](https://www.bea.gov/research/papers/2017/imputing-rents-owner-occupied-housing-directly-modelling-their-distribution)
- Another large imputation covers banking services provided "without charge or for a small fee" (imputed interest). Food furnished to employees is also imputed. — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)

**Exclusions (production boundary)**
- "certain household activities—such as housework, do-it-yourself projects, and care of family members—are excluded." — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- "illegal activities, such as gambling and prostitution in some states, should in principle be included … However, these activities are excluded from the U.S. accounts because … data are not available." PCE "Excludes purchases of illegal goods and services." — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf); [ch. 5, PCE](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-05.pdf)
- "the growth of trees in an uncultivated forest is not included in production, but the harvesting of the trees from that forest is included." — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)

**Used goods, existing assets, financial assets**
- Used vehicles: "net purchases of used motor vehicles consist of dealers' margins … In calculating GDP, the intersectoral net transactions offset, leaving the margins on the transactions as value added." PCE: "Transactions between households are not reflected in PCE because they cancel in the aggregation of the personal sector." — [BEA NIPA Handbook ch. 5](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-05.pdf)
- Existing homes: the house itself is excluded, but BEA capitalizes as residential investment "all of the nonfinancial ownership transfer costs that are associated with the purchase of a residential asset … title insurance; title, abstract, and attorney fees; … state and local government documentary and stamp taxes; … surveys and engineering services; as well as the previously capitalized brokers' commissions on the sale of residential structures." — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- Capital gains and transfers of existing assets are excluded from NIPA income: "Capital gains or losses … reflect changes in the prices of existing assets and thus do not represent changes in the real stock of produced assets"; "Capital transfers … reflect changes in the ownership of existing assets." Personal income "includes ordinary dividends … but it excludes the capital gains." Financial assets (including shares) "are covered in the financial accounts of the United States … maintained by the Federal Reserve Board," not the production accounts. — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)

**Value added and gross output**
- "value added is defined as the difference between an industry's gross output (sales or receipts plus other operating income and inventory change) and its intermediate inputs." — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- BEA's double-counting example: "in gross output, the value of the tires is counted twice—once in the value of the auto manufacturer's output and once in the value of the tire manufacturer's output." In 2017, gross output was $34.5T while GDP was $19.6T. — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)

**Income approach (GDI)**
- "GDI is equal to compensation of employees, plus taxes on production and imports less subsidies, plus net operating surplus, plus consumption of fixed capital." Compensation = wages and salaries + supplements. — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)

**GDP vs. GNP/GNI**
- "domestic measures are concerned with where an activity takes place, while national measures are concerned with to whom the activity is attributed." "GNP is equal to GDP plus income receipts from the rest of the world less income payments to the rest of the world, and it is conceptually equivalent to gross national income." — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- BEA's plant examples: "for an assembly plant that is owned by a Japanese auto company and located in the United States, all of its output is included in GDP, but only the portion of the value that reflects U.S. residents' labor and property is included in GNP. And, for an assembly plant that is owned by a U.S. auto company and located in Great Britain, none of its output is included in GDP, but the portion … that reflects U.S. residents' labor or property is included in GNP." This directly validates the slide's "within a country" bullet. — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- U.S. GNP 2025 = $30,846.1B, against GDP of $30,861.3B (GNP $15.2B lower). In 2023, GNP ($27,892.4B) exceeded GDP ($27,825.9B). — [FRED GNPA](https://fred.stlouisfed.org/series/GNPA); [FRED GDPA](https://fred.stlouisfed.org/series/GDPA)

**Real measures**
- BEA's real measures use "chain-type indexes that are calculated using a Fisher formula." This is not the single fixed base year the textbook uses. "Implicit price deflators … are calculated as the ratio of the current-dollar value to the corresponding chained-dollar value, multiplied by 100." — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)

#### Slide-claim check

| Slide claim | Verdict | Source |
|---|---|---|
| GDP = market value of all final goods and services produced within a country in a given year | ✅ Matches (BEA adds "structures") | [BEA ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf) |
| Government purchases (vaccines, schools) included | ✅ Valued at cost of production | [BEA ch. 9](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-09.pdf) |
| Washing your own car excluded | ✅ Household activities excluded | [BEA ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf) |
| Used cars / resales excluded | ✅ Item excluded, but the **dealer margin is included** | [BEA ch. 5](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-05.pdf) |
| Foreign-owned plants in U.S. included; U.S.-owned plants abroad excluded | ✅ BEA's own Japanese/British plant example | [BEA ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf) |
| Inventories counted in the year produced | ✅ Change in private inventories is part of I | [BEA ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf) |
| Investment includes new housing, R&D, equipment; not existing houses | ✅ Plus software and entertainment originals; **broker commissions on existing homes are counted** | [BEA ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf) |
| G excludes transfers (Social Security, UI) | ✅ "not counted as production" | [BEA ch. 9](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-09.pdf) |
| Only market activity counts | ⚠️ Simplification: imputed rent on owner-occupied housing (~8% of GDP) is the big exception | [BEA ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf); [BEA WP2017-7](https://www.bea.gov/research/papers/2017/imputing-rents-owner-occupied-housing-directly-modelling-their-distribution) |
| Output = spending = income | ✅ Conceptually; in practice GDP ≠ GDI because of the statistical discrepancy | [BEA ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf); [BEA Q2 2026 release](https://www.bea.gov/news/2026/gdp-third-estimate-industries-corporate-profits-state-gdp-and-state-personal-income-2nd) |

### Inferences
- Exam trap logic in one sentence: count **newly produced value** in the year it was produced. Exclude anything that is (a) a transfer of an existing asset (used car, existing house, stock, bond), (b) a pure transfer payment (Social Security, unemployment insurance, gifts), (c) an intermediate input (steel sold to automaker), or (d) produced outside U.S. borders. Then remember that any **service** attached to the transaction (dealer margin, realtor commission, broker fee) is new production and does count.
- A "harder than the slides" question might ask: "A homeowner pays off her mortgage and stops paying rent to a landlord. What happens to GDP?" Answer: nothing, because imputed rent keeps GDP invariant to owning vs. renting.
- Imports are not subtracted because imports are "bad". They are subtracted only to remove foreign production that is already counted inside C, I, and G. Buying an imported good therefore leaves GDP unchanged, except for the domestic retail margin.

### Gaps
- BEA's handbook does not name unemployment insurance specifically in the passages I read. UI is classed as a government social benefit (a transfer), but I did not retrieve BEA text naming it explicitly.
- I did not retrieve the BEA handbook chapter on gross private domestic investment (ch. 6) or the PCE chapter's imputed-rent table, so the ~8%-of-GDP figure rests on the 2017 working-paper summary rather than current-year data.

---

## Key Question 3: Evidence that labor's share of income is declining (BLS series, Karabarbounis & Neiman 2014, Autor et al. 2020)

### Takeaway
The slides are right. The BLS nonfarm-business labor share index (2017=100) peaked at 117.1 in 1960Q4 and hit its **lowest reading in the series' history, 93.4, in 2026Q2**. BEA's compensation share of GDI fell from about 51–52% (1950s–1970) to **42.0% in 2025**, tying the 2013 record low. Two leading explanations: cheaper investment goods led firms to substitute capital for labor (Karabarbounis & Neiman, about half of the global decline), and sales shifted toward low-labor-share "superstar" firms (Autor et al.).

### Cited Findings
- **BLS / FRED PRS85006173** ("Nonfarm Business Sector: Labor Share for All Workers," index 2017=100):

  | Date | Index |
  |---|---|
  | 1947Q1 | 116.0 |
  | 1960Q4 (series maximum) | 117.1 |
  | 2000Q1 | 112.8 |
  | 2010Q1 | 99.4 |
  | 2020Q2 (pandemic spike) | 104.2 |
  | 2024Q1 | 96.9 |
  | 2025Q1 | 97.9 |
  | **2026Q2** | **93.4** (series minimum; −20% from the 1960 peak) |

  — [FRED PRS85006173](https://fred.stlouisfed.org/series/PRS85006173)
- **BEA compensation of employees as a share of GDI** (FRED W270RE1A156NBEA):
  - 1960: 50.2%; 1970: 51.6% (peak, tied with 1953)
  - 1980: 48.8%; 2000: 46.6%
  - 2010: 42.5%; 2013: 42.0% (low); 2019: 43.4%
  - 2020: 44.5%; 2025: **42.0%**

  — [FRED W270RE1A156NBEA](https://fred.stlouisfed.org/series/W270RE1A156NBEA)
- **Penn World Table labor share for the U.S.** (FRED LABSHPUSA156NRUG): 0.649 in 1970 (series max), 0.637 in 2000, 0.568 in 2023 (series min). — [FRED LABSHPUSA156NRUG](https://fred.stlouisfed.org/series/LABSHPUSA156NRUG)
- **Karabarbounis & Neiman (2014)**, "The Global Decline of the Labor Share," *QJE* 129(1): 61–103:
  - "the global labor share has significantly declined since the early 1980s, with the decline occurring within the large majority of countries and industries."
  - "The lower price of investment goods explains roughly half of the observed decline in the labor share."
  - "Of the 59 countries with at least 15 years of data between 1975 and 2012, 42 exhibited downward trends."
  - A "25 percent decline in the global relative price of investment … since 1975" delivers "roughly half of the 5 percentage point decline in the global labor share."

  — [NBER WP 19136 (PDF)](https://www.nber.org/system/files/working_papers/w19136/w19136.pdf); [NBER w19136 page](https://www.nber.org/papers/w19136)
- **Autor, Dorn, Katz, Patterson & Van Reenen (2020)**, "The Fall of the Labor Share and the Rise of Superstar Firms," *QJE* 135(2): 645–709, DOI 10.1093/qje/qjaa004:
  - Uses U.S. Economic Census microdata from 1982 onward.
  - Argues that industries became dominated by "superstar" firms with high markups and low labor shares.
  - Concentration rose most where the labor share fell most.
  - The aggregate decline comes mainly from **reallocation of sales between firms**, not from falling labor shares within firms.

  — [Harvard (Katz) publication page](https://lkatz.scholars.harvard.edu/publications/fall-labor-share-and-rise-superstar-firms); [LSE eprint](https://eprints.lse.ac.uk/104480); [MIT-hosted paper](https://shapingwork.mit.edu/wp-content/uploads/2023/10/THE-FALL-OF-THE-LABOR-SHARE-AND-THE-RISE-OF-SUPERSTAR-FIRMSast.pdf)
- Karabarbounis & Neiman note that the overall labor share "is about 10 percentage points lower than the corporate labor share in part due to" the treatment of mixed/self-employment income. Different measures therefore give different **levels**, but the **downward trend** appears across measures. — [NBER WP 19136](https://www.nber.org/system/files/working_papers/w19136/w19136.pdf)

### Inferences
- Slide check: "GDP as total income = wages + profits; labor's share declining" holds on all three series above, whichever one is used. The cleanest exam phrasing: "a rising share of national income goes to capital (profits/rents) rather than labor."
- Levels differ by measure: 42% (compensation/GDI) vs. 57% (PWT, which assigns part of self-employment income to labor) vs. an index. A test should ask about the **direction**, not a specific level.
- The 2020 jump in labor share was a composition effect: low-wage jobs disappeared and profits fell. It does not reverse the trend.

### Gaps
- I did not fetch the BLS source page for PRS85006173 directly. Values come from FRED's mirror of BLS data.
- I did not verify measurement critiques of the decline (e.g., the role of housing, depreciation, or intellectual-property capitalization). They exist in the literature but are not cited here.

---

## Key Question 4: GDP's limitations: shadow economy, household production, leisure (U.S. vs. France), Stiglitz-Sen-Fitoussi, consumer surplus from free goods, and Bastiat's broken window

### Takeaway
Every limitation on the slides is backed by solid sources:
- **Shadow economy:** small in the U.S. (~5.7–9.5% of GDP, average 7.6% over 1991–2017; one of the three smallest in the world) against a 30.9–31.9% global average.
- **Household production:** BEA's satellite account adds **25% to GDP in 2020** (37% in 1965).
- **Leisure:** French workers put in **~305 fewer hours per year** than Americans (≈420 fewer for dependent employees) in OECD 2024 data, and French PPP GDP per capita is **27.4% (2024) to 28.9% (2025) lower**. That matches the slide's "300–400 hours" and "28%".
- **Stiglitz-Sen-Fitoussi (2009)** urged a shift "from measuring economic production to measuring people's well-being."
- **Bastiat's 1850 essay** is the original source of the broken-window parable.

### Cited Findings

**Shadow economy**
- **IMF WP/18/17** (Medina & Schneider, Jan 2018), "Shadow Economies Around the World: What Did We Learn Over the Last 20 Years?":
  - Covers 158 countries over 1991–2015, with an average of **31.9%** of GDP.
  - Largest: Bolivia (62.3%) and Zimbabwe (60.6%). Smallest: Switzerland (7.2%) and Austria (8.9%).

  — [IMF WP/18/17](https://www.imf.org/en/Publications/WP/Issues/2018/01/25/Shadow-Economies-Around-the-World-What-Did-We-Learn-Over-the-Last-20-Years-45583)
- **Updated estimates by the same authors** (CESifo WP 7981, Dec 2019; MIMIC method):
  - Covers 157 countries over 1991–2017, with an average of **30.9%**.
  - "The three smallest shadow economies are Switzerland with 6.4%, **United States with 7.6%**, and Austria with 7.9% of GDP."
  - The U.S. ranged from 9.5% (1991) down to **5.7% (2017)**.
  - France averaged 12.9% and stood at 11.7% in 2017.
  - The average decline from 1991 to 2017 was 6.8 pp.

  — [CESifo WP 7981 (PDF)](https://www.cesifo.org/DocDL/cesifo1_wp7981.pdf)
- BEA excludes illegal activity from U.S. GDP for data reasons (see KQ2). — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)

**Household production (BEA satellite account)**
- Bridgman, Craig & Kanal, *Survey of Current Business* (Feb 2022), "Accounting for Household Production in the National Accounts: An Update 1965–2020":

  | Year | NIPA GDP | GDP including household production |
  |---|---|---|
  | 1965 | $742.3B | $1,019.7B |
  | 2020 | $20,893.7B | $26,210.6B |

  Computed effect: household production **raises GDP by 37.4% (1965)** and **25.4% (2020)**, about **$5.3T** in 2020.
  - The household sector was "only 22 percent of the satellite accounts output in 2019" and rose in 2020 because of the pandemic.
  - Hours are valued at household-worker wages: "$10.93 in 2019 to $12.71 in 2020."
  - Including household production lowers measured nominal growth for 1965–2020 from 6.3% to 6.1% a year, because "Household production has declined in significance over time as more women engage in market work."

  — [BEA SCB Feb 2022 (PDF)](https://apps.bea.gov/scb/issues/2022/02-february/pdf/0222-household-production.pdf)
- BEA's household production page lists newer "Household Production Expanded Indicators, 1965–2024" (BEA Working Paper WP2026–15, June 2026). — [BEA household production page](https://www.bea.gov/data/special-topics/household-production)

**Leisure: U.S. vs. France**
- OECD "Average annual hours actually worked per worker" (via the JIL Databook 2026, Table 6-1, OECD data as of Aug 2025):

  | Group | U.S. | France | Gap |
  |---|---|---|---|
  | Total employment, 2024 | **1,796** | **1,491** | **305 h** |
  | Total employment, 2023 | 1,805 | 1,489 | 316 h |
  | Dependent employees, 2024 | 1,810 | 1,390 | **420 h** |

  OECD caveat: the data "are not suitable for comparisons of the level of average annual hours of work for a given year" across countries, because sources differ. — [JIL Databook 2026, Table 6-1 (OECD source)](https://www.jil.go.jp/kokunai/statistics/databook/2026/06/d2026_6T-01.pdf); [OECD Data Explorer](https://data-explorer.oecd.org/)
- GDP per capita, PPP (current international $), World Bank WDI (updated 2026-10-08):

  | Year | U.S. | France | France below U.S. (computed) |
  |---|---|---|---|
  | 2024 | $86,170 | $62,525 | **27.4%** |
  | 2025 | $90,027 | $63,975 | **28.9%** |

  At market exchange rates in 2025, France is $48,986 against $90,027 for the U.S. — [World Bank NY.GDP.PCAP.PP.CD](https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.CD?locations=US-FR); [World Bank API query](https://api.worldbank.org/v2/country/USA;FRA/indicator/NY.GDP.PCAP.PP.CD?format=json&date=2019:2025)

**Stiglitz-Sen-Fitoussi Commission (2009)**
- Set up by France in 2008 to identify "the limits of GDP as an indicator of economic performance and social progress." Members included Arrow, Atkinson, Deaton, Heckman, and Kahneman. — [Commission summary (PDF)](https://www.cps.fgv.br/cps/bd/curso/Global-Social/7Stiglitz_Sen_Fitoussi_Short.pdf); [UN Statistical Commission doc (France, 2011)](https://ecosoc.un.org/sites/default/files/documents/2023/2011-35-France-E.pdf)
- Key quotes from the summary:
  - "the time is ripe for our measurement system to shift emphasis from measuring economic production to measuring people's well-being … Changing emphasis does not mean dismissing GDP and production measures."
  - Recommendation 1: "When evaluating material well-being, look at income and consumption rather than production."
  - Recommendation 4: "Give more prominence to the distribution of income, consumption and wealth."
  - Recommendation 5: "Broaden income measures to non-market activities."
  - On leisure: "Consuming the same bundle of goods and services but working for 1500 hours a year instead of 2000 hours a year implies an increase in one's standard of living."
  - Recommendation 12: environmental sustainability "deserve[s] a separate follow-up based on a well-chosen set of physical indicators."

  — [Commission summary (PDF)](https://www.cps.fgv.br/cps/bd/curso/Global-Social/7Stiglitz_Sen_Fitoussi_Short.pdf)
- The OECD carried on the work through a High-Level Expert Group (2013–2018), "Beyond GDP." — [OECD, Beyond GDP](https://www.oecd.org/en/publications/beyond-gdp_9789264307292-en/full-report/component-2)

**Free goods and consumer surplus (Google/Wikipedia point)**
- Brynjolfsson, Collis & Eggers (2019), "Using massive online choice experiments to measure changes in well-being," *PNAS* 116: 7250–7255:
  - The median user would need **$17,530 per year** to give up search engines.
  - U.S. Facebook users would need a median of **$40–50 per month** to leave Facebook.
  - GDP misses this value because the services carry a zero price.

  — [MIT Sloan summary](https://mitsloan.mit.edu/ideas-made-to-matter/how-much-are-search-engines-worth-to-you); [Paper PDF](https://ide.mit.edu/wp-content/uploads/2019/03/1815663116.full-gdp.pdf)

**Bastiat's broken window**
- *Ce qu'on voit et ce qu'on ne voit pas* ("What Is Seen and What Is Not Seen") was written in July 1850 and published as a pamphlet by Guillaumin in Paris that year. Its first chapter is "The Broken Window." — [Liberty Fund OLL](https://oll.libertyfund.org/page/wswns); [Wikipedia: Parable of the broken window](https://en.wikipedia.org/wiki/Parable_of_the_broken_window)
- Key quotes (FEE translation, Seymour Cain; the Econlib edition lists the essay collection's first publication as 1848):
  - "The glazier will come, do his job, receive six francs … That is what is seen."
  - "It is not seen that, since our citizen has spent six francs for one thing, he will not be able to spend them for another." He "would have replaced … his worn-out shoes or added another book to his library."
  - Conclusion: "Society loses the value of objects unnecessarily destroyed" and "Destruction is not profitable."

  — [Econlib, Bastiat, *Selected Essays*, ch. 1](https://www.econlib.org/library/Bastiat/basEss1.html)
- In NIPA terms, accidental damage and disaster losses hit the **stock** of assets: since 2009, "irreparable damage to, or the destruction of, fixed assets is no longer recorded as consumption of fixed capital." Rebuilding, on the other hand, is counted as new production (a **flow**). — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)

### Inferences
- **Back-of-envelope (mine):** if French workers worked U.S. hours per worker at the same output per hour, with the same employment rate, French GDP per capita would be about $62,525 × 1,796/1,491 ≈ $75,300, and the 27.4% gap would shrink to about 12.6%. Hours per worker therefore explain roughly half the gap. This ignores employment-rate differences and diminishing returns, and the OECD warns against level comparisons, so treat it as illustrative.
- **Broken window:** GDP rises when the window is replaced (glazier output is a flow), but wealth (the stock of windows) is unchanged at best, and the shoes that would have been made are forgone. Exam phrase: "GDP measures flows, not stocks; destruction can raise measured GDP while lowering wealth and well-being."
- **Shadow economy:** because the U.S. shadow economy is among the world's smallest, cross-country GDP comparisons understate the true output of high-informality countries (Bolivia, Nigeria) by much more than they understate the U.S.
- **Household production:** its share has fallen as women entered paid work, so measured GDP growth since 1965 is somewhat overstated as a measure of total production. Childcare that moves from home to daycare raises GDP without any change in actual output.

### Gaps
- The U.S.-specific estimate in IMF WP/18/17 could not be retrieved (the PDF link returned "Blob not found"). The U.S. figures come from the authors' 2019 CESifo update instead.
- I did not read BEA WP2026–15 (household production 1965–2024), so I have no household-production figure later than 2020.
- I did not verify the exact source of the Stevenson & Wolfers slides' "28% lower" and "300–400 hours" claims. The World Bank PPP and OECD hours data are consistent with them, but the book may use a different year or source.
- I found no source quantifying GDP bias from environmental degradation (e.g., "green GDP") in this pass.

---

## Key Question 5: GDP and well-being: life satisfaction (Stevenson & Wolfers 2008) and life expectancy (the Preston curve)

### Takeaway
Across countries, life satisfaction rises roughly **linearly with log GDP per capita**, with no satiation point. In the Gallup World Poll the correlation exceeds 0.8 (Stevenson & Wolfers 2008, rejecting the Easterlin paradox). Life expectancy rises with income in a **concave** "Preston curve" that has **shifted up over time**: Preston attributed 75–90% of 1930s–1960s life-expectancy gains to factors other than income growth. Both findings support the slide's claim that GDP is correlated with, but not identical to, well-being.

### Cited Findings
- **Stevenson & Wolfers (2008)**, "Economic Growth and Subjective Well-Being: Reassessing the Easterlin Paradox," *Brookings Papers on Economic Activity*, Spring 2008:
  - Abstract: "we establish a clear positive link between average levels of subjective well-being and GDP per capita across countries, and find no evidence of a satiation point beyond which wealthier countries have no further increases in subjective well-being … similar to that between subjective well-being and income observed within countries … we find economic growth associated with rising happiness."
  - Gallup World Poll (2006), life-satisfaction "ladder" question: "Across the 131 countries … the correlation exceeds 0.8," and "the estimated coefficient on log GDP per capita, 0.42, is similar to those obtained using the World Values Survey, the Pew survey." The coefficient is on a standardized ordered-probit well-being index, not raw ladder points.

  — [Brookings article page](https://www.brookings.edu/articles/economic-growth-and-subjective-well-being-reassessing-the-easterlin-paradox/); [BPEA PDF](https://www.brookings.edu/wp-content/uploads/2008/03/2008a_bpea_stevenson.pdf)
- **The course textbook's authors are the same Stevenson & Wolfers.** Their Worth Publishers (Macmillan Learning) *Principles of Microeconomics* and *Principles of Macroeconomics* were announced in 2019 for Fall 2020, and the course uses the Macro 2nd edition (©2023). Their own research (above) is therefore the likely basis for the slide "GDP correlates with well-being (life satisfaction)". An exam may expect the "no satiation point / log-linear" takeaway. — [Ford School news (2019)](https://fordschool.umich.edu/news/2019/published-acclaimed-ford-school-economists-seek-transform-college-economics-through-new?theme=ipc); [Macmillan Learning, Principles of Economics](https://store.macmillanlearning.com/Us/product/Principles-of-Economics/p/1319330150)
- **Preston (1975)**, "The changing relation between mortality and level of economic development," *Population Studies* 29(2): 231–248, doi 10.2307/2173509. It was reprinted in the *Bulletin of the WHO* 81(11): 833–841 (2003) and the *International Journal of Epidemiology* 36(3): 484–490 (2007). — [Europe PMC record](https://europepmc.org/article/MED/11630494); [WHO Bulletin reprint record](https://europepmc.org/article/MED/14758412)
- Preston's scatter of life expectancy against national income per head covered the 1900s, 1930s, and 1960s. Life expectancy "rose substantially in these decades no matter what the income level," and "factors exogenous to a country's current level of income probably account for 75–90% of the growth" in world life expectancy between the 1930s and 1960s. Only "10–25% of this gain" is attributed to income growth. — [The Pump Handle (summary of Preston 1975)](https://www.thepumphandle.org/2013/04/01/economic-development-and-mortality-samuel-prestons-1975-classic/)

### Inferences
- The log-linear finding implies that a given **percentage** increase in income raises well-being by about the same amount at any income level. In dollars, +$1,000 matters far more in a poor country than in a rich one, which is consistent with diminishing marginal utility. Exam phrasing: "happiness rises with the log of income; no satiation point found."
- The Preston curve's upward shift is a strong "GDP is not everything" example: technology and public health (vaccines, sanitation) raised life expectancy at every income level.

### Gaps
- I did not retrieve the original 1975 article text. The 75–90% figure comes from a secondary summary (The Pump Handle) that quotes Preston.
- I did not pull a current cross-country life-expectancy-vs-GDP dataset (e.g., World Bank/OWID 2024) to update the curve.
- Newer work (Killingsworth 2021; Kahneman-Killingsworth-Mellers 2023 on income and experienced well-being) was not covered.

---

## Key Question 6: Recession definition: the "two consecutive quarters" rule of thumb vs. NBER, with the 2022 H1 example

### Takeaway
"Two consecutive quarters of negative real GDP growth" is a press **rule of thumb**, not the official definition. The NBER Business Cycle Dating Committee defines a recession as "a significant decline in economic activity that is spread across the economy and lasts more than a few months" (depth, diffusion, duration). It weights payroll employment and real personal income less transfers most heavily. In 2022 H1, BEA's advance data showed −1.6% and −0.9%, a "technical recession". NBER never declared one, and later revisions turned Q2 2022 **positive** (+0.6% in the current vintage).

### Cited Findings
- NBER: a recession is "a significant decline in economic activity that is spread across the economy and lasts more than a few months." Depth, diffusion, and duration are treated "as somewhat interchangeable." The indicators include:
  - real personal income less transfers
  - nonfarm payroll employment
  - household-survey employment
  - real consumption spending
  - real manufacturing and trade sales
  - industrial production

  The committee gives the most weight to real personal income less transfers and payroll employment. The most recent peak and trough are **February 2020** and **April 2020**. — [NBER Business Cycle Dating](https://www.nber.org/research/business-cycle-dating)
- NBER FAQ on the two-quarter rule:
  - "Most of the recessions identified by our procedures do consist of two or more consecutive quarters of declining real GDP," but "In 2001, for example, the recession did not include two consecutive quarters of decline in real GDP."
  - "we do not identify economic activity solely with real GDP."
  - Real GDI gets equal weight with real GDP.

  — [NBER Business Cycle Dating FAQ](https://www.nber.org/business-cycle-dating-procedure-frequently-asked-questions)
- BEA advance estimate (July 28, 2022): real GDP "decreased at an annual rate of 0.9 percent in the second quarter of 2022," after a first-quarter decline revised to 1.6%. — [BEA Q2 2022 advance estimate](https://www.bea.gov/news/2022/gross-domestic-product-second-quarter-2022-advance-estimate)
- Revision history of 2022 H1 real GDP growth (annualized, computed from ALFRED GDPC1 vintages):

  | Vintage | Q1 2022 | Q2 2022 |
  |---|---|---|
  | Aug 2022 | −1.6% | −0.9% |
  | Oct 2022 | −1.6% | −0.6% |
  | Oct 2023 | −2.0% | −0.6% |
  | Oct 2024 | −1.0% | **+0.3%** |
  | Oct 2025 | −1.0% | +0.6% |
  | Oct 13, 2026 | −1.0% | +0.6% |

  — [ALFRED GDPC1](https://alfred.stlouisfed.org/series?seid=GDPC1)

### Inferences
- In 2022 the "two-quarter" test was met in real time, then **un-met after revisions**, while payroll employment kept growing. This is a clean exam illustration of why NBER does not rely on a single preliminary GDP series.
- Two consecutive negative quarters is neither necessary (2001) nor, in NBER's practice, sufficient (2022).

### Gaps
- I did not retrieve any formal NBER statement specifically about 2022 (NBER does not normally announce "non-recessions"). The evidence that none was declared is the chronology's last peak/trough (Feb/Apr 2020).
- I did not pull 2022 payroll employment data to document the labor-market side.

---

## Key Question 7: Every calculation method a hard exam would test, with worked examples (arithmetic verified)

### Takeaway
The required calculation methods are:
1. Nominal GDP = Σ(P×Q) at current prices.
2. Real GDP = Σ(P_base × Q_current).
3. Deflator = Nominal/Real × 100.
4. Growth = (X₁ − X₀)/X₀ × 100; quarterly growth is annualized by compounding.
5. Value added = sales − intermediate inputs, and Σ value added = final sale price.
6. Expenditure approach Y = C + I + G + (X − M), screened for traps.
7. Income approach: wages + profits (BEA: compensation + taxes on production less subsidies + net operating surplus + depreciation).
8. Per-capita GDP = GDP/population; real per-capita growth ≈ real GDP growth − population growth.
9. GNP = GDP + factor income from abroad − factor income paid abroad.

All worked examples below were checked in Python.

### Cited Findings

#### Formula sheet (with authority)
- GDP = C + I + G + (X − M). — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- I = nonresidential fixed (structures + equipment + IP products) + residential + change in private inventories. — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- Value added = gross output − intermediate inputs, and Σ value added across industries = GDP. — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- GDI = compensation + (taxes on production & imports − subsidies) + net operating surplus + consumption of fixed capital. — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- Implicit price deflator = current-dollar ÷ chained-dollar × 100. BEA itself uses Fisher chain-type indexes rather than a fixed base year. — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- GNP = GDP + income receipts from the rest of the world − income payments to the rest of the world. — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- BEA's headline quarterly growth is a seasonally adjusted **annual rate**. For example, Q2 2026's 2.2% is "0.6 percent quarterly." — [BEA Q2 2026 third estimate](https://www.bea.gov/news/2026/gdp-third-estimate-industries-corporate-profits-state-gdp-and-state-personal-income-2nd)

#### Worked Example 1: Nominal GDP, real GDP, deflator, and growth (extends the slide's apples and oranges)

| Good | 2024 (base) P | 2024 Q | 2025 P | 2025 Q |
|---|---|---|---|---|
| Apples | $5 | 10 | $6 | 12 |
| Oranges | $10 | 30 | $11 | 33 |

1. Nominal GDP 2024 = 10×5 + 30×10 = **$350**. In the base year, real = nominal, so the deflator = 100.
2. Nominal GDP 2025 = 12×6 + 33×11 = 72 + 363 = **$435**.
3. Real GDP 2025 (2024 prices) = 12×5 + 33×10 = 60 + 330 = **$390**.
4. Deflator 2025 = 435/390 × 100 = **111.54**, so inflation ≈ **11.54%**.
5. Nominal growth = (435 − 350)/350 = **24.29%**. Real growth = (390 − 350)/350 = **11.43%**.
6. Check: (1.1143)(1.1154) = 1.2429. The shortcut "nominal growth ≈ real growth + inflation" gives 22.97%, which is close but not exact. Hard exams sometimes test that the exact relationship is multiplicative.

The slide's doubled-price case: if prices double with output unchanged, nominal = 10×10 + 30×20 = **$700**, real (base prices) = **$350**, the deflator = **200**, and real growth = **0%**.

#### Worked Example 2: Value added through the production chain, and income = output

| Stage | Sale price | Intermediate input cost | Value added | Wages | Profits |
|---|---|---|---|---|---|
| Farmer: wheat → miller | $1.00 | $0 | $1.00 | $0.60 | $0.40 |
| Miller: flour → baker | $1.50 | $1.00 | $0.50 | $0.30 | $0.20 |
| Baker: bread → grocer | $3.00 | $1.50 | $1.50 | $1.00 | $0.50 |
| Grocer: bread → consumer | $4.00 | $3.00 | $1.00 | $0.70 | $0.30 |
| **Total** | $9.50 (sum of all sales) | | **$4.00** | **$2.60** | **$1.40** |

- Σ value added = **$4.00** = the final sale price to the consumer (the expenditure approach).
- Summing all sales ($9.50) **double-counts** the intermediate goods by $5.50. This is the same logic as BEA's tire example.
- Income approach: wages + profits = 2.60 + 1.40 = **$4.00** = GDP. Labor's share = 2.60/4.00 = **65%**.
- This verifies output = spending = income for the circular flow.

#### Worked Example 3: Expenditure approach with traps (all figures in $ billions)

| Item | Count? | Component | Amount counted |
|---|---|---|---|
| Household purchases of new goods & services (includes $40 of imported goods) | Yes | C | 500 |
| Cars from a Japanese-owned plant in Ohio, sold to U.S. households | Yes (produced in U.S.) | C | 25 |
| Household buys a used car from a neighbor for $10 | **No** (existing good) | — | 0 |
| Used-car dealer's margin on used cars sold to households | **Yes** (new service) | C | 2 |
| Households buy $50 of corporate stock | **No** (financial asset) | — | 0 |
| Brokerage commissions on those stock purchases | **Yes** (service) | C | 1 |
| Social Security benefits paid ($80) | **No** (transfer) | — | 0 |
| Unemployment insurance benefits ($20) | **No** (transfer) | — | 0 |
| Government purchases (vaccines, teacher salaries, highways) | Yes | G | 200 |
| Business purchases of new equipment & software/R&D | Yes | I | 90 |
| Newly built houses | Yes | I (residential) | 60 |
| Purchase of an existing house ($120) | **No** (existing asset) | — | 0 |
| Realtor's commission on that existing house | **Yes** | I (residential) | 7 |
| Increase in business inventories | Yes | I (inventory change) | 15 |
| Steel bought by U.S. automakers ($30) | **No** (intermediate, already in car prices) | — | 0 |
| Exports | Yes | X | 70 |
| Imports (includes the $40 inside C) | Subtract | M | 110 |
| Output of a U.S.-owned factory in Mexico ($40) | **No** (not produced in U.S.; counts in U.S. GNP) | — | 0 |

- C = 500 + 25 + 2 + 1 = **528**
- I = 90 + 60 + 7 + 15 = **172**
- G = **200**
- NX = 70 − 110 = **−40**
- **GDP = 528 + 172 + 200 − 40 = $860B**
- Distractor total if a student wrongly adds every listed dollar amount: much larger. Each excluded item maps to a BEA rule: [used vehicles and household-to-household sales](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-05.pdf); [transfers](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-09.pdf); [existing assets, capital gains, broker commissions capitalized, imports offset, domestic/national](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf).

#### Worked Example 4: Inventory timing, resale, and GDP vs. GNP
- **(a) Inventory.** A $35,000 car is built in December 2025 and sits unsold on the lot. **2025:** change in inventories +$35,000, so I and GDP each rise by $35,000. It sells to a household in March 2026 for $35,000. **2026:** C +$35,000 and inventory change −$35,000, so the net effect on GDP is **$0**. If it sells for $36,000, 2026 GDP rises by **$1,000** (the dealer's service). Basis: inventories are valued as a change in physical volume within I. — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf)
- **(b) Resale.** The household resells the car in 2027 to a neighbor for $28,000, so 2027 GDP is unchanged. Through a dealer, only the dealer's margin counts. — [BEA NIPA Handbook ch. 5](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-05.pdf)
- **(c) GNP.** Suppose GDP = $1,000, U.S. residents earn $30 from factories they own abroad, and foreigners earn $45 from factories they own in the U.S. Then GNP = 1,000 + 30 − 45 = **$955**. Real U.S. data: 2025 GNP $30,846.1B vs. GDP $30,861.3B. — [BEA NIPA Handbook ch. 2](https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-02.pdf); [FRED GNPA](https://fred.stlouisfed.org/series/GNPA)

#### Worked Example 5: Real U.S. data (2024 → 2025): per capita, real vs. nominal growth, deflator inflation
- Inputs: nominal GDP $29,381.0B → $30,861.3B; real GDP (chained 2017 $) $23,394.9B → $23,943.3B; population 340.095M → 341.944M. — [FRED GDPA](https://fred.stlouisfed.org/series/GDPA); [FRED GDPCA](https://fred.stlouisfed.org/series/GDPCA); [FRED B230RC0A052NBEA](https://fred.stlouisfed.org/series/B230RC0A052NBEA)
- Calculations:
  - Nominal GDP per capita 2025 = 30,861.3B / 341.944M = **$90,252**, matching BEA/FRED exactly. — [FRED A939RC0A052NBEA](https://fred.stlouisfed.org/series/A939RC0A052NBEA)
  - Nominal growth = 30,861.3/29,381.0 − 1 = **5.04%**. Real growth = 23,943.3/23,394.9 − 1 = **2.34%**.
  - Implicit deflator: 2024 = 29,381.0/23,394.9 × 100 = **125.59**; 2025 = **128.89**. Inflation (deflator) = **2.63%**.
  - Real GDP per capita growth = (1.0234)/(341.944/340.095) − 1 = **1.79%**, which is close to 2.34% − 0.54% (population growth).

#### Worked Example 6: Annualizing quarterly growth, plus the "technical recession" test
- Q1 2026 real GDP = $24,274.4B; Q2 2026 = $24,408.0B. — [FRED GDPC1](https://fred.stlouisfed.org/series/GDPC1)
  - Quarterly change = 24,408.0/24,274.4 − 1 = **0.55%**.
  - Annualized = (1.0055)^4 − 1 = **2.22%**, matching BEA's "2.2 percent" and its "0.6 percent quarterly." The simple ×4 shortcut gives 2.20%.
  - Nominal: (32,563.0/31,906.3)^4 − 1 = **8.49%**, matching BEA's 8.5%.
- Two-quarter test with **real-time** 2022 data: −1.6% and −0.9%, so the rule-of-thumb criterion was met. With **current** data, −1.0% and +0.6%, it was not met. NBER declared no recession either way. — [BEA Q2 2022 advance](https://www.bea.gov/news/2022/gross-domestic-product-second-quarter-2022-advance-estimate); [ALFRED GDPC1](https://alfred.stlouisfed.org/series?seid=GDPC1); [NBER](https://www.nber.org/research/business-cycle-dating)

#### Mini-drills (quick checks)
- **Share of GDP:** C share 2025 = 20,870.2 / 30,861.3 = 67.6%. — [FRED PCEC](https://fred.stlouisfed.org/series/PCEC)
- **Recovering one value from two others:** nominal = $500B and deflator = 125, so real = 500/1.25 = $400B. Real = $400B and nominal = $440B, so deflator = 110.
- **Closed economy:** NX = 0, so Y = C + I + G.
- **Household production:** valuing it (2020) raises GDP by 26,210.6/20,893.7 − 1 = 25.4%. — [BEA SCB 2022](https://apps.bea.gov/scb/issues/2022/02-february/pdf/0222-household-production.pdf)
- **U.S. vs. France gap:** 1 − 62,525/86,170 = 27.4% (PPP, 2024). — [World Bank](https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.CD?locations=US-FR)

### Inferences
- The most commonly missed points on hard exams:
  1. The service attached to a used or financial transaction still counts (dealer margin, broker commission, realtor fee).
  2. Imports bought by consumers leave GDP unchanged, because they appear in C and are subtracted in M.
  3. Unsold production counts as investment in the year it is made.
  4. Government transfers are not G.
  5. A base-year deflator is always 100.
  6. Growth rates compound. Multiplying a quarterly rate by four is only an approximation.
- If a test gives a P×Q table and asks "what share of nominal GDP growth was due to price increases," compute real growth and the deflator separately (Example 1). Nominal growth ≈ real growth + inflation is only approximate.

### Gaps
- I deliberately did not consult publisher test banks or instructor answer keys. The worked examples are original constructions consistent with BEA definitions, not reproductions of textbook problems.
- I confirmed the chapter title (Stevenson & Wolfers 2e, Ch. 9 "Sizing Up the Economy Using GDP") from Macmillan's table of contents, but I did not see the chapter text. The book's own worked-example conventions (e.g., which base year it prefers, how it phrases traps) are unverified. — [Macmillan Learning TOC](https://store.macmillanlearning.com/Us/product/Principles-of-Macroeconomics/p/1319432085)
- The textbook's fixed-base-year method differs from BEA's chain-weighted (Fisher) method. Exam answers should use the textbook method unless asked otherwise.
