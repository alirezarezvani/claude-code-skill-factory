"""
Agent Generator
Creates Claude Code agent files with enhanced YAML frontmatter and validation.
"""

from typing import Dict, List, Any, Optional
import re


class AgentGenerator:
    """Generates Claude Code agent .md files with proper formatting."""

    # Color assignments by agent type
    COLOR_MAP = {
        "Strategic": "blue",
        "Implementation": "green",
        "Quality": "red",
        "Coordination": "purple",
        "Domain-Specific": "orange"
    }

    # Tool recommendations by agent type
    TOOL_RECOMMENDATIONS = {
        "Strategic": ["Read", "Write", "Grep"],
        "Implementation": ["Read", "Write", "Edit", "Bash", "Grep", "Glob"],
        "Quality": ["Read", "Write", "Edit", "Bash", "Grep", "Glob"],
        "Coordination": ["Read", "Write", "Grep"]
    }

    # Model recommendations
    MODEL_RECOMMENDATIONS = {
        "Strategic": "opus",  # Strategic thinking benefits from Opus
        "Implementation": "sonnet",  # Code generation works well with Sonnet
        "Quality": "sonnet",  # Testing and validation with Sonnet
        "Coordination": "opus"  # Orchestration benefits from Opus reasoning
    }

    def __init__(self):
        """Initialize agent generator."""
        pass

    def generate_agent(self, config: Dict[str, Any]) -> str:
        """
        Generate a complete agent .md file.

        Args:
            config: Agent configuration dictionary

        Returns:
            Complete agent file content as string
        """
        # Validate required fields
        self._validate_config(config)

        # Generate YAML frontmatter
        yaml_frontmatter = self._generate_yaml(config)

        # Generate system prompt
        system_prompt = config.get("system_prompt", "")

        # Combine into complete agent file
        agent_file = f"{yaml_frontmatter}\n{system_prompt}"

        return agent_file

    def _validate_config(self, config: Dict[str, Any]) -> None:
        """
        Validate agent configuration.

        Args:
            config: Configuration to validate

        Raises:
            ValueError: If configuration is invalid
        """
        required_fields = ["agent_name", "description"]

        for field in required_fields:
            if field not in config or not config[field]:
                raise ValueError(f"Required field '{field}' is missing")

        # Validate kebab-case name
        name = config["agent_name"]
        if not re.match(r'^[a-z]+(-[a-z]+)*$', name):
            raise ValueError(f"Agent name '{name}' must be in kebab-case (lowercase-with-hyphens)")

        # Validate agent type
        valid_types = ["Strategic", "Implementation", "Quality", "Coordination", "Domain-Specific"]
        agent_type = config.get("agent_type", "")
        if agent_type and agent_type not in valid_types:
            raise ValueError(f"Agent type must be one of: {', '.join(valid_types)}")

    def _generate_yaml(self, config: Dict[str, Any]) -> str:
        """
        Generate YAML frontmatter with enhanced fields.

        Args:
            config: Agent configuration

        Returns:
            YAML frontmatter as string
        """
        name = config["agent_name"]
        description = config["description"]

        # Get or infer tools
        tools = config.get("tools")
        if not tools:
            agent_type = config.get("agent_type", "Implementation")
            tools = ", ".join(self.TOOL_RECOMMENDATIONS.get(agent_type, ["Read", "Write", "Edit"]))
        elif isinstance(tools, list):
            tools = ", ".join(tools)

        # Get or infer model
        model = config.get("model")
        if not model:
            agent_type = config.get("agent_type", "Implementation")
            model = self.MODEL_RECOMMENDATIONS.get(agent_type, "sonnet")

        # Get or infer color
        color = config.get("color")
        if not color:
            agent_type = config.get("agent_type", "Implementation")
            color = self.COLOR_MAP.get(agent_type, "green")

        # Get field (domain)
        field = config.get("field", "general")

        # Get expertise level
        expertise = config.get("expertise", "intermediate")

        # Get MCP tools
        mcp_tools = config.get("mcp_tools", "")
        if isinstance(mcp_tools, list):
            mcp_tools = ", ".join(mcp_tools)

        # Build YAML frontmatter
        yaml_lines = [
            "---",
            f"name: {name}",
            f"description: {description}"
        ]

        # Add optional fields
        if tools:
            yaml_lines.append(f"tools: {tools}")

        if model:
            yaml_lines.append(f"model: {model}")

        yaml_lines.append(f"color: {color}")
        yaml_lines.append(f"field: {field}")
        yaml_lines.append(f"expertise: {expertise}")

        if mcp_tools:
            yaml_lines.append(f"mcp_tools: {mcp_tools}")

        yaml_lines.append("---")

        return "\n".join(yaml_lines)

    def validate_yaml_format(self, yaml_content: str) -> Dict[str, Any]:
        """
        Validate YAML frontmatter format.

        Args:
            yaml_content: YAML frontmatter content

        Returns:
            Validation result with errors if any
        """
        errors = []

        # Check for opening/closing ---
        if not yaml_content.startswith("---\n"):
            errors.append("YAML must start with '---'")

        if "\n---" not in yaml_content[4:]:
            errors.append("YAML must end with '---'")

        # Extract YAML content
        yaml_body = yaml_content.split("---")[1] if "---" in yaml_content else ""

        # Check for name field with kebab-case
        name_match = re.search(r'^name:\s*(.+)$', yaml_body, re.MULTILINE)
        if not name_match:
            errors.append("Missing 'name' field")
        elif name_match:
            name_value = name_match.group(1).strip()
            if not re.match(r'^[a-z]+(-[a-z]+)*$', name_value):
                errors.append(f"Name '{name_value}' must be kebab-case (lowercase-with-hyphens)")

        # Check for description
        if "description:" not in yaml_body:
            errors.append("Missing 'description' field")

        # Check tools format (comma-separated, not array)
        if "tools:" in yaml_body:
            tools_match = re.search(r'^tools:\s*(.+)$', yaml_body, re.MULTILINE)
            if tools_match:
                tools_value = tools_match.group(1).strip()
                if tools_value.startswith("[") or tools_value.startswith("{"):
                    errors.append("Tools must be comma-separated string, not array format")

        return {
            "valid": len(errors) == 0,
            "errors": errors
        }


def generate_agent_file(
    agent_name: str,
    description: str,
    system_prompt: str,
    agent_type: str = "Implementation",
    field: str = "general",
    tools: Optional[str] = None,
    model: Optional[str] = None,
    color: Optional[str] = None,
    expertise: str = "intermediate",
    mcp_tools: Optional[str] = None
) -> str:
    """
    Convenience function to generate an agent file.

    Args:
        agent_name: Kebab-case agent name
        description: When to invoke this agent
        system_prompt: Complete system prompt instructions
        agent_type: Strategic, Implementation, Quality, or Coordination
        field: Domain area
        tools: Comma-separated tool list (optional)
        model: Model to use (optional)
        color: Visual color coding (optional)
        expertise: beginner, intermediate, or expert
        mcp_tools: Comma-separated MCP tools (optional)

    Returns:
        Complete agent .md file content
    """
    config = {
        "agent_name": agent_name,
        "description": description,
        "system_prompt": system_prompt,
        "agent_type": agent_type,
        "field": field,
        "expertise": expertise
    }

    if tools:
        config["tools"] = tools
    if model:
        config["model"] = model
    if color:
        config["color"] = color
    if mcp_tools:
        config["mcp_tools"] = mcp_tools

    generator = AgentGenerator()
    return generator.generate_agent(config)
