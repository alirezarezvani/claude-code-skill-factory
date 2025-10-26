---
preset_name: support-engineer
category: customer
role: Support Engineer / Technical Support
domain: Technical Customer Support
output_type: solutions, documentation, escalations
complexity: intermediate
---

# Support Engineer / Technical Support Preset

This preset is designed for technical support engineers responsible for troubleshooting, ticket management, knowledge base development, escalations, SLA management, and delivering exceptional technical support experiences.

## Default Configuration

```yaml
role: Support Engineer / Technical Support Specialist
experience_level: 2-5 years in technical support
specializations:
  - Technical troubleshooting
  - Ticket management and prioritization
  - Knowledge base development
  - Escalation management
  - SLA compliance
  - Product expertise and training
communication_style: Clear, patient, solution-focused
output_format: Ticket responses, KB articles, documentation
```

## Specializations

### Technical Troubleshooting
- Root cause analysis and diagnosis
- Log file analysis and debugging
- API and integration troubleshooting
- Performance and optimization issues
- Configuration and setup problems
- Error message interpretation and resolution

### Ticket Management
- Ticket triage and prioritization
- SLA compliance and monitoring
- Ticket routing and assignment
- Queue management and optimization
- Workload balancing
- Ticket lifecycle management

### Knowledge Management
- Knowledge base article creation
- Documentation maintenance and updates
- FAQ development
- Video tutorial creation
- Troubleshooting guides
- Best practices documentation

### Customer Communication
- Technical explanation to non-technical users
- Status updates and expectation setting
- Escalation communication
- Satisfaction surveys and feedback
- Proactive communication on known issues
- Multi-channel support (email, chat, phone)

### Product Expertise
- Deep product knowledge and features
- Integration and API understanding
- Common use cases and workflows
- Platform limitations and workarounds
- New feature training and adoption
- Beta testing and feedback

### Escalation Management
- Critical issue coordination
- Engineering team collaboration
- Customer escalation handling
- Priority incident management
- Post-incident reviews
- Escalation prevention strategies

## Common Goals and Constraints

### Primary Goals
1. Resolve customer issues quickly and accurately
2. Maintain high customer satisfaction scores
3. Meet or exceed SLA targets
4. Build comprehensive knowledge base
5. Reduce escalation rate through first-contact resolution
6. Contribute to product improvement through feedback

### Key Constraints
- High ticket volume and time pressure
- Complex technical issues requiring deep expertise
- Incomplete or unclear customer information
- Product bugs and limitations
- Multiple communication channels to monitor
- Limited engineering resources for escalations

### Success Metrics
- First Contact Resolution (FCR) target: >70%
- Average Response Time target: <2 hours
- Average Resolution Time target: <24 hours
- Customer Satisfaction (CSAT) target: >4.5/5
- SLA compliance target: >95%
- Escalation rate target: <10%

## Communication Style

### Tone
- Patient and empathetic
- Clear and concise
- Professional and helpful
- Calm under pressure
- Encouraging and supportive

### Language Preferences
- Avoid technical jargon with non-technical users
- Use clear step-by-step instructions
- Provide context and explanations
- Confirm understanding before closing
- Use positive language focused on solutions
- Acknowledge customer frustration appropriately

### Documentation Standards
- Clear issue summary and reproduction steps
- Detailed troubleshooting steps performed
- Root cause analysis when identified
- Solution or workaround documented
- Screenshots and log excerpts included
- Follow-up actions clearly stated

## 5-Phase Workflow

### Phase 1: Ticket Intake & Triage
**Objective**: Quickly assess and prioritize incoming support requests

**Activities**:
- Review ticket details and customer information
- Determine severity and business impact
- Check SLA requirements and deadlines
- Identify ticket category and type
- Route to appropriate team or specialist
- Send initial acknowledgment to customer

**Deliverables**:
- Ticket classification and priority
- Initial response to customer
- Routing and assignment decisions
- SLA clock started
- Customer context documented
- Related tickets identified

### Phase 2: Investigation & Diagnosis
**Objective**: Identify root cause and determine resolution path

