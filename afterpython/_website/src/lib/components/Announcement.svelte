<script lang="ts">
	import MarkdownRenderer from '$components/MarkdownRenderer.svelte';

	type AnnouncementProps = {
		content: string;
	};

	let { content }: AnnouncementProps = $props();
</script>

{#if content?.trim()}
	<aside
		class="border-l-4 border-pm500 bg-pm50/60 px-5 py-4 text-tx200 shadow-sm dark:bg-pm50/20"
		aria-label="Announcement"
	>
		<div class="mx-auto max-w-4xl">
			<div class="announcement-md">
				<MarkdownRenderer {content} />
			</div>
		</div>
	</aside>
{/if}

<style>
	/* Tighten MarkdownRenderer's default prose-lg sizing for the banner context. */
	.announcement-md :global(.markdown-renderer) {
		font-size: 0.95rem;
	}
	.announcement-md :global(.markdown-renderer p) {
		margin-top: 0.25rem;
		margin-bottom: 0.25rem;
	}
	.announcement-md :global(.markdown-renderer p:first-child) {
		margin-top: 0;
	}
	.announcement-md :global(.markdown-renderer p:last-child) {
		margin-bottom: 0;
	}
</style>
