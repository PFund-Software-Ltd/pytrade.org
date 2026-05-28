import type { ContentType, ContentJson } from '$lib/types';
import { dev } from '$app/environment';
import { env } from '$env/dynamic/public';
import { resolve } from '$app/paths';

// All valid content types (single source of truth)
export const CONTENT_TYPES = ['blog', 'tutorial', 'example', 'guide'] as const;

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
		const contentData = await import(`$static/${contentType}.json`);

		// Return data as-is - AfterPython already provides flattened structure
		return contentData.default;
	} catch {
		// If content file doesn't exist, return empty array
		return [];
	}
}

/**
 * Generate the href for a post based on environment (dev vs prod)
 *
 * @param post - The post object
 * @param contentType - The type of content
 * @returns The href string
 */
export function getPostHref(post: ContentJson, contentType: ContentType): string {
	return dev
		? env[`PUBLIC_${contentType.toUpperCase()}_URL`] + `/${post.slug}`
		: resolve(`/${contentType}/${post.slug}`);
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
	return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
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
