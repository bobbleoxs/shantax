+++
date = 2021-06-08T23:00:00Z
draft = true
slug = "BuildinganHsCodeClassification"
title = "Building an HS Code Classification Model"

+++
### I. What is HS code?

International trade relies on HS (stands for Harmonised System) codes to classify goods transported across borders. Incorrect HS code classification may result in penalties and seizure of goods.

HS code is used by all countries globally to classify imported and exported goods down to 6-digit. The HS code is split into three groups of two codes.

* First two digits - categorize product (e.g. garment)
* Second two digits -  classify further (e.g. t-shirt)
* Third two digits - specify details of the product (e.g. women cotton t-shirt)

Individual countries also add in a further group of 2 to 6 digits to describe the goods in even more detail. For example, the US assigns a 10-digit code, of which the last 4 is known as Schedule B number.

Tariffs and customs duties are imposed on imported and exported goods based on the HS code classification. It is used to recognise any preferential trade agreement.

The HS code is organized into 21 sections, with 96 chapters in each section, and each chapter is divided into around 5,000 headings and subheadings. The system is enormous. Many factors affect the classification of HS code, including but not limited to product composition, form and use.

### II. Challenges with HS code classification

Given the variety and volume of goods in international trade, assigning the correct HS code often presents challenges. Some of the major challenges I encountered when working on this project include:

* Fragmented data source - like many other taxes, the data source for HS code is not neatly presented, especially in a large multinational organisation. Often there are multiple teams holding one or several pieces of information.
* Inaccurate data - to this day, many countries still rely on human experience to assign the correct HS code to goods for their respective country and purposes, often resulting in the wrong classification.
* Missing out on preferential rates under trade agreements - each country has individually negotiated rates on certain types of goods, but this may not always be considered when it comes to assigning HS code. In addition, trade agreements also change over time, outdated information or ineffective communication from government authorities also could result in incorrect classification.

### III. Building an HS code classification model

Given the significance of HS code in international trade and the various challenges in classifying them correctly, we set out to work on an automated classification model which assigns HS code using algorithms to help the customs team tackle the challenges.

We aimed to solve the problem on a country by country basis, given each country has its own rules on how many digits go into the HS code and a different set of trade agreements.

The determination of HS code classification almost solely relies on invoice descriptions. In the spirit of agile working, we started with a prototype for the Philippines only.

Key parameters of the project are listed below:

**Data**

Only 3000 rows of data are available including invoice description and corresponding HS code (labels). The invoice descriptions are in English.

**Models**

Given the limited size of data, we sued a combination of machine learning and fuzzy search method with refined weighting;  
We used a genetic algorithm to automatically fine-tune and select the best machine learning model;

**Results**

The model results provide the top three most likely HS codes with examples for users to view. The combined model achieved an accuracy of 92%.

**User interface**

The classification models were wrapped up in the backend of a web app, where users could input their own invoice description for the model to return the top three most likely HS codes.

![](/uploads/screenshot-2021-09-15-at-22-34-57.png)