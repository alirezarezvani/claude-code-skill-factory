# How to Use the Scrum Master Agent Skill

## Quick Start

Hey Claude—I just added the "scrum-master-agent" skill. Can you analyze Sprint 45 and tell me if we're on track?

*(Attach: Linear export JSON, Jira CSV, GitHub Projects export, or Azure DevOps work items)*

---

## Example Invocations

### Daily Standup (Ultra-Lightweight)

**Example 1:**
```
@scrum-master-agent

Generate a quick standup summary for Sprint 45.

[Attach: sample_input_linear.json]
```

**Expected Output**: 50-100 token summary with completion status, in-progress count, and blockers (if any).

---

### Sprint Planning

**Example 2:**
```
@scrum-master-agent

Help me plan Sprint 46. Team capacity is 80 points. Prioritize the backlog based on effort, value, and risk.

[Attach: CSV with backlog stories]
```

**Example 3:**
```
@scrum-master-agent

We have 4 engineers with 40 points capacity each (160 total). Alice is on PTO for 3 days, Bob has 2 days of meetings. Calculate adjusted capacity and recommend which stories to include.

[Attach: sample_input_linear.json]
```

**Expected Output**: Prioritized story list (P0/P1/P2), capacity allocation, recommendations for scope adjustments.

---

### Burndown Analysis

**Example 4:**
```
@scrum-master-agent

Analyze Sprint 45 burndown. Are we on track to finish by Nov 19? If not, when will we likely complete?

[Attach: Jira sprint export JSON]
```

**Expected Output**: Burndown comparison (ideal vs actual), predicted completion date, velocity assessment.

---

### Sprint Review (Full Report)

**Example 5:**
```
@scrum-master-agent

Generate a comprehensive sprint review for Sprint 45. Include velocity trends, burndown analysis, sprint health score, and risk alerts.

[Attach: Linear export with 3 sprints of historical data]
```

**Expected Output**: 500-1000 token report with:
- Velocity metrics and trends
- Burndown chart (ASCII for CLI, table for Claude Desktop)
- Sprint health score (0-100) with breakdown
- Risk alerts (conditional, only if issues exist)
- Prioritized recommendations

---

### Retrospective

**Example 6:**
```
@scrum-master-agent

Generate a retrospective report for Sprint 45. Focus on what went well, what needs improvement, and action items.

[Attach: GitHub Projects export]
```

**Expected Output**: Retrospective analysis with:
- What went well (achievements)
- What needs improvement (issues)
- Action items (P0/P1/P2 with owners and due dates)

---

### Capacity Planning

**Example 7:**
```
@scrum-master-agent

Calculate team capacity for Sprint 46:
- Team: Alice (40 pts), Bob (40 pts), Charlie (40 pts), Diana (40 pts)
- Alice: 3 days PTO
- Bob: 2 days meetings
- Sprint: 10 working days

How many points should we commit to?
```

**Expected Output**: Adjusted capacity calculation with buffer recommendation.

---

### Multi-Tool Comparison

**Example 8:**
```
@scrum-master-agent

Compare velocity trends across the last 3 sprints. I have Linear data for Sprints 43-44 and Jira data for Sprint 45.

[Attach: Multiple JSON files]
```

**Expected Output**: Velocity trend analysis with insights on improving/declining/stable performance.

---

### Risk Analysis

**Example 9:**
```
@scrum-master-agent

Identify high-risk stories in the backlog. Flag anything with:
- More than 8 points
- Blocked status
- Missing dependencies
- Unassigned

[Attach: Backlog CSV]
```

**Expected Output**: List of high-risk stories with risk mitigation recommendations.

---

### Custom Priority Scoring

**Example 10:**
```
@scrum-master-agent

Prioritize the backlog using these custom weights:
- Business value: 60%
- Implementation effort: 25%
- Technical risk: 15%

[Attach: Linear export]
```

**Expected Output**: Re-prioritized story list with custom scoring.

---

## What to Provide

### Minimum Required Data
- **Sprint metadata**: Sprint name, start date, end date
- **Stories**: ID, title, story points, status, assignee
- **Format**: JSON (preferred), CSV, or YAML

### Optional Data (Enhances Analysis)
- **Team data**: Member names, capacity, availability
- **Historical data**: Previous 3-5 sprints for trend analysis
- **Priority labels**: High/Medium/Low
- **Blocked status**: True/false with blocker reason
- **Dependencies**: IDs of dependent stories
- **Labels/Tags**: For value scoring (e.g., "customer-facing", "revenue-impact")

### Supported Tools
- **Linear**: Export project to JSON from project view
- **Jira**: Use REST API or export to CSV
- **GitHub Projects**: Export to CSV or use GraphQL query
- **Azure DevOps**: Export work item query results to JSON/CSV

---

## What You'll Get

