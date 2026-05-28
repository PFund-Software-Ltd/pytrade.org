import { CONTENT_TYPES } from '$lib/utils/content';

// Derive the type from the constant
export type ContentType = (typeof CONTENT_TYPES)[number];

// Content structure from AfterPython-generated JSON files (blog.json, tutorial.json, etc.)
export interface ContentJson {
	slug: string;
	title: string;
	description?: string;
	date?: string;
	authors?: Array<{ name: string; email?: string; github?: string; twitter?: string }>;
	tags?: string[];
	thumbnail?: string;
	thumbnailOptimized?: string;
	featured?: boolean;  // if true, it is a featured post
}
