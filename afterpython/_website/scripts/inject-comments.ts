// Add the comment loader (static/comments.js) to MyST-built content pages.
// MyST has no option for custom scripts, so we patch its HTML:
//   - production: run after `vp build` on build/{content_type}/**/*.html
//   - dev: vite.config.ts injects on the fly when serving static/{content_type}/**/index.html
import { existsSync, readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';

export const COMMENT_CONTENT_TYPES = ['blog', 'tutorial', 'example', 'guide'];
const MARKER = 'data-ap-comments';

export function injectCommentsScript(html: string, basePath: string): string {
	if (html.includes(MARKER)) return html;
	const tag = `<script src="${basePath}/comments.js" ${MARKER} defer></script>`;
	return html.replace('</head>', `${tag}</head>`);
}

function htmlFiles(dir: string): string[] {
	return readdirSync(dir, { withFileTypes: true, recursive: true })
		.filter((e) => e.isFile() && e.name.endsWith('.html'))
		.map((e) => join(e.parentPath, e.name));
}

// CLI: vpx scripts/inject-comments.ts [buildDir]
if (import.meta.url === pathToFileURL(process.argv[1]).href) {
	const buildDir = process.argv[2] ?? 'build';
	const basePath = process.env.BASE_PATH ?? '';
	if (!existsSync(join(buildDir, 'comments.json'))) {
		console.log('No comments.json, skip injecting comments');
	} else {
		let count = 0;
		for (const type of COMMENT_CONTENT_TYPES) {
			const dir = join(buildDir, type);
			if (!existsSync(dir)) continue;
			for (const file of htmlFiles(dir)) {
				const html = readFileSync(file, 'utf-8');
				const out = injectCommentsScript(html, basePath);
				if (out !== html) {
					writeFileSync(file, out);
					count++;
				}
			}
		}
		console.log(`Injected comments into ${count} pages`);
	}
}
