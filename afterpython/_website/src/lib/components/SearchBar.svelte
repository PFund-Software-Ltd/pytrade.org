<script lang="ts">
	import { onMount } from 'svelte';
	import { dev } from '$app/environment';
	import { resolve } from '$app/paths';
	import '@pagefind/component-ui/css';

	onMount(async () => {
		if (dev) return;

		await import('@pagefind/component-ui');
	});
</script>

<pagefind-config bundle-path={resolve('/pagefind/')}></pagefind-config>
<pagefind-modal-trigger compact></pagefind-modal-trigger>
<pagefind-modal></pagefind-modal>
