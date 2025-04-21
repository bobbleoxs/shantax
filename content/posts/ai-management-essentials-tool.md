+++
date = 2025-04-15T12:00:00Z
slug = "ai-management-essentials-tool"
title = "Building an Interactive AI Management Essentials Tool"
+++

During the Easter weekend, I worked on a mini project to create an [interactive version of the UK government's AI Management Essentials ("AIME") Tool](https://aime.shan.tax/). The [original DSIT questionnaire](https://www.gov.uk/government/consultations/ai-management-essentials-tool/ai-management-essentials-tool-accessible) is static and covers 10 essential sections across three key areas:
- Internal Processes (AI system record, AI policy, Fairness)
- Managing Risks (Impact assessment, Risk assessment, Data management, Bias mitigation, Data protection)
- Communication (Issue reporting, Third party communication)

As organizations increasingly adopt AI systems, proper governance and management frameworks become critical.  The self-assessment questionnaire from DSIT offers an excellent starting points for organisations to conisder what Ai management framework would be most suitable for their specific scenario. 

On 4 June 2025, I have the privilege to facilitate the discussion of AIME at this year's [CIOT's Tax Technology Conference in Birmingham](https://taxtechnology.org.uk/). To encourage collaborative discussion and gain instant user feedback to further improve the AIME tool, I decided to have a go transforming the static format into an interactive platform where participants can:
- Select specific sections to complete based on their interests or priorities
- Receive instant summaries of their responses per section
- Compare their results with aggregated peer responses
- Engage in meaningful discussions around AI governance challenges and solutions

## The Technology Behind the Tool

This project combines several modern technologies:
- [lovable.dev](https://lovable.dev) for rapid prototyping of the interactive interface
- [ChatGPT](https://chatgpt.com/) for UI/UX refinement and assistance with implementation
- [Cursor](https://www.cursor.com/en) connected to GitHub for streamlined development and version control
- [Supabase](https://supabase.com/) for secure backend database management to store participant responses

The interface follows the UK [Government Digital Service (GDS) design principles](https://www.gov.uk/guidance/government-design-principles), ensuring familiarity for users acquainted with government digital services.

## Facilitating Meaningful Discussions on AI Governance

I hope this tool can be particularly valuable in its ability to spark conversations. By collecting and displaying aggregated responses, it helps participants understand:
- Where their organization stands relative to peers
- Common challenges across the industry
- Areas where most organizations excel or struggle with AI management

This collective intelligence approach transforms what was once a solitary assessment into a community learning experience. Additionally, the database of responses provides DSIT with valuable feedback on how organizations are interpreting and implementing their guidance.

## Why This Matters for Tax Professionals

As tax functions increasingly integrate AI into their workflows - from automated compliance to predictive analytics - understanding governance frameworks becomes essential. I hope more people can participate in discussions of further developing this tool which will help our tax professionals:

1. Assess their current AI management practices
2. Identify potential gaps or areas for improvement
3. Compare their organization's approach with industry benchmarks
4. Engage in informed discussions about AI governance

## Join Us at the Tax Tech Conference

We will be discusing the use of this tool at the upcoming [CIOT's Tax Tech Conference](https://taxtechnology.org.uk/) on 4 June 2025. Participants will have the opportunity to:
- Complete sections of the questionnaire
- View their individual and collective results in real-time
- Participate in facilitated discussions based on the findings
- Contribute to a broader understanding of AI management practices in the tax sector

## The Road Ahead

This interactive tool aims to benefit customers with an intuitive user experience but also provides valuable feedback to DSIT about how their tool is being used and understood. All responses are stored anonymously in a secure online database, offering insights that could inform future iterations of the government's guidance.

I may expand the tool based on user feedback. Possible improvements include detailed analytics, industry benchmarks, or integration with existing frameworks.

## Try It Today

You can explore the tool now. Visit [here](https://aime.shan.tax) to try it out and get a head start on understanding your organization's AI management practices.

Have questions or feedback? I'd love to hear from you - just drop me a message or share your thoughts in the comments below.