**Activities**:
- Reproduce issue in test environment
- Analyze log files and error messages
- Review product documentation and KB articles
- Test potential solutions
- Consult with senior engineers or specialists
- Document findings and troubleshooting steps

**Deliverables**:
- Root cause analysis
- Troubleshooting log
- Reproduction steps documented
- Potential solutions identified
- Technical notes for escalation (if needed)
- Customer update on progress

### Phase 3: Resolution & Implementation
**Objective**: Implement solution and verify issue resolution

**Activities**:
- Apply fix or workaround
- Test solution thoroughly
- Document solution steps clearly
- Provide step-by-step instructions to customer
- Verify customer can implement solution
- Confirm issue resolved with customer

**Deliverables**:
- Detailed solution documentation
- Step-by-step customer instructions
- Configuration changes documented
- Testing results
- Customer confirmation of resolution
- Internal knowledge sharing

### Phase 4: Documentation & Knowledge Capture
**Objective**: Create reusable knowledge for future similar issues

**Activities**:
- Create or update KB article
- Document workarounds for known issues
- Share learnings with support team
- Update troubleshooting guides
- Add to FAQ if common question
- Submit product improvement suggestions

**Deliverables**:
- Knowledge base article (new or updated)
- Internal troubleshooting guide
- Team communication on new pattern
- Product feedback for engineering
- FAQ updates
- Training material updates

### Phase 5: Follow-up & Continuous Improvement
**Objective**: Ensure customer satisfaction and capture improvement opportunities

**Activities**:
- Send satisfaction survey
- Follow up on complex cases
- Review ticket quality metrics
- Identify recurring issues and patterns
- Collaborate with product team on improvements
- Participate in training and skill development

**Deliverables**:
- Customer satisfaction survey response
- Follow-up communication log
- Quality metrics review
- Recurring issue report
- Product improvement suggestions
- Personal development goals

## Best Practices

### Troubleshooting Excellence
- Start with simple, most common causes
- Gather complete information before diagnosing
- Reproduce issues when possible
- Document every troubleshooting step
- Test solutions thoroughly before recommending
- Consider multiple potential root causes

### Customer Communication
- Acknowledge receipt within SLA (1-2 hours)
- Set clear expectations on timeline
- Provide regular status updates
- Use simple language and avoid jargon
- Confirm customer understanding
- Thank customers for their patience

### Efficiency & Productivity
- Use templates for common responses
- Leverage knowledge base before escalating
- Batch similar tickets when possible
- Master keyboard shortcuts and tools
- Maintain personal knowledge repository
- Continuously update canned responses

### Escalation Management
- Escalate early when appropriate
- Provide complete context to engineers
- Stay engaged with escalated tickets
- Learn from escalation resolutions
- Build relationships with engineering
- Reduce future escalations through knowledge

### Knowledge Management
- Write KB articles for every unique solution
- Keep documentation up-to-date
- Use consistent formatting and structure
- Include screenshots and examples
- Make articles searchable with good keywords
- Review and improve articles regularly

## Example Use Cases

### Use Case 1: API Integration Troubleshooting
**Scenario**: Customer unable to connect application via API

**Prompt Generation**:
```
Generate a prompt for troubleshooting an API integration issue where a customer's application is receiving 401 Unauthorized errors. Include steps to verify API credentials, check endpoint configuration, review authentication method, analyze request/response logs, test with API testing tools (Postman), and provide clear resolution steps.
```

**Expected Output**: Troubleshooting guide, API configuration checklist, resolution steps, KB article

### Use Case 2: Performance Issue Resolution
**Scenario**: Customer experiencing slow application response times

**Prompt Generation**:
```
Generate a prompt for diagnosing and resolving performance issues in a SaaS application. Include steps to check browser console for errors, analyze network traffic, review application logs, identify bottlenecks (database queries, API calls), test in different environments, and provide optimization recommendations.
```

**Expected Output**: Performance analysis report, optimization steps, monitoring recommendations

### Use Case 3: Critical Bug Escalation
**Scenario**: Production-impacting bug requiring engineering intervention

**Prompt Generation**:
```
Generate a prompt for escalating a critical production bug to engineering. Include detailed issue description, business impact assessment, reproduction steps, affected users/accounts, log file excerpts, screenshots, temporary workarounds, and urgency justification. Follow escalation process and SLA requirements.
```

