+++
date = 2021-03-25T00:00:00Z
slug = "BuildinganHsCodeClassification"
title = "Building an HS Code Classification Model"

+++
### **I. What are HS codes?**

International trade relies on [Harmonized System](https://en.wikipedia.org/wiki/Harmonized_System) (“HS”) codes to classify goods transported across borders. Incorrect HS code classification may result in penalties and seizure of goods.

HS codes are used by all countries globally to classify imported and exported goods down to 6-digits. The HS code is split into three two-digit groups:

* First two digits - categorize product (e.g. “61” for Apparel & Clothing)
* Second two digits - classify further (e.g. “6109” for t-shirts)
* Third two digits - specify details of the product (e.g. “610910” for cotton t-shirts)

An additional 2 to 6 digits are added by individual countries to describe the goods in even more detail. For example, the US assigns a 10-digit code, of which the last 4 is known as the [Schedule B number](https://www.trade.gov/harmonized-system-hs-codes).

Tariffs and customs duties are imposed on imported and exported goods based on their HS code classification. The HS code classification is also used to recognise any preferential trade agreement.

The Harmonized System is organized into 21 sections, with 96 chapters in each section, and each chapter is divided into around 5,000 headings and subheadings. The system is enormous. Many factors affect the classification of HS codes, including but not limited to product composition, form, and use.

### **II. Challenges with HS code classification**

Given the variety and volume of goods in international trade, assigning the correct HS code often presents challenges. Some major challenges encountered when working on this project include:

* **Fragmented data source** - like many other taxes, the data source for HS codes is not neatly presented, especially in a large multinational organisation. Often there are multiple teams holding one or several pieces of information.
* **Inaccurate data** - to this day, many countries still rely on human experience to assign the correct HS code to goods for their respective country and purposes, often resulting in the wrong classification.
* **Missing out on preferential rates under trade agreements** - each country has individually negotiated rates on certain types of goods, but this may not always be considered when it comes to assigning HS codes. In addition, trade agreements also change over time, and outdated information or ineffective communication from government authorities can also result in incorrect classification.

### **III. Building an HS code classification model**

Given the significance of HS codes in international trade and the various challenges in classifying them correctly, I set out to create an automated classification model which uses algorithms to assist the customs teams in selecting HS codes.

I aimed to solve the problem on a country-by-country basis, given each country has its own rules on how many digits go into the HS code and a different set of trade agreements.

I determine the classification almost solely relying on invoice descriptions. In the spirit of lean working, I started with a prototype for the Philippines only.

Key parameters of the project are listed below:

**Data**

Only 3000 rows of data are available including invoice description and corresponding HS code (target “labels” for the algorithm). The invoice descriptions are in English.

**Models**

Given the limited size of data, I used a combination of machine learning and fuzzy string matching, with a refined weighting between these two methods;

I used natural language processing techniques for extracting model features from the invoice descriptions, and a [genetic algorithm](http://epistasislab.github.io/tpot/ "genetic algorithm") to automatically fine-tune and select the best machine learning model;

**Results**

For a given input, the model returns the top three most likely HS codes, along with several examples for each HS code, for users to review. The combined model achieved an accuracy of 92%.

**User interface**

The classification model was productionised via a Django-powered web application. The frontend interface allows users to input their own invoice description, whereupon the model then returns the top three most likely HS codes.

![](/uploads/screenshot-2021-09-15-at-22-34-57.png)