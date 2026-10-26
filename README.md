# RFS file prompt

Reusable prompt, document checklist and Python scripts for preparing Restated Financial
Statements (RFS) under SEBI ICDR Regulations (Indian GAAP, Schedule III Division I) from
Tally trial balances, in the "TB -> Notes (SUMIF on Masters) -> BS / P&L -> other annexures" format.

## Contents

| File | Purpose |
|---|---|
| `RFS_Prompt_and_Document_Checklist.md` | Copy-paste prompt (Part A) and list of documents required (Part B) |
| `scripts/parse_tb.py` | Reads a Tally TB export; signs balances from the Dr/Cr format; flags repeated ledgers |
| `scripts/tree.py` | Rebuilds the group/ledger hierarchy using totals, so only ledgers are counted |
| `scripts/extract.py` | Runs the above for each year and writes `work/tb_all.json` |
| `scripts/classify.py` | Ledger -> Schedule III mapping rules (edit for each company) |
| `scripts/build_rfs.py` | Builds the RFS workbook (TB sheets with Masters, Notes, BS_1, PL_2, CFS_3, SAP_4, SOA_5, ratios, RPT, tax shelter, etc.) |

## How to run

```
mkdir input
# put Tally TB exports in input/ as TrialBal_FY_23-24.xlsx, TrialBal_FY_24-25.xlsx, TrialBal_FY_25-26.xlsx
python3 scripts/extract.py
python3 scripts/build_rfs.py output.xlsx
```
Then open the file in Excel / LibreOffice to recalculate.

## Adapting for a new company

`build_rfs.py` was written for one engagement. Before reuse, update:
- MasterData values (company name, CIN, address, directors, dates, closing stock, tax rate, auditor details)
- `classify.py` rules and the `SPECIAL` ledger map (director loan ledgers, etc.)
- Restatement journal entries in the "Adj Entry RFS" section
- Shareholder register and ageing figures (source schedules)
- Year labels / file names if the years change

`input/`, `work/` and all Excel files are git-ignored so client data is not committed.
