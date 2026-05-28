<script lang="ts">
	import type { ContentJson, ContentType } from '$lib/types';
	import { getPostHref, getThumbnailUrl, formatDate, getAuthorName } from '$lib/utils/content';
	import PostContent from './PostContent.svelte';

	let { post, contentType }: { post: ContentJson; contentType: ContentType } = $props();

	const href = $derived(getPostHref(post, contentType));
	const thumbnailUrl = $derived(getThumbnailUrl(post));
	const formattedDate = $derived(formatDate(post.date));
	const authorName = $derived(getAuthorName(post));

	let postContent: PostContent;
</script>

<a
	{href}
	class="group block overflow-hidden rounded-lg bg-bg100 shadow-md transition-all duration-200 hover:shadow-2xl"
	onmouseleave={() => postContent?.resetTags()}
>
	<div class="grid gap-0 md:grid-cols-2">
		<!-- Left: Thumbnail (50% width on desktop) -->
		{#if thumbnailUrl}
			<div class="aspect-video overflow-hidden bg-bg300 md:aspect-auto">
				<img
					src={thumbnailUrl}
					alt={post.title}
					class="h-full w-full object-cover transition-transform duration-200 group-hover:scale-105"
				/>
			</div>
		{/if}

		<!-- Right: Content (50% width on desktop) -->
		<PostContent bind:this={postContent} {post} {formattedDate} {authorName} variant="featured" />
	</div>
</a>
