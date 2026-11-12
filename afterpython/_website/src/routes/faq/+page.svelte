<script lang="ts">
	import type { PageProps } from './$types';
	import MarkdownRenderer from '#lib/components/MarkdownRenderer.svelte';

	const { data }: PageProps = $props();

	type FaqItem = { question: string; answer: string; category?: string };
	type Entry = FaqItem & { id: string; title: string };
	// consecutive items with the same category form a group; uncategorized
	// items form groups with an empty name and no heading
	type Group = { name: string; id: string; items: Entry[] };

	// question markdown -> plain text for the sidebar and anchor ids
	function plainText(markdown: string): string {
		return markdown
			.replace(/!?\[([^\]]*)\]\([^)]*\)/g, '$1')
			.replace(/[`*_~]/g, '')
			.trim();
	}

	function slugify(text: string): string {
		return (
			text
				.toLowerCase()
				.replace(/[^a-z0-9]+/g, '-')
				.replace(/^-+|-+$/g, '')
				.slice(0, 80) || 'question'
		);
	}

	const groups = $derived.by<Group[]>(() => {
		const used: Record<string, true> = {};
		const uniqueId = (base: string) => {
			let id = base;
			for (let n = 2; used[id]; n++) id = `${base}-${n}`;
			used[id] = true;
			return id;
		};
		const result: Group[] = [];
		for (const item of data.faq as FaqItem[]) {
			const name = item.category?.trim() ?? '';
			let group = result.at(-1);
			if (!group || group.name !== name) {
				group = { name, id: name ? uniqueId(slugify(name)) : '', items: [] };
				result.push(group);
			}
			const title = plainText(item.question);
			group.items.push({ ...item, title, id: uniqueId(slugify(title)) });
		}
		return result;
	});

	const entries = $derived(groups.flatMap((g) => g.items));

	// scrollspy: the active question is the last one whose heading has
	// scrolled past the top quarter of the viewport
	let activeId = $state('');
	// a question the reader jumped to (sidebar, # link, URL hash) stays active
	// until they scroll themselves. Short questions near the end can't scroll
	// up to the threshold, so position alone would highlight a neighbour.
	let pinnedId = '';

	function followHash() {
		const id = decodeURIComponent(location.hash.slice(1));
		if (!entries.some((e) => e.id === id)) return;
		pinnedId = id;
		activeId = id;
	}

	function unpin() {
		pinnedId = '';
	}

	function updateActive() {
		// the jump itself fires scroll events, so only user input unpins
		if (pinnedId) return;
		const threshold = window.innerHeight * 0.25;
		let current = entries[0]?.id ?? '';
		for (const entry of entries) {
			const el = document.getElementById(entry.id);
			if (el && el.getBoundingClientRect().top <= threshold) current = entry.id;
		}
		// at the very bottom the last questions may never reach the threshold
		const atBottom =
			window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 2;
		if (atBottom && entries.length) current = entries[entries.length - 1].id;
		activeId = current;
	}

	$effect(() => {
		followHash();
		updateActive();
		let frame = 0;
		const onScroll = () => {
			cancelAnimationFrame(frame);
			frame = requestAnimationFrame(updateActive);
		};
		// clicking the link of the current hash again fires no hashchange
		const onClick = (event: MouseEvent) => {
			const link = (event.target as Element).closest?.('a[href^="#"]');
			if (link) requestAnimationFrame(followHash);
		};
		const userScroll = ['wheel', 'touchmove', 'keydown', 'mousedown'] as const;
		window.addEventListener('scroll', onScroll, { passive: true });
		window.addEventListener('resize', onScroll);
		window.addEventListener('hashchange', followHash);
		document.addEventListener('click', onClick);
		for (const type of userScroll) {
			window.addEventListener(type, unpin, { passive: true });
		}
		return () => {
			cancelAnimationFrame(frame);
			window.removeEventListener('scroll', onScroll);
			window.removeEventListener('resize', onScroll);
			window.removeEventListener('hashchange', followHash);
			document.removeEventListener('click', onClick);
			for (const type of userScroll) {
				window.removeEventListener(type, unpin);
			}
		};
	});
</script>

<svelte:head>
	<title>FAQs</title>
</svelte:head>

{#snippet toc(compact: boolean)}
	<ul class="space-y-1 text-sm">
		{#each groups as group, i (i)}
			{#if group.name}
				<li
					class="pt-5 pb-1 text-xs font-bold tracking-wider text-tx50 uppercase first:pt-0 {compact
						? ''
						: 'pl-4'}"
				>
					{group.name}
				</li>
			{/if}
			{#each group.items as entry (entry.id)}
				{@const active = !compact && entry.id === activeId}
				<li>
					<a
						href="#{entry.id}"
						aria-current={active ? 'location' : undefined}
						class="block py-1 leading-snug transition-colors {compact
							? 'text-tx300 hover:text-pm500'
							: '-ml-px border-l'} {compact
							? group.name
								? 'pl-3'
								: ''
							: group.name
								? 'pl-7'
								: 'pl-4'} {active
							? 'border-pm500 font-medium text-pm500'
							: compact
								? ''
								: 'border-transparent text-tx400 hover:border-tx500 hover:text-tx50'}"
					>
						{entry.title}
					</a>
				</li>
			{/each}
		{/each}
	</ul>
{/snippet}

<section class="container mx-auto min-h-[94vh] max-w-6xl px-4 py-12 lg:py-16">
	<header class="mb-10 max-w-3xl lg:mb-14">
		<h1 class="text-4xl font-bold tracking-tight text-tx50 sm:text-5xl">
			Frequently asked questions
		</h1>
		<p class="mt-4 text-lg text-tx300">Answers to common questions.</p>
	</header>

	{#if entries.length === 0}
		<p class="text-tx300">No FAQs available.</p>
	{:else}
		<div class="lg:grid lg:grid-cols-[minmax(0,1fr)_16rem] lg:gap-16">
			<div class="max-w-3xl min-w-0">
				<!-- small screens: the sidebar becomes a collapsible list at the top -->
				<details class="mb-8 rounded-lg border border-bg300 bg-bg100 px-4 py-3 lg:hidden">
					<summary class="cursor-pointer text-sm font-medium text-tx50">
						Jump to a question
					</summary>
					<div class="mt-3">{@render toc(true)}</div>
				</details>

				{#each groups as group, i (i)}
					<div class="faq-group" class:categorized={group.name}>
						{#if group.name}
							<h2
								id={group.id}
								class="scroll-mt-8 pb-2 text-sm font-semibold tracking-wider text-pm500 uppercase"
							>
								{group.name}
							</h2>
						{/if}
						{#each group.items as entry (entry.id)}
							<article id={entry.id} class="faq-item scroll-mt-8 py-8">
								<h3 class="group relative text-xl leading-snug font-semibold text-tx50">
									<!-- in the left gutter so it never wraps onto a line of its own -->
									<a
										href="#{entry.id}"
										class="absolute top-0 -left-6 hidden w-6 font-normal text-tx500 no-underline opacity-0 transition-opacity group-hover:opacity-100 hover:text-pm500 focus:opacity-100 lg:block"
										aria-label="Link to this question">#</a
									>
									<MarkdownRenderer content={entry.question} inline />
								</h3>
								<div class="faq-answer mt-3">
									<MarkdownRenderer content={entry.answer} size="base" />
								</div>
							</article>
						{/each}
					</div>
				{/each}
			</div>

			<aside class="hidden lg:block">
				<nav
					aria-label="Questions on this page"
					class="sticky top-8 max-h-[calc(100vh-4rem)] overflow-y-auto pb-8"
				>
					<p class="mb-3 text-xs font-semibold tracking-wider text-tx400 uppercase">On this page</p>
					<div class="border-l border-bg300">{@render toc(false)}</div>
				</nav>
			</aside>
		</div>
	{/if}
</section>

<style>
	/* hairline between questions, not above the first one in a group */
	.faq-item + .faq-item {
		border-top: 1px solid var(--color-bg300);
	}
	/* inside a category the label already groups the questions; whitespace
	   alone separates them */
	.categorized .faq-item + .faq-item {
		border-top: none;
		padding-top: 1rem;
	}
	.faq-item:first-of-type {
		padding-top: 0.5rem;
	}
	/* the same hairline between groups, with the category label below it */
	.faq-group + .faq-group {
		border-top: 1px solid var(--color-bg300);
		padding-top: 1.5rem;
	}

	/* answers: comfortable line length and quieter inline code than the
	   site-wide orange, which turns code-heavy answers into noise */
	.faq-answer {
		max-width: 65ch;
	}
	.faq-answer :global(p),
	.faq-answer :global(li) {
		color: var(--color-tx200);
	}
	.faq-answer :global(:not(pre) > code) {
		color: var(--color-tx100);
		border: 1px solid var(--color-bg400);
	}
	.faq-answer :global(.prose > :last-child) {
		margin-bottom: 0;
	}
</style>
