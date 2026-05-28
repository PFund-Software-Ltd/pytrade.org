<script lang="ts">
	import type { ContentJson } from '$lib/types';

	let {
		post,
		formattedDate,
		authorName,
		variant = 'card'
	}: {
		post: ContentJson;
		formattedDate: string | null;
		authorName: string;
		variant?: 'card' | 'featured';
	} = $props();

	// Maximum number of tags to display
	const MAX_TAGS = $derived(variant === 'card' ? 3 : 4);
	let displayedTags = $derived(MAX_TAGS);

	// Expose reset method for parent components
	export function resetTags() {
		displayedTags = MAX_TAGS;
	}

	// Variant-specific classes
	const classes = $derived({
		container:
			variant === 'card'
				? 'flex flex-col gap-1 p-4'
				: 'flex flex-col justify-center gap-1 p-6 md:p-8',
		title:
			variant === 'card'
				? 'line-clamp-2 h-14 text-xl font-semibold text-tx50 group-hover:text-pm500'
				: 'h-20 text-3xl font-bold text-tx50 group-hover:text-pm500 md:text-4xl',
		date: variant === 'card' ? 'h-5 text-sm text-tx300' : 'h-6 text-base text-tx300',
		author: variant === 'card' ? 'h-5 text-sm text-tx300' : 'h-6 text-base text-tx300',
		tagsContainer: variant === 'card' ? 'mb-1 flex gap-1' : 'mb-2 flex gap-1',
		tag:
			variant === 'card'
				? 'rounded bg-bg300 px-2 py-0.5 text-xs text-tx300'
				: 'rounded bg-bg300 px-2 py-1 text-sm text-tx300',
		tagMore:
			variant === 'card'
				? 'flex cursor-pointer items-center text-xs text-tx300 hover:text-pm500'
				: 'flex cursor-pointer items-center text-sm text-tx300 hover:text-pm500',
		description: variant === 'card' ? 'mt-2 h-16' : 'mt-3 h-24',
		descriptionText:
			variant === 'card' ? 'line-clamp-3 text-sm text-tx200' : 'line-clamp-4 text-base text-tx200'
	});
</script>

<!-- Content -->
<div class={classes.container}>
	<!-- Title (reserved height for consistency) -->
	{#if variant === 'card'}
		<h3 class={classes.title}>
			{post.title}
		</h3>
	{:else}
		<h2 class={classes.title}>
			{post.title}
		</h2>
	{/if}

	<!-- Date (reserved row for consistency) -->
	<div class={classes.date}>
		{#if formattedDate}
			<time datetime={post.date}>
				{formattedDate}
			</time>
		{/if}
	</div>

	<!-- Authors (reserved row for consistency) -->
	<div class={classes.author}>
		{authorName}
	</div>

	<!-- Tags (reserved row for consistency) -->
	<!-- svelte-ignore a11y_no_static_element_interactions -->
	<div
		class={[
			classes.tagsContainer,
			{
				'h-6 overflow-hidden':
					variant === 'card' && (post.tags ? displayedTags !== post.tags.length : true),
				'h-8 overflow-hidden':
					variant === 'featured' && (post.tags ? displayedTags !== post.tags.length : true),
				'flex-wrap': post.tags ? displayedTags === post.tags.length : false
			}
		]}
	>
		{#if post.tags && post.tags.length > 0}
			{#each post.tags.slice(0, displayedTags) as tag}
				<span class={classes.tag}>
					{tag}
				</span>
			{/each}
			{#if post.tags.length > displayedTags}
				<span
					class={classes.tagMore}
					onmouseenter={() => {
						displayedTags = post.tags!.length;
					}}
				>
					+{post.tags.length - displayedTags}
				</span>
			{/if}
		{/if}
	</div>

	<!-- Description (reserved height for consistency) -->
	<div class={classes.description}>
		{#if post.description}
			<p class={classes.descriptionText}>
				{post.description}
			</p>
		{/if}
	</div>

	<!-- CTA (featured variant only) -->
	{#if variant === 'featured'}
		<div
			class="mt-4 flex items-center gap-2 font-medium text-pm500 transition-all group-hover:gap-3"
		>
			<span>Read more</span>
			<svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M17 8l4 4m0 0l-4 4m4-4H3"
				/>
			</svg>
		</div>
	{/if}
</div>
