#!/bin/bash
#
# Package Script for Codex CLI Bridge Skill
#
# Creates a distributable ZIP file containing all necessary files
# for the codex-cli-bridge skill.
#
# Usage:
#   ./package.sh                 # Create ZIP in current directory
#   ./package.sh /output/path    # Create ZIP in specific location
#

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Package metadata
SKILL_NAME="codex-cli-bridge"
VERSION="1.0.0"
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
PACKAGE_NAME="${SKILL_NAME}-v${VERSION}-${TIMESTAMP}.zip"

# Determine output directory
if [ -n "$1" ]; then
    OUTPUT_DIR="$1"
else
    OUTPUT_DIR="."
fi

# Full output path
OUTPUT_PATH="${OUTPUT_DIR}/${PACKAGE_NAME}"

echo -e "${GREEN}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║   Codex CLI Bridge Skill - Package Creator v${VERSION}    ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════╝${NC}"
echo

# Check if zip is available
if ! command -v zip &> /dev/null; then
    echo -e "${RED}❌ Error: 'zip' command not found${NC}"
    echo "Install zip: sudo apt-get install zip (or brew install zip on macOS)"
    exit 1
fi

# Get script directory (skill root)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SKILL_DIR="$SCRIPT_DIR"

echo -e "${YELLOW}📦 Preparing package...${NC}"
echo "   Skill: ${SKILL_NAME}"
echo "   Version: ${VERSION}"
echo "   Source: ${SKILL_DIR}"
echo "   Output: ${OUTPUT_PATH}"
echo

# Create temporary directory for packaging
TEMP_DIR=$(mktemp -d)
PACKAGE_ROOT="${TEMP_DIR}/${SKILL_NAME}"
mkdir -p "${PACKAGE_ROOT}"

echo -e "${YELLOW}📋 Copying files...${NC}"

# Core Python modules
echo "   • Python modules..."
cp "${SKILL_DIR}/bridge.py" "${PACKAGE_ROOT}/"
cp "${SKILL_DIR}/safety_mechanism.py" "${PACKAGE_ROOT}/"
cp "${SKILL_DIR}/claude_parser.py" "${PACKAGE_ROOT}/"
cp "${SKILL_DIR}/project_analyzer.py" "${PACKAGE_ROOT}/"
cp "${SKILL_DIR}/agents_md_generator.py" "${PACKAGE_ROOT}/"
cp "${SKILL_DIR}/skill_documenter.py" "${PACKAGE_ROOT}/"
cp "${SKILL_DIR}/codex_executor.py" "${PACKAGE_ROOT}/"

# Make bridge.py executable
chmod +x "${PACKAGE_ROOT}/bridge.py"

# Documentation
echo "   • Documentation..."
cp "${SKILL_DIR}/SKILL.md" "${PACKAGE_ROOT}/"
cp "${SKILL_DIR}/README.md" "${PACKAGE_ROOT}/"
cp "${SKILL_DIR}/HOW_TO_USE.md" "${PACKAGE_ROOT}/"
cp "${SKILL_DIR}/INSTALL.md" "${PACKAGE_ROOT}/"
cp "${SKILL_DIR}/CHANGELOG.md" "${PACKAGE_ROOT}/"

# Sample files
echo "   • Sample files..."
cp "${SKILL_DIR}/sample_input.json" "${PACKAGE_ROOT}/"
cp "${SKILL_DIR}/expected_output.json" "${PACKAGE_ROOT}/"

# Templates directory (if exists)
if [ -d "${SKILL_DIR}/templates" ]; then
    echo "   • Templates..."
    mkdir -p "${PACKAGE_ROOT}/templates"
    cp -r "${SKILL_DIR}/templates/"* "${PACKAGE_ROOT}/templates/" 2>/dev/null || true
fi

# License (if exists)
if [ -f "${SKILL_DIR}/LICENSE" ]; then
    echo "   • License..."
    cp "${SKILL_DIR}/LICENSE" "${PACKAGE_ROOT}/"
else
    echo "   ⚠️  License file not found (skipping)"
fi

# Create VERSION file
echo "${VERSION}" > "${PACKAGE_ROOT}/VERSION"
echo "$(date +"%Y-%m-%d %H:%M:%S")" > "${PACKAGE_ROOT}/BUILD_DATE"

# Create installation instructions
cat > "${PACKAGE_ROOT}/INSTALL_QUICK.txt" << 'EOF'
QUICK INSTALLATION GUIDE
========================

1. Extract this ZIP file
2. Copy the codex-cli-bridge folder to ~/.claude/skills/
3. Install dependencies: pip3 install PyYAML
4. Verify: python3 ~/.claude/skills/codex-cli-bridge/bridge.py --validate

For detailed instructions, see INSTALL.md

Requirements:
- Codex CLI v0.48.0+
- Python 3.7+
- PyYAML library
EOF

echo
echo -e "${YELLOW}📦 Creating ZIP package...${NC}"

# Change to temp directory and create zip
cd "${TEMP_DIR}"
zip -r "${OUTPUT_PATH}" "${SKILL_NAME}" > /dev/null

# Get file size
FILE_SIZE=$(du -h "${OUTPUT_PATH}" | cut -f1)

echo
echo -e "${GREEN}✅ Package created successfully!${NC}"
echo
echo "   📦 Package: ${PACKAGE_NAME}"
echo "   📏 Size: ${FILE_SIZE}"
echo "   📍 Location: ${OUTPUT_PATH}"
echo

# Calculate checksum
if command -v sha256sum &> /dev/null; then
    CHECKSUM=$(sha256sum "${OUTPUT_PATH}" | cut -d' ' -f1)
    echo "   🔒 SHA256: ${CHECKSUM}"
    echo "${CHECKSUM}" > "${OUTPUT_PATH}.sha256"
    echo "   Checksum saved to: ${OUTPUT_PATH}.sha256"
    echo
elif command -v shasum &> /dev/null; then
    CHECKSUM=$(shasum -a 256 "${OUTPUT_PATH}" | cut -d' ' -f1)
    echo "   🔒 SHA256: ${CHECKSUM}"
    echo "${CHECKSUM}" > "${OUTPUT_PATH}.sha256"
    echo "   Checksum saved to: ${OUTPUT_PATH}.sha256"
    echo
fi

# List contents
echo -e "${YELLOW}📋 Package contents:${NC}"
unzip -l "${OUTPUT_PATH}" | tail -n +4 | head -n -2 | awk '{print "   " $4}'
echo

# Clean up temp directory
rm -rf "${TEMP_DIR}"

echo -e "${GREEN}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║              Package Creation Complete! 🎉               ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════╝${NC}"
echo
echo "Next steps:"
echo "  1. Test the package:"
echo "     unzip ${PACKAGE_NAME}"
echo "     python3 ${SKILL_NAME}/bridge.py --validate"
echo
echo "  2. Distribute the package:"
echo "     Upload ${PACKAGE_NAME} to your distribution channel"
echo
echo "  3. Verify checksum (optional):"
echo "     sha256sum -c ${PACKAGE_NAME}.sha256"
echo

exit 0
