# Chapter 12 "Inflation and Money" (Stevenson & Wolfers, *Principles of Macroeconomics*, 2nd ed., Macmillan Learning/Worth, ©2023): slide validation, latest data, and calculation methods

Textbook attribution (per coordinator correction): the course text is **Betsey Stevenson & Justin Wolfers, *Principles of Macroeconomics*, 2nd ed.**, not Goolsbee/Levitt/Syverson. The book's framing and terms, such as the "inflation fallacy" and the inflation-adjustment formula, are attributed to Stevenson & Wolfers below.

Research date: 2026-10-14. The slides use 2021–2022 data; the latest figures here are through the September 2026 CPI, released this morning, and the August 2026 PCE. I pulled CPI and PCE values from FRED's CSV downloads of the BLS and BEA series and recomputed every derived number in Python. Wherever an index value is given to three decimals, it comes from those series.

---

## Q0. Textbook identification (Stevenson & Wolfers) and whether the slide's specific claims check out

### Takeaway
The textbook is **Stevenson & Wolfers, *Principles of Macroeconomics*, 2nd ed. (Macmillan Learning/Worth, ©2023)**. Its Ch. 12 is "Inflation and Money," which the coordinator has confirmed and the Macmillan catalog shows. The original brief's Goolsbee/Levitt/Syverson attribution was wrong; that team's text is *Microeconomics*. Almost every number on the slides checks out against primary sources. There are three caveats: the Target revenue years are fiscal years labeled by the calendar year in which they end; the iPhone "66%" figure is based on the $599 8GB original iPhone; and the "~1%/year CPI bias" is the Boskin-era figure, with later estimates at about 0.85–0.9.

