import { redirect } from '@sveltejs/kit';
import type { PageServerLoad, EntryGenerator } from './$types';
import type { ContentType, ContentJson } from '$lib/types';
import { CONTENT_TYPES } from '$lib/utils';

export const prerender = true;

export const entries: EntryGenerator = async () => {
	const entries: Array<{ content_type: ContentType; slug: string }> = [];

	// Dynamically load slugs from {content_type}.json files
	for (const contentType of CONTENT_TYPES) {
		try {
			const contentData = await import(`$static/${contentType}.json`);
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
	// Redirect to the static MyST-generated HTML
	// The static HTML files are in static/{content_type}/{slug}/index.html
	// and will be served at /{content_type}/{slug}/index.html
	redirect(307, `/${params.content_type}/${params.slug}/index.html`);
};
