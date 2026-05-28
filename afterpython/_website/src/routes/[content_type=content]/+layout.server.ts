import type { LayoutServerLoad } from './$types';
import type { ContentType, ContentJson } from '$lib/types';
import { loadContentByType } from '$lib/utils';

export const prerender = true;

export const load: LayoutServerLoad = async ({ url, parent }): Promise<{ projectName: string, contentType: ContentType, posts: ContentJson[] }> => {
	const parentData = await parent();
	
	// Extract content type from URL path (e.g., /blog -> blog)
	const contentType = url.pathname.split('/')[1] as ContentType;

	// Load content data, e.g. blog.json, tutorial.json, example.json, guide.json, etc.
	const posts = await loadContentByType(contentType);

	return {
		projectName: parentData.name,
		contentType,
		posts,
	};
};