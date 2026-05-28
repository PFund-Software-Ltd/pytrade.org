import type { LayoutServerLoad } from './$types';
import { CONTENT_TYPES } from '$lib/utils/content';
import { existsSync } from 'fs';
import { resolve } from 'path';

const DEFAULT_FAVICON = 'favicon.ico';

export const prerender = true;

async function checkContentType(type: string): Promise<boolean> {
	try {
		await import(`$static/${type}.json`);
		return true;
	} catch {
		return false;
	}
}

function checkDocExists(): boolean {
	// Check if static/doc directory exists
	return existsSync(resolve('static', 'doc'));
}

function checkApiReferenceExists(): boolean {
	// pdoc-generated static HTML lives in static/api_reference/.
	// Present when `ap build` ran without --skip-api; absent during `ap dev`
	// (cleanup wipes it) and after `ap build --skip-api`.
	return existsSync(resolve('static', 'api_reference'));
}

type LogoMetadata = {
	logo?: string;
	logo_dark?: string;
	favicon?: string;
};

export const load: LayoutServerLoad = async () => {
	try {
		// Dynamic import to handle missing file gracefully
		const metadata = await import('$static/metadata.json');
		const metadataData = metadata.default as typeof metadata.default & LogoMetadata;

		// Check which content types exist - dynamically from CONTENT_TYPES
		const contentTypesArray = await Promise.all(
			CONTENT_TYPES.map(async (type) => [type, await checkContentType(type)])
		);
		const contentTypes = Object.fromEntries(contentTypesArray);

		// Special handling for doc - check if directory exists instead of JSON
		contentTypes.doc = checkDocExists();
		contentTypes.api_reference = checkApiReferenceExists();

		// FAQ is sourced from static/faq.json but isn't part of CONTENT_TYPES
		contentTypes.faq = await checkContentType('faq');

		return {
			...metadataData,
			favicon: metadataData.favicon ?? DEFAULT_FAVICON,
			metadataError: null,
			contentTypes
		};
	} catch {
		// metadata.json is missing or invalid - return minimal data to keep layout working
		const emptyContentTypes = Object.fromEntries(
			[...CONTENT_TYPES, 'doc', 'faq', 'api_reference'].map((type) => [type, false])
		);

		return {
			name: '',
			summary: '',
			description: '',
			project_url: [],
			metadataError:
				'Project metadata not found. Please ensure metadata.json exists in the static folder. Did you forget to run `ap build`?',
			contentTypes: emptyContentTypes,
			favicon: DEFAULT_FAVICON
		};
	}
};
