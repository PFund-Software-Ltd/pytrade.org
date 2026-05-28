<script lang="ts">
	import '../app.css';
	import type { LayoutProps } from './$types';
	import ThemeToggle from '$components/ThemeToggle.svelte';
	import Logo from '$components/Logo.svelte';
	import Footer from '$components/Footer.svelte';
	import SearchBar from '$components/SearchBar.svelte';
	import GitHubIcon from '$components/GitHubIcon.svelte';
	import { dev } from '$app/environment';
	import { env } from '$env/dynamic/public';
	import { resolve } from '$app/paths';

	let { data, children }: LayoutProps = $props();

	const faviconType = $derived(
		data.favicon?.endsWith('.svg') ? 'image/svg+xml' : 'image/x-icon'
	);

	// Extract repository URL safely
	const repositoryUrl = $derived(
		data.project_url?.find((url: string) => url.startsWith('repository,'))?.split(', ')[1]
	);

	// Dynamic title from metadata
	const siteTitle = $derived(data.name + "'s Website" || 'AfterPython Project Website');
</script>

<svelte:head>
	<title>{siteTitle}</title>
	<link rel="icon" type={faviconType} href={resolve(`/${data.favicon}`)} />
</svelte:head>

<div class="flex min-h-screen flex-col bg-bg50">
	<nav class="container mx-auto py-3 text-base font-medium text-tx50">
		<div class="flex items-center">
			<Logo size="md" text={data.name} logo={data.logo} logoDark={data.logo_dark} />
			<ul class="flex flex-1 justify-center gap-18">
				{#if dev ? env.PUBLIC_DOC_URL : data.contentTypes?.doc}
					<li>
						<a
							href={dev ? env.PUBLIC_DOC_URL : resolve('/doc')}
							target="_blank"
							rel="external noopener noreferrer"
						>
							Documentation
						</a>
					</li>
				{/if}
				{#if data.contentTypes?.api_reference}
					<li>
						<a
							href="{resolve('/api_reference')}/"
							target="_blank"
							rel="external noopener noreferrer"
						>
							API Reference
						</a>
					</li>
				{/if}
				{#if dev ? env.PUBLIC_TUTORIAL_URL : data.contentTypes?.tutorial}
					<li>
						<a href={resolve('/tutorial')} data-sveltekit-preload-data>Tutorials</a>
					</li>
				{/if}
				{#if dev ? env.PUBLIC_EXAMPLE_URL : data.contentTypes?.example}
					<li>
						<a href={resolve('/example')} data-sveltekit-preload-data>Examples</a>
					</li>
				{/if}
				{#if dev ? env.PUBLIC_GUIDE_URL : data.contentTypes?.guide}
					<li>
						<a href={resolve('/guide')} data-sveltekit-preload-data>Guides</a>
					</li>
				{/if}
				{#if dev ? env.PUBLIC_BLOG_URL : data.contentTypes?.blog}
					<li>
						<a href={resolve('/blog')} data-sveltekit-preload-data>Blog</a>
					</li>
				{/if}
				{#if data.contentTypes?.faq}
					<li>
						<a href={resolve('/faq')} data-sveltekit-preload-data>FAQs</a>
					</li>
				{/if}
				<!-- <li>
					<a href={'/exercises'}>Exercises</a>
				</li>
				<li>
					<a href={'/changelog'}>Changelog</a>
				</li>
				<li>
					<a href={'/community'}>Community</a>
				</li> -->
			</ul>
			<div class="flex items-center gap-2">
				<SearchBar />
				<GitHubIcon size={18} url={repositoryUrl} />
				<ThemeToggle />
			</div>
		</div>
	</nav>

	{@render children()}

	<Footer
		projectName={data.name}
		projectSummary={data.summary}
		contentTypes={data.contentTypes}
		{repositoryUrl}
	/>
</div>
