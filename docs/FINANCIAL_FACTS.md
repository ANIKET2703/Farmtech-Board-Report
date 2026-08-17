# FarmTech: verified financial facts (human-checked baseline)

Before building the pipeline I read every source document and recorded each figure here
with its page reference. This file is the baseline the AI extraction output was checked
against, and the source of the expected values in the unit tests
(`tests/test_metrics_engine.py`).

All amounts in EUR unless stated.

---

## Entity timeline

| Entity | Note |
|---|---|
| Ashgrove Farm Solutions Limited | Pre-IPO group (trading as FarmTech). Audited consolidated FY accounts to 30 June. |
| FarmTech Limited | Company balance sheet as at 8 Dec 2025 (scanned, pre-listing reorganisation). |
| FarmTech PLC | Listed entity. Euronext Access+ Dublin, admitted 22 Dec 2025. Ticker FRMT, ISIN IE00BFRMT001. Shares in issue: 3,022,372 (nominal EUR 0.01). |

Financial year ends 30 June. "FY25" = year ended 30 Jun 2025. "HY26" = 6 months ended 31 Dec 2025.

---

## Consolidated P&L (source: AFS FY25 p.10; HY26 PR consolidated P&L)

| Line | FY24 | FY25 | HY25 (6m to Dec-24) | HY26 (6m to Dec-25) |
|---|---|---|---|---|
| Turnover | 922,345 | 1,121,568 | 456,848 | 475,449 |
| Cost of sales | (342,826) | (252,645) | (93,264) | (86,914) |
| Gross profit | 579,519 | 868,923 | 364,484* | 388,535 |
| Distribution costs | (3,153) | (1,453) | 0 | 0 |
| Administrative expenses | (2,091,543) | (1,723,318) | (908,397) | (1,047,847) |
| Other operating income | 0 | 6,697 | 0 | 11,080 |
| Group operating loss | (1,515,177) | (849,151) | (543,913) | (648,232) |
| Other gains and losses | 427 | 0 | 0 | 0 |
| Interest payable | (64) | (2,779) | (1,388) | (1,864) |
| Loss before taxation | (1,514,814) | (851,930) | (545,301) | (650,096) |
| Tax credit/(charge) | 43,366 | 60,986 | 0 | 0 |
| Loss for period | (1,471,448) | (790,944) | (545,301) | (650,096) |

*The HY26 PR prints HY25 gross profit as 364,484, but turnover minus cost of sales is
456,848 - 93,264 = 363,584. That EUR 900 inconsistency is in the published source.
Values are recorded exactly as printed and the difference is flagged as a data-quality
finding in the app.

Margins (computed): gross margin FY24 62.8%, FY25 77.5%, HY25 79.8%, HY26 81.7%.

## Consolidated balance sheet (AFS p.11; HY26 PR)

| Line | 30 Jun 24 | 30 Jun 25 | 31 Dec 24 | 31 Dec 25 |
|---|---|---|---|---|
| Goodwill | - | - | 0 | 897,197 |
| Development costs (intangible) | - | - | 0 | 321,285 |
| Tangible assets | 87,623 | 65,376 | 87,586 | 56,288 |
| Debtors | 234,138 | 164,824 | 282,941 | 252,120 |
| Cash | 569,016 | 187,781 | 96,991 | 985,155 |
| Creditors < 1 yr | (120,705) | (326,754) | (120,749) | (518,721) |
| Contingent consideration | - | - | - | (1,139,000) |
| Creditors > 1 yr | 0 | (112,098) | (114,527) | (102,475) |
| Net assets/(liabilities) | 770,072 | (20,871) | 232,243* | 751,849 |
| Share capital | 193 | 193 | 193 | 33,500 |
| Share premium | 1,138,949 | 1,138,949 | 1,138,952 | 402,000 |
| Retained earnings | (369,070) | (1,160,013) | (906,902) | 316,349 |

*The HY26 PR labels the comparatives "as at 31-Dec-24". The post-listing capital
structure (share capital 33,500, premium 402,000, positive retained earnings 316,349)
reflects the reorganisation into FarmTech. Flagged in the app rather than
force-reconciled.

## Consolidated cash flow (AFS p.15; HY26 PR)

