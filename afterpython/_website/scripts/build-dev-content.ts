// Build the test content in dev/ with mystmd and copy it into static/,
// mirroring what `ap build` does in afterpython (build.py, postbuild, content_json.py).
// Usage: vp run build:dev-content
import { execFileSync } from 'node:child_process';
import { cpSync, existsSync, readdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const CONTENT_TYPES = ['blog'] as const;
const basePath = process.env.BASE_PATH ?? '';
const myst = join('node_modules', '.bin', 'myst');

for (const contentType of CONTENT_TYPES) {
	const src = join('dev', contentType);
	const out = join('static', contentType);

	rmSync(join(src, '_build'), { recursive: true, force: true });
	execFileSync(join('..', '..', myst), ['build', '--html'], {
		cwd: src,
		stdio: 'inherit',
		env: { ...process.env, BASE_URL: `${basePath}/${contentType}`, BASE_PATH: basePath }
	});

	// MyST's index.html is the placeholder index.md; /{content_type} is the SvelteKit landing page
	// (see afterpython builders/index_md.py delete_placeholder_index_md_files)
	rmSync(join(src, '_build', 'html', 'index.html'), { force: true });
	rmSync(out, { recursive: true, force: true });
	cpSync(join(src, '_build', 'html'), out, { recursive: true });
	const publicDir = join(src, '_build', 'site', 'public');
	if (existsSync(publicDir)) cpSync(publicDir, join(out, 'build'), { recursive: true });

	// {content_type}.json manifest (see afterpython builders/content_json.py)
	const contentDir = join(src, '_build', 'site', 'content');
	const items = readdirSync(contentDir)
		.filter((f) => f.endsWith('.json') && f !== 'index.json')
		.map((f) => {
			const c = JSON.parse(readFileSync(join(contentDir, f), 'utf-8'));
			const fm = c.frontmatter ?? {};
			const prefix = (p: string) => (p ? `/${contentType}/build${p}` : '');
			const thumbnail = fm.thumbnail || '';
			return {
				version: c.version,
				slug: c.slug,
				location: c.location,
				featured: false,
				title: fm.title || '',
				description: fm.description || '',
				tags: fm.tags || [],
				date: fm.date || '',
				thumbnail: prefix(thumbnail),
				thumbnailOptimized: prefix(fm.thumbnailOptimized || thumbnail),
				authors: fm.authors || []
			};
		});
	writeFileSync(join('static', `${contentType}.json`), JSON.stringify(items, null, 2));
	console.log(`Built ${contentType}: ${items.length} items`);
}