### Output Adapts to Context
- **Claude AI Desktop**: Rich markdown tables, emoji indicators, detailed reports
- **Claude Code (CLI)**: ASCII charts, terminal-friendly output, concise summaries
- **API**: JSON export for tool integration

### Report Types
1. **Daily Standup**: 50-100 tokens (ultra-lightweight)
2. **Sprint Planning**: 200-500 tokens (moderate detail)
3. **Sprint Review**: 500-1000 tokens (comprehensive)
4. **Retrospective**: 300-500 tokens (action-focused)
5. **JSON Export**: Full metrics for dashboards/tools

### Token Efficiency Features
- **Summary-first**: Key metrics up front, details on request
- **Conditional alerts**: Only shows warnings/risks if they exist
- **Progressive disclosure**: Start small, drill down as needed
- **Lazy calculation**: Computes only what's requested

---

## Pro Tips

### Best Practices
1. **Consistent data format**: Stick to JSON for best results
2. **Daily updates**: Update story status daily for accurate burndown
3. **Historical data**: Provide 3-5 previous sprints for trend analysis
4. **Label strategy**: Use consistent labels (e.g., "customer-facing", "revenue-impact") for value scoring

### Workflow Integration
1. **Automate exports**: Set up CI/CD to export Linear/Jira data nightly
2. **Morning standup**: Generate lightweight summary every morning
3. **Mid-sprint check**: Run health score on day 5-7
4. **Sprint planning**: Use priority scoring to allocate top 80% of capacity
5. **Retrospectives**: Generate within 24 hours of sprint end

### Customization
- Adjust priority scoring weights (default: value 50%, effort 30%, risk 20%)
- Configure health score weights (default: velocity 40%, burndown 30%, blocked 20%, morale 10%)
- Set custom buffer percentage (default: 15%)

---

## Troubleshooting

### "Missing required fields" error
Ensure your data includes: `sprint_name`, `start_date`, `end_date`, `stories` (with `id`, `title`, `points`, `status`)

### "Can't calculate burndown" error
Provide valid `start_date` and `end_date` in ISO 8601 format (YYYY-MM-DD)

### "No historical data" warning
Velocity trends require 3+ previous sprints. Provide historical data for better forecasting.

### "Tool adapter not found" error
Set `"tool": "linear|jira|github|azure"` in JSON, or use generic format (will auto-detect)

---

## Advanced Usage

### Custom Value Functions
You can define custom priority scoring in your request:
```
Prioritize stories using this formula: priority = (value * 3 + (10 - effort) * 2 + (10 - risk)) / 6
```

### Batch Analysis
Analyze multiple sprints at once:
```
Compare Sprints 43, 44, and 45. Show velocity trends, cycle time improvements, and recurring blockers.
```

### Integration with Other Skills
Combine with other skills for richer analysis:
- `@aws-solution-architect` for infrastructure planning based on sprint velocity
- `@content-researcher` for researching best practices mentioned in retrospectives
- `@prompt-factory` for generating team-specific prompts

---

## Need Help?

Ask Claude:
- "What metrics can you calculate?"
- "Show me an example of priority scoring"
- "How do I export data from Linear/Jira/GitHub?"
- "What's the best format for my data?"

---

## Notification Examples (Optional)

Notifications are **disabled by default** and require webhook setup. See README.md for configuration.

### Example 11: Daily Standup with Slack Notification
```
@scrum-master-agent

Generate daily standup summary for Sprint 45 and send notification to Slack.

[Attach: Linear export]
```

**Expected Output**: Standup report + "Notification sent" confirmation

---

### Example 12: Sprint Review with Teams Notification
```
@scrum-master-agent

Full sprint review for Sprint 45. Send summary to Microsoft Teams channel.

[Attach: Jira export]
```

**Expected Output**: Comprehensive review + Teams notification confirmation

---

### Notification Format

**Slack** (Rich blocks):
- Header with sprint name
- Velocity, health score, completion rate, status (4 fields)
- Top 3 risks (conditional)

**Microsoft Teams** (Adaptive Cards):
- Title with sprint name
- Fact set with metrics
- Risk list (conditional)

**Token Budget**: 50-100 tokens per notification (highly efficient)

---

### Configuration Options

**Option 1: YAML Config File**
```yaml
notifications:
  enabled: true
  channel: slack  # or teams
  slack_webhook: https://hooks.slack.com/services/YOUR/WEBHOOK/URL
  teams_webhook: https://outlook.office.com/webhook/YOUR/WEBHOOK/URL
```

**Option 2: Environment Variables**
```bash
export NOTIFY_ENABLED=true
export NOTIFY_CHANNEL=slack
export SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

**Getting Webhook URLs:**
- Slack: https://api.slack.com/messaging/webhooks
- Teams: Channel → "..." → Connectors → Incoming Webhook

---

---

**Version**: 1.1.0 (with Notification Support)
**Last Updated**: 2025-11-05
**Skill Type**: Multi-file capability with Python calculations
