<script lang="ts">
	import FeaturedPost from '$lib/components/FeaturedPost.svelte';
	import PostCard from '$components/PostCard.svelte';
	import FilterBar from '$lib/components/FilterBar.svelte';
	import Pagination from '$lib/components/Pagination.svelte';
	import { getThumbnailUrl } from '$lib/utils/content';
	import type { PageData } from './$types';
	import type { ContentJson } from '$lib/types';

	let { data }: { data: PageData } = $props();

	// Filter and pagination state
	let selectedTags = $state<string[]>([]);
	let sortBy = $state<'date-desc' | 'date-asc' | 'title-asc' | 'title-desc'>('date-desc');
	let currentPage = $state(1);
	const postsPerPage = 9; // 3x3 grid

	// Check if ALL posts lack thumbnails
	const allPostsLackThumbnails = $derived(
		data.posts.length > 0 && data.posts.every((post) => !getThumbnailUrl(post))
	);

	// Extract all unique tags from posts
	const allTags = $derived.by(() => {
		const tagSet = new Set<string>();
		data.posts.forEach((post) => {
			post.tags?.forEach((tag) => tagSet.add(tag));
		});
		return Array.from(tagSet).sort();
	});

	// Filter posts by selected tags
	const filteredPosts = $derived.by(() => {
		let posts = data.posts;

		// Filter by tags
		if (selectedTags.length > 0) {
			posts = posts.filter((post) => post.tags?.some((tag) => selectedTags.includes(tag)));
		}

		// Helper function to check for valid date
		const hasValidDate = (post: ContentJson): boolean => !!post.date && post.date.trim() !== '';

		// Sort posts
		const sorted = [...posts];
		if (sortBy === 'date-desc' || sortBy === 'date-asc') {
			// Check if ANY posts have dates
			const hasAnyDates = sorted.some(hasValidDate);

			if (hasAnyDates) {
				sorted.sort((a, b) => {
					// Posts without dates (empty string, null, undefined) go to the END
					const hasDateA = hasValidDate(a);
					const hasDateB = hasValidDate(b);

					if (!hasDateA && !hasDateB) return 0; // Both missing → keep order
					if (!hasDateA) return 1; // a missing → push down
					if (!hasDateB) return -1; // b missing → push down

					// Both have dates → normal sort
					const dateA = new Date(a.date!).getTime();
					const dateB = new Date(b.date!).getTime();
					return sortBy === 'date-desc' ? dateB - dateA : dateA - dateB;
				});
			}
			// Case 3: No dates at all → skip sorting, keep original order
		} else if (sortBy === 'title-asc') {
			sorted.sort((a, b) => a.title.localeCompare(b.title));
		} else if (sortBy === 'title-desc') {
			sorted.sort((a, b) => b.title.localeCompare(a.title));
		}

		return sorted;
	});

	// Get featured post (marked as featured, or first if none marked) and paginated grid posts
	const featuredPost = $derived(filteredPosts.find((post) => post.featured));
	const allGridPosts = $derived.by(() => {
		return filteredPosts.filter((post) => post !== featuredPost);
	});

	// Calculate pagination
	const totalPages = $derived(Math.ceil(allGridPosts.length / postsPerPage));
	const paginatedGridPosts = $derived.by(() => {
		const start = (currentPage - 1) * postsPerPage;
		const end = start + postsPerPage;
		return allGridPosts.slice(start, end);
	});

	// Reset to page 1 when filters change
	$effect(() => {
		// This runs whenever selectedTags or sortBy changes
		selectedTags;
		sortBy;
		currentPage = 1;
	});

	// Capitalize content type for display
	const displayTitle = $derived.by(() => {
		return data.contentType.charAt(0).toUpperCase() + data.contentType.slice(1);
	});

	
</script>

<svelte:head>
	<title>{displayTitle} - {data.projectName || 'afterpython'}</title>
	<meta
		name="description"
		content="Browse {displayTitle.toLowerCase()} for {data.projectName || 'afterpython'}"
	/>
</svelte:head>

<div class="container mx-auto px-4 py-8">
	<!-- Page Title -->
	<h1 class="mb-8 text-4xl font-bold text-tx50">
		{displayTitle}
	</h1>

	<!-- Featured Post (if exists) -->
	{#if featuredPost}
		<div class="mb-20">
			<FeaturedPost post={featuredPost} contentType={data.contentType} />
		</div>
	{/if}

	<FilterBar
		contentType={data.contentType}
		{allTags}
		bind:selectedTags
		bind:sortBy
	/>

	<!-- Grid Items -->
	{#if paginatedGridPosts.length > 0}
		<div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
			{#each paginatedGridPosts as post (post.slug)}
				<PostCard {post} contentType={data.contentType} hideThumbnail={allPostsLackThumbnails} />
			{/each}
		</div>
	{:else if allGridPosts.length === 0}
		<p class="py-12 text-center text-tx400">No posts available yet.</p>
	{:else}
		<p class="py-12 text-center text-tx400">No posts match the selected filters.</p>
	{/if}

	<Pagination bind:currentPage {totalPages} />
</div>
