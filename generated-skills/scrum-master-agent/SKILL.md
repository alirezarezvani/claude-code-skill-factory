---
name: scrum-master-agent
description: Comprehensive Scrum Master assistant for sprint planning, backlog grooming, retrospectives, capacity planning, and daily standups with intelligent context-aware reporting
---

# Scrum Master Agent

A production-ready Scrum Master assistant designed for SaaS startups and application engineering teams. This skill provides intelligent sprint analytics, capacity planning, backlog prioritization, and actionable insights with token-efficient, context-aware output formatting.

## Capabilities

### Sprint Management
- **Sprint Planning**: Capacity-based story allocation with velocity tracking
- **Backlog Grooming**: Priority scoring with effort/value/risk analysis
- **Sprint Health Monitoring**: Real-time burndown tracking with predictive alerts
- **Velocity Analysis**: Historical trend analysis with forecasting

### Team Operations
- **Daily Standups**: Ultra-lightweight progress summaries (50-100 tokens)
- **Capacity Planning**: Team availability calculation with holiday/PTO handling
- **Sprint Retrospectives**: Action items extraction with sentiment analysis
- **Risk Detection**: Automated alerts for scope creep, velocity drops, blocked tasks

### Multi-Tool Integration
- **Linear**: Native JSON import with Linear-specific field mapping
- **Jira**: REST API adapter with custom field support
- **GitHub Projects**: GraphQL integration with issue/PR tracking
- **Azure DevOps**: Work item queries with sprint hierarchy


### Notification Integration
- **Slack Notifications**: Token-efficient webhook integration with rich block formatting
- **MS Teams Notifications**: Adaptive Card integration for Microsoft Teams channels
- **Optional/Disabled by Default**: No setup required to use skill, notifications opt-in
- **User Choice**: Select Slack or Teams via configuration or environment variables
- **Concise Summaries**: 50-100 token notifications with top 3 risks only
### Intelligent Output Design
- **Context Detection**: Automatically adapts to Claude AI Desktop vs Claude Code
- **Token Efficiency**: Summary-first approach with progressive disclosure
- **Conditional Alerts**: Only shows warnings/risks when they exist
- **Format Optimization**: Markdown tables for Claude AI, ASCII charts for CLI

## Input Requirements

### Supported Formats
1. **JSON** (Recommended):
   ```json
   {
     "tool": "linear|jira|github|azure",
     "sprint_name": "Sprint 45",
     "start_date": "2025-11-05",
     "end_date": "2025-11-19",
     "team_capacity": 80,
     "stories": [...]
   }
   ```

2. **CSV**:
   ```csv
   story_id,title,points,status,assignee,priority,blocked
   STORY-123,User login,5,In Progress,Alice,High,false
   ```

3. **YAML**:
   ```yaml
   sprint:
     name: "Sprint 45"
     team:
       - name: Alice
         capacity: 40
       - name: Bob
         capacity: 40
   ```

4. **Tool-Specific Exports**:
   - Linear: Export to JSON from project view
   - Jira: Use REST API or CSV export
   - GitHub Projects: GraphQL query or CSV export
   - Azure DevOps: Work Item Query Results

### Required Fields
- **Sprint metadata**: name, start_date, end_date, team_capacity
- **Stories**: id, title, points, status, assignee
- **Optional**: priority, blocked, dependencies, labels, created_date

### Data Quality
- Story points must be numeric (Fibonacci or T-shirt sizes)
- Dates in ISO 8601 format (YYYY-MM-DD)
- Status values normalized to: Todo, In Progress, In Review, Done
- Team capacity in story points per sprint

## Output Formats

### 1. Daily Standups (Ultra-Lightweight)
**Token Budget**: 50-100 tokens
```
🚀 Sprint 45 - Day 7/10

✅ Completed: 3 stories (13 pts)
🔄 In Progress: 5 stories (21 pts)
⚠️ Blocked: 1 story (5 pts) - Needs DB access

Velocity: On track (65% complete, 70% time elapsed)
```

### 2. Sprint Planning (Moderate Detail)
**Token Budget**: 200-500 tokens
```
📊 Sprint 45 Planning Summary

Capacity: 80 pts | Committed: 75 pts | Buffer: 5 pts

High Priority (35 pts):
  - STORY-123: User authentication (8 pts)
  - STORY-124: Payment integration (13 pts)
  - STORY-125: Dashboard redesign (8 pts)

Recommendations:
  1. P0: Address DB access blocker
  2. P1: Reduce scope if velocity drops below 85%
  3. P2: Consider splitting STORY-124 (13 pts is risky)
```

### 3. Sprint Review (Full Report)
**Token Budget**: 500-1000 tokens

