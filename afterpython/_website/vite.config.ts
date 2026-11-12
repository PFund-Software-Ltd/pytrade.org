// vp migrate: merged .oxlintrc.json (f622ab95f47822c0c75ab1ce554f056b).
import { mdsvex } from 'mdsvex';
import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import tailwindcss from '@tailwindcss/vite';
import { sveltekit } from '@sveltejs/kit/vite';
import { existsSync, readFileSync } from 'node:fs';
import { COMMENT_CONTENT_TYPES, injectCommentsScript } from './scripts/inject-comments.ts';
import { defineConfig, lazyPlugins, type Plugin } from 'vite-plus';

const outputDir = 'build';

// Dev only: serve static/<dir>/index.html for directory URLs (e.g. /doc/, /api_reference/),
// as static hosts do in production. Lets plain `vp dev` open the prebuilt MyST pages in static/.
// Also injects the comment loader into content pages (done by scripts/inject-comments.ts on build).
function serveStaticDirIndex(): Plugin {
	return {
		name: 'serve-static-dir-index',
		apply: 'serve',
		configureServer(server) {
			server.middlewares.use((req, res, next) => {
				const url = new URL(req.url ?? '/', 'http://localhost');
				const base = server.config.base.replace(/\/$/, '');
				const dir = url.pathname.slice(base.length).replace(/\/$/, '');
				const file =
					dir && !dir.includes('.') && existsSync(`static${dir}/index.html`)
						? `${dir}/index.html`
						: dir.endsWith('.html') && existsSync(`static${dir}`)
							? dir
							: '';
				if (!file) return next();
				if (COMMENT_CONTENT_TYPES.includes(file.split('/')[1])) {
					res.setHeader('Content-Type', 'text/html; charset=utf-8');
					return res.end(injectCommentsScript(readFileSync(`static${file}`, 'utf-8'), base));
				}
				req.url = `${base}${file}${url.search}`;
				next();
			});
		}
	};
}

// Dev only: static/*.json (faq.json, metadata.json, blog.json, ...) is imported by server
// load functions only, so Vite never tells the browser to reload when it changes.
// `ap dev` rewrites these files while running; reload open pages so edits show up.
function reloadOnStaticData(): Plugin {
	return {
		name: 'reload-on-static-data',
		apply: 'serve',
		configureServer(server) {
			const reload = (file: string) => {
				if (/[/\\]static[/\\][^/\\]+\.json$/.test(file)) {
					server.ws.send({ type: 'full-reload' });
				}
			};
			server.watcher.on('change', reload);
			server.watcher.on('add', reload);
			server.watcher.on('unlink', reload);
		}
	};
}

