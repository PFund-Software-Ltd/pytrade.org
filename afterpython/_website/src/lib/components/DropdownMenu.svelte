<script lang="ts">
  import type { Snippet } from "svelte";

  type Props = {
    children: Snippet;
    label: string;
    align?: 'left' | 'center';
  };

  let { children, label, align = 'center' }: Props = $props();
</script>

<div class="relative group">
  <button>{label}</button>
  <div class={[
    'absolute hidden group-hover:block',
    'bg-bg50 rounded-md shadow-lg py-2',
    align === 'left' ? '' : 'left-1/2 -translate-x-1/2',
  ]}>
    {@render children()}
  </div>
</div>