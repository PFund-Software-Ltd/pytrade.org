<script lang="ts">
	let {
		currentPage = $bindable(1),
		totalPages,
		onPageChange
	}: {
		currentPage: number;
		totalPages: number;
		onPageChange?: (page: number) => void;
	} = $props();

	// Calculate page numbers to show
	const visiblePages = $derived.by(() => {
		const pages: (number | '...')[] = [];
		const maxVisible = 7; // Show at most 7 page buttons

		if (totalPages <= maxVisible) {
			// Show all pages if total is small
			for (let i = 1; i <= totalPages; i++) {
				pages.push(i);
			}
		} else {
			// Always show first page
			pages.push(1);

			if (currentPage <= 3) {
				// Near start: show 1, 2, 3, 4, ..., last
				for (let i = 2; i <= 4; i++) {
					pages.push(i);
				}
				pages.push('...');
				pages.push(totalPages);
			} else if (currentPage >= totalPages - 2) {
				// Near end: show 1, ..., last-3, last-2, last-1, last
				pages.push('...');
				for (let i = totalPages - 3; i <= totalPages; i++) {
					pages.push(i);
				}
			} else {
				// Middle: show 1, ..., current-1, current, current+1, ..., last
				pages.push('...');
				for (let i = currentPage - 1; i <= currentPage + 1; i++) {
					pages.push(i);
				}
				pages.push('...');
				pages.push(totalPages);
			}
		}

		return pages;
	});

	function goToPage(page: number) {
		if (page < 1 || page > totalPages || page === currentPage) return;
		currentPage = page;
		onPageChange?.(page);
		// Scroll to top of page
		// window.scrollTo({ top: 0, behavior: 'smooth' });
	}

	function goToPrevious() {
		if (currentPage > 1) {
			goToPage(currentPage - 1);
		}
	}

	function goToNext() {
		if (currentPage < totalPages) {
			goToPage(currentPage + 1);
		}
	}
</script>

{#if totalPages >= 1}
	<nav class="flex justify-center items-center gap-2 py-8" aria-label="Pagination">
		<!-- Previous Button -->
		<button
			type="button"
			onclick={goToPrevious}
			disabled={currentPage === 1}
			class="px-3 py-2 rounded bg-bg100 text-tx50 border border-bd800 hover:bg-bg200 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center gap-2"
			aria-label="Previous page"
		>
			<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
				<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
			</svg>
		</button>

		<!-- Page Numbers -->
		<div class="flex gap-2">
			{#each visiblePages as page}
				{#if page === '...'}
					<span class="px-3 py-2 text-tx300">...</span>
				{:else}
					<button
						type="button"
						onclick={() => goToPage(page)}
						class={[
							'min-w-10 px-3 py-2 rounded transition-colors',
							currentPage === page
								? 'bg-pm500 text-white font-semibold'
								: 'bg-bg100 text-tx50 border border-bd800 hover:bg-bg200'
						]}
						aria-label="Page {page}"
						aria-current={currentPage === page ? 'page' : undefined}
					>
						{page}
					</button>
				{/if}
			{/each}
		</div>

		<!-- Next Button -->
		<button
			type="button"
			onclick={goToNext}
			disabled={currentPage === totalPages}
			class="px-3 py-2 rounded bg-bg100 text-tx50 border border-bd800 hover:bg-bg200 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center gap-2"
			aria-label="Next page"
		>
			<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
				<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
			</svg>
		</button>
	</nav>
{/if}
