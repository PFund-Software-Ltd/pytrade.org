<script lang="ts">
	import type { LayoutProps } from './$types';

	let { children }: LayoutProps = $props();
</script>

<!-- Child routes render here (listing page or individual post) -->
{@render children()}