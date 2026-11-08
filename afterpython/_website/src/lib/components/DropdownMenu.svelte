<script lang="ts">
	import type { Snippet } from 'svelte';

	type Props = {
		children: Snippet;
		label: string;
		align?: 'left' | 'center';
	};

	let { children, label, align = 'center' }: Props = $props();
</script>

<div class="group relative">
	<button>{label}</button>
	<div
		class={[
			'absolute hidden group-hover:block',
			'rounded-md bg-bg50 py-2 shadow-lg',
			align === 'left' ? '' : 'left-1/2 -translate-x-1/2'
		]}
	>
		{@render children()}
	</div>
</div>
