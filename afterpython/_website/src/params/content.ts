import type { ContentType } from '$lib/types';
import { CONTENT_TYPES } from '$lib/utils';

// used to match the content type in [content_type=content]
export function match(value: string): value is ContentType {
	return CONTENT_TYPES.some(type => type === value);
}