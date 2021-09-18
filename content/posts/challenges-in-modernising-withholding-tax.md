+++
date = 2021-06-21T23:00:00Z
slug = "BuildingaWithholdingTaxDeterminationEngine"
title = "Building a Withholding Tax Determination Engine"

+++
### **I. What is withholding tax?**

Withholding tax ("WHT") refers to an amount of tax withheld at source at a certain rate determined by local tax law. The most common example is payroll taxes withheld and paid by employers on employee wages. Withholding taxes also apply where sellers and buyers are situated in different jurisdictions, with rates varying by country or due to specific double tax treaties between tax authorities.

WHT can be applied to different types of remuneration, such as dividend, interest, royalty, commission, fees, and rentals, as well as transactions, i.e. digital transactions. The recipient (payee) could be employees, business partners, and overseas entities.

WHT is not the same as VAT or other forms of indirect taxes. In some countries, VAT charged by a provider has to be withheld by the payer and paid to the tax authorities, but this is not a WHT.

WHT includes both domestic withholding tax (in-country or locally) and international withholding, subject to local tax law or double tax treaties.

### **II. Withholding tax challenges**

Like many other taxes, withholding tax data can be collected via a mixture of online and offline sources. From the account payable (AP) side, companies often receive invoices, include them in the ERP system with relevant accounting treatments, leaving withholding tax as an afterthought.

A solution to these problems is to build a “withholding tax engine” which can automatically determine the correct WHT rate, tailored to the nature of each transaction based on tax law, and calculate the corresponding WHT amount. Major challenges encountered in building a withholding tax engine include:

* **Fragmented data sources** - where sales/purchase data was detached from withholding tax posting and added on afterward.
* **Missing data** - invoices come in different forms and types, sometimes handwritten. There are inevitably missing fields that may otherwise be valuable information in determining the correct withholding tax rate.
* **Mismatched or inconsistent data** - given the variety of invoices, the information is often inconsistent, resulting in bad quality data; this requires numerous edge cases to be accounted for.
* **Small data size** - despite being a transaction-level tax, there is limited data that is complete, accurate, and consistent; this means supervised learning models utilising natural language processing techniques are less appropriate. Unsupervised learning is therefore a more appropriate method to explore first.
* **Significant differences in country rules** - unlike VAT or GST, countries don't always have the same tax base for withholding taxes. It’s a spider web of rules which requires considerations on a country-by-country basis.
* **Double tax treaties** - other than the differences in underlying country rules, each country may have also negotiated different treaty agreements on withholding tax rates for each tax category (e.g. royalties, dividend, interest), adding further complexities.

### **III. Building a withholding tax engine**

The building work was split into a 5-step process:

1. **Check and sort the data available** on Sales Invoices (SI), Good Receipts (GR), and Purchase Order (PO) for one country only as a prototype;
2. **Review the rules per country**. Each country would have negotiated separate tax treaties, so it makes sense to train separate models for the determination engine for each country;
3. **Hard code rules where possible. Determining WHT can be done in part using logical hard-coded rules arising from my review of each country’s tax treaties.**
4. **Use trained machine learning models to refine the result**. Applying language modelling and unsupervised learning to make data-backed judgments based on invoice descriptions;
5. **Build a UI** to host the engine to allow users to interact with the determination engine.

After a successful build of the prototype, the next step is to iterate and refine the models based on user feedback and explore the possibility of scaling the prototype to other countries. This implementation process would be worthy of a separate blog post.