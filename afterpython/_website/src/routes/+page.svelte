<script lang="ts">
	import type { PageProps } from './$types';
	import MarkdownRenderer from '$components/MarkdownRenderer.svelte';
	import Announcement from '$components/Announcement.svelte';
	import StarIcon from '$components/StarIcon.svelte';
	import { dev } from '$app/environment';
	import { env } from '$env/dynamic/public';
	import { resolve } from '$app/paths';

	const { data }: PageProps = $props();

	// Extract repository URL safely
	const repositoryUrl = $derived(
		data.project_url?.find((url: string) => url.startsWith('repository,'))?.split(', ')[1]
	);

	// Page-specific title
	const pageTitle = $derived(data.name ? `${data.name} - Home` : 'Home');
</script>

<svelte:head>
	<title>{pageTitle}</title>
	{#if data.summary}
		<meta name="description" content={data.summary} />
		<!-- Open Graph -->
		<meta property="og:title" content={pageTitle} />
		<meta property="og:description" content={data.summary} />
		<meta property="og:type" content="website" />
		<meta property="og:image" content="/thumbnail.png" />
		<!-- Twitter Card -->
		<meta name="twitter:card" content="summary_large_image" />
		<meta name="twitter:title" content={pageTitle} />
		<meta name="twitter:description" content={data.summary} />
	{/if}
</svelte:head>

{#if data.announcement}
	<Announcement content={data.announcement} />
{/if}

{#if data.metadataError}
	<!-- Error state: metadata.json is missing -->
	<section
		class="mt-[12vh] flex min-h-[60vh] flex-col items-center justify-center gap-6 px-4 text-center"
	>
		<div class="w-full max-w-2xl rounded-2xl border-2 border-pm500 bg-bg200 px-6 py-8 shadow-lg">
			<h1 class="mb-4 text-4xl font-bold text-pm500">500</h1>
			<p class="mb-2 text-left text-xl text-tx100">
				{data.metadataError}
			</p>
		</div>
	</section>
{:else}
	<!-- Normal state: metadata loaded successfully -->
	<section
		class="mt-[12vh] flex min-h-[60vh] flex-col items-center justify-center gap-6 px-4 text-center"
	>
		<h1
			class="flex flex-wrap justify-center gap-x-2 text-6xl font-bold tracking-tight text-tx50 md:text-7xl"
		>
			{#each data.name.split(' ') as word, wordIndex}
				<span class="inline-flex">
					{#each word.split('') as char, charIndex}
						<span
							class="animate-slide-in inline-block opacity-0"
							style="animation-delay: {(wordIndex * word.length + charIndex) *
								0.05}s; animation-fill-mode: forwards;"
						>
							{char}
						</span>
					{/each}
				</span>
			{/each}
		</h1>
		<p class="max-w-2xl text-xl text-tx300 md:text-2xl">
			{data.summary}
		</p>

		<div class="flex flex-wrap justify-center gap-4">
			{#if repositoryUrl}
				<a
					href={repositoryUrl}
					target="_blank"
					rel="noopener noreferrer"
					class="group flex transform items-center gap-2 rounded-lg bg-yellow-400 px-6 py-3 font-semibold text-gray-900 shadow-lg transition-all duration-200 hover:scale-105 hover:bg-yellow-500 hover:shadow-xl dark:bg-yellow-400 dark:text-gray-900 dark:hover:bg-yellow-500"
				>
					<StarIcon size={20} filled={true} class="star-blink" />
					Star on GitHub
				</a>
			{/if}
			{#if data.contentTypes?.doc}
				<a
					href={dev ? env.PUBLIC_DOC_URL : resolve('/doc')}
					rel="external noopener noreferrer"
					class="rounded-lg bg-pm500 px-6 py-3 font-medium text-white transition-colors hover:bg-pm600"
				>
					Go to Documentation
				</a>
			{/if}
		</div>

		{#if data.readme_py}
			<iframe
				src={resolve('/readme_py/readme_py.html')}
				title="README"
				loading="lazy"
				class="h-[96vh] w-full max-w-4xl rounded-2xl border mb-28 border-bg300 bg-bg100 text-left shadow-lg"
			></iframe>
		{:else if data.description}
			<div
				class="w-full max-w-4xl rounded-2xl border border-bg300 bg-bg100 px-6 py-8 text-left shadow-lg"
			>
				<MarkdownRenderer content={data.description} />
			</div>
		{/if}
	</section>
{/if}

<style>
	@keyframes star-blink {
		0%,
		100% {
			opacity: 1;
			transform: scale(1);
		}
		50% {
			opacity: 0.6;
			transform: scale(1.2);
		}
	}

	:global(.star-blink) {
		animation: star-blink 1.5s ease-in-out infinite;
	}

	@keyframes slide-in {
		0% {
			opacity: 0;
			transform: translateX(100px) rotate(90deg);
		}
		100% {
			opacity: 1;
			transform: translateX(0) rotate(0deg);
		}
	}

	.animate-slide-in {
		animation: slide-in 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
	}
</style>
