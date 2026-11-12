import type { ContentType, ContentJson } from '#lib/types/index.ts';
import { dev } from '$app/env';
import {
	PUBLIC_DOC_URL,
	PUBLIC_BLOG_URL,
	PUBLIC_TUTORIAL_URL,
	PUBLIC_EXAMPLE_URL,
	PUBLIC_GUIDE_URL
} from '$app/env/public';
import { resolve } from '$app/paths';

export { CONTENT_TYPES } from './content-types.ts';

// MyST dev-server URLs (written to .env.development by `ap dev`), see src/env.ts
const DEV_CONTENT_URLS: Record<ContentType | 'doc', string> = {
	doc: PUBLIC_DOC_URL,
	blog: PUBLIC_BLOG_URL,
	tutorial: PUBLIC_TUTORIAL_URL,
	example: PUBLIC_EXAMPLE_URL,
	guide: PUBLIC_GUIDE_URL
};

/**
 * MyST dev-server URL for a content type, or '' when none is running (e.g. plain `vp dev`
 * without `ap dev`, or production builds) so callers fall back to the static pages.
 */
export function devContentUrl(contentType: ContentType | 'doc'): string {
	return dev ? DEV_CONTENT_URLS[contentType] : '';
}

/**
 * Loads content JSON file for a given content type
 * Used by all content type layouts (blog, tutorial, example, guide)
 *
 * @param contentType - The type of content to load
 * @returns Array of content posts
 */
export async function loadContentByType(contentType: ContentType): Promise<ContentJson[]> {
	try {
		// Dynamic import of content JSON file (blog.json, tutorial.json, etc.)
		const contentData = await import(`#static/${contentType}.json`);

		// Return data as-is - AfterPython already provides flattened structure
		return contentData.default;
	} catch {
		// If content file doesn't exist, return empty array
		return [];
	}
}

/**
 * Generate the href for a post: the MyST dev server if running, else the static page
 *
 * @param post - The post object
 * @param contentType - The type of content
 * @returns The href string
 */
export function getPostHref(post: ContentJson, contentType: ContentType): string {
	const devUrl = devContentUrl(contentType);
	return devUrl
		? `${devUrl}/${post.slug}`
		: // trailing slash: the MyST page is {type}/{slug}/index.html, so this is the
			// URL it's served at without a redirect
			`${resolve('/[content_type=content]/[slug]', { content_type: contentType, slug: post.slug })}/`;
}

/**
 * Get the thumbnail URL for a post (with fallbacks)
 *
 * @param post - The post object
 * @returns The thumbnail URL
 */
export function getThumbnailUrl(post: ContentJson): string | null {
	return post.thumbnailOptimized || post.thumbnail || null;
}

/**
 * Format a date string to a readable format
 *
 * @param dateString - The date string to format
 * @returns Formatted date string or null if invalid
 */
export function formatDate(dateString?: string): string | null {
	if (!dateString || dateString.trim() === '') return null;
	const date = new Date(dateString);
	if (isNaN(date.getTime())) return null;
	// Date-only strings ("2026-11-11") parse as midnight UTC; format in UTC too,
	// otherwise viewers west of UTC see the previous day (MyST pages show it as written).
	return date.toLocaleDateString('en-US', {
		year: 'numeric',
		month: 'short',
		day: 'numeric',
		timeZone: 'UTC'
	});
}

/**
 * Get the first author name from a post
 *
 * @param post - The post object
 * @returns The author name or empty string
 */
export function getAuthorName(post: ContentJson): string {
	return post.authors?.[0]?.name || '';
}
