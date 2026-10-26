# Reusable prompt – Restated Financial Statements (RFS)

Copy the prompt below, fill the [brackets], and attach the documents listed in Part B.

---

## PART A – PROMPT

```
Prepare Restated Financial Statements (RFS) for [Company Name] for FY [YYYY-YY], FY [YYYY-YY] and FY [YYYY-YY]
[and stub period ended DD-MM-YYYY, if any], as per the latest SEBI ICDR Regulations 2018
([SME IPO – Chapter IX / Main Board]), Indian GAAP, Schedule III Division I, amounts in Rs. lakhs (2 decimals).
Generate ONE Excel file.

Attached: Tally trial balances for each year (Excel, with opening / debit / credit / closing and Dr/Cr),
audited financial statements of each year, and the supporting documents listed.
Use the attached reference RFS Excel for FORMAT ONLY – do not take any data from it.

1. TRIAL BALANCES
   - Paste each Tally TB as-is in its own sheet named "TB YYYY-YY" (keep Tally formatting).
   - Add columns: F "Group" (BS / P&L), G "Masters" (the exact note line it maps to),
     H "Net Amount" (=E or =-E so the natural balance is positive), I "In Lakhs" (=H / scale).
   - For the earliest TB also add opening Masters / Opening Net Amount / Opening In Lakhs
     (gives the opening balance sheet for cash flow and averages).
   - Tag only ledgers (not groups); mark ledgers repeated in the Tally export as "not considered".
   - Re-tag by sign: debtors with credit balance -> Advance from customers, creditors with debit
     balance -> Advance to suppliers, overdrawn bank -> Short-term borrowings, etc.

2. NOTES (Annexure VI) – linked to the TBs
   - Sheets: Notes_Equity & Reserves, Notes_Liabilities, Notes_PPE, Notes_Assets, Notes_P&L.
   - Every note line = SUMIF('TB YYYY-YY'!$G:$G, note line text, 'TB YYYY-YY'!$I:$I) for each year,
     plus restatement adjustments from "Adj Entry RFS" where applicable.
   - Balance sheet notes also show the opening balance sheet date column.
   - Include: share capital (authorised, issued, reconciliation of shares, promoters and >5% holders),
     reserves movement (opening, profit, adjustments in books, restatement adjustments, closing),
     borrowings (with terms, security, director-wise loan movement), trade payables (MSME disclosure,
     ageing), PPE movement, deferred tax, inventories, trade receivables (ageing), cash and bank,
     loans and advances, other assets/liabilities, revenue, other income (with % of PBT and nature),
     purchases, changes in inventories, employee benefits, finance costs, depreciation, other expenses
     (payment to auditors), tax expense, EPS.
   - Note numbers chain by formula (=previous note + 1).

3. BS_1 (Annexure I) and PL_2 (Annexure II) – link only to note totals. Opening balance sheet column
   shown beside the BS for cash flow purposes. Small check cell on row 1 (BS difference / PAT check).

4. Other annexures – flow only from the Notes, BS_1 and PL_2:
   CFS_3 (Annexure III, indirect method), SAP_4 (Annexure IV – background, basis of preparation,
   significant accounting policies), SOA_5 (Annexure V – reconciliation of restated profit and
   shareholders' funds with notes, material regrouping, non-adjusting items), RPT, Gratuity and
   contingencies, Tax Computation (statement of tax shelter), Accounting ratios (EPS, RONW, NAV,
   EBITDA), Analytical Ratios (Schedule III ratios with variance reasons), Capitalisation,
   Additional Disclosures (Schedule III).

5. Restatement adjustments: record as journal entries in "Adj Entry RFS" (date, particulars, Masters,
   Group, Dr, Cr, narration), with amounts linked to the TB / workings. Realign prior-period items,
   gratuity, deferred tax, MSME interest, depreciation, tax etc. to the years they relate to.

6. Source sheets: MasterData (company, CIN, scale, dates, face value, closing stock, tax rate,
   signatories, auditor details), Debtor Ageing, Creditor Ageing, Shareholder Register.

7. Style: humanised, like the reference – Times New Roman 10, "As at March 31, YYYY" headers,
   accounting number format, "Sd/-" signature blocks with auditor and directors, no AI-style
   summary/mapping/check sheets. Every figure formula-driven; only TBs and source schedules are inputs.

8. Before building, review the TBs vs audited financials and ASK me about any doubts
   (framework, adjustments, stub period, units, mismatches). After building, recalculate, confirm
   zero formula errors and nil checks (BS tally, cash flow tie, PAT and net worth reconciliation),
   and list any further data needed.
```

