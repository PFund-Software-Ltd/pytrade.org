import { redirect } from '@sveltejs/kit';
import { asset } from '$app/paths';
import type { AssetPath } from '$app/types';
import type { PageServerLoad, EntryGenerator } from './$types';
import type { ContentType, ContentJson } from '#lib/types/index.ts';
import { CONTENT_TYPES } from '#lib/utils/index.ts';

export const prerender = true;

export const entries: EntryGenerator = async () => {
	const entries: Array<{ content_type: ContentType; slug: string }> = [];

	// Dynamically load slugs from {content_type}.json files
	for (const contentType of CONTENT_TYPES) {
		try {
			const contentData = await import(`#static/${contentType}.json`);
			const posts: ContentJson[] = contentData.default;

			// Extract slugs from the JSON
			for (const post of posts) {
				if (post.slug) {
					entries.push({ content_type: contentType, slug: post.slug });
				}
			}
		} catch {
			// If the JSON file doesn't exist, skip this content type
			continue;
		}
	}

	return entries;
};

export const load: PageServerLoad = ({ params }) => {
	// Redirect old /{content_type}/{slug} links to the static MyST-generated HTML
	// in static/{content_type}/{slug}/index.html, at its canonical URL
	// {base}/{content_type}/{slug}/ (not .../index.html, a duplicate of it)
	redirect(307, asset(`${params.content_type}/${params.slug}/` as AssetPath));
};
