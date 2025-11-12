# Frontend Development Guidelines

This file provides guidance for frontend development in this project.

## Overview

React 18 SPA with TypeScript, Tailwind CSS, and React Query for server state. Component-based architecture with hooks, performance optimization, and comprehensive testing.

## Project Structure

```
frontend/
├── src/
│   ├── components/          # Reusable components
│   │   ├── common/          # Shared UI components
│   │   │   ├── Button.tsx
│   │   │   ├── Input.tsx
│   │   │   └── Modal.tsx
│   │   ├── layout/          # Layout components
│   │   │   ├── Header.tsx
│   │   │   ├── Footer.tsx
│   │   │   └── Sidebar.tsx
│   │   └── features/        # Feature-specific components
│   │       ├── UserList.tsx
│   │       └── ProductCard.tsx
│   ├── pages/               # Page components (routes)
│   │   ├── HomePage.tsx
│   │   ├── UserPage.tsx
│   │   └── NotFoundPage.tsx
│   ├── hooks/               # Custom React hooks
│   │   ├── useAuth.ts
│   │   ├── useUser.ts
│   │   └── useLocalStorage.ts
│   ├── store/               # State management
│   │   ├── AuthContext.tsx
│   │   └── ThemeContext.tsx
│   ├── services/            # API client functions
│   │   ├── api.ts
│   │   ├── auth.service.ts
│   │   └── user.service.ts
│   ├── utils/               # Utility functions
│   │   ├── formatters.ts
│   │   ├── validators.ts
│   │   └── constants.ts
│   ├── styles/              # Global styles
│   │   └── global.css
│   ├── types/               # TypeScript types
│   │   ├── user.types.ts
│   │   └── api.types.ts
│   ├── App.tsx              # Root component
│   ├── main.tsx             # Entry point
│   └── router.tsx           # Route definitions
├── public/                  # Static assets
│   ├── images/
│   ├── fonts/
│   └── favicon.ico
├── tests/
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests
│   └── e2e/                 # End-to-end tests
├── .env.example
├── package.json
├── vite.config.ts
├── tailwind.config.js
└── tsconfig.json
```

## File Structure