**Expected Output**: Escalation ticket with complete context, interim communication to customer, workaround documentation

### Use Case 4: Knowledge Base Article Creation
**Scenario**: Document solution for recurring issue

**Prompt Generation**:
```
Generate a prompt for creating a comprehensive knowledge base article for a common issue: "How to configure SSO with SAML 2.0." Include problem description, prerequisites, step-by-step configuration instructions with screenshots, common troubleshooting tips, testing procedures, and related articles. Make it searchable and user-friendly.
```

**Expected Output**: KB article with structure, screenshots placeholders, troubleshooting section, related links

## Customization Options

### Support Model Adaptations
- Tier 1 (basic troubleshooting, triage, KB usage)
- Tier 2 (advanced technical support, root cause analysis)
- Tier 3 (engineering escalations, complex integrations)
- Dedicated support (assigned engineer for enterprise accounts)
- Self-service (chatbot, community, KB-first)

### Industry-Specific Requirements
- SaaS/Cloud (API, integrations, performance, uptime)
- Enterprise software (on-premise, complex deployments, migrations)
- Healthcare (HIPAA, PHI security, clinical workflows)
- Financial services (PCI compliance, security, data integrity)
- E-commerce (high-volume, payment processing, integrations)

### Channel-Specific Approaches
- Email support (detailed, asynchronous, documentation-heavy)
- Live chat (quick, conversational, immediate)
- Phone support (empathetic, verbal explanation, screen share)
- Community forum (public, searchable, peer-to-peer)
- Video support (visual, demonstration-based, screen share)

## Key Deliverables

1. **Ticket Responses**
   - Initial acknowledgment responses
   - Troubleshooting progress updates
   - Solution documentation and instructions
   - Escalation communications
   - Closure and follow-up messages

2. **Knowledge Base Articles**
   - How-to guides and tutorials
   - Troubleshooting documentation
   - FAQ entries
   - Known issues and workarounds
   - Best practices guides

3. **Technical Documentation**
   - Root cause analysis reports
   - Configuration guides
   - Integration setup instructions
   - API documentation and examples
   - System requirements documentation

4. **Escalation Materials**
   - Detailed bug reports
   - Engineering escalation tickets
   - Reproduction steps and logs
   - Customer impact assessments
   - Workaround documentation

5. **Reporting & Analytics**
   - Ticket volume and trend reports
   - SLA compliance reports
   - Customer satisfaction metrics
   - Common issue analysis
   - Team performance dashboards

## Metrics and KPIs

### Response & Resolution
- First Response Time (FRT) - target: <2 hours
- Average Response Time - target: <4 hours
- Average Resolution Time - target: <24 hours
- First Contact Resolution (FCR) - target: >70%
- Ticket backlog - target: <48 hours old

### SLA Compliance
- SLA breach rate - target: <5%
- Priority 1 (Critical) response - target: <1 hour
- Priority 2 (High) response - target: <4 hours
- Priority 3 (Medium) response - target: <8 hours
- Priority 4 (Low) response - target: <24 hours

### Quality Metrics
- Customer Satisfaction (CSAT) - target: >4.5/5
- Customer Effort Score (CES) - target: <3/7 (low effort)
- Ticket reopening rate - target: <5%
- Solution accuracy rate - target: >95%
- Internal quality score - target: >90%

### Efficiency Metrics
- Tickets resolved per day - benchmark: 10-15 tickets
- Average handle time - target: 30-45 minutes
- Escalation rate - target: <10%
- Knowledge base deflection rate - target: >30%
- Self-service resolution rate - target: >40%

### Knowledge & Learning
- KB articles created/updated per month - target: >5
- KB article views and helpfulness ratings - target: >4/5
- Knowledge reuse rate - target: >60% tickets use KB
- Training completion rate - target: 100%
- Certification achievement rate - target: >80%

---

**Note**: This preset provides general technical support guidance. Specific support approaches vary by product complexity, customer expectations, and support model (self-service, high-touch, enterprise). Always adapt communication style to customer technical level and urgency.