| Line | FY24 | FY25 | HY25 | HY26 |
|---|---|---|---|---|
| Net cash used in operating | (1,563,374) | (502,259) | (603,243) | (549,790) |
| Net cash used in investing | (44,852) | (4,624) | 0 | (11,390) |
| Net cash from financing | (5,154) | 125,648 | 131,218 | 1,358,554 |
| Net movement | (1,613,380) | (381,235) | (472,025) | 797,374 |
| Opening cash | 2,182,396 | 569,016 | 569,016 | 187,781 |
| Closing cash | 569,016 | 187,781 | 96,991 | 985,155 |

FY25 detail: depreciation 27,311; interest paid 2,779; tax repaid 38,094;
working-capital movement +284,706 (debtors +92,207, creditors +192,499); new long-term
loan 134,000; repayment of short-term loan (8,352).
HY26 detail: depreciation 13,419; working capital +86,884; loan repayments (167,282);
share issue 1,525,835.

## Debt (AFS notes 12-13; HY26 PR)

- FY25 bank loans total 125,648: under 1yr 13,550; 1-2yr 14,070; 2-5yr 46,230; over 5yr 51,798. New EUR 134,000 SBCI-backed term loan drawn FY25.
- Directors' current accounts at FY25: 178,237 (Fiona Dolan 67,000; Ronan Casey 111,237).
- HY26: bank debt stated 102.5k (creditors > 1yr 102,475).

## Employees and directors (AFS notes 6, 16)

- Average employees: FY24 21, FY25 19.
- Directors' remuneration FY25: 286,070 + pension 13,985 (FY24: 419,404 + 28,636).

## KPIs and commercial (Information Document section 7.3, p.11, p.26; HY26 PR)

- FY25 customers: 136 accounts = 41 Enterprise + 88 Independent + 7 R&D.
- FY25 channel revenue mix: Enterprise 62%, Independent 11%, R&D 27%.
- FY25 geography: Ireland ~71%, ex-Ireland ~29% (11 jurisdictions active).
- FY25 avg Enterprise ACV: Soil 16,494; Terrain 28,842; ERA 78,926.
- R&D expenditure: ~17% of revenue FY25, ~22% FY24.
- HY26: ~938k deals closed across 19 enterprise customers; ~670k open pipeline; 10 deals of roughly 570k closed Nov-Dec 2025.

## FarmTech 2030 strategy targets

- Revenue CAGR of at least 50% (FY26-FY30, base FY25 = 1,121,568).
- EBITDA positive during FY2028.
- More than 100 Enterprise customers by FY2030; Enterprise ACV above 67,000.
- Ireland below 50% of revenue by end FY2030.

## Corporate events

- Terravue Ltd (UK geospatial AI) acquired HY26: goodwill 897,197, no cash consideration, contingent consideration 1,139,000 (performance-linked). Founders joined as Head of Research / Head of Software Engineering.
- EUR 1.5m equity raise completed (1,525,835 per cash flow).
- Direct listing, Euronext Access+ Dublin, 22 Dec 2025 (sponsor: Kepler Capital Markets).
- Leadership transition PR, 24 Jun 2026.
- FY2028 EBITDA-positive guidance; FY26 outlook "in line with expectations", H1 seasonally weaker.

## Market data and admission (Listing PR p.3; Euronext exports in data/market/)

- Shares in issue at Admission: 3,022,372 ordinary shares of EUR 0.01 nominal (unchanged per the AGM Circular, Jun 2026).
- Share admission price EUR 6.869; market capitalisation at Admission disclosed as EUR 20,761,000 (rounded; 3,022,372 x 6.869 = 20,760,673).
- Closing price 3 Jul 2026: EUR 8.24; 52-week range 8.04-8.24; 52-week change +19.96% (ties to 8.24 / 6.869 - 1). Zero reported trading volume in the sampled window.
- ISIN IE00BFRMT001 · ticker FRMT · Euronext Access+ Dublin.

## Known data-quality findings (surfaced in the app)

1. HY25 gross profit line (364,484) vs turnover minus COS (363,584): EUR 900 inconsistency in the source PR.
2. HY26 PR goodwill: 897,197 on the balance sheet vs 897,127 in the notes (EUR 70 discrepancy).
3. HY26 PR balance-sheet comparatives labelled 31-Dec-24 show the pre-listing capital structure; post-listing equity was restated in the reorganisation.
4. AFS accounts and the FarmTech Limited balance sheet are scanned images with no text layer, so extraction had to be vision-based.
5. No monthly data is published in any filing, so MoM views cannot be built from source. Omitted rather than estimated.