Includes:
- Velocity trends (ASCII chart for CLI, table for Claude AI)
- Burndown analysis with predictive completion date
- Team performance metrics (throughput, cycle time)
- Risk alerts (conditional - only if issues exist)
- Prioritized recommendations (P0/P1/P2)

### 4. Retrospective Analysis
**Token Budget**: 300-500 tokens
```
🔍 Sprint 45 Retrospective

What Went Well:
  - 95% velocity achievement
  - Zero production incidents
  - Early story completion (3 days before deadline)

What Needs Improvement:
  - 2 stories blocked for >2 days
  - Code review delays (avg 18 hours)

Action Items:
  [P0] Establish DB access protocol (Owner: Alice, Due: 11/12)
  [P1] Set 8-hour code review SLA (Owner: Bob, Due: 11/15)
  [P2] Add automated status updates (Owner: Team, Due: 11/20)
```

### 5. Optional JSON Export
For tool integration and dashboards:
```json
{
  "sprint": "Sprint 45",
  "metrics": {
    "velocity": 75,
    "completion_rate": 0.95,
    "cycle_time_avg": 3.2
  },
  "risks": [...],
  "recommendations": [...]
}
```

## How to Use

### Quick Invocations

**Daily Standup**:
```
@scrum-master-agent

Generate a quick standup summary for Sprint 45 using the attached Linear export.
```

**Sprint Planning**:
```
@scrum-master-agent

Help me plan Sprint 46. Team capacity is 80 points. Here's the backlog (CSV attached).
Prioritize based on effort, value, and risk.
```

**Burndown Analysis**:
```
@scrum-master-agent

Analyze Sprint 45 burndown. Are we on track? When will we likely finish?
Attached: Jira sprint export (JSON)
```

**Retrospective**:
```
@scrum-master-agent

Generate retrospective report for Sprint 45. Focus on blockers and cycle time.
Attached: GitHub Projects export (CSV)
```

**Capacity Planning**:
```
@scrum-master-agent

Calculate team capacity for next sprint. Alice is on PTO for 3 days, Bob has 2 days of meetings.
Team size: 4 engineers (40 pts each normally).
```

### Advanced Usage

**Multi-Tool Comparison**:
```
Compare velocity trends across last 3 sprints using Linear data for Sprint 43-44 and Jira data for Sprint 45.
```

**Risk Analysis**:
```
Identify high-risk stories in the backlog. Flag anything with >8 points, blockers, or missing dependencies.
```

**Custom Metrics**:
```
Calculate sprint health score based on: velocity (40%), burndown trend (30%), blocked items (20%), team morale (10%).
```

## Scripts

### Core Modules

- **`parse_input.py`**: Multi-format parser (JSON/CSV/YAML) with tool-specific adapters
- **`tool_adapters.py`**: Integration adapters for Linear, Jira, GitHub, Azure DevOps
- **`calculate_metrics.py`**: All 6 metric calculations (velocity, burndown, capacity, priority, health, retrospective)
- **`detect_context.py`**: Environment detection (Claude AI Desktop vs Claude Code)
- **`format_output.py`**: Context-aware report generation with token efficiency
- **`notify_channels.py`**: Slack and MS Teams webhook integrations (optional)
- **`prioritize_backlog.py`**: Priority scoring with effort/value/risk analysis

### Calculation Details

**1. Velocity Analysis**:
- Historical average over last 3-5 sprints
- Trend analysis (improving/declining/stable)
- Forecasting for next sprint

**2. Burndown Tracking**:
- Daily story point completion
- Ideal burndown line calculation
- Predictive completion date (linear regression)

**3. Capacity Planning**:
- Team availability calculation (PTO, holidays, meetings)
- Story point allocation
- Buffer recommendation (10-20% of capacity)

**4. Priority Scoring**:
- **Effort**: Story points (normalized 0-10)
- **Value**: Business impact (High=10, Medium=5, Low=2)
- **Risk**: Blockers, dependencies, complexity (0-10)
- **Formula**: `priority_score = (value * 2 + (10 - effort) + (10 - risk)) / 4`

**5. Sprint Health Score**:
- **Velocity**: Actual vs committed (40% weight)
- **Burndown**: Actual vs ideal (30% weight)
- **Blocked Items**: Count and duration (20% weight)
- **Team Morale**: Optional sentiment input (10% weight)
- **Scale**: 0-100 (90+ = Excellent, 70-89 = Good, 50-69 = Fair, <50 = At Risk)

**6. Retrospective Analysis**:
- Completed vs committed stories
- Blocked item analysis (count, duration, causes)
- Cycle time metrics (avg time from start to done)
- Action item extraction from retro notes

