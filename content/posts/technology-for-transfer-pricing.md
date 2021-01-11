+++
date = 2020-11-27T11:25:00Z
slug = "technology-for-transfer-pricing"
title = "Technology for Transfer Pricing"

+++
My tax technology journey starts with transfer pricing ("TP") given much of the TP work involves tailored [data analytics](https://shan.tax/posts/cbcr-analysis/) and [visualisation](https://shan.tax/posts/data-visualisation-in-tax/). For technical correspondence with tax authorities, I also provided econometric based statistical analyses. For multinational companies, TP is a highly visible area of tax with governments agreeing to exchange data and hence many potential technology applications. It is therefore desirable to establish a modern data-driven TP management in-house with a systematic overarching design. The diagram below helps to demonstrate how different pieces fit together.

![](/uploads/tp-tech-overview.png)

### TP Data Store

A secure, clean and efficient database is fundamental to successfully implement any technology solution in TP. To find the right type of database for any TP technology application, one will need to consider many aspects of requirements, for example:

* the type of data you will use, e.g. numerical, texts, multimedia
* the quality and consistency your data will be
* who and how the data should be managed in the long run
* what querying mechanism including frequency you require
* the structure or model you want the data to have
* where you want to store it

I termed the database as "TP data store" but its actual form and substance would depend on specific business requirements and to a large extent - the existing ERP systems. Broadly a TP data store needs to satisfy requirements from both back end and front end. As tax professionals, we often have specific requirements on the front end - the TP data store should enable a series of workflow on technology applications, from data collection, transformation, reporting, analysis, review, approve, to submission and, archiving. Based on the relevant requirements, tax professionals will work with IT professionals in many areas such as database architect, information security, platform and application services to complete the back end requirements.

It is a "store" because ideally the TP data is organised in a modular way so each component could be used and reused somewhat independently and on-demand. "Independently" could be interpreted in multiple dimensions. For example, different users access to the TP data store could access the same attributes built by others; or one could query the same attribute over multiple years to create a tailored trend and anomaly analysis. Consequently, careful design with a holistic view of the database is necessary between tax and IT professionals.

### TP Technology Applications

With the TP data store in place, we will have a closer look at different technology applications available in TP. There are broadly five main areas of TP technology applications:

* TP strategy
* TP audit and rulings
* TP implementation
* TP documentation and benchmarking
* TP operation

The last two categories, documentation and benchmarking, and operation TP typically rely on structured data, i.e. data in pre-defined formats, such as the ERP system data. I implemented TP documentation bot using Robotic Process Automation (RPA) and automatic TP data extraction from a universal data lake. Clean, good quality data at source remains the biggest challenge in this type of applications.

For the first three categories, on the other hand, much of the data remain unstructured and require much more manual efforts. For example, I designed and implemented a workflow application to monitor TP policy exceptions - although the process is automated using Microsoft's Power platform with audit trial, we still rely on human judgements on final review and approval.

It is certainly possible to build some natural language processing element into the process of reviewing the unstructured data but the built process itself requires domain expertise and meaningful interpretation. I worked on an audit text analysis engine. The biggest challenge I faced there was to meaningfully extract entities and relations within the vast amount of TP audit files and obtain insights from the extractions.

### Concluding thoughts

This blog discussed technology in TP in two main parts: data and applications. From experience, to set up a TP specific data store can be very difficult, given TP data is often nested within several ERPs from finance to supply chain, requiring buy-in and coordination from several teams. As a result, a top-down approach from prototyping specific business requirements may prove better to acquire stakeholders' buy-in and scale up thereafter.