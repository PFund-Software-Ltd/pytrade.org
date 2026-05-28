<script lang="ts">
	import type { PageProps } from '../$types';
	import Accordion from '$components/Accordion.svelte';
	import MarkdownRenderer from '$components/MarkdownRenderer.svelte';

	const { data }: PageProps = $props();

	type FaqItem = { question: string; answer: string; category?: string };

	type Block =
		| { type: 'uncategorized'; items: FaqItem[] }
		| { type: 'category'; name: string; items: FaqItem[] };

	const blocks = $derived.by<Block[]>(() => {
		const result: Block[] = [];
		for (const item of data.faq as FaqItem[]) {
			const category = item.category?.trim() ?? '';
			const last = result[result.length - 1];
			if (!category) {
				if (last && last.type === 'uncategorized') {
					last.items.push(item);
				} else {
					result.push({ type: 'uncategorized', items: [item] });
				}
			} else {
				if (last && last.type === 'category' && last.name === category) {
					last.items.push(item);
				} else {
					result.push({ type: 'category', name: category, items: [item] });
				}
			}
		}
		return result;
	});
</script>

<svelte:head>
	<title>FAQs</title>
</svelte:head>

<section class="container mx-auto min-h-[94vh] max-w-3xl px-4 py-12">
	<h1 class="mb-2 text-4xl font-bold text-tx50">Frequently Asked Questions</h1>
	<p class="mb-8 text-tx300">Answers to common questions.</p>

	{#if blocks.length === 0}
		<p class="text-tx300">No FAQs available.</p>
	{:else}
		<div class="rounded-2xl border border-bg300 bg-bg100 px-6 shadow-sm">
			{#each blocks as block, i (i)}
				{#if block.type === 'uncategorized'}
					{#each block.items as item, j (j)}
						<Accordion open={true}>
							{#snippet header()}
								<MarkdownRenderer content={item.question} />
							{/snippet}
							<MarkdownRenderer content={item.answer} />
						</Accordion>
					{/each}
				{:else}
					<Accordion open={false}>
						{#snippet header()}
							<span class="text-xs font-semibold uppercase tracking-widest text-pm500">
								{block.name}
							</span>
						{/snippet}
						<div class="pl-4">
							{#each block.items as item, j (j)}
								<Accordion open={false}>
									{#snippet header()}
										<MarkdownRenderer content={item.question} />
									{/snippet}
									<MarkdownRenderer content={item.answer} />
								</Accordion>
							{/each}
						</div>
					</Accordion>
				{/if}
			{/each}
		</div>
	{/if}
</section>
