<script lang="ts">
  import type { Snippet } from "svelte";

  type Props = {
    children: Snippet;
    href: string;
    class?: string;
  };

  let { children, href, class: className = '' }: Props = $props();
</script>

<a {href} class="block px-4 py-2 text-tx50 hover:bg-bg400 {className}">
  {@render children()}
</a>