export default defineConfig(({ mode }) => {
	const isDev = mode === 'development';
	return {
		lint: {
			plugins: ['oxc', 'typescript', 'unicorn'],
			jsPlugins: [
				'eslint-plugin-svelte',
				{
					name: 'vite-plus',
					specifier: 'vite-plus/oxlint-plugin'
				}
			],
			categories: {
				correctness: 'warn'
			},
			env: {
				builtin: true,
				browser: true,
				node: true
			},
			ignorePatterns: [
				'**/node_modules',
				'**/.output',
				'**/.vercel',
				'**/.netlify',
				'**/.wrangler',
				'.svelte-kit',
				'build',
				'**/.DS_Store',
				'**/Thumbs.db',
				'**/.env',
				'**/.env.*',
				'!**/.env.example',
				'!**/.env.test',
				'**/vite.config.js.timestamp-*',
				'**/vite.config.ts.timestamp-*',
				'**/.local/',
				'**/.vscode/',
				'**/.cursor/',
				'**/.claude/',
				'static/doc',
				'static/blog',
				'static/tutorial',
				'static/example',
				'static/guide',
				'static/llms.txt',
				'static/readme_py/',
				'static/api_reference/',
				'static/*.json'
			],
			rules: {
				'constructor-super': 'error',
				'for-direction': 'error',
				'getter-return': 'error',
				'no-async-promise-executor': 'error',
				'no-case-declarations': 'error',
				'no-class-assign': 'error',
				'no-compare-neg-zero': 'error',
				'no-cond-assign': 'error',
				'no-const-assign': 'error',
				'no-constant-binary-expression': 'error',
				'no-constant-condition': 'error',
				'no-control-regex': 'error',
				'no-debugger': 'error',
				'no-delete-var': 'error',
				'no-dupe-class-members': 'error',
				'no-dupe-else-if': 'error',
				'no-dupe-keys': 'error',
				'no-duplicate-case': 'error',
				'no-empty': 'error',
				'no-empty-character-class': 'error',
				'no-empty-pattern': 'error',
				'no-empty-static-block': 'error',
				'no-ex-assign': 'error',
				'no-extra-boolean-cast': 'error',
				'no-fallthrough': 'error',
				'no-func-assign': 'error',
				'no-global-assign': 'error',
				'no-import-assign': 'error',
				'no-invalid-regexp': 'error',
				'no-irregular-whitespace': 'error',
				'no-loss-of-precision': 'error',
				'no-misleading-character-class': 'error',
				'no-new-native-nonconstructor': 'error',
				'no-nonoctal-decimal-escape': 'error',
				'no-obj-calls': 'error',
				'no-prototype-builtins': 'error',
				'no-redeclare': 'error',
				'no-regex-spaces': 'error',
				'no-self-assign': 'error',
				'no-setter-return': 'error',
				'no-shadow-restricted-names': 'error',
				'no-sparse-arrays': 'error',
				'no-this-before-super': 'error',
				'no-unassigned-vars': 'error',
				'no-undef': 'error',
				'no-unexpected-multiline': 'error',
				'no-unreachable': 'error',
				'no-unsafe-finally': 'error',
				'no-unsafe-negation': 'error',
				'no-unsafe-optional-chaining': 'error',
				'no-unused-labels': 'error',
				'no-unused-private-class-members': 'error',
				'no-unused-vars': 'error',
				'no-useless-assignment': 'error',
				'no-useless-backreference': 'error',
				'no-useless-catch': 'error',
				'no-useless-escape': 'error',
				'no-with': 'error',
				'preserve-caught-error': 'error',
				'require-yield': 'error',
				'use-isnan': 'error',
				'valid-typeof': 'error',
				'no-array-constructor': 'error',
				'no-unused-expressions': 'error',
				'svelte/comment-directive': 'error',
				'svelte/infinite-reactive-loop': 'error',
				'svelte/no-at-debug-tags': 'warn',
				'svelte/no-at-html-tags': 'error',
				'svelte/no-dom-manipulating': 'error',
				'svelte/no-dupe-else-if-blocks': 'error',
				'svelte/no-dupe-on-directives': 'error',
				'svelte/no-dupe-style-properties': 'error',
				'svelte/no-dupe-use-directives': 'error',
				'svelte/no-export-load-in-svelte-module-in-kit-pages': 'error',
				'svelte/no-immutable-reactive-statements': 'error',
				'svelte/no-inner-declarations': 'error',
				'svelte/no-inspect': 'warn',
				'svelte/no-navigation-without-resolve': 'error',
				'svelte/no-not-function-handler': 'error',
				'svelte/no-object-in-text-mustaches': 'error',
				'svelte/no-raw-special-elements': 'error',
				'svelte/no-reactive-functions': 'error',
				'svelte/no-reactive-literals': 'error',
				'svelte/no-reactive-reassign': 'error',
				'svelte/no-shorthand-style-property-overrides': 'error',
				'svelte/no-store-async': 'error',
				'svelte/no-svelte-internal': 'error',
				'svelte/no-unknown-style-directive-property': 'error',
				'svelte/no-unnecessary-state-wrap': 'error',
				'svelte/no-unused-props': 'error',
				'svelte/no-unused-svelte-ignore': 'error',
				'svelte/no-useless-children-snippet': 'error',
				'svelte/no-useless-mustaches': 'error',
				'svelte/prefer-svelte-reactivity': 'error',
				'svelte/prefer-writable-derived': 'error',
				'svelte/require-each-key': 'error',
				'svelte/require-event-dispatcher-types': 'error',
				'svelte/require-store-reactive-access': 'error',
				'svelte/system': 'error',
				'svelte/valid-each-key': 'error',
				'svelte/valid-prop-names-in-kit-pages': 'error',
				'typescript/ban-ts-comment': 'error',
				'typescript/no-duplicate-enum-values': 'error',
				'typescript/no-empty-object-type': 'error',
				'typescript/no-explicit-any': 'error',
				'typescript/no-extra-non-null-assertion': 'error',
				'typescript/no-misused-new': 'error',
				'typescript/no-namespace': 'error',
				'typescript/no-non-null-asserted-optional-chain': 'error',
				'typescript/no-require-imports': 'error',
				'typescript/no-this-alias': 'error',
				'typescript/no-unnecessary-type-constraint': 'error',
				'typescript/no-unsafe-declaration-merging': 'error',
				'typescript/no-unsafe-function-type': 'error',
				'typescript/no-wrapper-object-types': 'error',
				'typescript/prefer-as-const': 'error',
				'typescript/prefer-namespace-keyword': 'error',
				'typescript/triple-slash-reference': 'error',
				'vite-plus/prefer-vite-plus-imports': 'error'
			},
			overrides: [
				{
					files: ['**/*.ts', '**/*.tsx', '**/*.mts', '**/*.cts'],
					rules: {
						'constructor-super': 'off',
						'getter-return': 'off',
						'no-class-assign': 'off',
						'no-const-assign': 'off',
						'no-dupe-class-members': 'off',
						'no-dupe-keys': 'off',
						'no-func-assign': 'off',
						'no-import-assign': 'off',
						'no-new-native-nonconstructor': 'off',
						'no-obj-calls': 'off',
						'no-redeclare': 'off',
						'no-setter-return': 'off',
						'no-this-before-super': 'off',
						'no-undef': 'off',
						'no-unreachable': 'off',
						'no-unsafe-negation': 'off',
						'no-var': 'error',
						'no-with': 'off',
						'prefer-const': 'error',
						'prefer-rest-params': 'error',
						'prefer-spread': 'error'
					}
				},
				{
					files: ['*.svelte', '**/*.svelte'],
					rules: {
						'no-inner-declarations': 'off',
						'no-self-assign': 'off'
					},
					jsPlugins: ['eslint-plugin-svelte'],
					globals: {
						$state: 'readonly',
						$derived: 'readonly',
						$effect: 'readonly',
						$props: 'readonly',
						$bindable: 'readonly',
						$inspect: 'readonly',
						$host: 'readonly'
					}
				}
			],
			options: {
				typeAware: true,
				typeCheck: true
			}
		},
		fmt: {
			useTabs: true,
			singleQuote: true,
			trailingComma: 'none',
			printWidth: 100,
			sortPackageJson: false,
			sortTailwindcss: {
				stylesheet: './src/app.css'
			},
			svelte: {},
			associations: [
				{
					files: ['*.svelte'],
					language: 'svelte'
				}
			],
			ignorePatterns: [
				'package-lock.json',
				'pnpm-lock.yaml',
				'yarn.lock',
				'bun.lock',
				'bun.lockb',
				'/static/',
				'/dev/'
			]
		},
		plugins: lazyPlugins(() => [
			serveStaticDirIndex(),
			reloadOnStaticData(),
			tailwindcss(),
			sveltekit({
				preprocess: [vitePreprocess(), mdsvex()],
				extensions: ['.svelte', '.svx'],
				adapter: adapter({
					// default options are shown. On some platforms
					// these options are set automatically — see below
					pages: outputDir,
					assets: outputDir,
					fallback: '200.html', // may differ from host to host
					precompress: false,
					strict: true
				}),
				prerender: {
					// Allow routes to be skipped if they have no entries
					// This handles cases where content types (blog, tutorial, etc.) don't exist
					handleUnseenRoutes: 'warn'
				},
				// GitHub Pages serves sites from a subdirectory (e.g., username.github.io/repo-name/)
				// Set base path via BASE_PATH env var so all routes and assets are correctly prefixed
				// Without this, routes like /doc would resolve to username.github.io/doc instead of username.github.io/afterpython/doc
				// relative: false, so resolve()/asset() return absolute paths. With relative paths, the prerendered
				// redirect in [content_type]/[slug] is e.g. "../example/slug/", which the client router resolves
				// against /example/slug/ on client-side navigation, landing on /example/example/slug/ (404)
				paths: { base: (process.env.BASE_PATH || '') as '' | `/${string}`, relative: false }
				// Path aliases ($lib, $components, $static) are now subpath imports
				// (#lib/*, #static/*) declared in the "imports" field of package.json
			})
		]),
		build: {
			minify: isDev ? false : 'esbuild',
			sourcemap: isDev
		}
	};
});
