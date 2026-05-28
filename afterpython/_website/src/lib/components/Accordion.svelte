<script lang="ts">
	import { untrack, type Snippet } from 'svelte';

	type AccordionProps = {
		open?: boolean;
		header: Snippet;
		children: Snippet;
		class?: string;
	};

	let { open = false, header, children, class: className = '' }: AccordionProps = $props();

	let isOpen = $state(untrack(() => open));
</script>

<div class="border-b border-bg300 {className}">
	<button
		type="button"
		onclick={() => (isOpen = !isOpen)}
		aria-expanded={isOpen}
		class="flex w-full items-center justify-between gap-4 py-4 text-left text-tx50 transition-colors hover:text-pm500"
	>
		<span class="flex-1">{@render header()}</span>
		<svg
			class="h-4 w-4 shrink-0 transition-transform duration-200"
			class:rotate-180={isOpen}
			viewBox="0 0 20 20"
			fill="currentColor"
			aria-hidden="true"
		>
			<path
				fill-rule="evenodd"
				d="M5.23 7.21a.75.75 0 011.06.02L10 11.06l3.71-3.83a.75.75 0 111.08 1.04l-4.25 4.39a.75.75 0 01-1.08 0L5.21 8.27a.75.75 0 01.02-1.06z"
				clip-rule="evenodd"
			/>
		</svg>
	</button>
	{#if isOpen}
		<div class="pb-4 text-tx300">
			{@render children()}
		</div>
	{/if}
</div>
