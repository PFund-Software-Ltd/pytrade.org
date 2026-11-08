// All valid content types (single source of truth)
// Kept free of `$app/*` imports: src/params.ts imports this and is loaded directly by Node.
export const CONTENT_TYPES = ['blog', 'tutorial', 'example', 'guide'] as const;
