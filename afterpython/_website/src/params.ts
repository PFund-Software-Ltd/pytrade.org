import { defineParams } from '@sveltejs/kit/params';
import type { ContentType } from '#lib/types/index.ts';
import { CONTENT_TYPES } from '#lib/utils/content-types.ts';

// used to match the content type in [content_type=content]
function matchContent(value: string): value is ContentType {
	return CONTENT_TYPES.some((type) => type === value);
}

export const params = defineParams({
	content: (param) => (matchContent(param) ? param : undefined)
});
