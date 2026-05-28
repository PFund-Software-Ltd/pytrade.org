import { mdsvex } from 'mdsvex';
import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

const outputDir = "build";

const config = {
	preprocess: [vitePreprocess(), mdsvex()],
	kit: {
		adapter: adapter({
			// default options are shown. On some platforms
			// these options are set automatically — see below
			pages: outputDir,
			assets: outputDir,
			fallback: '200.html', // may differ from host to host
			precompress: false,
			strict: true,
		}),
		prerender: {
			// Allow routes to be skipped if they have no entries
			// This handles cases where content types (blog, tutorial, etc.) don't exist
			handleUnseenRoutes: 'warn'
		},
		// GitHub Pages serves sites from a subdirectory (e.g., username.github.io/repo-name/)
		// Set base path via BASE_PATH env var so all routes and assets are correctly prefixed
		// Without this, routes like /doc would resolve to username.github.io/doc instead of username.github.io/afterpython/doc
		paths: {
			base: process.env.BASE_PATH || '',
		},
		alias: {
			// '@': 'src/',
			'$components': 'src/lib/components/',
			'$static': 'static/',
		},
	},
	extensions: ['.svelte', '.svx']
};

export default config;
