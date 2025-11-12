# CLAUDE.md

Quick guidance for this prototype project.

## Overview

Rapid prototyping project using TypeScript, React, and Node.js. Focus on speed and iteration over production-readiness.

## Project Structure

```
project-root/
├── src/
│   ├── components/      # React components
│   ├── pages/           # Page components
│   ├── hooks/           # Custom hooks
│   └── utils/           # Utility functions
├── public/              # Static assets
├── tests/               # Test files
├── package.json
├── tsconfig.json
└── README.md
```

## File Structure

- **src/components/** - Reusable UI components
- **src/pages/** - Route-level page components
- **src/hooks/** - Custom React hooks for shared logic
- **src/utils/** - Helper functions and utilities
- **tests/** - Unit and integration tests

## Setup & Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Run tests
npm test
```

## Core Principles

1. **Move Fast**: Prioritize speed over perfection
2. **Keep It Simple**: Avoid unnecessary complexity
3. **Iterate Quickly**: Test and refine rapidly

## Tech Stack

- **Frontend**: TypeScript, React
- **Backend**: Node.js, Express
- **Build**: Vite
- **Testing**: Jest, React Testing Library

## Development Workflow

1. Create feature branch: `git checkout -b feature/name`
2. Implement and test locally
3. Commit changes: `git commit -m "Add feature"`
4. Push to remote: `git push`
5. Deploy to staging for testing

## Quick Commands

```bash
npm run dev          # Start development server
npm test             # Run all tests
npm run build        # Build for production
npm run lint         # Check code quality
```

---

**Project Type**: Prototype
**Team Size**: Solo
**Lines**: ~75 (Minimal template with native format)
