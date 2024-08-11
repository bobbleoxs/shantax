+++ 
date = 2024-08-11T15:48:00Z
slug = "trenches" 
title = "👩🏻‍💻 The Hidden Complexity of Tax Data Analytics: 10 Lessons from the Trenches 👩🏻‍🏭"
+++

![](/uploads/trenches.png)

The analysis of tax data often yields contradictory paradoxes, requiring both numerical precision as well as analytical interpretation of tax regulations. With Pillar 2 looming, understanding best practices for tax data collection, analysis, calculation, and reporting is paramount.

Whether you're an Excel expert, an Alteryx aficionado, proficient with Python, or skilled using SQL, the following is some hard won practical tips for working with real-world tax data, from data cleaning to building machine learning tax models.

1. **The Deceptive Nature of "Clean" Data**

In tax, data cleaning is often seen as a perfunctory first step - a bureaucratic hurdle before the real work begins. ERP systems generate highly structured financial data exports, creating a false sense of security. The cliche "garbage in and garbage out" is well known, but it's hard to know when the inputs are garbage. The resulting impact of unclean data on final analytical outputs can be disastrous.

I treat the initial step of data exploration like a detective approaching a crime scene. Every dataset, no matter how innocuous it appears, is guilty until proven innocent. Duplicates, missing values, truncated data - these are the usual suspects. The real culprits can be quite insidious: inconsistent encoding, mixed data types, identical but different order of filters for extraction, or omitted time series that lurk in the shadows, waiting to derail your analysis when you least expect it.

