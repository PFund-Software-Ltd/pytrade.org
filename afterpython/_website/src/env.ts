import { defineEnvVars } from '@sveltejs/kit/env';

// Dev-server URLs injected by `ap dev` (see .env.development). Unset in production builds,
// where they fall back to an empty string and the static /doc, /blog, ... routes are used instead.
export const variables = defineEnvVars({
	PUBLIC_DOC_URL: { public: true, schema: (input) => input ?? '' },
	PUBLIC_TUTORIAL_URL: { public: true, schema: (input) => input ?? '' },
	PUBLIC_EXAMPLE_URL: { public: true, schema: (input) => input ?? '' },
	PUBLIC_GUIDE_URL: { public: true, schema: (input) => input ?? '' },
	PUBLIC_BLOG_URL: { public: true, schema: (input) => input ?? '' }
});