---

## PART B – DOCUMENTS REQUIRED

### 1. Books of account
1. Tally trial balance for each year (and stub period) – ledger-wise with opening, debit, credit and closing balances (Excel export, Dr/Cr shown).
2. Audited financial statements for each year – balance sheet, P&L, cash flow, notes, auditor's report, CARO, signed copy.
3. Audit / finalisation entries passed after the TB, if the TB is not final.
4. Closing stock for each year (inventory valuation / certificate).

### 2. Company and share capital
5. Certificate of incorporation, fresh certificate on conversion to public company, MOA / AOA.
6. MCA master data – CIN, registered office, directors / KMP with DIN, dates of appointment / cessation.
7. Register of members and shareholding pattern as at each year end (promoters, holders >5%).
8. Allotment history (dates, number of shares, premium, consideration), bonus / split / rights issues, increases in authorised capital – including any after the latest balance sheet date.

### 3. Fixed assets
9. Fixed asset register – gross block, additions with dates, deletions, accumulated depreciation, useful life / rates.
10. Depreciation as per the Income-tax Act (block-wise) for each year.
11. Details of capital work-in-progress / intangible assets under development (ageing, cost capitalised).
12. Title deeds of immovable property.

### 4. Borrowings
13. Sanction letters for all loans / OD / CC / bill discounting / channel finance – limit, security, rate, tenure, guarantees.
14. Loan repayment schedules / statements (to work out current maturities and principal repaid).
15. Monthly / quarterly stock and book-debt statements submitted to banks.
16. Confirmation of loans from directors / related parties.

### 5. Receivables, payables and other balances
17. Debtors ageing as at each year end (from due date; disputed / undisputed).
18. Creditors ageing as at each year end with MSME / non-MSME classification (Udyam details).
19. MSME interest calculation on delayed payments.
20. Balance confirmations, bad debts written off, provision for doubtful debts.
21. Fixed deposit statements (including lien / margin money), bank statements and reconciliations at each year end.

### 6. Employee benefits
22. Actuarial valuation reports for gratuity (and leave encashment) for each year – obligation, expense, assumptions, current / non-current split.
23. PF / ESI challans and returns (late payment details).

### 7. Taxation
24. Computation of total income, ITRs and tax audit reports (Form 3CD) for each year.
25. Deferred tax working.
26. Advance tax / TDS / TCS details (26AS / AIS), refunds, interest u/s 234.
27. GST returns (GSTR-1, 3B, 9 / 9C) and turnover reconciliation.
28. Income tax / GST assessment orders, demands, notices.

### 8. Related parties
29. List of related parties – KMP, relatives, entities in which KMP have significant influence, subsidiaries / associates.
30. Related-party transactions for each year – remuneration (director-wise), loans taken / repaid, rent, purchases / sales, reimbursements, guarantees, closing balances.

### 9. Contingencies and commitments
31. Bank guarantees issued, letters of credit.
32. Pending litigation, claims not acknowledged as debt, tax demands under dispute.
33. Capital commitments.

### 10. Other information
34. Board minutes / resolutions relevant to the period (borrowings, allotments, remuneration).
35. Foreign currency transactions and unhedged exposure (if any).
36. CSR applicability and spend (if applicable).
37. Segment information (if more than one segment / geography).
38. Prior-period items, errors, and changes in accounting policy identified (for restatement).
39. Audit qualifications, emphasis of matter and CARO remarks for each year.
40. Peer-reviewed auditor details – firm name, FRN, peer review certificate number, partner, membership number, UDIN, date and place of signing.
41. Issue details for the capitalisation statement (issue size / price, when finalised).
42. Reference RFS Excel (for format only).
