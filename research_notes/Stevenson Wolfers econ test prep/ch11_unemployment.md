# Chapter 11 "Unemployment" (Goolsbee, Levitt & Syverson, Worth): Slide validation, latest data, and calculation methods

Notes compiled 2026-10-14. The instructor's slides use 2021 data; the latest data here is the September 2026 Employment Situation, released Oct 2, 2026. I could not access the textbook itself, so these notes check the slide content against BLS, CBO, NBER, FRED and the original academic papers. I did not search for or use any publisher test banks or instructor answer keys. All arithmetic was checked in Python.

---

## Q1. What are the official BLS (Current Population Survey) definitions? Do the slides' classifications match them? (Includes U-1 to U-6 and the employment-population ratio)

### Takeaway
The slides' definitions match BLS's. There are three nuances an exam could test, and the slides don't state them explicitly:
- Job search must be **active** and within the **past 4 weeks**.
- People on **temporary layoff** count as unemployed even if they aren't searching.
- **Unpaid** work counts as employment only for 15+ hours in a family business.

U-6 is the broadest measure. It adds marginally attached workers and people working part time for economic reasons.

### Cited Findings
**Population base**
- The base population ("universe") is the **civilian noninstitutional population age 16+**. — [BLS CPS Concepts & Definitions](https://www.bls.gov/cps/definitions.htm)
- The CPS covers civilians 16+ with **no upper age limit**. It **excludes** people in institutions (correctional facilities, residential nursing or mental-health facilities) and people on **active duty in the Armed Forces**. — [BLS "How the Government Measures Unemployment"](https://www.bls.gov/cps/cps_htgm.htm)
- **Reference week:** usually the 7-day Sunday–Saturday week that includes the **12th of the month**. — [BLS Definitions](https://www.bls.gov/cps/definitions.htm)
- **Sample:** about **60,000 eligible households** a month (roughly 110,000 people), interviewed by Census Bureau staff. — [BLS HTGM](https://www.bls.gov/cps/cps_htgm.htm)

**Employed.** A person is employed if, during the reference week, they did any of the following ([BLS Definitions](https://www.bls.gov/cps/definitions.htm)):
- "worked at least 1 hour as a paid employee" (or worked in their own business);
- "were temporarily absent from their job, business, or farm, whether or not they were paid for the time off" (vacation, illness, labor dispute);
- "worked without pay for a minimum of 15 hours in a business or farm owned by a member of their family."

**Unemployed.** A person is unemployed if they had no job, were available for work, and "made at least one specific, active effort to find a job during the **4-week period** ending with the survey reference week." The one exception: people who "were temporarily laid off and expecting to be recalled" count as unemployed **without searching**. — [BLS Definitions](https://www.bls.gov/cps/definitions.htm); [BLS HTGM](https://www.bls.gov/cps/cps_htgm.htm)

**Active vs. passive search.**
- Active methods "have the potential to result in a job offer without any further action." Examples: contacting employers or employment agencies, asking friends or relatives, submitting résumés, answering job ads, checking union or professional registers.
- Passive methods (attending a training course, or only reading job postings) **do not count**.
- Sources: [BLS Definitions](https://www.bls.gov/cps/definitions.htm); [BLS HTGM](https://www.bls.gov/cps/cps_htgm.htm)

**Not in the labor force.** A person is not in the labor force if they were not employed and had not actively looked for work (or been on temporary layoff) in the last 4 weeks. — [BLS Definitions](https://www.bls.gov/cps/definitions.htm)

**Marginally attached and discouraged workers**
- **Marginally attached:** people who are neither working nor looking, but who want and are available for a job and have looked sometime in the **past 12 months**. — [BLS Table A-15](https://www.bls.gov/news.release/empsit.t15.htm)
- **Discouraged workers** are a subset of the marginally attached: their reason for not looking is that they believe no jobs are available. "Discouraged workers are not counted among the unemployed." — [BLS Definitions](https://www.bls.gov/cps/definitions.htm)

**Part time for economic reasons.** People who worked 1–34 hours for an economic reason. In other words, they want and are available for full-time work "but have had to settle for a part-time schedule." They count as **employed**. — [BLS Definitions](https://www.bls.gov/cps/definitions.htm); [BLS Table A-15](https://www.bls.gov/news.release/empsit.t15.htm)

**Unemployment insurance (UI) is not part of the definition**
- A person does **not** have to receive UI to be counted as unemployed. Only about **one-third** of the unemployed received regular UI benefits over the past decade.
- BLS doesn't measure unemployment from UI claims because UI doesn't cover everyone: it misses the self-employed, people who have exhausted benefits, new entrants, and people who were disqualified.
- Source: [BLS HTGM](https://www.bls.gov/cps/cps_htgm.htm)

**Rates.** BLS defines ([BLS Definitions](https://www.bls.gov/cps/definitions.htm)):
- Labor force = employed + unemployed.
- LFPR = labor force ÷ civilian noninstitutional population.
- Employment-population ratio = employed ÷ civilian noninstitutional population.
- Unemployment rate = unemployed ÷ labor force.

**Alternative measures U-1 to U-6** (exact BLS wording, from [BLS Table A-15](https://www.bls.gov/news.release/empsit.t15.htm)):
- **U-1:** persons unemployed 15 weeks or longer, as a % of the civilian labor force.
- **U-2:** job losers and persons who completed temporary jobs, as a % of the civilian labor force.
- **U-3:** total unemployed, as a % of the civilian labor force. This is the **official unemployment rate**.
- **U-4:** (unemployed + discouraged workers) ÷ (labor force + discouraged workers).
- **U-5:** (unemployed + all marginally attached) ÷ (labor force + all marginally attached).
- **U-6:** (unemployed + all marginally attached + part time for economic reasons) ÷ (labor force + all marginally attached).

**Seasonally adjusted values, September 2026:** U-1 1.8%; U-2 1.9%; U-3 4.2%; U-4 4.4%; U-5 5.0%; U-6 7.6%. — [BLS Table A-15](https://www.bls.gov/news.release/empsit.t15.htm)

### Inferences
- **The slides' concept check matches BLS rules:**
  - A student tutoring 4 paid hours a week is **employed**, because the threshold is at least 1 paid hour.
  - A laid-off worker with interviews lined up is **unemployed**, because interviewing and contacting employers are active search methods.
  - An **unpaid intern** is **not employed**, because unpaid work counts only for 15+ hours in a family business. The intern is in the "not in labor force" category **unless** they also actively searched for paid work in the past 4 weeks. In that case they are **unemployed**. This is an inference from the definitions; BLS's pages don't discuss interns specifically.
- **Order of the alternative measures:** U-4 through U-6 add people to **both** the numerator and the denominator. U-6 is always at least as large as U-5, which is at least U-4, which is at least U-3. U-1 and U-2 are subsets of U-3, so they are smaller than U-3.
- **"Discouraged workers are in NILF" (slides) is correct for U-3.** Exams sometimes ask which measure *does* include them: U-4, U-5 and U-6 all do.

### Gaps
- I did not verify BLS's current treatment of people "waiting to start a new job within 30 days" who are not searching. The 1994 CPS redesign changed this rule, and I did not fetch a source on it.

---

## Q2. What are the latest US labor-market figures (2025–2026), the 2021 annual averages used on the slides, long-run LFPR trends by sex, and international comparisons?

### Takeaway
- **Latest (September 2026):** unemployment rate (UR) **4.2%**, LFPR **61.8%**, employment-population ratio (E-pop) **59.2%**, U-6 **7.6%**.
- **2021 annual averages (the slides' data):** UR **5.3%**, LFPR **61.7%**, E-pop **58.4%**.
- **Long-run trends:**
  - Women's LFPR rose from about **33% (1948)** to a peak near **60% (1999–2000)** and has been about 57% recently.
  - Men's LFPR fell from about **87% (1948)** to about **67–68%**.
  - In July 2026 overall LFPR hit **61.4%**, the lowest since 1976 apart from the pandemic. Analysts mostly attribute the recent decline to population aging (retirements).

### Cited Findings
**Latest monthly data, September 2026 (released Oct 2, 2026)**
- From the release: UR **4.2%**; **7.1 million** unemployed; LFPR **61.8%**; E-pop **59.2%**. — [BLS Employment Situation](https://www.bls.gov/news.release/empsit.nr0.htm)
  - Long-term unemployed (27+ weeks): **1.9 million**, which is 27.1% of the unemployed.
  - Part time for economic reasons: **4.5 million**.
  - Not in the labor force but want a job: **5.8 million**.
  - Marginally attached: **1.5 million**, of whom **414,000** are discouraged workers.
  - Nonfarm payrolls: **+29,000**.
- **Exact levels for September 2026 (thousands, seasonally adjusted):**
  - Civilian noninstitutional population: **275,554** — [FRED CNP16OV](https://fred.stlouisfed.org/series/CNP16OV)
  - Labor force: **170,262** — [FRED CLF16OV](https://fred.stlouisfed.org/series/CLF16OV)
  - Employed: **163,152** — [FRED CE16OV](https://fred.stlouisfed.org/series/CE16OV)
  - Unemployed: **7,109** — [FRED UNEMPLOY](https://fred.stlouisfed.org/series/UNEMPLOY)
  - These are BLS data republished on FRED.
- **Recent path:**
  - UR: 4.3% (Jul 2025) → 4.5% (Nov 2025) → 4.1% (Jul–Aug 2026) → 4.2% (Sep 2026). — [FRED UNRATE](https://fred.stlouisfed.org/series/UNRATE)
  - U-6: 8.7% (Nov 2025) → 7.6% (Sep 2026). — [FRED U6RATE](https://fred.stlouisfed.org/series/U6RATE)
  - LFPR: 62.5% (Sep 2025) → **61.4% (Jul 2026)** → 61.8% (Sep 2026). — [FRED CIVPART](https://fred.stlouisfed.org/series/CIVPART)
- **October 2025 data were never collected** because of the federal government shutdown. The 2025 annual averages are therefore **11-month averages** and "not strictly comparable" with other years. — [BLS Table cpsaat01](https://www.bls.gov/cps/cpsaat01.htm)

**Annual averages (thousands). Source for all rows: [BLS cpsaat01](https://www.bls.gov/cps/cpsaat01.htm)**

| Year | Population | Labor force | LFPR | Employed | E-pop | Unemployed | UR | Not in labor force |
|---|---|---|---|---|---|---|---|---|
| 2019 | 259,175 | 163,539 | 63.1 | 157,538 | 60.8 | 6,001 | 3.7 | 95,636 |
| 2020 | 260,329 | 160,742 | 61.7 | 147,795 | 56.8 | 12,947 | 8.1 | 99,587 |
| **2021** | **261,445** | **161,204** | **61.7** | **152,581** | **58.4** | **8,623** | **5.3** | **100,241** |
| 2022 | 263,973 | 164,287 | 62.2 | 158,291 | 60.0 | 5,996 | 3.6 | 99,686 |
| 2023 | 266,942 | 167,116 | 62.6 | 161,037 | 60.3 | 6,080 | 3.6 | 99,826 |
| 2024 | 268,571 | 168,106 | 62.6 | 161,346 | 60.1 | 6,761 | 4.0 | 100,465 |
| 2025* | 273,653 | 170,807 | 62.4 | 163,493 | 59.7 | 7,314 | 4.3 | 102,846 |

*11-month average.

- BLS warns that "revisions to population controls and other changes can affect the comparability of labor force levels over time." — [BLS cpsaat01](https://www.bls.gov/cps/cpsaat01.htm)
- **2021 U-6** averaged about **9.4%**. This is my own average of the monthly values. — [FRED U6RATE](https://fred.stlouisfed.org/series/U6RATE)
- **Pandemic peak, April 2020:** UR **14.8%**; U-6 **22.9%**; LFPR **60.1%**. — [FRED UNRATE](https://fred.stlouisfed.org/series/UNRATE); [FRED U6RATE](https://fred.stlouisfed.org/series/U6RATE); [FRED CIVPART](https://fred.stlouisfed.org/series/CIVPART)

**Long-run LFPR trends** (annual averages I computed from monthly seasonally adjusted data; [FRED CIVPART](https://fred.stlouisfed.org/series/CIVPART), [FRED LNS11300001 (men)](https://fred.stlouisfed.org/series/LNS11300001), [FRED LNS11300002 (women)](https://fred.stlouisfed.org/series/LNS11300002))

| Year | Total | Men | Women |
|---|---|---|---|
| 1948 | 58.8 | 86.6 | 32.7 |
| 1970 | 60.4 | 79.7 | 43.4 |
| 1990 | 66.5 | 76.4 | 57.5 |
| 2000 | 67.1 | 74.8 | 59.9 |
| 2021 | 61.7 | 67.6 | 56.1 |
| 2025 | 62.4 | 67.8 | 57.3 |
| 2026 (Jan–Sep) | 61.8 | 67.1 | 56.8 |

- **All-time monthly peaks:**
  - Total LFPR: **67.3% (January 2000)**.
  - Women: **60.3% (April 2000)**.
  - Men: **87.4% (October 1949)**. Men's all-time low was **66.1% (April 2020)**.
  - Sources: [FRED CIVPART](https://fred.stlouisfed.org/series/CIVPART); [FRED LNS11300002](https://fred.stlouisfed.org/series/LNS11300002); [FRED LNS11300001](https://fred.stlouisfed.org/series/LNS11300001)
- **July 2026 low:** LFPR fell to 61.4%, which, excluding the pandemic, is "the lowest level since 1976." Employ America estimates that about **0.55 point** of the past year's 0.8-point drop reflects an older population mix. — [Axios, Aug 13 2026](https://www.axios.com/2026/08/13/labor-market-demographics-boomers)
  - My check against FRED agrees: excluding March 2020–December 2021, the last month with LFPR at or below 61.4% was March 1976. — [FRED CIVPART](https://fred.stlouisfed.org/series/CIVPART)
- **New York Fed (March 2023):** population aging, which raised the number of retirements, can explain essentially the **entire** post-February-2020 participation gap (about 0.9 point). — [NY Fed Liberty Street Economics](https://libertystreeteconomics.newyorkfed.org/2023/03/what-has-driven-the-labor-force-participation-gap-since-february-2020)
- **BLS Monthly Labor Review (2018):** the long decline since 2000 is mainly secular. Baby-boomer retirement is the main driver, along with falling prime-age male participation. BLS projected LFPR of about **59%** by the late 2020s. — [BLS MLR 2018](https://www.bls.gov/opub/mlr/2018/beyond-bls/down-and-down-we-go-the-falling-us-labor-force-participation-rate.htm)
- **Earlier estimates (secondary summary):** CBO and the Chicago and Kansas City Feds attributed about **half** of the post-2007 decline, and about **one-third** of the decline since 2000, to aging. — [CBPP blog](https://www.cbpp.org/blog/why-is-labor-force-participation-shrinking-contd)

**International comparison.** OECD harmonized unemployment rates (ages 15+, seasonally adjusted), via FRED:

| Country | Latest month (2026) | 2021 annual | 2025 annual | Source |
|---|---|---|---|---|
| Spain | **10.0%** (Jul) | 14.9% | 10.5% | [FRED LRHUTTTTESM156S](https://fred.stlouisfed.org/series/LRHUTTTTESM156S) |
| France | **8.3%** (Jul) | 7.9% | 7.7% | [FRED LRHUTTTTFRM156S](https://fred.stlouisfed.org/series/LRHUTTTTFRM156S) |
| Italy | **5.8%** (Jul) | 9.6% | 6.1% | [FRED LRHUTTTTITM156S](https://fred.stlouisfed.org/series/LRHUTTTTITM156S) |
| Germany | **4.0%** (Jul) | 3.6% | 3.8% | [FRED LRHUTTTTDEM156S](https://fred.stlouisfed.org/series/LRHUTTTTDEM156S) |
| Japan | **2.4%** (Jul) | 2.8% | 2.5% | [FRED LRHUTTTTJPM156S](https://fred.stlouisfed.org/series/LRHUTTTTJPM156S) |
| United States | — | 5.4% | 4.3% | [FRED LRHUTTTTUSA156S](https://fred.stlouisfed.org/series/LRHUTTTTUSA156S) |

### Inferences
- **Slides' direction of trends is confirmed:** women's LFPR rose, men's fell, and the recent decline is partly retirements.
- **Exam nuance:** women's LFPR has been **flat to slightly down since about 2000**. It did not keep rising.
- **The slides' 2021 data reflect a pandemic-depressed year.** UR was 5.3% in 2021, versus 3.6% in 2022–23 and 4.2% today.
- **International pattern still holds:** Spain, France and Italy are higher than the US; Germany and Japan are lower. But Italy's gap has narrowed a lot (9.6% in 2021 to 5.8% in 2026).

### Gaps
- I did not find BLS's annual-average LFPR by sex in a BLS table. The figures above are my averages of FRED's monthly seasonally adjusted series, which may differ from BLS's official annual averages by about 0.1 point.
- I did not check how the January 2026 population controls affect the drop in LFPR from 2025 to 2026.

---

## Q3. What is CBO's current estimate of the natural rate (the noncyclical rate of unemployment)? Does it fit the slides' "~4–5%" equilibrium rate?

### Takeaway
CBO's noncyclical rate is **about 4.4%** for 2025–26, edging down to about 4.2% by 2036. The FOMC's longer-run median is **4.2%**. Both sit inside the slides' 4–5% range. With UR at 4.1–4.2%, cyclical unemployment is now slightly **negative** (about −0.2 to −0.3 point).

### Cited Findings
- **CBO's estimates** (February 2026 *Budget and Economic Outlook* vintage): about **4.40%** in 2025Q4–2026Q2 and **4.39%** in 2026Q3–Q4, declining to **4.16%** by 2036Q4. FRED last updated the series on Feb 27, 2026. — [FRED NROU (source: CBO)](https://fred.stlouisfed.org/series/NROU)
- **CBO's definition** (from the series notes): the natural rate (NAIRU) is "the rate of unemployment arising from all sources except fluctuations in aggregate demand." In 2021, CBO renamed the series from "Natural Rate of Unemployment (Long-Term)" to "**Noncyclical Rate of Unemployment**." — [FRED NROU](https://fred.stlouisfed.org/series/NROU)
- **Historical CBO values:** about **5.0%** in 2010; about **4.45–4.49%** in 2019–2021. — [FRED NROU](https://fred.stlouisfed.org/series/NROU)
- **FOMC longer-run unemployment rate (median of Summary of Economic Projections):** **4.2%** at the March, June and September 16, 2026 meetings. — [FRED UNRATEMDLR](https://fred.stlouisfed.org/series/UNRATEMDLR)

### Inferences
- **Worked decomposition:** actual UR = natural rate (frictional + structural) + cyclical.
  - 2026Q3: average UR = (4.1 + 4.1 + 4.2) ÷ 3 = **4.13%**. Cyclical = 4.13 − 4.39 = **−0.26 point**, meaning the labor market is slightly tighter than its natural level.
  - 2010: UR 9.61% − 5.03% = **about +4.6 points** of cyclical unemployment (Great Recession aftermath).
  - 2021: 5.35% − 4.45% = **about +0.9 point**.
  - Inputs from [FRED UNRATE](https://fred.stlouisfed.org/series/UNRATE) and [FRED NROU](https://fred.stlouisfed.org/series/NROU).

### Gaps
- I could not fetch CBO's own page (cbo.gov returned HTTP 403). The figures come from FRED's republication of CBO's series.

---

## Q4. Efficiency wages: what are the facts about Ford's $5 day and Raff & Summers (1987)?

### Takeaway
**Confirmed:**
- Ford announced the $5 day on **January 5, 1914**.
- Turnover was **370% in 1913**.
- Raff & Summers (1987) conclude the episode strongly supports efficiency-wage theories: queues for Ford jobs, plus higher productivity and profits.

**Flag:** the slides give a $2.25 prevailing wage. Sources say Ford's previous rate was **$2.34 for a 9-hour day** (and the $5 was for an 8-hour day).

### Cited Findings
- **Announcement:** Henry Ford and James Couzens announced the plan on **January 5, 1914**. — [The Henry Ford, "Ford's Five-Dollar Day"](https://www.thehenryford.org/collections/explore/articles/fords-five-dollar-day)
- **Old vs. new wage:** the new minimum was **$5 for an eight-hour day**, "more than doubling the previous minimum of **$2.34 for a nine-hour day**." — [EBSCO Research Starter](https://ebsco.com/research-starters/history/henry-ford-institutes-500-day-minimum-wage); the same $2.34 figure appears in [The Henry Ford's "$5 Day" set](https://www.thehenryford.org/collections-and-research/digital-collections/expert-sets/7138) (via search snippet).
- **Turnover:** assembly-line work bored employees, and Ford faced "a crippling labor turnover rate of **370 percent**." — [The Henry Ford](https://www.thehenryford.org/collections/explore/articles/fords-five-dollar-day)
- **Hiring to stay staffed:** Ford reportedly had to hire about **52,000** workers in a year to maintain a workforce of about **13,000–14,000** (historian Stephen Meyer, as cited in an op-ed). This figure is less firmly sourced. — [TribLive commentary](https://archive.triblive.com/opinion/featured-commentary/henry-ford-didnt-pay-5-a-day-just-to-be-nice/)
- **How the $5 was structured:**
  - It was about $2.30 base pay plus a **$2.70 profit-sharing bonus**.
  - The bonus depended on behavior that company inspectors checked through home visits: no drinking, no family abuse, no boarders, a clean home, and regular saving.
  - Thousands of applicants arrived and riots broke out. Crowds were dispersed with fire hoses.
  - Source: [The Henry Ford](https://www.thehenryford.org/collections/explore/articles/fords-five-dollar-day)
- **Women:** at first the $5 day applied only to male employees. It was extended to women in **October 1916**. — [EBSCO](https://ebsco.com/research-starters/history/henry-ford-institutes-500-day-minimum-wage)
- **Raff & Summers, "Did Henry Ford Pay Efficiency Wages?"** *Journal of Labor Economics* 5(4), Oct 1987, pp. S57–S86 (NBER WP 2101, 1986).
  - Findings: "substantial queues for Ford jobs" and "significant increases in Ford productivity and profits." They conclude the Ford experience "strongly supports" efficiency-wage theories.
  - Sources: [NBER w2101](https://www.nber.org/papers/w2101); [IDEAS/RePEc](https://ideas.repec.org/a/ucp/jlabec/v5y1987i4ps57-86.html)
- **Counterpoint:** Raff (1988) argued that efficiency-wage theories in which higher wages raise output are "implausible" here, and that **rent-sharing** fits the episode better. — [Raff 1988, *Journal of Economic History*](https://ideas.repec.org/a/cup/jechis/v48y1988i02p387-399_00.html)

### Inferences
- **Efficiency-wage logic for the exam:** a wage set above equilibrium cuts turnover, absenteeism and shirking, and raises productivity. But it also creates **excess labor supply** (queues of applicants), which is **structural unemployment**. Ford's job queues are the textbook illustration.

### Gaps
- I could not confirm the slides' "$2.25 prevailing wage." It may be the textbook's rounding or a Detroit-area average. Ford-specific sources say $2.34 for 9 hours.
- The Raff & Summers PDF is a scanned image with no text layer, so I could not extract the paper's own turnover or absenteeism tables.
- I did not verify the effective date (as opposed to the January 5 announcement), which is commonly given as January 12, 1914.

---

## Q5. Unions: what are the latest membership rates, and what is the union wage premium?

### Takeaway
- **2025 (released Feb 18, 2026):** union membership was **10.0%** overall, but **5.9%** in the private sector and **32.9%** in the public sector.
- The slides' "~7% of private-sector workers" is **outdated**. The private rate was 6.1% in 2021 and 5.9% in 2025.
- The slides' "~15% union wage premium" matches the long-standing regression-adjusted consensus. The **raw** gap in median weekly earnings is about 20%.

### Cited Findings
- **2025:**
  - **10.0%** of wage and salary workers were union members (**14.7 million**).
  - Private sector **5.9%**; public sector **32.9%**.
  - Union representation (members plus covered nonmembers): **11.2%** (16.5 million).
  - Median weekly earnings (full-time): **$1,404** for union members vs. **$1,174** for nonunion workers. BLS notes these comparisons "do not control for many factors."
  - Source: [BLS Union Members Summary (Feb 18, 2026)](https://www.bls.gov/news.release/union2.nr0.htm)
- **2021 (matching the slides' data year):** overall **10.3%** (about 14.0 million); private sector **6.1%**; public sector **33.9%**. — [BLS Union Members 2021 (Jan 20, 2022)](https://www.bls.gov/news.release/archives/union2_01202022.htm)
- **Wage premium:** Hirsch (2003) describes labor economists' consensus that the average union–nonunion wage gap is **about 15%** (based largely on H. Gregg Lewis's work), and argues it is probably biased downward. — [Hirsch, IZA DP 795](https://docs.iza.org/dp795.pdf)

### Inferences
- **Raw gap calculation:** $1,404 ÷ $1,174 = **1.196**, so union median earnings are about **19.6% higher** (equivalently, nonunion earnings are 83.6%, about 84%, of union earnings). The adjusted premium (~15%) is smaller because unions are concentrated in higher-paying occupations and industries.
- **How unions cause structural unemployment:** union-negotiated wages above market-clearing levels reduce the quantity of labor demanded in covered sectors. Displaced workers may queue for union jobs ("wait unemployment") or crowd into the nonunion sector.

### Gaps
- I did not obtain the latest regression-adjusted union premium from Unionstats.com.

---

## Q6. Minimum wage: what does the evidence actually say?

### Takeaway
The slides say research suggests "negligible overall unemployment effects." That is **defensible but contested**:
- Card & Krueger (1994) and Cengiz, Dube, Lindner & Zipperer (2019) find little or no job loss.
- Neumark & Wascher's re-analysis, the Seattle hours study, and CBO's $15 scoring imply some losses.
- Effects seem to depend on how high the minimum is relative to local wages.

A careful answer is "small or negligible employment effects for moderate increases; uncertainty grows with large increases."

### Cited Findings
- **Card & Krueger (1994, *AER* 84(4): 772–793):**
  - New Jersey raised its minimum from **$4.25 to $5.05** on April 1, 1992. Pennsylvania's stayed constant, giving a control group.
  - They surveyed **410 fast-food restaurants** and found **no reduction in employment** in New Jersey.
  - Source: [Card & Krueger 1994 (PDF)](https://www.eco.uc3m.es/docencia/EconomiaAplicada/materiales/CardKrueger94_en.pdf)
- **Neumark & Wascher re-evaluation:** using payroll records from 230 restaurants, they estimated a **4.6% decrease** in NJ employment relative to Pennsylvania. — [NBER w5224](https://nber.org/papers/w5224)
- **Cengiz, Dube, Lindner & Zipperer (2019, *QJE* 134(3): 1405–1454):**
  - Studied **138 state minimum-wage increases** (1979–2016) using a "bunching estimator."
  - The overall number of low-wage jobs "remained essentially unchanged over the five years following the increase." The missing jobs below the new minimum were offset by excess jobs at or just above it.
  - "No evidence of disemployment when we consider higher levels of minimum wages," though some evidence of reduced employment in **tradable** sectors.
  - Sources: [NBER w25434](https://www.nber.org/papers/w25434); [LSE Research Online](https://researchonline.lse.ac.uk/id/eprint/88682)
- **Seattle (Jardim, Long, Plotnick et al., NBER WP 23532, 2017):**
  - The increase to **$13** reduced hours in low-wage jobs by **about 9%**, while hourly wages rose about 3%.
  - Net effect: **−$125 per month** in earnings for low-wage workers in 2016.
  - A contemporaneous UC Berkeley study (Reich et al.) of food service found **no** adverse employment effect.
  - Sources: [NBER conference paper](https://conference.nber.org/conf_papers/f99777/f99777.pdf); [Research Council summary](https://researchcouncil.org/novel-research-adds-to-our-understanding-of-seattles-minimum-wage/)
- **CBO, July 2019** ($15 federal minimum by 2025):
  - **Median** estimate: **1.3 million** fewer workers employed, likely range "about zero to 3.7 million."
  - Pay would rise for at least **17 million** workers (plus possibly 10 million more), and **1.3 million** people would be lifted out of poverty.
  - A **$12** option would mean about **300,000** fewer jobs.
  - Sources: [NPR summary](https://www.npr.org/2019/07/08/739607964/-15-minimum-wage-would-boost-17-million-workers-cut-1-3-million-jobs-cbo-says); CBO report at [cbo.gov/publication/55410](https://www.cbo.gov/publication/55410) (blocked when I tried to fetch it)
- **CBO, February 2021** (Raise the Wage Act, $15 by June 2025):
  - **1.4 million** fewer jobs (about 0.9% of employment) and **900,000** fewer people in poverty.
  - Net wage gain about **$333 billion**; deficits **+$54 billion** over 2021–2031.
  - Sources: [CNN](https://edition.cnn.com/2021/02/08/politics/cbo-report-15-dollar-minimum-wage); [Al Jazeera](https://www.aljazeera.com/economy/2021/2/8/fight-for-15-biden-plan-costs-54bn-lifts-900000-from-poverty); CBO report at [cbo.gov/publication/56975](https://www.cbo.gov/publication/56975) (blocked)

### Inferences
- **Theory to know for the exam:** in the competitive model, a **binding** minimum wage (set above equilibrium) creates a labor surplus, which is structural unemployment. In a monopsony model, a modest minimum can **raise** employment. That is one reason the empirical effects are small.
- **Size matters:** CBO's $12 option shows much smaller losses than its $15 option, consistent with effects growing with the size of the increase.

### Gaps
- I could not fetch the CBO reports directly. I did not verify CBO's 2021 likely range (commonly reported as "about 0 to 2.7 million"), or the final published version of the Seattle study (*AEJ: Economic Policy*, 2022).

---

## Q7. Unemployment insurance: how does it affect search duration and the quality of job matches?

### Takeaway
- **Slides confirmed:** UI replaces **about half** of prior wages, up to a state maximum, for up to **26 weeks** (about 6 months) in most states.
- **Longer potential benefits lengthen unemployment:** each added week of benefits adds about **0.16–0.20 weeks** to spells (Katz & Meyer 1990).
- **Liquidity matters:** Card, Chetty & Weber (2007) find that extra cash-on-hand slows job-finding, partly because people can afford to search.
- **Match quality:**
  - Card, Chetty & Weber find little effect.
  - Nekoei & Weber (2017) find longer UI **raises re-employment wages and firm quality**.
- **Pandemic $600 supplements:** large spending effects but small job-finding effects (Ganong et al.). A San Francisco Fed estimate is larger.

### Cited Findings
- **US UI basics:** in most states the basic program provides "up to **26 weeks** of benefits... replacing **about half** of their previous wages, up to a maximum benefit amount." Some states provide fewer weeks. The permanent Extended Benefits program adds 13 or 20 weeks when state unemployment is high. — [CBPP Policy Basics: Unemployment Insurance](https://www.cbpp.org/research/policy-basics-unemployment-insurance)
- **Katz & Meyer (1990, *J. Public Economics* 41(1): 45–72):**
  - A one-week increase in potential benefit duration raises the average unemployment spell by about **0.16–0.20 weeks**.
  - Extending duration raises mean unemployment more than a budget-equivalent increase in benefit levels.
  - Sources: [NBER w2741](https://www.nber.org/papers/w2741); [Katz faculty page](https://lkatz.scholars.harvard.edu/publications/impact-potential-duration-unemployment-benefits-duration-unemployment)
  - PolitiFact's summary: extending benefits from 6 months to 1 year raises mean unemployment duration by **4–5 weeks**. — [PolitiFact](https://www.politifact.com/factchecks/2009/aug/04/michelle-malkin/michelle-malkin-says-former-clinton-official-says-/)
- **Card, Chetty & Weber (2007, *QJE* 122(4): 1511–1560), using Austrian data:**
  - Severance pay of **2 months' earnings** lowers job-finding rates by **8–12%**.
  - Extending UI from **20 to 30 weeks** lowers job-finding in the first 20 weeks by **5–9%**.
  - Longer search has "little or no effect" on subsequent match quality.
  - Sources: [NBER w12639](https://www.nber.org/papers/w12639); [IDEAS](https://ideas.repec.org/a/oup/qjecon/v122y2007i4p1511-1560..html)
- **Nekoei & Weber (2017, *AER* 107(2): 527–561):**
  - Used an age-based regression discontinuity design on Austrian data.
  - Extending UI **raises post-unemployment wages** "by improving reemployment firms' quality and attenuating wage drops." In other words, it produces better matches.
  - Sources: [IZA DP 9034](https://www.iza.org/publications/dp9034); [AER DOI 10.1257/aer.20150528](https://www.aeaweb.org/articles?id=10.1257/aer.20150528); [openICPSR replication](https://www.openicpsr.org/openicpsr/project/113058/version/V1/view)
- **Ganong, Greig, Noel et al.** (pandemic UI; published in *AER* 2024 per the AEA summary): the supplements had **large effects on spending but small effects on job-finding**. — [JPMorgan Chase Institute](https://www.jpmorganchase.com/institute/all-topics/labor-markets-and-workforce/unemployment-insurance-job-search-and-spending-during-the-pandemic); [AEA Research Highlight](https://benny.aeaweb.org/research/charts/job-finding-unemployment-benefits)
- **Dissent:** a San Francisco Fed working paper estimates a **22% reduction** in job-finding rates for the typical recipient from the $600 supplement, which it calls a "moderate" disincentive. — [FRBSF WP 2021-13](https://www.frbsf.org/wp-content/uploads/wp2021-13.pdf)

### Inferences
- **Exam framing:** UI **lowers the opportunity cost of search**, which raises frictional unemployment by lengthening spells. But it can **improve match quality**: workers aren't forced to take the first poor-fit job. That is a social benefit, so the slides' framing is consistent with the evidence.

### Gaps
- I did not verify a source for the exact current number of states offering fewer than 26 weeks. The CBPP pages are partly dated (one is a 2015 update).

---

## Q8. What are the costs of unemployment: mass-layoff earnings losses, mortality, effects on children, and hysteresis?

### Takeaway
**The slides' figures are confirmed exactly.** Davis & von Wachter (2011) find that men displaced in mass layoffs lose **1.4 years** of pre-displacement earnings (present value) when national unemployment is **below 6%**, and **2.8 years** when it is **above 8%**.

The other costs also hold up:
- Mortality rises **50–100%** in the year after displacement (Sullivan & von Wachter 2009).
- Children of displaced fathers earn **about 9% less** as adults (Oreopoulos, Page & Stevens 2008).
- Hysteresis is the idea that high unemployment can raise the natural rate (Blanchard & Summers 1986).

### Cited Findings
- **Davis & von Wachter, "Recessions and the Costs of Job Loss"** (*Brookings Papers on Economic Activity*, Fall 2011, 43(2): 1–72; NBER WP 17638):
  - Uses Social Security records for 1974–2008.
  - "Men lose an average of **1.4 years** of pre-displacement earnings if displaced in mass-layoff events that occur when the national unemployment rate is **below 6 percent**. They lose a staggering **2.8 years** of pre-displacement earnings if displaced when the unemployment rate **exceeds 8 percent**."
  - These figures "reflect discounting at a **5% annual rate over 20 years** after displacement."
  - Sources: [NBER w17638](https://www.nber.org/papers/w17638); [Brookings](https://www.brookings.edu/bpea-articles/recessions-and-the-costs-of-job-loss/)
- **Dollar figure (NBER Digest):** for men under 50 with 3+ years of tenure, job loss reduces the present value of earnings by about **$77,557 (2000 dollars)**. — [NBER Digest, Apr 2012](https://www.nber.org/digest/apr12/recessions-and-cost-job-loss). I got this figure from a search summary, not a direct page read.
- **Sullivan & von Wachter, "Job Displacement and Mortality"** (*QJE* 124(3): 1265–1306, 2009):
  - For high-seniority male workers, mortality in the year after displacement is **50–100% higher** than expected.
  - Even 20 years later, annual death hazards are **10–15% higher**.
  - If those increases persisted, they would imply a **1.0–1.5 year** loss in life expectancy for a worker displaced at age 40.
  - Sources: [IDEAS](https://ideas.repec.org/a/oup/qjecon/v124y2009i3p1265-1306..html); [NBER w13626](https://www.nber.org/papers/w13626)
- **Oreopoulos, Page & Stevens, "The Intergenerational Effects of Worker Displacement"** (*JOLE* 26(3): 455–483, 2008):
  - Uses Canadian data.
  - Children whose fathers were displaced earn **about 9% less** per year as adults.
  - They are also more likely to receive UI and social assistance.
  - Sources: [NBER w11587](https://nber.org/papers/w11587); [IDEAS](https://ideas.repec.org/p/cda/wpaper/38.html)
- **Blanchard & Summers, "Hysteresis and the European Unemployment Problem"** (*NBER Macroeconomics Annual* 1986, pp. 15–78; NBER WP 1950):
  - Hysteresis means shocks that raise actual unemployment can also raise the **natural rate**.
  - Mechanism: in wage bargaining, employed "insiders" set wages to protect their own jobs, while unemployed "outsiders" are disenfranchised.
  - They apply the idea to persistent unemployment in Europe and to the US Great Depression.
  - Sources: [NBER w1950](https://www.nber.org/papers/w1950); [NBER chapter PDF](https://www.nber.org/system/files/chapters/c4245/c4245.pdf)

### Inferences
- **"1.4 vs 2.8 years" means multiples of annual pre-layoff earnings, in present value.** For example, a worker earning $50,000 a year loses about $70,000 in a strong labor market (1.4 × $50,000) and about $140,000 in a weak one (2.8 × $50,000). This example is illustrative, not from the paper.
- **Other costs.** Lower tax revenue and higher transfer spending, such as UI, are standard fiscal costs. I found no single citable figure for these in this pass.

### Gaps
- I did not find a citable estimate for the fiscal cost (lost tax revenue) of unemployment.

---

## Q9. What is a recession? How do the NBER definition, the "two consecutive quarters" rule and the Sahm rule compare?

### Takeaway
"Two consecutive quarters of negative GDP growth" is a **rule of thumb**, not the official US definition. NBER defines a recession as "a significant decline in economic activity that is spread across the economy and lasts more than a few months," and says it follows "no fixed rule."

The 2022 episode shows the difference:
- Advance estimates showed **two negative quarters** (−1.6% and −0.9%), but NBER declared **no** recession.
- Revised data now show Q2 2022 at **+0.6%**.

The Sahm rule stood at **0.00** in September 2026, well below its 0.50 recession trigger.

### Cited Findings
- **NBER definition:** "a significant decline in economic activity that is spread across the economy and lasts more than a few months."
  - The committee weighs depth, diffusion and duration, which are partly interchangeable.
  - It relies most on **real personal income less transfers** and **nonfarm payroll employment**. It also uses household-survey employment, real consumer spending, manufacturing and trade sales, and industrial production.
  - There is "no fixed rule."
  - Most recent cycle: peak **February 2020**, trough **April 2020**.
  - Source: [NBER Business Cycle Dating](https://www.nber.org/research/business-cycle-dating)
- **BEA advance estimate, July 28, 2022:** real GDP "decreased at an annual rate of **0.9 percent** in the second quarter of 2022"; Q1 2022 "decreased **1.6 percent**." — [BEA](https://www.bea.gov/news/2022/gross-domestic-product-second-quarter-2022-advance-estimate)
- **Current-vintage data:** 2022Q1 **−1.0%**, 2022Q2 **+0.6%** (annualized). — [FRED A191RL1Q225SBEA](https://fred.stlouisfed.org/series/A191RL1Q225SBEA)
- **Sahm rule** (created by Claudia Sahm):
  - Signals a recession when the 3-month moving average of the national unemployment rate rises **0.50 percentage point or more** above its lowest 3-month average of the previous 12 months.
  - Real-time value for **September 2026: 0.00**.
  - Source: [FRED SAHMREALTIME](https://fred.stlouisfed.org/series/SAHMREALTIME)

### Inferences
- **Sahm check (my calculation):** the 3-month average for July–September 2026 is (4.1 + 4.1 + 4.2) ÷ 3 = 4.13%. The minimum 3-month average over the prior 12 months is also about 4.13–4.20%, so the indicator is about 0, consistent with FRED.
- **Answering "the two-quarter rule" on a test:** the safest answer is to call it a common shorthand, and to say the official US dates are set by the NBER Business Cycle Dating Committee using a broader definition.

### Gaps
- None material.

---

## Q10. Calculation methods: what formulas and worked examples could a hard exam test? (All arithmetic verified in Python)

### Takeaway
Most exam questions come down to five identities and to tracking which categories a person moves between:
- LF = E + U
- UR = U ÷ LF
- LFPR = LF ÷ Pop
- E-pop = E ÷ Pop
- NILF = Pop − LF

The trickiest questions involve flows that move people **between** the labor force and NILF, because those change the **denominator** of the unemployment rate. The other high-yield method is computing the surplus at a wage floor from labor supply and demand equations.

### Cited Findings
- **Formulas** (Pop = civilian noninstitutional population 16+, E = employed, U = unemployed, LF = labor force):
  - LF = E + U
  - UR = U ÷ LF
  - LFPR = LF ÷ Pop
  - E-pop = E ÷ Pop
  - NILF = Pop − LF
  - Source: [BLS Definitions](https://www.bls.gov/cps/definitions.htm)
- **Alternative-measure formulas:** U-4, U-5 and U-6 add discouraged workers, the marginally attached, and people part time for economic reasons as specified in [BLS Table A-15](https://www.bls.gov/news.release/empsit.t15.htm).
- **Ohio monthly levels** (seasonally adjusted, current data vintage): Dec 2021 = 234,951 unemployed and 5,501,305 employed (UR 4.1%); Aug–Oct 2022 ≈ 235.8–237.3k unemployed and about 5.53M employed (UR 4.1%); Aug 2026 = 195,290 unemployed and 5,662,115 employed (UR **3.3%**). — [FRED LASST390000000000004](https://fred.stlouisfed.org/series/LASST390000000000004), [FRED LASST390000000000005](https://fred.stlouisfed.org/series/LASST390000000000005), [FRED OHUR](https://fred.stlouisfed.org/series/OHUR)
- **Ohio 2021 annual average** (not seasonally adjusted): 301,412 unemployed and 5,436,614 employed (UR **5.3%**). — [FRED LAUST390000000000004A](https://fred.stlouisfed.org/series/LAUST390000000000004A), [FRED LAUST390000000000005A](https://fred.stlouisfed.org/series/LAUST390000000000005A)

**Worked Example 1: Ohio (the slides' numbers)**
- U = 236k, E = 5,526k.
- LF = 236 + 5,526 = **5,762k**.
- UR = 236 ÷ 5,762 = 0.04096 = **4.1%** ✓ (matches the slide).
- LFPR cannot be computed: it needs Ohio's 16+ civilian noninstitutional population. A good trick question.

**Worked Example 2: US national**
- *2021 annual averages* ([BLS cpsaat01](https://www.bls.gov/cps/cpsaat01.htm)):
  - LF = 152,581 + 8,623 = **161,204** ✓
  - UR = 8,623 ÷ 161,204 = **5.35% → 5.3%**
  - LFPR = 161,204 ÷ 261,445 = **61.66% → 61.7%**
  - E-pop = 152,581 ÷ 261,445 = **58.36% → 58.4%**
  - NILF = 261,445 − 161,204 = **100,241** ✓
- *September 2026* (FRED levels above):
  - UR = 7,109 ÷ 170,262 = **4.18% → 4.2%**
  - LFPR = 170,262 ÷ 275,554 = **61.79% → 61.8%**
  - E-pop = 163,152 ÷ 275,554 = **59.21% → 59.2%**
  - E + U = 170,261, one off from the published 170,262 because of rounding.

**Worked Example 3: Alternative measures for September 2026, rebuilt from components** (inputs from the [BLS Employment Situation](https://www.bls.gov/news.release/empsit.nr0.htm): U = 7.109M; LF = 170.262M; discouraged 0.414M; marginally attached 1.5M; part time for economic reasons 4.5M)
- U-4 = (7.109 + 0.414) ÷ (170.262 + 0.414) = 7.523 ÷ 170.676 = **4.41%**. Published: 4.4 ✓
- U-5 = (7.109 + 1.5) ÷ (170.262 + 1.5) = 8.609 ÷ 171.762 = **5.01%**. Published: 5.0 ✓
- U-6 = (7.109 + 1.5 + 4.5) ÷ (170.262 + 1.5) = 13.109 ÷ 171.762 = **7.63%**. Published: 7.6 ✓
- Note that part-time-for-economic-reasons workers go in the U-6 **numerator only**. They are already in LF as employed.

**Worked Example 4: Flow scenarios**

Baseline: Pop = 1,000, E = 600, U = 40, NILF = 360. So LF = 640, **UR = 6.25%**, **LFPR = 64.0%**, **E-pop = 60.0%**.

| Scenario (10 people move) | E | U | LF | UR | LFPR | E-pop |
|---|---|---|---|---|---|---|
| (a) 10 unemployed become **discouraged** and stop searching (U → NILF) | 600 | 30 | 630 | **4.76% ↓** | **63.0% ↓** | 60.0% = |
| (b) 10 unemployed **find jobs** (U → E) | 610 | 30 | 640 | **4.69% ↓** | 64.0% = | 61.0% ↑ |
| (c) 10 NILF (e.g., students) **start searching** (NILF → U) | 600 | 50 | 650 | **7.69% ↑** | **65.0% ↑** | 60.0% = |
| (d) 10 employed **retire** (E → NILF) | 590 | 40 | 630 | **6.35% ↑** | 63.0% ↓ | 59.0% ↓ |
| (e) 10 employed **laid off** and searching (E → U) | 590 | 50 | 640 | 7.81% ↑ | 64.0% = | 59.0% ↓ |
| (f) 100 new 16-year-olds enter the population, all NILF | 600 | 40 | 640 | 6.25% = | 58.18% ↓ | 54.55% ↓ |
| (g) 10 unemployed take **involuntary part-time** jobs | 610 | 30 | 640 | 4.69% ↓ | 64.0% = | 61.0% ↑ (U-6 numerator unchanged for these 10) |

- Scenario (a) is the classic exam trap: the unemployment rate falls for a "bad" reason.
- Scenario (d) is counterintuitive: when **employed** workers retire, the UR **rises**, because LF shrinks while U stays the same.

**Worked Example 5: Structural unemployment from a wage floor**

Labor supply Ls = 20W; labor demand Ld = 1000 − 30W.

*Equilibrium:*
- 20W = 1000 − 30W → 50W = 1000 → **W\* = 20**, **L\* = 400**. No surplus.

*Minimum wage W = 25 (binding, since 25 > 20):*
- Ls = 500; Ld = 1000 − 750 = 250.
- **Surplus (structural unemployment) = 250.**
- Employment = min(Ls, Ld) = **250**, down 150 from 400.
- Of the 250 unemployed: **150 lost jobs** (400 − 250) and **100 are new entrants** drawn in by the higher wage (500 − 400).
- Unemployment rate in this market = 250 ÷ 500 = **50%**.

*Other wage floors:*

| Wage floor | Ls | Ld | Surplus | Employment | UR in this market |
|---|---|---|---|---|---|
| W = 18 | — | — | 0 | 400 | 0% (floor below 20 is non-binding; market clears) |
| W = 22 | 440 | 340 | **100** | 340 | 100 ÷ 440 = 22.7% |
| W = 30 | 600 | 100 | 500 | 100 | 83.3% |

The same method applies to an **efficiency wage** or a **union wage** set above W\*.

**Worked Example 6: Natural vs. cyclical decomposition** ([FRED UNRATE](https://fred.stlouisfed.org/series/UNRATE), [FRED NROU](https://fred.stlouisfed.org/series/NROU))
- Cyclical UR = actual UR − natural rate.
  - 2026Q3: 4.13 − 4.39 = **−0.26 point**.
  - 2010: 9.61 − 5.03 = **+4.58 points**.
  - 2021: 5.35 − 4.45 = **+0.90 point**.
- Natural rate = frictional + structural, so it is never zero even at "full employment."

### Inferences
**Classification cheat-sheet** (applying [BLS Definitions](https://www.bls.gov/cps/definitions.htm) and [BLS HTGM](https://www.bls.gov/cps/cps_htgm.htm); individual cases are my applications of the rules):

*Employed*
- Works 1+ paid hours a week, including a student tutoring 4 hours for pay.
- Self-employed.
- On vacation, sick, or on strike (temporarily absent).
- Works 15+ unpaid hours in a family business. At 10 unpaid hours, the person is not employed.
- Involuntary part-time worker. Employed, but counted in U-6.
- A working 80-year-old. There is no upper age limit.

*Unemployed*
- Laid off and interviewing (active search).
- On temporary layoff awaiting recall, even without searching.
- Quit a job to search ("job leaver").
- A new graduate sending out résumés.

*Not in the labor force*
- Retirees; full-time students who are not searching; stay-at-home caregivers.
- Unpaid interns or volunteers who are not searching for paid work.
- Someone who only browses job postings (passive search).
- Discouraged workers. They are counted in U-4 to U-6.

*Excluded from the population entirely*
- Active-duty military.
- Prison inmates and nursing-home residents.
- Anyone under 16.

*Receiving UI* is **irrelevant** to classification.

### Gaps
- I could not find the exact Ohio month and data vintage behind the slides' 236k/5,526k. In current-vintage LAUS data, Ohio's unemployment rate was 4.1% with similar levels in December 2021 and August–October 2022. The slides' figures are not the 2021 annual average, which was 5.3%. They likely come from an earlier data vintage or a specific month.

---

## Q11. Validation summary: which slide claims hold, which need updating, and which are unverified?

### Takeaway
Most slide content is **confirmed**. Items to update or flag:
- The private-sector union rate is now **5.9%** (2025), not ~7%.
- Ford's prior wage was **$2.34** (9-hour day), not $2.25.
- "Two consecutive quarters of negative GDP" is a rule of thumb, not NBER's definition.
- The minimum-wage evidence is **contested**, not simply "negligible."
- The 2021 data are pandemic-affected. UR is 4.2% now versus 5.3% in 2021.

### Cited Findings
**Confirmed**
- **Population definition:** 16+, no upper age limit, military and institutionalized excluded. — [BLS HTGM](https://www.bls.gov/cps/cps_htgm.htm)
- **Employed:** at least 1 paid hour, self-employed, or temporarily absent. — [BLS Definitions](https://www.bls.gov/cps/definitions.htm)
- **Unemployed:** active search is required; wanting a job isn't enough. — [BLS Definitions](https://www.bls.gov/cps/definitions.htm)
- **Discouraged workers are not in the labor force.** — [BLS Definitions](https://www.bls.gov/cps/definitions.htm)
- **Equilibrium (natural) rate of about 4–5%:** CBO puts it at 4.4%; the FOMC's longer-run median is 4.2%. — [FRED NROU](https://fred.stlouisfed.org/series/NROU); [FRED UNRATEMDLR](https://fred.stlouisfed.org/series/UNRATEMDLR)
- **UI pays about half of prior wages for about 6 months (26 weeks).** — [CBPP](https://www.cbpp.org/research/policy-basics-unemployment-insurance)
- **Ford:** the $5 day was announced in January 1914. — [The Henry Ford](https://www.thehenryford.org/collections/explore/articles/fords-five-dollar-day)
- **Union premium of about 15%** (regression-adjusted consensus). — [Hirsch IZA DP 795](https://docs.iza.org/dp795.pdf)
- **Mass-layoff losses:** 1.4 years vs. 2.8 years of earnings. — [NBER w17638](https://www.nber.org/papers/w17638)
- **Social costs:** higher mortality ([Sullivan & von Wachter](https://ideas.repec.org/a/oup/qjecon/v124y2009i3p1265-1306..html)) and worse outcomes for children ([Oreopoulos et al.](https://nber.org/papers/w11587)).
- **Hysteresis:** [Blanchard & Summers](https://www.nber.org/papers/w1950).
- **International ranking** (Spain, France, Italy above the US; Germany, Japan below). — [FRED OECD series](https://fred.stlouisfed.org/series/LRHUTTTTESM156S)
- **Ohio unemployment rate of 4.1%** from 236 ÷ 5,762. Arithmetic verified (see Q10).

**Update**
- **Private-sector union rate:** 6.1% in 2021 and 5.9% in 2025, versus the slides' "~7%." — [BLS 2021](https://www.bls.gov/news.release/archives/union2_01202022.htm); [BLS 2025](https://www.bls.gov/news.release/union2.nr0.htm)

**Flag**
- **Ford's prior wage:** sources say $2.34 for a 9-hour day versus the slides' $2.25. — [EBSCO](https://ebsco.com/research-starters/history/henry-ford-institutes-500-day-minimum-wage)
- **Recession definition:** NBER uses "no fixed rule." — [NBER](https://www.nber.org/research/business-cycle-dating)
- **Minimum wage:** the evidence is contested. — [Neumark & Wascher w5224](https://nber.org/papers/w5224); [NPR on CBO 2019](https://www.npr.org/2019/07/08/739607964/-15-minimum-wage-would-boost-17-million-workers-cut-1-3-million-jobs-cbo-says)

### Inferences
- The slides appear to be built from an earlier edition's data, which would explain the ~7% private union rate and the 2021 figures. The concepts and calculation methods are all consistent with official definitions.

### Gaps
- I did not have access to the textbook's actual text, so I could not confirm which specific figures (the $2.25 wage, the ~7% union rate) come from the book rather than the instructor.
- No test-bank or answer-key material was sought or used.
