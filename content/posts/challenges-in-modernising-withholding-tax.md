+++
date = 2021-09-11T23:00:00Z
slug = "BuildingaWithholdingTaxDeterminationEngine"
title = "Building a Withholding Tax Determination Engine"

+++
### I. What is withholding tax?

Withholding tax ("WHT") refers to an amount of tax withheld at source at a certain rate determined by local tax law. Typically, the rate also varies if the seller and buyer are situated in two countries and there are specific double tax treaties between the tax authorities, respectively.

WHT can be applied to different types of remuneration, such as dividend, interest, royalty, commission, fees and rentals, as well as transactions, i.e. digital transactions. The recipient (payee) could be employees, business partners, and overseas entities. Employee tax is essentially one type of WHT, but it is generally accounted for under salaries.

> WHT is not the same as VAT or other forms of indirect taxes. In some countries, VAT charged by a provider has to be withheld by the payer and paid to the tax authorities, which is not a WHT.

WHT includes both domestic withholding tax (in-country or locally) and international withholding, subject to local tax law or double tax treaties as discussed above.

### II. Challenges with withholding taxes

Like many other taxes, the data source for withholding tax can be a mixture of online and offline collection. From the account payable (AP) side, companies often receive invoices, include them in the ERP system with relevant accounting treatments, leaving withholding tax as an afterthought. 

### III. Building a withholding tax engine

I've split it into a 4 step process: 

1. Check the information available on Sales Invoices (SI), Good Receipts (GR), and Purchase Order (PO); 
2. Look through the rules per country. Each country would have negotiated separate tax treaties, so it makes sense to model the determination engine on a country basis;
3. Split the withholding tax rules into two parts, one that I could hard code, the other I may need to rely on some language model to make judgment;
4. Build an UI to host the engine