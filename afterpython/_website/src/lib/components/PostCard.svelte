<script lang="ts">
	import type { ContentJson, ContentType } from '#lib/types/index.ts';
	import { getPostHref, getThumbnailUrl, formatDate, getAuthorName } from '#lib/utils/content.ts';
	import PostContent from './PostContent.svelte';

	let {
		post,
		contentType,
		hideThumbnail = false
	}: { post: ContentJson; contentType: ContentType; hideThumbnail?: boolean } = $props();

	const href = $derived(getPostHref(post, contentType));
	const thumbnailUrl = $derived(getThumbnailUrl(post));
	const formattedDate = $derived(formatDate(post.date));
	const authorName = $derived(getAuthorName(post));

	let postContent: PostContent;
</script>

<a
	{href}
	class="group block overflow-hidden rounded-lg border border-bd900 bg-bg200 shadow-sm transition-all duration-200 hover:-translate-y-1 hover:shadow-xl"
	onmouseleave={() => postContent?.resetTags()}
>
	<!-- Thumbnail -->
	{#if !hideThumbnail && thumbnailUrl}
		<div class="aspect-video w-full overflow-hidden bg-bg300">
			<img
				src={thumbnailUrl}
				alt={post.title}
				class="h-full w-full object-cover transition-transform duration-200 group-hover:scale-105"
			/>
		</div>
	{/if}

	<PostContent bind:this={postContent} {post} {formattedDate} {authorName} variant="card" />
</a>
