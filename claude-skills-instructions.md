[Skip to main content](https://www.anthropic.com/news/skills#main-content) [Skip to footer](https://www.anthropic.com/news/skills#footer)

[Home](https://www.anthropic.com/)

- [Research](https://www.anthropic.com/research)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- Commitments
- Learn
- [News](https://www.anthropic.com/news)

[Try Claude](https://claude.ai/)

Product

# Introducing Agent Skills

Oct 16, 2025●3 min read

![](https://www-cdn.anthropic.com/images/4zrzovbb/website/77dd9077412abc790bf2bc6fa3383b37724d6305-1000x1000.svg)

Claude can now use _Skills_ to improve how it performs specific tasks. Skills are folders that include instructions, scripts, and resources that Claude can load when needed.

Claude will only access a skill when it's relevant to the task at hand. When used, skills make Claude better at specialized tasks like working with Excel or following your organization's brand guidelines.

Claude Skills: Specialized capabilities you can customize - YouTube

[Photo image of Anthropic](https://www.youtube.com/channel/UCrDwWp7EBBv4NwvScIpBDOA?embeds_referring_euri=https%3A%2F%2Fwww.anthropic.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.anthropic.com)

Anthropic

294K subscribers

[Claude Skills: Specialized capabilities you can customize](https://www.youtube.com/watch?v=IoqpBKrNaZI)

Anthropic

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

0:00 / 1:10
•Live

•

You've already seen Skills at work in Claude apps, where Claude uses them to create files like spreadsheets and presentations. Now, you can build your own skills and use them across Claude apps, Claude Code, and our API.

## How Skills work

While working on tasks, Claude scans available skills to find relevant matches. When one matches, it loads only the minimal information and files needed—keeping Claude fast while accessing specialized expertise.

Skills are:

- **Composable**: Skills stack together. Claude automatically identifies which skills are needed and coordinates their use.
- **Portable**: Skills use the same format everywhere. Build once, use across Claude apps, Claude Code, and API.
- **Efficient**: Only loads what's needed, when it's needed.
- **Powerful**: Skills can include executable code for tasks where traditional programming is more reliable than token generation.

Think of Skills as custom onboarding materials that let you package expertise, making Claude a specialist on what matters most to you. For a technical deep-dive on the Agent Skills design pattern, architecture, and development best practices, read our [engineering blog.](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

## Skills work with every Claude product

### **Claude apps**

Skills are available to Pro, Max, Team and Enterprise users. We provide skills for common tasks like document creation, examples you can customize, and the ability to create your own custom skills.

![The Skills capabilities interface in Claude.ai with example Skills toggled on. ](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Faf2845deb68f4074e12f8b0c1ea3b9cae8946cac-1920x1080.png&w=3840&q=75)

Claude automatically invokes relevant skills based on your task—no manual selection needed. You'll even see skills in Claude's chain of thought as it works.

Creating skills is simple. The "skill-creator" skill provides interactive guidance: Claude asks about your workflow, generates the folder structure, formats the SKILL.md file, and bundles the resources you need. No manual file editing required.

Creating custom Skills with Claude - YouTube

[Photo image of Anthropic](https://www.youtube.com/channel/UCrDwWp7EBBv4NwvScIpBDOA?embeds_referring_euri=https%3A%2F%2Fwww.anthropic.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.anthropic.com)

Anthropic

294K subscribers

[Creating custom Skills with Claude](https://www.youtube.com/watch?v=kS1MJFZWMq4)

Anthropic

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

0:00 / 0:48
•Live

•

Enable Skills in [Settings](https://claude.ai/redirect/website.v1.253709d6-3c61-41b2-9779-4826d567f27e/settings/features). For Team and Enterprise users, admins must first enable Skills organization-wide.

### **Claude Developer Platform (API)**

Agent Skills, which we often refer to simply as Skills, can now be added to Messages API requests and the new `/v1/skills` endpoint gives developers programmatic control over custom skill versioning and management. Skills require the [Code Execution Tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/code-execution-tool) beta, which provides the secure environment they need to run.

Use Anthropic-created skills to have Claude read and generate professional Excel spreadsheets with formulas, PowerPoint presentations, Word documents, and fillable PDFs. Developers can create custom Skills to extend Claude's capabilities for their specific use cases.

Developers can also easily create, view, and upgrade skill versions through the Claude Console.

Explore the [documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) or [Anthropic Academy](https://www.anthropic.com/learn/build-with-claude) to learn more.

![Box logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F890f0f2ef5b8bcfff0d8dfd000ace220cb440864-120x65.png&w=256&q=75)

“

> Skills teaches Claude how to work with Box content. Users can transform stored files into PowerPoint presentations, Excel spreadsheets, and Word documents that follow their organization's standards—saving hours of effort.
>
> Yashodha Bhavnani
>
> Head of AI, Box

![Notion logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/f9ea50555647585fc11a0df17655e98956e0b488-1216x350.svg)

“

> With Skills, Claude works seamlessly with Notion - taking users from questions to action faster. Less prompt wrangling on complex tasks, more predictable results.
>
> MJ Felix
>
> Product Manager, Notion

![Canva logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F3b2022164e7d66fc302c845547a7bc782f97a68c-1536x864.png&w=256&q=75)

“

> Canva plans to leverage Skills to customize agents and expand what they can do. This unlocks new ways to bring Canva deeper into agentic workflows—helping teams capture their unique context and create stunning, high-quality designs effortlessly.
>
> Anwar Haneef
>
> GM & Head of Ecosystem, Canva

![Rakuten logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/0e7636568b10b8552dbe89ff9a0b36a74ff47527-166x49.svg)

“

> Skills streamline our management accounting and finance workflows. Claude processes multiple spreadsheets, catches critical anomalies, and generates reports using our procedures. What once took a day, we can now accomplish in an hour.
>
> Yusuke Kaji
>
> General Manager AI, Rakuten

### **Claude Code**

Skills extend Claude Code with your team's expertise and workflows. Install skills via plugins from the anthropics/skills marketplace. Claude loads them automatically when relevant. Share skills through version control with your team. You can also manually install skills by adding them to `~/.claude/skills`. The Claude Agent SDK provides the same Agent Skills support for building custom agents.

## Getting started

- **Claude apps:** [User Guide](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills) & [Help Center](https://support.claude.com/en/articles/12512176-what-are-skills)
- **API developers:** [Documentation](https://docs.claude.com/en/api/skills-guide)
- **Claude Code:** [Documentation](https://docs.claude.com/en/docs/claude-code/skills)
- **Example Skills to customize:** [GitHub repository](https://github.com/anthropics/skills)

## What's next

We're working toward simplified skill creation workflows and enterprise-wide deployment capabilities, making it easier for organizations to distribute skills across teams.

Keep in mind, this feature gives Claude access to execute code. While powerful, it means being mindful about which skills you use—stick to trusted sources to keep your data safe. [Learn more](https://support.claude.com/en/articles/12512180-using-skills-in-claude#h_2746475e70).

[Share on Twitter](https://twitter.com/intent/tweet?text=https://www.anthropic.com/news/skills)[Share on LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/news/skills)

[News\\
\\
**Claude Code on the web**\\
\\
Oct 20, 2025](https://www.anthropic.com/news/claude-code-on-the-web) [News\\
\\
**Claude for Life Sciences**\\
\\
Oct 20, 2025](https://www.anthropic.com/news/claude-for-life-sciences) [News\\
\\
**Claude and your productivity platforms**\\
\\
Oct 16, 2025](https://www.anthropic.com/news/productivity-platforms)

[Return to homepage](https://www.anthropic.com/)

### Products

- [Claude](https://claude.com/product/overview)
- [Claude Code](https://claude.com/product/claude-code)
- [Max plan](https://claude.com/pricing/max)
- [Team plan](https://claude.com/pricing/team)
- [Enterprise plan](https://claude.com/pricing/enterprise)
- [Download app](https://claude.ai/download)
- [Pricing](https://claude.com/pricing)
- [Log in to Claude](https://claude.ai/)

### Models

- [Opus](https://www.anthropic.com/claude/opus)
- [Sonnet](https://www.anthropic.com/claude/sonnet)
- [Haiku](https://www.anthropic.com/claude/haiku)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Claude Developer Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](https://docs.claude.com/en/home)
- [Pricing](https://claude.com/pricing#api)
- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud’s Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)
- [Console login](http://console.anthropic.com/)

### Learn

- [Courses](https://www.anthropic.com/learn)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-index)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](https://www.anthropic.com/transparency)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Terms and policies

Privacy choices- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)

© 2025 Anthropic PBC

- [Visit our LinkedIn page](https://www.linkedin.com/company/anthropicresearch)
- [Visit our X (formerly Twitter) profile](https://x.com/AnthropicAI)
- [Visit our YouTube channel](https://www.youtube.com/@anthropic-ai)