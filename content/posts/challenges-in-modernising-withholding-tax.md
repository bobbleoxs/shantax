+++
date = 2021-08-15T23:00:00Z
slug = "BuildingaWithholdingTaxDeterminationEngine"
title = "Building a Withholding Tax Determination Engine"

+++
### I. What is withholding tax?

Withholding tax ("WHT") refers to an amount of tax withheld at source at a certain rate determined by local tax law. Typically, the rate also varies if the seller and buyer are situated in two countries and there are specific double tax treaties between the tax authorities, respectively.

WHT can be applied to different types of remuneration, such as dividend, interest, royalty, commission, fees and rentals, as well as transactions, i.e. digital transactions. The recipient (payee) could be employees, business partners, and overseas entities. Employee tax is essentially one type of WHT, but it is generally accounted for under salaries.

> WHT is not the same as VAT or other forms of indirect taxes. In some countries, VAT charged by a provider has to be withheld by the payer and paid to the tax authorities, which is not a WHT.

WHT includes both domestic withholding tax (in-country or locally) and international withholding, subject to local tax law or double tax treaties as discussed above.

### II. Challenges with withholding taxes

Like many other taxes, the data source for withholding tax can be a mixture of online and offline collection. From the account payable (AP) side, companies often receive invoices, include them in the ERP system with relevant accounting treatments, leaving withholding tax as an afterthought. Major challenges I encounter in building a withholding tax engine include:

* Fragmented data sources - where sales/purchase data is detached from withholding tax posting and was only added on afterwards.
* Missing data - invoices come in different forms and types, sometimes even handwritten. There are inevitably missing fields that may be valuable information in determining the correct withholding tax rate.
* Mismatched or inconsistent data - given the varieties of invoices, the information therein is often inconsistent, resulting in bad quality data and requiring numerous edge cases to be accounted for.
* Small data size - despite being a transaction-level tax, complete, accurate and consistent data is often limited, and proving little use in creating a supervised learning model for language processing. Unsupervised learning is therefore the most appropriate method to explore first.
* Significant differences in country rules - unlike VAT or GST, countries don't always have the same tax base for withholding taxes. It is indeed a spider web of rules which requires considerations on a country by country basis.
* Double tax treaties - other than the differences in underlying country rules, each country would have also negotiated different treaty agreements on withholding tax rate per tax category (e.g. royalties, dividend, interest), adding further complexities.

### III. Building a withholding tax engine

I split the building work into a 4-step process:

1. Check and sort the data available on Sales Invoices (SI), Good Receipts (GR), and Purchase Order (PO) for one country only as a prototype;
2. Look through the rules per country. Each country would have negotiated separate tax treaties, so it makes sense to model the determination engine on a country basis;
3. Split the code for withholding tax rules into two parts: part one addresses the rules I could hard code into logic, whereas part two applies language model and unsupervised learning to make judgments based on invoice descriptions;
4. Build a UI to host the engine to allow users to interact with the determination engine

After a successful build of the prototype, the next step is to into the learning points from the initial build, make respective improvements based on user feedback and explore the possibility of scaling the prototype to other countries worldwide. This implementation process would be worthy of a separate blog post.