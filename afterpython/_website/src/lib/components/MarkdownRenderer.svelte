<script lang="ts">
	import { Marked } from 'marked';
	import { markedHighlight } from 'marked-highlight';
	import { gfmHeadingId } from 'marked-gfm-heading-id';
	import hljs from 'highlight.js';
	import 'highlight.js/styles/github-dark.css';
	import { resolve } from '$app/paths';
	import type { Path } from '$app/types';

	type Props = {
		content: string;
		// inline: render a one-line snippet (e.g. a FAQ question) as phrasing
		// content with no <p> wrapper or prose styles, so it inherits the
		// surrounding text style instead of overriding it
		inline?: boolean;
		size?: 'base' | 'lg';
	};

	const { content, inline = false, size = 'lg' }: Props = $props();

	// Create a new marked instance to avoid global state issues
	const marked = new Marked();

	// Configure marked with extensions
	marked.use(
		{
			// Root-relative links/images (e.g. "/faq") would skip BASE_PATH; prefix them
			walkTokens(token) {
				if (
					(token.type === 'link' || token.type === 'image') &&
					token.href.startsWith('/') &&
					!token.href.startsWith('//')
				) {
					token.href = resolve(token.href.slice(1) as Path);
				}
			}
		},
		gfmHeadingId(),
		markedHighlight({
			langPrefix: 'hljs language-',
			highlight(code, lang) {
				const language = hljs.getLanguage(lang) ? lang : 'plaintext';
				return hljs.highlight(code, { language }).value;
			}
		})
	);

	marked.setOptions({
		gfm: true,
		breaks: true
	});

	const htmlContent = $derived(
		(inline ? marked.parseInline(content) : marked.parse(content)) as string
	);
	// literal class names so Tailwind can find them
	const sizeClass = $derived(size === 'lg' ? 'prose-lg' : 'prose-base');
</script>

{#if inline}
	<span class="markdown-renderer">{@html htmlContent}</span>
{:else}
	<div
		class="markdown-renderer prose-tbody:text-tx200 prose {sizeClass} max-w-none prose-headings:text-tx50 prose-p:text-tx300 prose-a:text-pm500 prose-a:no-underline hover:prose-a:underline prose-blockquote:border-l-pm500 prose-blockquote:text-tx200 prose-strong:text-tx100 prose-code:text-pm500 prose-pre:bg-bg200 prose-li:text-tx200 prose-th:bg-bg200 prose-th:text-tx50 prose-td:border-bg300 prose-td:text-tx200 prose-img:m-0 prose-img:inline-block"
	>
		{@html htmlContent}
	</div>
{/if}

<style>
	/* Inline code: a tinted chip instead of Tailwind Typography's literal backticks */
	.markdown-renderer :global(code::before),
	.markdown-renderer :global(code::after) {
		content: none;
	}

	.markdown-renderer :global(:not(pre) > code) {
		border-radius: 0.25rem;
		background-color: var(--color-bg300);
		padding: 0.125rem 0.375rem;
		font-size: 0.875em;
		font-weight: 500;
	}

	/* Code blocks: highlight.js's dark theme brings its own background and
	   padding; let it fill the <pre> instead of sitting inside it as a box in
	   a box (its light-on-dark colours need that dark background in both themes) */
	.markdown-renderer :global(pre:has(> code.hljs)) {
		padding: 0;
		overflow: hidden;
	}
	.markdown-renderer :global(pre > code.hljs) {
		padding: 1rem 1.25rem;
	}

	/* Blockquotes are notes and asides here, not quotations: no curly quotes */
	.markdown-renderer :global(blockquote p::before),
	.markdown-renderer :global(blockquote p::after) {
		content: none;
	}

	/* Badge layout - paragraphs with images displayed as flex */
	.markdown-renderer :global(p:has(> img:first-child)) {
		display: flex;
		flex-wrap: wrap;
		gap: 0.28rem;
		align-items: center;
		justify-content: center;
	}

	/* Force table text colors to be readable in dark mode */
	.markdown-renderer :global(table),
	.markdown-renderer :global(thead),
	.markdown-renderer :global(tbody),
	.markdown-renderer :global(tr),
	.markdown-renderer :global(td) {
		color: var(--color-tx200) !important;
	}

	.markdown-renderer :global(th) {
		color: var(--color-tx50) !important;
	}

	/* Details/summary elements */
	.markdown-renderer :global(details),
	.markdown-renderer :global(summary) {
		color: var(--color-tx200) !important;
	}
</style>