My choice of weapon are automated data profiling tools such as [YData Profiling](https://docs.profiling.ydata.ai/latest/) and [D-Tale](https://github.com/man-group/dtale). It's like having a forensic team at your disposal, quickly scanning the scene and highlighting potential areas of interest. But tools are just that – tools. Analytical mastery requires developing an intuition for data, a sixth sense that tingles when something doesn't quite add up.

2. **The Counterintuitive Power of Slowing Down**

While tax is not always a fast-paced discipline, tax technology teams are often under pressure to respond rapidly to analytical queries. These are often written in the arcane language of tax regulations rather than clear technical specifications. The temptation to dive straight into writing code can be irresistible. Some paradoxical advice: slowing down at the start dramatically speeds up the overall process.

> "Give me six hours to chop down a tree and I will spend the first four sharpening the axe." - Abraham Lincoln 

Instead of immediately starting to code the requirements, I've learned to first sketch out a decision tree, flowchart or mind map of the logic I'm about create based on my understanding of the query. It's like plotting your route before embarking on a journey. An added advantage of this approach is to align non-technical tax colleagues' understanding and expose edge cases and flaws in your logic while they are cheap to fix. It takes time to plan your journey upfront, but it can save you from countless dead ends and U-turns later on.

In tax analytics, clarity of thought precedes clarity of code. A well-structured logic map is worth a thousand lines of hastily written code.

> "First, solve the problem. Then, write the code." – John Johnson

3. **Coding for Humans not Machines**

Code isn't just instructions for a machine - it's a precise form of communication with your future self and colleagues across tax and engineering. Data analytics code should be documented like any other tax report, including a top-line summary and descriptive code comments. This enhances reproducibility and assists explainability. Your future self will be thankful when a tax audit case is opened a year later and you're required to explain the calculation logic. 

I advocate using auto-formatting tools (e.g. [Jupyter black](https://pypi.org/project/jupyter-black/)) and linters (e.g. [ruff](https://docs.astral.sh/ruff/)) to automatically enforce code quality standards. It's not just about aesthetics - it's about creating code that tells a story. When a new team member can read your analysis and understand not just what it does, but why it does it, you've succeeded.

In tax, our data analyses may need to stand up to future scrutiny from auditors, regulators, or even court officials. Write your code with the clarity and precision you'd use in a legal document.

4. **The Lifesaving Magic of Unit Tests**

I used to think unit tests were a luxury, something only "real" software engineers need to worry about when putting their work into production. I've since learned that adding one-line ("unit") tests throughout every data analysis can be lifesaving, flagging hard-to-spot data quality issues that would otherwise have been easily missed.

Consider writing tests to check for common data issues to detect the presence of empty fields, duplicate values in unique identifiers, whether rounding has been done consistently, or to test assumptions around handling edge cases. Tools such as [Pandera](https://pandera.readthedocs.io/) or Pyd[Pydantic](https://docs.pydantic.dev/latest/)antic can help streamline this process of "defensive data testing".

This practice is even more useful when it comes to tracking down errors, such as a calculation discrepancy, which are otherwise much like searching for a needle in a haystack. Furthermore, writing tests will force you to think deeply about your code's behaviour, often revealing logical flaws before they become costly mistakes.

5. **The Power of Visualisation**

> "The greatest value of a picture is when it forces us to notice what we never expected to see." — John W. Turkey

Numbers and text can lie, or at least mislead. This is especially true in tax data analytics. A simple bar chart can be used to understand historic input VAT trends over time. Overlaying a line chart of purchase history can reveal surprise discrepancies. A [Sankey diagram](https://en.wikipedia.org/wiki/Sankey_diagram) can be used to visualise the internal workings of cashflows before inspecting the final resulting numbers per country, potentially triggering unexpected withholding taxes and transfer pricing issues.

Creating quick, simple visualisations should an integral part of any tax data analytics workflow. It's not about making pretty charts for presentations; it's about leveraging our brain's remarkable ability to spot patterns and anomalies from visual diagrams that would otherwise be hidden in rows of numbers. This in turn aids us to raise relevant questions for tax and commercial teams.

6. **The Efficiency of Structured Chaos**

Starting a new tax data analytics project is exciting and we tend to dive straight into the "dirty end", leaving the organisation of the project "later" - a later that rarely came. However, utilising a project template or a "cookie cutter" is a massive time-saver for later when the project grows bigger. Raw and processed data, code, documentation, dependencies, tax legislations, and tests, should all follow a set structure and be organised into their rightful places. 

This structure forces me to think about data flow and code organisation from the start. It makes collaboration easier, as team members know exactly where to find what they need. Most importantly, it allows me to focus on solving tax problems instead of constantly reinventing the wheel.

In tax technology, consistency isn't just about the data - it's about process too.

7. **The Unexpected Value of Exporting Interim Results**

For non-technical tax colleagues who do not code, data transformations and programmatic analysis can appear to be "black box" (or even black magic!). Data enters the box, results come out of the box, and it's easy to assume that the magic in the middle is only of interest to fellow engineers. It can be frustrating to explain these internal workings to non-technical stakeholders.

My own tip here is to export snapshots of the tax data at various stages of transformation, or sampled excerpts if the data is large, to help stakeholders see how the data has evolved at each stage. These snapshots are useful for debugging purposes, for analytical audibility, and an invaluable tool for stakeholder communication. They allow tax experts to review the data in familiar tools like Excel, enabling them to spot potential issues or edge cases that might not be apparent in the final output.

This practice bridges the gap between technical implementation and tax expertise, providing a trail of breadcrumbs that allows others to follow the analytical journey, step by step.

8. **The Time-Saving Magic of Result Caching**

Time is always at a premium in tax data analytics, especially during busy seasons. Repeatedly crunching the same massive datasets for slightly different queries is suboptimal.

For any analysis that involves heavy data processing and transformation which might be used again at a later stage, cache the intermediate results. This can be done by saving interim results to disk as CSV or Feather format, or using materialised views when working with SQL databases. 

This facilitates rapid iteration on downstream analyses without constantly revisiting the entire data pipeline. In tax data analytics, we should be smart about what to compute and when.

9. **Future-Proofing Your Code**

Tax laws change. From DAC7 to Pillar 2, stacks of FAQs, papers and examples demonstrate the fluidity of interpretation in implementing these requirements. This can be especially challenging if you work in a company that handles multiple jurisdictions, and every change brings a risk that your carefully crafted analyses and models become obsolete.

Treat each tax data analysis like a living document, designed to evolve with changing regulations. Structure your analysis with change in mind: separate the core logic from specific parameters, use configuration files for values likely to change, and build in flexibility wherever possible.

This approach requires a little more upfront thought and adds complexity to your initial implementation. The payoff in terms of maintainability and adaptability is enormous. It's the difference between dreading regulatory changes and being able to confidently tell stakeholders, "We can handle that."

10. **The Promise and Peril of Generative AI**

Tools like ChatGPT and GitHub's Copilot are reshaping how we approach coding and problem-solving in tax analytics. Even this article was proof-read by a GPT-powered writing agent tailored to my tax blog writing style. 

These tools are powerful allies when used judiciously. I've used them to optimise code for greater memory efficiency, rapidly add descriptive comments, and to spot subtle bugs that I might have otherwise overlooked. But they're certainly not magic bullets.

I've had my share of AI-induced wild goose chases, where a plausible-sounding suggestion led me down a rabbit hole of non-compliant or inefficient solutions. I've also heard horror stories of non-tech colleagues blindly trusting coding advice given with undesirable results. AI is a tool, not a replacement for tax and data expertise or, most importantly, critical thinking.

> "Clean code always looks like it was written by someone who cares." — Robert C. Martin

As tax technology professionals, our role is evolving. We're no longer just tax experts of a specific area of tax - we need to utilise the powerful tools at our disposal to produce results that are not just technically correct, but compliant and sensible in the complex world of tax. Embrace the complexity, stay curious, and keep pushing the boundaries of what's possible.
