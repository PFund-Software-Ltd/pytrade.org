// Comment section (giscus) for MyST-built content pages.
// Injected into static/{content_type}/**/index.html by scripts/inject-comments.ts.
// Reads its config from comments.json next to this file; does nothing if it's missing.
(() => {
	const script = document.currentScript;
	if (!script) return;
	const baseUrl = new URL('.', script.src); // site root, includes BASE_PATH
	const GISCUS_ORIGIN = 'https://giscus.app';
	const CONTAINER_ID = 'ap-comments';

	/** @type {{repo: string, repoId: string, category: string, categoryId: string, contentTypes?: string[], lang?: string} | null} */
	let config = null;
	let currentTerm = '';

	const theme = () => (document.documentElement.classList.contains('dark') ? 'dark' : 'light');

	// e.g. "/afterpython/blog/hello-world/" -> "blog/hello-world"; null for non-post pages
	function termForPage() {
		if (!config) return null;
		const path = decodeURIComponent(location.pathname)
			.slice(baseUrl.pathname.length)
			.replace(/\/(index\.html)?$/, '');
		const [contentType, ...rest] = path.split('/');
		const types = config.contentTypes ?? ['blog', 'tutorial', 'example', 'guide'];
		if (!types.includes(contentType) || rest.length === 0) return null; // listing page
		return path;
	}

	function mount(term) {
		const article = document.querySelector('main article');
		if (!article) return;
		const container = document.createElement('section');
		container.id = CONTAINER_ID;
		container.dataset.term = term;
		container.style.marginTop = '3rem';
		// Above MyST's prev/next links when present
		const footerLinks = article.querySelector('.myst-footer-links');
		article.insertBefore(container, footerLinks);

		const s = document.createElement('script');
		s.src = `${GISCUS_ORIGIN}/client.js`;
		s.async = true;
		s.crossOrigin = 'anonymous';
		Object.entries({
			repo: config.repo,
			repoId: config.repoId,
			category: config.category,
			categoryId: config.categoryId,
			mapping: 'specific',
			term,
			strict: '1',
			reactionsEnabled: '1',
			emitMetadata: '0',
			inputPosition: 'top',
			theme: theme(),
			lang: config.lang ?? 'en',
			loading: 'lazy'
		}).forEach(([k, v]) => (s.dataset[k] = v));
		container.appendChild(s);
	}

	// MyST navigates client-side and re-renders the article, so re-check on DOM changes
	function sync() {
		const term = termForPage();
		const existing = document.getElementById(CONTAINER_ID);
		if (existing && (existing.dataset.term !== term || !existing.isConnected)) existing.remove();
		if (term && !document.getElementById(CONTAINER_ID)) mount(term);
		currentTerm = term ?? '';
	}

	function setTheme() {
		const iframe = document.querySelector('iframe.giscus-frame');
		iframe?.contentWindow?.postMessage({ giscus: { setConfig: { theme: theme() } } }, GISCUS_ORIGIN);
	}

	fetch(new URL('comments.json', baseUrl))
		.then((r) => (r.ok ? r.json() : null))
		.then((c) => {
			if (!c?.repo || !c?.repoId || !c?.categoryId) return;
			config = c;
			let queued = false;
			new MutationObserver(() => {
				if (queued) return;
				queued = true;
				requestAnimationFrame(() => {
					queued = false;
					if (termForPage() !== currentTerm || !document.getElementById(CONTAINER_ID)) sync();
				});
			}).observe(document.body, { childList: true, subtree: true });
			new MutationObserver(setTheme).observe(document.documentElement, {
				attributes: true,
				attributeFilter: ['class']
			});
			sync();
		})
		.catch(() => {});
})();
