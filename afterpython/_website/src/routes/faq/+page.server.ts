import type { PageServerLoad } from './$types';

export const prerender = true;

type FaqItem = {
	question: string;
	answer: string;
	category?: string;
};

const FILE = 'faq' as const;

export const load: PageServerLoad = async () => {
	try {
		const faq = await import(`$static/${FILE}.json`);
		return { faq: (faq.default ?? faq) as FaqItem[] };
	} catch {
		return { faq: [] as FaqItem[] };
	}
};