## Best Practices

### Data Quality
1. **Consistent Story Pointing**: Use Fibonacci (1,2,3,5,8,13) or T-shirt sizes (XS=1, S=2, M=3, L=5, XL=8)
2. **Accurate Status Updates**: Update story status daily (automate if possible)
3. **Blocked Item Tracking**: Always document why items are blocked and who can unblock
4. **Sprint Boundaries**: Never change sprint scope after day 3 (exception: critical bugs)

### Workflow Integration
1. **Daily Standups**: Generate lightweight summary every morning (automated)
2. **Sprint Planning**: Use priority scoring to allocate top 80% of capacity
3. **Mid-Sprint Check**: Run health score on day 5-7 to catch issues early
4. **Retrospectives**: Generate within 24 hours of sprint end while feedback is fresh

### Token Efficiency
1. **Progressive Disclosure**: Start with summary, offer details on request
2. **Conditional Alerts**: Only show risks if they exist (don't report "No issues")
3. **Lazy Calculation**: Compute detailed metrics only when asked
4. **Caching**: Reuse calculations across multiple report types

### Team Adoption
1. **Start Simple**: Begin with daily standups, add complexity gradually
2. **Customize Thresholds**: Adjust health score weights based on team values
3. **Automate Inputs**: Set up CI/CD to export tool data automatically
4. **Iterate**: Refine priority scoring based on team feedback

## Limitations

### Data Requirements
- Requires structured sprint data (not suitable for ad-hoc work)
- Story points must be assigned (can't prioritize unpointed stories)
- Historical data needed for velocity trends (minimum 3 sprints)

### Accuracy Considerations
- **Priority scoring** is heuristic-based, not ML-driven (no predictive analytics)
- **Burndown predictions** assume linear velocity (doesn't account for holidays, blockers)
- **Health score** is subjective and depends on accurate weight configuration

### Scope Boundaries
- **Does NOT**: Integrate directly with tools (requires exports)
- **Does NOT**: Send notifications or update tool state (read-only)
- **Does NOT**: Replace Scrum Master judgment (augments decision-making)

### Tool-Specific Notes
- **Linear**: Requires manual JSON export (no API key support in this version)
- **Jira**: Custom fields may need mapping in `tool_adapters.py`
- **GitHub Projects**: Beta GraphQL API may change (adapter may need updates)
- **Azure DevOps**: Work item hierarchy can be complex (flatten in export)

## When NOT to Use This Skill

- **Kanban workflows**: Skill is optimized for Scrum sprints (not continuous flow)
- **Non-software projects**: Priority scoring assumes software development context
- **Single-person teams**: Overhead not justified for solo developers
- **Ad-hoc work**: Requires structured sprint planning and tracking

## Installation

### Claude Code (Recommended)
```bash
cp -r scrum-master-agent ~/.claude/skills/
```

### Claude AI Desktop
Drag the `scrum-master-agent.zip` file into Claude Desktop.

### Claude API
Use the `/v1/skills` endpoint to upload the skill package.

### Notification Setup (Optional)

Notifications are **disabled by default** and completely optional. The skill works perfectly without any notification setup.

**Option 1: Configuration File (Recommended)**
```bash
# Copy example config
cp config.example.yaml config.yaml

# Edit config.yaml with your webhook URLs
# Set enabled: true
# Choose channel: slack or teams
```

**Option 2: Environment Variables**
```bash
export NOTIFY_ENABLED=true
export NOTIFY_CHANNEL=slack  # or teams
export SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
export TEAMS_WEBHOOK_URL=https://outlook.office.com/webhook/YOUR/WEBHOOK/URL
```

**Getting Webhook URLs:**

*Slack*:
1. Go to https://api.slack.com/messaging/webhooks
2. Create app and activate Incoming Webhooks
3. Add webhook to workspace and select channel
4. Copy webhook URL

*Microsoft Teams*:
1. Open Teams channel
2. Click "..." → Connectors → Incoming Webhook
3. Configure webhook with name
4. Copy webhook URL

**Using Notifications:**
```
@scrum-master-agent

Generate daily standup summary and send notification to Slack.
```

Notifications are token-efficient (50-100 tokens max) with:
- Sprint name and status
- Velocity and health metrics
- Top 3 risks only (conditional)
- Rich formatting (Slack blocks, Teams Adaptive Cards)

## Version

**Version**: 1.1.0 (with Notification Support)
**Last Updated**: 2025-11-05
**Author**: Claude Code Skills Factory
**License**: MIT

## Support

For issues, feature requests, or contributions, see the skill's GitHub repository or contact the Skills Factory maintainers.
