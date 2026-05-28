<script lang="ts">
	import type { ContentType } from '$lib/types';
	import { CONTENT_TYPES } from '$lib/utils/content';
	import { goto } from '$app/navigation';

	let {
		contentType,
		allTags = [],
		selectedTags = $bindable([]),
		sortBy = $bindable('date-desc')
	}: {
		contentType: ContentType;
		allTags?: string[];
		selectedTags?: string[];
		sortBy?: 'date-desc' | 'date-asc' | 'title-asc' | 'title-desc';
	} = $props();

	let showTagDropdown = $state(false);
	let tagDropdownRef: HTMLDivElement | null = $state(null);

	// Handle clicks outside the TagDropdown to close it
	$effect(() => {
		if (!showTagDropdown) return;

		function handleClickOutside(event: MouseEvent) {
			if (tagDropdownRef && !tagDropdownRef.contains(event.target as Node)) {
				showTagDropdown = false;
			}
		}

		document.addEventListener('click', handleClickOutside);
		return () => {
			document.removeEventListener('click', handleClickOutside);
		};
	});

	// Toggle tag selection
	function toggleTag(tag: string) {
		if (selectedTags.includes(tag)) {
			selectedTags = selectedTags.filter((t) => t !== tag);
		} else {
			selectedTags = [...selectedTags, tag];
		}
	}

	// Clear all filters
	function clearFilters() {
		selectedTags = [];
		sortBy = 'date-desc';
	}

	// Check if any filters are active
	const hasActiveFilters = $derived(selectedTags.length > 0 || sortBy !== 'date-desc');

	// Handle content type change
	function onContentTypeChange(newType: ContentType) {
		goto(`/${newType}`);
	}
</script>

<div class="mb-6">
	<div class="flex flex-col gap-3 md:flex-row">
		<!-- Content Type Dropdown -->
		<div class="flex-1">
			<label for="content-type" class="mb-1.5 block text-sm text-tx300"> Content Type </label>
			<select
				id="content-type"
				value={contentType}
				onchange={(e) => onContentTypeChange(e.currentTarget.value as ContentType)}
				class="w-full rounded border border-bd800 bg-bg50 px-3 py-2 text-tx50 transition-colors focus:border-pm500 focus:outline-none"
			>
				{#each CONTENT_TYPES as type}
					<option value={type}>{type.charAt(0).toUpperCase() + type.slice(1)}</option>
				{/each}
			</select>
		</div>

		<!-- Tags Multi-Select -->
		<div class="relative flex-1" bind:this={tagDropdownRef}>
			<label for="tags-filter" class="mb-1.5 block text-sm text-tx300"> Filter by Tags </label>
			<button
				id="tags-filter"
				type="button"
				onclick={() => (showTagDropdown = !showTagDropdown)}
				class="flex w-full items-center justify-between rounded border border-bd800 bg-bg50 px-3 py-2 text-left text-tx50 transition-colors focus:border-pm500 focus:outline-none"
			>
				<span class="truncate">
					{#if selectedTags.length === 0}
						All tags
					{:else if selectedTags.length === 1}
						{selectedTags[0]}
					{:else}
						{selectedTags.length} tags selected
					{/if}
				</span>
				<svg
					class="h-5 w-5 text-tx300 transition-transform {showTagDropdown ? 'rotate-180' : ''}"
					fill="none"
					stroke="currentColor"
					viewBox="0 0 24 24"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M19 9l-7 7-7-7"
					/>
				</svg>
			</button>

			{#if showTagDropdown && allTags.length > 0}
				<div
					class="absolute z-10 mt-1 max-h-60 w-full overflow-y-auto rounded border border-bd800 bg-bg50 shadow-lg"
				>
					{#each allTags as tag}
						<button
							type="button"
							onclick={() => toggleTag(tag)}
							class="flex w-full items-center gap-2 px-4 py-2 text-left text-tx50 transition-colors hover:bg-bg200"
						>
							<div
								class={[
									'flex h-5 w-5 items-center justify-center rounded border-2 border-bd700',
									selectedTags.includes(tag) ? 'border-pm500 bg-pm500' : 'bg-bg50'
								]}
							>
								{#if selectedTags.includes(tag)}
									<svg
										class="h-3 w-3 text-white"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="3"
											d="M5 13l4 4L19 7"
										/>
									</svg>
								{/if}
							</div>
							<span>{tag}</span>
						</button>
					{/each}
				</div>
			{/if}
		</div>

		<!-- Sort Options -->
		<div class="flex-1">
			<label for="sort-by" class="mb-1.5 block text-sm text-tx300"> Sort By </label>
			<select
				id="sort-by"
				bind:value={sortBy}
				class="w-full rounded border border-bd800 bg-bg50 px-3 py-2 text-tx50 transition-colors focus:border-pm500 focus:outline-none"
			>
				<option value="date-desc">Newest first</option>
				<option value="date-asc">Oldest first</option>
				<option value="title-asc">Title (A-Z)</option>
				<option value="title-desc">Title (Z-A)</option>
			</select>
		</div>
	</div>

	<!-- Active Filters Display & Clear Button -->
	{#if hasActiveFilters}
		<div class="mt-3 flex flex-wrap items-center gap-2">
			<span class="text-sm text-tx300">Active filters:</span>

			{#if selectedTags.length > 0}
				{#each selectedTags as tag}
					<button
						type="button"
						onclick={() => toggleTag(tag)}
						class="inline-flex items-center gap-1 rounded bg-pm500 px-2 py-1 text-sm text-white transition-colors hover:bg-pm600"
					>
						<span>{tag}</span>
						<svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M6 18L18 6M6 6l12 12"
							/>
						</svg>
					</button>
				{/each}
			{/if}

			{#if sortBy !== 'date-desc'}
				<span class="rounded bg-bg300 px-2 py-1 text-sm text-tx200">
					Sort: {sortBy === 'date-asc'
						? 'Oldest first'
						: sortBy === 'title-asc'
							? 'Title (A-Z)'
							: 'Title (Z-A)'}
				</span>
			{/if}

			<button
				type="button"
				onclick={clearFilters}
				class="ml-auto text-sm font-medium text-pm500 transition-colors hover:text-pm600"
			>
				Clear all
			</button>
		</div>
	{/if}
</div>