- **components/** - Reusable UI components
  - **common/** - Shared components (Button, Input, Modal)
  - **layout/** - Layout components (Header, Footer, Sidebar)
  - **features/** - Feature-specific components
- **pages/** - Page-level components mapped to routes
- **hooks/** - Custom React hooks for shared logic
- **store/** - Context providers for global state (auth, theme)
- **services/** - API client functions and HTTP calls
- **utils/** - Helper functions, formatters, validators
- **types/** - TypeScript type definitions and interfaces

## Architecture

**Component Hierarchy**: App → Router → Pages → Features → Common

**State Management**:
- **Local State**: `useState` for component-specific state
- **Global State**: Context API for auth, theme, user
- **Server State**: React Query for API data caching
- **Form State**: React Hook Form for complex forms

**Flow**:
```
User Action → Component → Service → API → React Query Cache → Component Update
```

## Setup & Installation

```bash
# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with:
# - VITE_API_URL (backend API URL)
# - VITE_ENV (development/staging/production)

# Start development server
npm run dev

# Server runs at http://localhost:5173
```

## Component Standards

### Functional Components with Hooks

- Prefer functional components with hooks over class components
- Use TypeScript for all components
- Keep components small and focused (< 200 lines)
- Extract reusable logic into custom hooks
- Use composition over inheritance

### Component Structure

```typescript
interface Props {
  userId: string;
  onUpdate?: () => void;
}

export function UserProfile({ userId, onUpdate }: Props) {
  // 1. Hooks first
  const { data, loading, error } = useUserData(userId);
  const [isEditing, setIsEditing] = useState(false);

  // 2. Event handlers
  const handleEdit = () => setIsEditing(true);

  // 3. Early returns
  if (loading) return <Spinner />;
  if (error) return <ErrorMessage error={error} />;

  // 4. Main render
  return <div>{/* component JSX */}</div>;
}
```

### TypeScript Best Practices

- Define interfaces for all props
- Use `type` for unions and primitives
- Avoid `any` - use `unknown` if truly dynamic
- Export types alongside components

## State Management

### Local State

- Keep component state local when possible
- Use `useState` for simple values
- Use `useReducer` for complex state logic

### Global State (Context API)

- Use Context API for app-wide state (theme, auth, user)
- Example: AuthContext, ThemeContext
- Avoid overuse - not for all shared state

### Server State (React Query)

- Use React Query for server state management
- Automatic caching, refetching, and updates
- Example:
  ```typescript
  const { data, isLoading, error } = useQuery({
    queryKey: ['users', userId],
    queryFn: () => fetchUser(userId)
  });
  ```

### Best Practices

- Avoid prop drilling - use context for deep state
- Document state shape and update patterns
- Keep state as close to usage as possible

## Styling Guidelines

### Tailwind CSS

- Use Tailwind CSS utility classes
- Create reusable component classes in `tailwind.config.js`
- Avoid inline styles except for truly dynamic values
- Use CSS variables for theming in `global.css`

### Responsive Design

- Ensure responsive design for all breakpoints (mobile-first)
- Breakpoints: `sm:` (640px), `md:` (768px), `lg:` (1024px), `xl:` (1280px)
- Test on mobile, tablet, desktop

### Dark Mode

- Implement dark mode with `dark:` variant
- Use CSS variables for theme colors
- Respect user's system preference

## Performance Optimization

### Code Splitting

- Lazy load routes with `React.lazy()` and `Suspense`
- Lazy load heavy components (charts, editors, modals)
- Example:
  ```typescript
  const Dashboard = lazy(() => import('./pages/Dashboard'));
  ```

### Image Optimization

- Optimize images (use WebP, AVIF formats)
- Use lazy loading with `loading="lazy"` attribute
- Serve responsive images with `srcset`

### Bundle Optimization

- Minimize bundle size - analyze with `npm run analyze`
- Use tree-shaking (import only what you need)
- Avoid importing entire libraries

### React Optimization

- Use `useMemo` for expensive calculations
- Use `useCallback` for function props
- Use `React.memo` for expensive components
- Avoid unnecessary re-renders

## Testing Requirements

### Unit Tests

- Write unit tests for utility functions
- Test business logic separately from UI
- Mock external dependencies
- Aim for 80%+ code coverage

### Component Tests

- Write component tests with React Testing Library
- Test user interactions, not implementation details
- Test accessibility (keyboard, screen readers)
- Example:
  ```typescript
  test('renders user profile', () => {
    render(<UserProfile userId="123" />);
    expect(screen.getByText(/profile/i)).toBeInTheDocument();
  });
  ```

### API Mocking

- Mock API calls with MSW (Mock Service Worker)
- Create realistic mock responses
- Test loading and error states

### E2E Tests

- Write E2E tests with Playwright for critical flows
- Test complete user journeys
- Run E2E tests in CI/CD

```bash
# Run tests
npm test                  # All tests
npm run test:unit         # Unit tests only
npm run test:e2e          # E2E tests with Playwright
npm run test:coverage     # With coverage report
```

## Accessibility (a11y)

### Semantic HTML

- Use semantic HTML elements (`<button>`, `<nav>`, `<main>`, `<article>`)
- Don't use `<div>` for interactive elements
- Use proper heading hierarchy (`<h1>` → `<h2>` → `<h3>`)

### Keyboard Navigation

- Ensure keyboard navigation works
- Test with Tab, Enter, Escape keys
- Add focus styles (don't remove outline)

### ARIA Labels

- Add ARIA labels where needed
- Use `aria-label`, `aria-labelledby`, `aria-describedby`
- Test with screen readers (VoiceOver, NVDA)

### Color Contrast

- Maintain color contrast ratios (WCAG AA minimum 4.5:1)
- Test with browser DevTools accessibility panel
- Don't rely on color alone to convey information

## Error Handling

### Error Boundaries

- Use Error Boundaries for component errors
- Implement fallback UI
- Log errors to monitoring service (Sentry)

### User-Friendly Messages

- Show user-friendly error messages
- Avoid technical jargon
- Provide actionable next steps

### Async Error Handling

- Handle loading and error states in all async operations
- Example:
  ```typescript
  if (isLoading) return <Spinner />;
  if (error) return <ErrorMessage error={error} />;
  ```

## Custom Hooks Pattern

Create custom hooks for reusable logic:

```typescript
function useUserData(userId: string) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchUserData(userId)
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [userId]);

  return { data, loading, error };
}
```

## Common Commands

```bash
# Development
npm run dev              # Start dev server (http://localhost:5173)
npm test                 # Run all tests
npm run test:watch       # Run tests in watch mode
npm run lint             # Run ESLint
npm run type-check       # TypeScript check
npm run format           # Format code with Prettier

# Production
npm run build            # Build for production
npm run preview          # Preview production build locally
npm run analyze          # Analyze bundle size

# Testing
npm run test:unit        # Unit tests only
npm run test:e2e         # E2E tests with Playwright
npm run test:coverage    # Coverage report
```

## Development Best Practices

- **Component Organization**: One component per file
- **Naming**: PascalCase for components, camelCase for functions/variables
- **Props**: Destructure props in function signature
- **Imports**: Group imports (React, libraries, local)
- **Comments**: Write comments for complex logic only
- **Console Logs**: Remove before committing

---

**Context**: Frontend (React/TypeScript/Tailwind)
**Lines**: ~225 (Frontend-specific template with native format)