### Cited Findings
- The Macmillan Learning catalog lists *Principles of Macroeconomics*, Second Edition, by **Betsey Stevenson and Justin Wolfers** (©2023). Part III, "Macroeconomic Foundations and the Long Run," contains Ch. 9 GDP, Ch. 10 Economic Growth, Ch. 11 Unemployment and **Ch. 12 Inflation and Money**. Ch. 19 is the Phillips Curve and Inflation and Ch. 22 is Monetary Policy. — [Macmillan Learning](https://store.macmillanlearning.com/us/product/Principles-of-Macroeconomics/p/1319432085)
- My search turned up only *Microeconomics* for Goolsbee, Levitt & Syverson (Worth/Macmillan Learning; 3rd ed. 2020, 4th ed. 2024), not a macro text with this chapter. — [laprocure listing](https://www.laprocure.com/product/1857150/goolsbee-austan-microeconomics-4th-edition); [CiNii author record](https://ci.nii.ac.jp/author/DA17745209)
- **Coca-Cola, all confirmed in Levy & Young (2004):**
  - 1899 contract: bottlers could buy syrup "at the nominal price of **92 cents per gallon in perpetuity**."
  - 1901 amendment: $0.90 per gallon of syrup plus $0.10 per gallon for advertising.
  - 1920: "The Company is losing **$29,000 per day** ($213,235 in 1992 prices) because of its inability to adjust the syrup price." The parent bottlers sued.
  - 1921: a new contract set syrup at **$1.17/gallon**, plus 6¢ for every 1¢ rise in sugar above 7¢/lb.
  - 1923: Robert Woodruff became president.
  - 1936: Coca-Cola vending machines were introduced.
  - 1950: Coke reached 6¢ in NYC for the first time.
  - **1953: "Woodruff asks the Treasury Department to issue a 7 1/2 cent coin."**
  - **1959: "The last of the nickel Cokes is gone."**
  - Source: [Levy & Young, MPRA version of JMCB 36(4), 2004, pp. 765–799](https://mpra.ub.uni-muenchen.de/1046/1/MPRA_paper_1046.pdf); [JSTOR](https://www.jstor.org/stable/3839041)
- Levy & Young on the coin request: "Woodruff submitted a request in 1953 to the newly elected President Dwight Eisenhower (his hunting companion and friend)… Eisenhower forwarded the request to the Treasury Department officials who did not like the idea." A 1951 note by Woodruff also floated a **3-cent coin**, which would allow a 6¢ Coke paid with two coins. — [Levy & Young (MPRA)](https://mpra.ub.uni-muenchen.de/1046/1/MPRA_paper_1046.pdf)
- Levy & Young on the vending machines: "most of the Coca-Cola's 400,000 vending machines" around 1950 were nickel-only. Vending accounted for about 18% of soft-drink sales in 1950 and about 25% by 1953. Doubling the price to a dime "was out of question." — [Levy & Young (MPRA)](https://mpra.ub.uni-muenchen.de/1046/1/MPRA_paper_1046.pdf)
- The authors' abstract names two main sources of the rigidity: (1) the bottler contract and implicit retail price maintenance, and (2) single-coin vending machine technology. — [Levy & Young (MPRA)](https://mpra.ub.uni-muenchen.de/1046/1/MPRA_paper_1046.pdf)
- A popular account (NPR Planet Money, via WGBH) agrees: machines took "a single coin: a nickel," the head of Coca-Cola "asked President Eisenhower for help (they were hunting buddies.) No luck," and the last nickel Coke "seems to have been in 1959." — [WGBH/NPR](https://wgbh.org/news/2012-11-19/why-coke-cost-a-nickel-for-70-years)
- **iPhone:**
  - The original iPhone launched in the US in June 2007 at **$499 (4GB) and $599 (8GB)**. — [Apple Newsroom, Jan 9 2007](https://www.apple.com/newsroom/2007/01/09Apple-Reinvents-the-Phone-with-iPhone/)
  - The iPhone 13 Pro started at **$999**. It was announced and pre-ordered in September 2021, so it was not a 2022 launch. — [MacTrast](https://www.mactrast.com/2021/09/apple-debuts-iphone-13-pro-and-iphone-13-pro-max-promotion-displays-a15-bionic-chip-up-to-1tb-storage/)
- **Force Awakens:** domestic gross was **$936,662,225**, which rounds to $937M. — [Box Office Mojo](https://www.boxofficemojo.com/title/tt2488496/)
- **Target, fiscal 2020 (year ended Jan 30, 2021):**
  - Total revenue was **$93.6B**, up 19.8% from 2019. — [Target Q4 2020 8-K exhibit 99](https://www.sec.gov/Archives/edgar/data/27419/000002741921000007/a2020q4ex-99.htm); [Target FY2020 10-K](https://www.sec.gov/Archives/edgar/data/27419/000002741921000010/tgt-20210130.htm)
  - The precise figure was $93.56B. — [Supermarket News](https://www.supermarketnews.com/retail-financial/target-adds-15-billion-top-line-fiscal-2020)
  - **Fiscal 2019 (year ended Feb 1, 2020) total revenue was about $78.1B.** Target names each fiscal year after the calendar year in which it *begins*.
  - Fiscal 2021 total revenue was **$106B**. — [Target corporate](https://corporate.target.com/news-features/article/2022/03/q4-fy2021)
- **CPI values used on the slides match the BLS CPI-U annual averages (1982–84=100):**
  - 2012 = **229.594** (slide: 229.6)
  - 2015 = **237.017** (slide: 237.0)
  - 2020 = **258.811** (slide: 258.8)
  - 2021 = **270.970** (slide: 271.0)
  - Source: [FRED CPIAUCNS (BLS CPI-U, NSA)](https://fred.stlouisfed.org/series/CPIAUCNS)
- **9.1% peak:** CPI-U June 2022 was 296.311 versus 271.696 in June 2021, a 12-month change of **9.06%**. This was the cycle peak. — [FRED CPIAUCNS](https://fred.stlouisfed.org/series/CPIAUCNS)
- **2% goal adopted January 2012:** the FOMC statement reads "Adopted effective January 24, 2012; as amended effective August 22, 2025." — [Federal Reserve 2025 Statement on Longer-Run Goals](https://www.federalreserve.gov/monetarypolicy/monetary-policy-strategy-tools-and-communications-statement-on-longer-run-goals-monetary-policy-strategy-2025.htm)
- **Germany 1922–23 hyperinflation:** the episode ran **Aug. 1922 – Dec. 1923** and peaked in **Oct. 1923 at 29,500% per month**. — [Hanke-Krus Hyperinflation Table](https://www.bcci.bg/resources/files/hanke-krus-hyperinflation-table.pdf)

### Inferences
- The slide's examples (Whiskers the cat, Force Awakens, Target, iPhone, Coke) and terms ("inflation fallacy"; the inflation-adjustment formula: value in today's dollars = past value × CPI_today / CPI_then) should be attributed to **Stevenson & Wolfers (2023), Ch. 12**.
- **Target labeling:**
  - The slide's "2020: $78.1B" is Target's FY2019, which ended Feb 2020.
  - The slide's "2021: $93.5B" is FY2020, which ended Jan 2021.
  - The arithmetic is internally consistent with the slide's CPI choices, but a strict reader would deflate FY2020 revenue mostly with 2020 prices.
  - On an exam, use the numbers exactly as given.
- **"66% above first iPhone":** $999/$599 − 1 = 66.8%, so the slide compares against the 8GB model. Against the $499 4GB model the increase is 100%.

### Gaps
- I did not access the text of Stevenson & Wolfers itself, which is publisher content. I cannot confirm that the Whiskers basket ($796.70 → $820), the Target or Force Awakens framing, or the "Shiller 1997" citation appear in the book exactly as on the slides.
- The slide's "Shiller 1997" corresponds to NBER Working Paper 5539, dated April 1996. It was later published as a chapter in an NBER volume, but I did not verify the 1997 publication details (see Q7).

---

## Q1. How does BLS build the CPI: CPI-U vs CPI-W vs chained CPI, the base period, weights and quality adjustment?

### Takeaway
The CPI-U is a fixed-basket, modified-Laspeyres index of urban consumers' out-of-pocket spending, normalized so that 1982–84 = 100. Within item categories it uses geometric means. Since January 2023 its weights have been updated annually from Consumer Expenditure Survey data. The CPI-W covers a subset of wage-earner households. The chained C-CPI-U uses a Törnqvist formula to capture substitution between categories.

### Cited Findings
- **Coverage:**
  - CPI-U covers "over 90 percent of the U.S. population." It excludes rural nonmetropolitan residents, farm households, people on military installations and institutional populations.
  - CPI-W covers about **30%** of the population: wage-earner and clerical households, a subset of CPI-U.
  - Source: [BLS CPI FAQ](https://www.bls.gov/cpi/questions-and-answers.htm)
- **Base period:** "The average index level over the 36 months of 1982, 1983, and 1984 is set to 100." — [BLS CPI FAQ](https://www.bls.gov/cpi/questions-and-answers.htm)
  - Check from FRED: the monthly CPI-U averages 99.99 over 1982–84. Annual averages were 1982 = 96.5, 1983 = 99.6, 1984 = 103.9. — [FRED CPIAUCNS](https://fred.stlouisfed.org/series/CPIAUCNS)
- **Sample size:** BLS records prices on "about **80,000 items each month**." — [BLS CPI FAQ](https://www.bls.gov/cpi/questions-and-answers.htm)
- **Structure:** **243 basic items × 32 index areas = 7,776 item-area combinations**. Prices are sampled from 75 primary sampling units (PSUs). — [BLS Handbook of Methods, CPI Calculation](https://www.bls.gov/opub/hom/cpi/calculation.htm)
- **Formulas:**
  - Lower level: most item strata use the **geometric mean** formula. Some strata, including selected shelter, utilities, government fees and medical care services, use a modified Laspeyres formula.
  - Upper level: CPI-U and CPI-W aggregate the basic indexes with a **modified Laspeyres** formula.
  - The final C-CPI-U uses a **Törnqvist** formula in a monthly chained construct.
  - Source: [BLS Handbook of Methods](https://www.bls.gov/opub/hom/cpi/calculation.htm)
- **Geometric means since 1999:** the lower-level geometric-mean change took effect in 1999, and quality-adjustment changes for PCs came in 1998. Both reduced substitution and quality bias. — [Brookings summary of Moulton (2018)](https://www.brookings.edu/articles/measuring-inflation-whats-changed-over-the-past-20-years-what-hasnt)
- **C-CPI-U revisions:** a preliminary estimate is published first, then revised quarterly; data become final 10–12 months after initial publication. Some economists regard it as closer to a cost-of-living index. — [BLS CPI FAQ](https://www.bls.gov/cpi/questions-and-answers.htm)
- **Weights:**
  - The weights come from the Consumer Expenditure Surveys. For the 2023 CPI the source was 2021 CE data, drawn from more than 20,000 interview consumer units and about 12,000 two-week diaries. — [BLS CPI FAQ](https://www.bls.gov/cpi/questions-and-answers.htm)
  - Starting with **January 2023** data, BLS updates weights **annually from a single calendar year** of spending.
  - Previously weights were updated **biennially** using two years of data, a practice begun in 2002. Before that they were updated roughly every 10 years.
  - The change cut the average lag between purchase and use in the index from **36 to 24 months**. It applies to CPI-U, CPI-W and the initial and interim C-CPI-U.
  - Source: [BLS 2023 weight update](https://www.bls.gov/cpi/tables/relative-importance/weight-update-information-2023.htm); [AEA forum note on the BLS announcement](https://benny.aeaweb.org/forum/2950/bls-to-update-cpi-spending-weights-annually-8-24-22)
- **Quality adjustment:**
  - When a replacement item isn't directly comparable, BLS uses direct comparison, direct quality adjustment (including **hedonic regression models** and manufacturers' cost data) or imputation. — [BLS Handbook](https://www.bls.gov/opub/hom/cpi/calculation.htm)
  - Hedonics are used in categories with frequent quality change, such as apparel (seasonal turnover) and appliances and electronics. — [BLS Quality Adjustment Q&A](https://www.bls.gov/cpi/quality-adjustment/questions-and-answers.htm)
  - For example, the TV model splits price into implicit values of features. — [BLS TVs](https://www.bls.gov/cpi/quality-adjustment/televisions.htm)
  - A 2020 BLS slide listed 18 of 35 apparel items as hedonically adjusted, along with TVs, phones and some services. That snapshot is dated. — [BLS presentation](https://www.bls.gov/cpi/additional-resources/quality-adjustment-price-programs-presentation.pdf)
- **Cost-of-living status:** BLS calls the CPI a **conditional** cost-of-living index because it omits public goods and environmental factors. — [BLS CPI FAQ](https://www.bls.gov/cpi/questions-and-answers.htm)
- **2025 shutdown gap:**
  - "BLS did not collect CPI data from October 1, 2025, through November 12, 2025." The missing data affected the October and November 2025 indexes. — [BLS shutdown impact page](https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi.htm)
  - **No October 2025 all-items CPI was published.** For most series the **2025 annual average is computed from 11 monthly values**. — [BLS shutdown FAQ](https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi-faq.htm)
  - FRED shows October 2025 as blank. — [FRED CPIAUCNS](https://fred.stlouisfed.org/series/CPIAUCNS)

### Inferences
- For exams:
  - "Fixed basket" means a Laspeyres-type index, which is the root of **upper-level substitution bias**. The chained CPI exists to correct it.
  - Geometric means (since 1999) address **lower-level** substitution, for example between apple varieties.
  - Hedonics address **quality bias**.
- Empirically, the C-CPI-U runs below the CPI-U by about 0.1–0.3 pp a year (annual-average inflation; see Q4 table). That gap is consistent with the substitution-bias story.

### Gaps
- I did not verify the exact current list of hedonically adjusted items or the date the C-CPI-U was introduced; it is usually cited as 2002, but I did not confirm this from a BLS page.
- I did not fetch current relative-importance weights, such as shelter's share.

---

## Q2. PCE vs CPI, why the Fed targets PCE, the 2012/2020/2025 framework history, and the GDP deflator vs CPI

### Takeaway
The Fed's 2% target, adopted in January 2012, is defined on **PCE** inflation. The PCE index is broader (it includes third-party health payments and rural households), its weights update monthly, and it runs about 0.4 pp below CPI on average. In August 2020 the Fed adopted flexible *average* inflation targeting. On **August 22, 2025** it dropped the averaging and "make-up" language while keeping the 2% PCE goal.

### Cited Findings
- **Current statement wording:** the FOMC "reaffirms its judgment that inflation at the rate of 2 percent, as measured by the annual change in the price index for personal consumption expenditures" is most consistent with its mandates.
  - "Adopted effective January 24, 2012; as amended effective August 22, 2025."
  - The 2025 text contains **no "average" or "moderately above 2 percent for some time"** language. It says the Committee "is prepared to act forcefully" to keep expectations anchored at 2%.
  - Source: [Fed 2025 Statement](https://www.federalreserve.gov/monetarypolicy/monetary-policy-strategy-tools-and-communications-statement-on-longer-run-goals-monetary-policy-strategy-2025.htm)
- **2020 framework:** on Aug 27, 2020 the FOMC unanimously approved a statement saying it "seeks to achieve inflation that **averages 2 percent over time**." It added that after periods of persistently low inflation, policy "will likely aim to achieve inflation **moderately above 2 percent for some time**," which is flexible average inflation targeting (FAIT). — [Fed press release Aug 27 2020](https://www.federalreserve.gov/newsevents/pressreleases/monetary20200827a.htm); [Fed Feb 2021 MPR](https://www.federalreserve.gov/monetarypolicy/2021-02-mpr-part2.htm)
- **2025 review:**
  - The review covered the Statement and communications. "The Committee's 2 percent longer-run inflation goal was not a focus of the review."
  - The revised statement was released Aug 22, 2025, and future reviews will happen "roughly every five years."
  - Source: [Fed 2025 Review overview](https://www.federalreserve.gov/monetarypolicy/guide-to-changes-in-statement-on-longer-run-goals-monetary-policy-strategy.htm)
- **PCE vs CPI (Cleveland Fed):**
  - Formula effect: PCE weights update **monthly**, CPI weights **annually**, so PCE better captures substitution ("steak for hamburger").
  - Scope effect: CPI covers "out-of-pocket spending… by urban households." PCE adds rural households and spending on consumers' behalf, such as employer health insurance, Medicare and Medicaid.
  - Weight effect: PCE gives health care a higher weight and housing a lower weight.
  - PCE has been the Fed's "preferred inflation measure since 2000."
  - **Since 2000, CPI inflation has averaged 0.39 pp above PCE inflation.**
  - Source: [Cleveland Fed infographic, Dec 2024](https://www.clevelandfed.org/collections/infographics/2024/infogr-20241205-cpi-versus-pce-price-index)
- **PCE draws on CPI data:** over 70% of PCE price data come from the CPI (Minneapolis Fed, as quoted). — [Conversable Economist](https://conversableeconomist.com/2012/01/17/consumer-price-index-vs-personal-consumption-expenditures-index/)
- **GDP deflator vs CPI:**
  - The deflator covers all *domestically produced* goods and services, including investment and government purchases. The CPI covers goods and services *bought by consumers*.
  - **Imports** are in the CPI but not the deflator. A foreign car's price rise raises the CPI but not the deflator.
  - The CPI uses a **fixed basket**, while the deflator's weights change with GDP composition.
  - The CPI is a Laspeyres index that can overstate the effect of price rises by ignoring substitution.
  - Source: [Mankiw & Scarth textbook excerpt (Macmillan)](https://digfir-published.macmillanusa.com/mankiwscarth5e/mankiwscarth5e_ch02_3.html) (secondary textbook source)
- **Latest Fed-relevant readings (FRED):**
  - PCE price index, Aug 2026: **3.4% y/y** (131.579 vs 127.229).
  - Core PCE, Aug 2026: **3.0% y/y**.
  - PCE inflation Dec 2025: 2.8% y/y.
  - Source: [FRED PCEPI](https://fred.stlouisfed.org/series/PCEPI); [FRED PCEPILFE](https://fred.stlouisfed.org/series/PCEPILFE)
- **GDP deflator:** Q2 2026 was up **4.0% y/y**. Annual-average deflator inflation was 7.2% (2022), 3.8% (2023), 2.6% (2024) and 2.6% (2025). — [FRED GDPDEF](https://fred.stlouisfed.org/series/GDPDEF)

### Inferences
- The slide's "2% goal" is correct. Two framework points are testable:
  - (a) The target is on **PCE**, not CPI.
  - (b) The 2020 FAIT "make-up" approach was **retired in Aug 2025**, so the target is no longer described as an average.
- Using annual averages, CPI-U inflation exceeded PCE inflation in 2022 (8.0 vs about 6.5), which illustrates the formula and weight effects. PCE annual average for 2022 is not shown above; the gap is illustrative.

### Gaps
- I did not fetch the BEA's own PCE methodology page or the Fed's February 2000 Monetary Policy Report that announced the switch to PCE. The 2000 date comes from the Cleveland Fed.
- The 2022 annual-average PCE inflation figure was not computed above. Recompute it from FRED PCEPI if it is needed.

---

## Q3. How much does the CPI overstate the cost of living? Boskin (1996) and later estimates

### Takeaway
The Boskin Commission (Dec 1996) estimated the CPI overstated cost-of-living growth by **1.1 pp a year**, broken down as 0.4 substitution, 0.6 quality and new products, and 0.1 outlet. Later estimates are smaller after BLS reforms: **Lebow & Rudd (2003) ≈ 0.9 pp** (CI 0.3–1.4), **Gordon (2000) ≈ 0.65 pp** and **Moulton (2018) ≈ 0.85 pp**. The slide's "~1%/year" is a fair rounding.

### Cited Findings
- **Boskin Commission report:** "Toward A More Accurate Measure of the Cost of Living," Dec 4, 1996. It found an upward bias of about **1.1 pp a year** in 1995–96 and about 1.3 pp before that. — [SSA archive of report](https://www.ssa.gov/history/reports/boskinrpt.html); summarized by [St. Louis Fed Regional Economist, July 1997](https://www.stlouisfed.org/publications/regional-economist/july-1997/critiquing-the-consumer-price-index)
- **Boskin vs Moulton by source (percentage points a year):** — [Brookings, Jul 25 2018](https://www.brookings.edu/articles/measuring-inflation-whats-changed-over-the-past-20-years-what-hasnt)

  | Source of bias | Boskin 1996 | Moulton 2018 |
  |---|---|---|
  | Upper-level substitution | 0.15 | 0.25 |
  | Lower-level substitution | 0.25 | 0.05 |
  | New products / quality | 0.60 | 0.37 |
  | New outlets | 0.10 | 0.08 |
  | Weighting | — | 0.10 |
  | **Total** | **1.10** | **0.85** |

- Robert Gordon, a commission member, later argued the 1995–96 bias should have been 1.2–1.3. — [St. Louis Fed](https://www.stlouisfed.org/publications/regional-economist/july-1997/critiquing-the-consumer-price-index)
- Gordon put the post-reform bias at about **0.65 pp**. — [NBER Digest, Oct 2000](https://www.nber.org/digest/oct00/recent-cpi-revisions)
- **Lebow & Rudd (JEL 41(1), 2003, pp. 159–201):** "We estimate that the CPI currently overstates the rate of change in the cost of living by about **0.9 percentage point**… with a confidence interval ranging from **0.3 to 1.4**." — [IDEAS/RePEc abstract](https://ideas.repec.org/a/aea/jeclit/v41y2003i1p159-201.html)
  - Their 2001 FEDS working-paper version gave about 0.6 pp (range 0.1–1.2), with roughly half from quality and new items. — [Fed FEDS 2001-61](https://www.federalreserve.gov/econres/feds/measurement-error-in-the-consumer-price-index-where-do-we-stand.htm)
- **Moulton's view of improvement:** BLS "substantially reduce[d]" lower-level substitution bias and quality and new-product bias, through the 1999 geometric mean and the 1998 PC quality adjustments. — [Brookings](https://www.brookings.edu/articles/measuring-inflation-whats-changed-over-the-past-20-years-what-hasnt)

### Inferences
- The **three bias sources on the slide** map onto the Boskin categories:
  - quality improvement maps to "quality change"
  - new products maps to "new products"
  - substitution bias maps to upper- and lower-level substitution
  - Outlet bias (shifting to discount stores) is a fourth category the slide omits.
- **Effect of the bias:** if measured inflation is 3.0% and the bias is 0.85 pp, true cost-of-living growth is about 2.15%. Over 20 years the bias compounds: 1.03^20 / 1.0215^20 ≈ 1.806 / 1.530 ≈ 1.18, so the CPI would overstate the price level by about 18%.
- The task brief mentions "Lebow & Rudd ~0.87." The published abstract says "about 0.9." The 0.87 may be the unrounded table total, but I did not see that table.

### Gaps
- The SSA copy of the Boskin report returned HTTP 403. The component figures (0.15/0.25/0.6/0.1) are confirmed through Brookings and the St. Louis Fed, not the primary text.
- I found no BLS estimate of bias later than Moulton's 2018 figure.

---

## Q4. Latest CPI-U levels and inflation rates (2015 → September 2026)

### Takeaway
CPI-U annual averages are 2015 = 237.017, 2020 = 258.811, 2021 = 270.970, 2022 = 292.655, 2023 = 304.702, 2024 = 313.689 and 2025 = 321.943 (11-month average). Inflation peaked at **9.1% in June 2022**, fell to about 2.3–3.0% through 2025, then **rose again in 2026**, reaching **3.7% y/y in September 2026** (core 2.6%).

### Cited Findings
- **CPI-U annual averages (NSA, 1982–84=100) and annual-average inflation:** computed from [FRED CPIAUCNS (BLS series CUUR0000SA0)](https://fred.stlouisfed.org/series/CPIAUCNS)

  | Year | Annual avg CPI-U | Inflation (annual avg) | Dec/Dec |
  |---|---|---|---|
  | 2012 | 229.594 | — | — |
  | 2015 | 237.017 | 0.1% | — |
  | 2019 | 255.657 | 1.8% | — |
  | 2020 | 258.811 | 1.2% | 1.4% |
  | 2021 | 270.970 | 4.7% | 7.0% |
  | 2022 | 292.655 | **8.0%** | 6.5% |
  | 2023 | 304.702 | 4.1% | 3.4% |
  | 2024 | 313.689 | 2.9% | 2.9% |
  | 2025 | 321.943* | 2.6% | 2.7% |

  \*The 2025 annual average excludes October, which BLS did not collect. — [BLS shutdown FAQ](https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi-faq.htm)
- **2021–22 surge, 12-month CPI-U change (NSA):** — [FRED CPIAUCNS](https://fred.stlouisfed.org/series/CPIAUCNS)
  - Apr 2021: 4.2%
  - Jun 2021: 5.4%
  - Dec 2021: 7.0%
  - Mar 2022: 8.5%
  - **Jun 2022: 9.1%** (296.311 vs 271.696), the peak
  - Dec 2022: 6.5%
  - Jun 2023: 3.0%
- **2025 path, 12-month change:** — [FRED CPIAUCNS](https://fred.stlouisfed.org/series/CPIAUCNS)
  - Jan 3.0%
  - Apr 2.3%
  - Sep 3.0%
  - Oct not published
  - Nov 2.7%
  - Dec 2.7%
- **2026 path, 12-month change:** — [FRED CPIAUCNS](https://fred.stlouisfed.org/series/CPIAUCNS)
  - Jan 2.4%
  - Feb 2.4%
  - Mar 3.3%
  - Apr 3.8%
  - May 4.2%
  - Jun 3.5%
  - Jul 3.4%
  - Aug 3.4%
  - **Sep 3.7%**
- **Large seasonally adjusted monthly moves in 2026:**
  - Mar: +0.9%
  - Jun: −0.4%
  - Sep: +0.6%
  - Source: [FRED CPIAUCSL](https://fred.stlouisfed.org/series/CPIAUCSL)
- **September 2026 CPI** (released Oct 14, 2026, 8:30 a.m. ET):
  - All items rose **0.6% SA** on the month and **3.7%** over 12 months.
  - Core (less food and energy) was up **2.6%** over 12 months.
  - Index level **336.940**.
  - The October 2026 CPI is scheduled for **Nov 10, 2026**.
  - Source: [BLS CPI news release](https://www.bls.gov/news.release/cpi.nr0.htm)
- **Other indexes, Sept 2026 y/y:**
  - CPI-W (330.654): **3.9%**. — [FRED CWUR0000SA0](https://fred.stlouisfed.org/series/CWUR0000SA0)
  - C-CPI-U (186.755, preliminary): **3.5%**. — [FRED SUUR0000SA0](https://fred.stlouisfed.org/series/SUUR0000SA0)
- **Annual-average inflation by index:**

  | Index | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|
  | CPI-U | 8.0 | 4.1 | 2.9 | 2.6 |
  | CPI-W | 8.5 | 3.8 | 2.9 | 2.5 |
  | C-CPI-U | 7.7 | 3.9 | 2.6 | 2.5 |
  | Core CPI | 6.2 | 4.8 | 3.4 | 2.8 |

  Source: [FRED](https://fred.stlouisfed.org/series/SUUR0000SA0); recent C-CPI-U values are subject to revision.

### Inferences
- In 2026 headline CPI inflation (3.7%) is well above core (2.6%), which suggests food and/or energy are driving the rise. I did not verify the cause.
- Inflation is again above the Fed's 2% goal on both CPI and PCE (3.4% in August).
- For converting slide examples into "today's dollars," use 2025 = 321.943 for the latest full-year comparison (with the October caveat) or Sept 2026 = 336.940 for the latest month.

### Gaps
- I did not research what drove the 2026 re-acceleration (e.g., energy, tariffs). Do not attribute a cause without checking the BLS release text.
- I did not cross-check FRED's 11-month 2025 average (321.943) against a BLS-published annual-average table, because the BLS data server returned 403 and the API quota was exhausted. It should match, since it uses the same 11 published values.

---

## Q5. Hyperinflation: definition and episodes (Germany, Zimbabwe, Venezuela)

### Takeaway
Under Cagan's (1956) convention, hyperinflation begins when monthly inflation exceeds **50%**, which is about **12,875% a year**. Germany peaked at **29,500% per month (Oct 1923)**, Zimbabwe at about **79.6 billion % per month (mid-Nov 2008)**, and Hungary (1946) holds the record. Venezuela's central bank reported **475% inflation for 2025**. That is very high but on average below the 50%-per-month line.

### Cited Findings
- **Cagan's definition:** hyperinflation is "a period during which inflation exceeds 50% per month." It ends when the monthly rate falls below 50% and stays there for at least a year. 50% per month equals 12,874.63% a year. — [Wikipedia: Hyperinflation](https://en.wikipedia.org/wiki/Hyperinflation); [BSI Economics on Cagan](https://bsi-economics.org/the-dynamics-of-hyperinflation-explanations-in-light-of-cagans-seminal-contribution/) (secondary sources quoting Cagan)
- **Hanke-Krus Hyperinflation Table (Cato WP no. 8, 2012; Routledge 2013):** — [Hanke-Krus table PDF](https://www.bcci.bg/resources/files/hanke-krus-hyperinflation-table.pdf); [Cato](https://www.cato.org/research/world-inflation-and-hyperinflation-table)

  | Episode | Start | End | Peak month | Peak monthly rate | Daily equivalent | Prices double every | Price index used |
  |---|---|---|---|---|---|---|---|
  | **Hungary** | Aug 1945 | Jul 1946 | Jul 1946 | **4.19 × 10¹⁶%** | 207% | 15.0 hours | — |
  | **Zimbabwe** | Mar 2007 | mid-Nov 2008 | mid-Nov 2008 | **7.96 × 10¹⁰%** | 98.0% | 24.7 hours | Implied exchange rate (from Old Mutual stock prices) |
  | **Germany** | Aug 1922 | Dec 1923 | Oct 1923 | **29,500%** | 20.9% | **3.70 days** | Wholesale prices |

  - Episodes separated by 12 or more months below 50% count as separate hyperinflations.
- **Venezuela:**
  - The central bank reported **475%** inflation for 2025, the highest in the world, after not publishing figures since October 2024. — [The Daily Star (AFP)](https://www.thedailystar.net/business/global-economy/news/venezuela-inflation-hit-475-2025-the-worlds-highest-level-4122636)
  - The IMF WEO had projected 269.9% for 2025 and **682.1% for 2026**. — [Bloomberg Línea](https://www.bloomberglinea.com/latinoamerica/venezuela/fmi-proyecta-inflacion-de-682-en-venezuela-en-2026-ademas-de-contraccion-en-su-economia/)
  - Press reports cite 2026 central bank data of about 52% cumulative for Jan–Feb 2026 and about 90% year-to-date in a later report. These figures are disputed and data are scarce.

### Inferences
- **Arithmetic checks (all computed):**
  - 1.5¹² − 1 = 128.75, i.e., 12,874.6% a year.
  - Germany: 296^(1/30) − 1 ≈ 20.9% a day (the table uses 30-day months).
  - Germany doubling time: ln 2 / ln 1.209 ≈ 3.7 days.
  - Venezuela 2025: 475% a year means 5.75^(1/12) − 1 ≈ **15.7% a month on average**, which is not Cagan hyperinflation on an annual-average basis.
- The slide's "Germany 1922–23" matches Hanke-Krus (Aug 1922 – Dec 1923).

### Gaps
- I did not verify Venezuela's 2016–2020 hyperinflation peak (start, end and peak monthly rate), for example from the updated Hanke-Krus table or the central bank's 2018 annual figure.
- I did not access Cagan's 1956 text directly.

---

## Q6. Costs of inflation: menu costs, shoe-leather costs, redistribution and the S&L crisis

### Takeaway
Expected inflation imposes **menu costs** and **shoe-leather costs**. In supermarkets, measured menu costs are about 0.7% of revenue. Unexpected inflation **redistributes wealth from lenders to borrowers** and confuses price signals. The S&L crisis is the textbook case: S&Ls funded long-term fixed-rate mortgages with short-term deposits and became insolvent when rates and inflation surged around 1979–82. The direct cost to taxpayers was about **$124B**.

### Cited Findings
- **Menu costs, Levy, Bergen, Dutta & Venable (QJE 112(3), 1997, pp. 791–824/825):**
  - Five multistore U.S. supermarket chains spent about **$105,887 per store per year** changing prices.
  - That equals **0.70% of revenues**, **35.2% of net margins** and **$0.52 per price change**.
  - The chain subject to item-pricing laws changed prices about 2.5 times less often.
  - Source: [IDEAS/RePEc](https://ideas.repec.org/a/oup/qjecon/v112y1997i3p791-824..html); [author PDF](https://econ.biu.ac.il/sites/econ/files/shared/people/LevyDaniel/qje.pdf)
  - Note: Wikipedia gives 32.5% of net margins; the primary abstract gives 35.2%.
- **Mankiw (1985), "Small Menu Costs and Large Business Cycles: A Macroeconomic Model of Monopoly," QJE 100(2), May 1985, pp. 529–538:**
  - In a static monopoly model, a firm that pays a small cost to change its price may rationally leave the price unchanged.
  - The resulting private choice is not socially optimal, so small menu costs can produce large welfare effects.
  - Source: [Harvard PDF](https://scholar.harvard.edu/sites/scholar.harvard.edu/files/mankiw/files/small_menu_costs.pdf)
- **Shoe-leather costs:** the time and effort spent reducing cash holdings when inflation erodes money's value (named for extra trips to the bank). They are small at 2–3% inflation and grow with inflation. — [Ryan O'Connell Finance explainer](https://ryanoconnellfinance.com/costs-of-inflation/) (weak, educational source)
- **S&L crisis mechanism and cost:**
  - "S&Ls used short-term passbook savings to fund long-term, fixed-rate home mortgages."
  - Regulation Q "perpetuated S&L maturity mismatching."
  - After Volcker's October 1979 policy shift, "between June 1979 and March 1980 short-term interest rates rose by more than six percentage points." In 1981–82 the average S&L interest spread was **negative (≈ −1.0% and −0.7%)**.
  - In mid-1982 the whole industry had **negative net worth of about $100B** (≈15% of liabilities) at market value.
  - **Direct taxpayer cost at end-2004: $124 billion.** Total FSLIC bailout costs "may eventually exceed $160 billion."
  - Source: [Econlib, Savings and Loan Crisis](https://www.econlib.org/library/Enc/SavingsandLoanCrisis.html)
- FSLIC and the RTC closed **1,043 institutions with $519B in assets**: 296 by FSLIC and 747 by the RTC. — [Curry & Shibut (2000), FDIC Banking Review, via Yale YPFS](https://elischolar.library.yale.edu/ypfs-documents/11175) (figures from search summary of the paper)
- A GAO-based estimate in an FDIC history puts the total direct and indirect cost at **$160.1B**. — [FDIC History of the Eighties, ch. 4](https://www-s.fdic.gov/resources/publications/history-eighties/volume-1/history-80s-volume-1-part1-04.pdf) (figure from search summary)
- **Inflation and mortgage rates in that era:**
  - CPI-U annual-average inflation: **11.3% (1979), 13.5% (1980), 10.3% (1981)**. — [FRED CPIAUCNS](https://fred.stlouisfed.org/series/CPIAUCNS)
  - Freddie Mac's 30-year mortgage rate peaked at **18.63% (Oct 9, 1981)**. The series begins April 1971 at 7.33%. — [FRED MORTGAGE30US](https://fred.stlouisfed.org/series/MORTGAGE30US)
  - The latest reading is 7.40% (Oct 8, 2026).

### Inferences
- Worked S&L example: a 1960s-vintage mortgage at 5% held during 1980's 13.5% inflation earned an approximate real return of 5 − 13.5 = −8.5%. The exact figure is 1.05/1.1355 − 1 = **−7.5%**. Meanwhile, deposit rates had to rise toward market rates, producing negative spreads.
- **Expected vs unexpected inflation (exam distinction):**
  - Expected inflation is built into nominal interest rates (the Fisher effect), so it does not redistribute.
  - Only the *surprise* component transfers wealth between lenders and borrowers.
  - Expected inflation still causes menu and shoe-leather costs.
- **Quinoa example:** when all prices rise unexpectedly, a quinoa farmer seeing a higher price for quinoa cannot tell whether *relative* demand for quinoa rose or the general price level rose. The farmer may overproduce, which is misallocation from confused price signals. The interpretation is consistent with the slide; I did not see Stevenson & Wolfers' own text.

### Gaps
- I could not verify the slide's "1960s 5% 30-year mortgages." FRED's PMMS series begins in 1971 (7.33%), and I did not retrieve 1960s contract-rate data, such as the FHFB series.
- I could not open the Curry & Shibut PDF directly (FDIC redirect and proxy error). The $153B total from the brief and the 1,043/$519B figures rely on search summaries.
- I found no Federal Reserve primary source defining shoe-leather costs.

---

## Q7. Money illusion, nominal wage rigidity, and the "inflation fallacy" (Shiller)

### Takeaway
Money illusion means people judge by nominal rather than real values. Shafir, Diamond & Tversky (1997) showed that people recognize real values when asked about economics, yet judge happiness, fairness and job retention nominally. Many workers' wages are sticky at zero nominal change (about 13–14% of job-stayers in 2016–19). Shiller's surveys find that the public dislikes inflation mainly because they believe wages don't keep up. Stevenson & Wolfers (Ch. 12) call this belief the **"inflation fallacy"**: wages also rise with inflation over time, so prices rising does not by itself mean a fall in living standards.

### Cited Findings
- **Shafir, Diamond & Tversky, "Money Illusion," QJE 112(2), 1997, pp. 341–374:** people evaluate in both nominal and real terms, and the mix produces a bias toward nominal evaluation. — [IDEAS/RePEc](https://ideas.repec.org/a/oup/qjecon/v112y1997i2p341-374..html)
- **Ann vs Barbara vignette:**
  - Both start at $30,000.
  - Ann gets a **2% raise with 0% inflation** (+$600). Barbara gets a **5% raise with 4% inflation** (+$1,500).
  - About **71%** said Ann was better off "in economic terms."
  - Most said **Barbara was happier**, and Ann was judged more likely to leave for another job.
  - Source: [Avantis Investors](https://www.avantisinvestors.com/avantis-insights/tripped-up-by-the-money-illusion/); [ScienceBlogs (Lehrer)](https://scienceblogs.com/cortex/2009/04/03/money-illusion)
  - A 2021 MTurk replication (n = 604) reproduced Problems 1–4. — [IDEAS (J. Econ. Psychology 2021)](https://ideas.repec.org/a/eee/joepsy/v83y2021ics0167487020301069.html)
- **Shiller, "Why Do People Dislike Inflation?":** NBER WP 5539, April 1996.
  - Surveyed 677 people in the U.S., Germany and Brazil.
  - Non-economists' biggest concern is that inflation "lowers people's standard of living." Many hold a sticky-wage view in which pay does not respond to inflationary shocks, often blamed on people or institutions "acting badly."
  - Other perceived costs: exploitation, political instability, lower morale and lost national prestige.
  - The largest gaps were between economists and non-economists.
  - Source: [NBER w5539](https://www.nber.org/papers/w5539)
- **Nominal wage rigidity:**
  - The SF Fed Wage Rigidity Meter measures, from CPS data, the share of job-stayers reporting **zero** year-over-year wage change.
  - It was about **13.4% in Q4 2019** and **14.4% in Q3 2018**.
  - The share rises after recessions and declines slowly.
  - Source: [SF Fed Wage Rigidity Meter (FRASER archive, Q4 2019)](https://fraser.stlouisfed.org/title/wage-rigidity-meter-6771/fourth-quarter-2019-622141/fulltext); [Kansas City Fed bulletin 2018](https://www.kansascityfed.org/research/economic-bulletin/nominal-wage-rigidities-future-path-wage-growth-2018)

### Inferences
- The real raises in the vignette are Ann +2.0% and Barbara 1.05/1.04 − 1 = **+0.96%** (≈1% approximate). This is a classic exam trap.
- **Why mild inflation can help with nominal wage rigidity:** with 2% inflation, a firm can cut a real wage by 2% just by holding the nominal wage flat. That supports the case for a positive (2%) target rather than zero. This is an inference consistent with the wage-rigidity evidence; the Fed statement does not say it.
- **Inflation fallacy** (Stevenson & Wolfers' term, per the slides): the public treats price rises as pure losses. In general equilibrium, nominal incomes rise too, so the welfare cost comes from *unexpected* redistribution and frictions, not from the price level per se.

### Gaps
- I did not retrieve the original Shafir et al. tables, so the exact respondent percentages for the "happier" and "leave the job" questions are unverified. The 71% figure comes from a secondary summary.
- I found no current (2024–26) Wage Rigidity Meter readings.
- I did not confirm the exact 1997 publication details of Shiller's chapter.

---

## Q8. Calculation methods with worked examples (arithmetic verified)

### Takeaway
Almost every exam calculation is one of six formulas:
- percent change: (new − old)/old
- index: cost_t / cost_base × 100
- inflation from an index: (I₂ − I₁)/I₁
- dollar conversion: $_target = $_original × (CPI_target / CPI_original)
- real growth: (1 + g_nominal)/(1 + π) − 1
- Fisher: (1 + i) = (1 + r)(1 + π), approximately r ≈ i − π

All worked examples below were recomputed in Python. CPI inputs come from [FRED CPIAUCNS](https://fred.stlouisfed.org/series/CPIAUCNS) unless noted.

### Cited Findings

#### Method summary
1. **Cost of basket:** Σ (quantity_i × price_i) using a *fixed* base-period basket.
2. **Price index:** (cost of basket in year t / cost of the same basket in base year) × 100. The base year's index = 100.
3. **Inflation rate:** (Index_t − Index_{t−1}) / Index_{t−1} × 100.
   - The index level minus 100 is the inflation rate *only* when the comparison is with the base year.
   - Percent change differs from percentage-point change.
4. **Converting dollars (Stevenson & Wolfers' inflation-adjustment formula):**
   - Value in year-T dollars = value in year-t dollars × (CPI_T / CPI_t).
   - Going backward uses the same formula: e.g., to express today's $ in 2015 dollars, multiply by CPI_2015 / CPI_today.
   - "Real value in base-year (e.g., 2012) dollars" = nominal × (CPI_2012 / CPI_t).
   - With the official 1982–84 base: real = nominal / CPI × 100.
5. **Real growth:** exact (1 + g_N)/(1 + π) − 1; approximately g_N − π. Equivalently, deflate each year to constant dollars, then take the percent change.
6. **Fisher equation:** exact (1 + i) = (1 + r)(1 + π), so r = (1 + i)/(1 + π) − 1; approximately r ≈ i − π.
   - The ex-ante real rate uses expected π. The ex-post (realized) real rate uses actual π.
   - The approximation error grows when rates are large.
7. **Real wage change:** (1 + nominal raise)/(1 + π) − 1.
8. **Purchasing power of a fixed nominal payment n years ahead:** P / (1 + π)ⁿ.
9. **Doubling time (rule of 70):** years ≈ 70 / π(%). Exact: ln 2 / ln(1 + π).
10. **Compounding monthly to annual:** (1 + m)¹² − 1. Annual to average monthly: (1 + a)^(1/12) − 1.

#### Ex. 1: Whiskers the cat (basket cost → inflation rate)
- 2021 basket $796.70, 2022 basket $820.00.
- Inflation = (820 − 796.70)/796.70 = 23.30/796.70 = **2.92% ≈ 2.9%** ✔ (matches slide).
- Index with 2021 = 100: 2022 index = 820/796.70 × 100 = **102.9**.

#### Ex. 2: Inflation from official index values
- 2021 → 2022 annual average: (292.655 − 270.970)/270.970 = **8.0%**.
- June 2021 → June 2022: (296.311 − 271.696)/271.696 = **9.06% ≈ 9.1%** (peak).
- Sept 2025 → Sept 2026: (336.940 − 324.800)/324.800 = **3.74% ≈ 3.7%**. Matches the [BLS release](https://www.bls.gov/news.release/cpi.nr0.htm).
- Rebasing: the 2022 CPI expressed with 2021 = 100 is 292.655/270.970 × 100 = **108.0**.

#### Ex. 3: Force Awakens (past $ → later $)
- Slide inputs: $937M × (271.0/237.0) = 937 × 1.14346 = **$1,071.4M ≈ $1,071M** in 2021 dollars ✔.
- With precise inputs ($936.66M; CPI 270.970/237.017): **$1,070.8M**. The gross is from [Box Office Mojo](https://www.boxofficemojo.com/title/tt2488496/).
- **Updated:**
  - In 2025 dollars: 936.66 × 321.943/237.017 = **$1,272.3M**.
  - In Sept-2026 dollars: 936.66 × 336.940/237.017 = **$1,331.5M**.

#### Ex. 4: Target real revenue in 2012 dollars and real growth
- 2020: $78.1B × (229.6/258.8) = **$69.29B ≈ $69B**.
- 2021: $93.5B × (229.6/271.0) = **$79.22B ≈ $79B**.
- Real growth = 79.22/69.29 − 1 = **14.3% ≈ 14%** ✔.
- Cross-checks:
  - Nominal growth is 93.5/78.1 − 1 = 19.7%.
  - Inflation 2020→2021 is 271.0/258.8 − 1 = 4.7%.
  - Exact real growth: 1.1972/1.0471 − 1 = 14.3%.
  - The **approximation** 19.7 − 4.7 = 15.0% overstates it by 0.7 pp, because rates are not small.
  - The base year does not change real growth: deflating to 2021 dollars gives the same 14.3%.
- Revenue figures and fiscal-year caveat: [Target 8-K](https://www.sec.gov/Archives/edgar/data/27419/000002741921000007/a2020q4ex-99.htm).

#### Ex. 5: Nominal vs real interest rate (slide example and the exact Fisher equation)
- 5% nominal, 3% inflation: approximate real rate 2%. Exact: 1.05/1.03 − 1 = **1.94%**.

#### Ex. 6: Who gains from *unexpected* inflation?
- Setup: a $10,000 one-year loan at 6% nominal, with **2% expected** inflation; actual inflation turns out to be **5%**.
- Expected real rate: ≈4% (exact 1.06/1.02 − 1 = **3.92%**).
- Realized real rate: ≈1% (exact 1.06/1.05 − 1 = **0.95%**).
- The borrower repays $10,600 either way. In beginning-of-year purchasing power, that is:
  - $10,600/1.02 = **$10,392.16** expected
  - $10,600/1.05 = **$10,095.24** actual
- About **$296.92** of purchasing power shifts from lender to borrower.
- Reverse case: if inflation comes in *below* expectations, the lender gains. Unexpected disinflation or deflation raises the real burden of debt.

#### Ex. 7: Fixed $1,400 mortgage payment
- Real value of the payment in 10 years:
  - at 2% inflation: 1,400/1.02¹⁰ = **$1,148.49**
  - at 5%: 1,400/1.05¹⁰ = **$859.48**
- Higher-than-expected inflation shrinks the borrower's real burden and the lender's real receipts.

#### Ex. 8: S&L crisis in numbers
- A 5% fixed mortgage in 1980, when CPI inflation was 13.5% (82.408 vs 72.575):
  - approximate real return: 5 − 13.5 = −8.5%
  - exact: 1.05/1.1355 − 1 = **−7.5%**
- This is a good illustration that the subtraction rule is inaccurate at high inflation.

#### Ex. 9: Real wage / money illusion
- Barbara (5% raise, 4% inflation): real raise 1.05/1.04 − 1 = **0.96%**, less than Ann's 2% raise at 0% inflation.
- Current-data version: a 4% raise ($50,000 → $52,000) against Sept-2026 inflation of 3.74%:
  - exact real raise: 1.04/1.0374 − 1 = **+0.25%**
  - approximation: 4 − 3.74 = +0.26%

#### Ex. 10: Comparing prices across decades (iPhone, Coke)
- **iPhone nominal comparison:** 999/599 − 1 = **66.8%** above the 8GB original; 999/499 − 1 = **100.2%** above the 4GB model. Prices: [Apple 2007](https://www.apple.com/newsroom/2007/01/09Apple-Reinvents-the-Phone-with-iPhone/).
- **iPhone real comparison:**
  - June 2007 CPI was 208.352; the 2022 average was 292.655.
  - $599 × 292.655/208.352 = **$841.37** in 2022 dollars.
  - So the $999 phone is only **18.7%** more expensive in real terms, even before any quality adjustment.
- **Nickel Coke:** 1959 CPI averaged 29.15. $0.05 × 321.943/29.15 = **$0.55** in 2025 dollars, or $0.58 in Sept-2026 dollars.
- **Coca-Cola's 1920 losses:** 1920 CPI was 20.04. $29,000 × 321.943/20.04 ≈ **$466,000 per day** in 2025 dollars. Levy & Young report $213,235 in 1992 prices.

#### Ex. 11: Going backward and doubling times
- $100 in Sept-2026 dollars = 100 × 237.017/336.940 = **$70.34 in 2015 dollars**.
- Rule of 70:
  - At 3.7% inflation the price level doubles in ≈70/3.7 = **18.9 years** (exact 19.1).
  - At 2%, it doubles in ≈**35 years**.
- Hyperinflation:
  - 50% per month gives (1.5)¹² − 1 = **12,875%** a year.
  - Germany's 29,500% per month gives ≈20.9% a day, so prices doubled roughly every 3.7 days. See the [Hanke-Krus table](https://www.bcci.bg/resources/files/hanke-krus-hyperinflation-table.pdf).

#### Ex. 12: Quantifying CPI bias
- If measured CPI inflation is 3.0% and the bias is 0.85 pp ([Moulton via Brookings](https://www.brookings.edu/articles/measuring-inflation-whats-changed-over-the-past-20-years-what-hasnt)), true cost-of-living inflation is ≈2.15%.
- Over 20 years the CPI would overstate the price-level rise by 1.03²⁰/1.0215²⁰ − 1 ≈ **18%**.
- Implication: indexing benefits or wages to the CPI over-compensates.

### Inferences
- **Common exam traps:**
  1. Subtracting index levels instead of computing a percent change.
  2. Inverting the CPI ratio when converting dollars. Check: converting to a *later* year with higher CPI must *increase* the dollar figure.
  3. Treating r ≈ i − π as exact when rates are large.
  4. Confusing expected with actual inflation in "who gains" questions. The *surprise* is what redistributes.
  5. Mixing fiscal and calendar years (the Target data).
  6. Assuming deflation is good for debtors. It raises their real burden.
  7. Treating a relative price change (e.g., quinoa) as inflation.
  8. Forgetting that a fixed basket (Laspeyres) overstates cost-of-living increases because of substitution, quality and new goods.
- When asked "in today's dollars," state the CPI used: 2025 annual average 321.943 or Sept 2026 336.940. Answers differ by about 4.7%.

### Gaps
- I have not checked any example against Stevenson & Wolfers' own end-of-chapter problems; publisher test banks and answer keys were deliberately not sought.
- Exam questions may use rounded CPI values (e.g., 271 vs 270.970). Small differences, such as $1,071.4M vs $1,070.8M, come from rounding only.
