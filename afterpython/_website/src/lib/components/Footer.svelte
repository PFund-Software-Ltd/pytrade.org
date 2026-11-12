<script lang="ts">
	import GitHubIcon from '#lib/components/GitHubIcon.svelte';
	import { devContentUrl } from '#lib/utils/index.ts';

	import { asset, resolve } from '$app/paths';
	import type { ContentType } from '#lib/types/index.ts';

	type FooterProps = {
		projectName?: string;
		repositoryUrl?: string;
		projectSummary?: string;
		contentTypes?: Record<ContentType | 'doc' | 'faq', boolean>;
	};

	let { projectName, repositoryUrl, projectSummary, contentTypes }: FooterProps = $props();

	const currentYear = new Date().getFullYear();
</script>

<footer class="mt-auto border-t border-bg300 bg-bg100">
	<div class="container mx-auto px-4 py-8">
		<!-- Main Footer Content -->
		<div class="mx-auto mb-8 grid max-w-4xl grid-cols-1 gap-8 md:grid-cols-2 md:gap-16">
			<!-- Project Info -->
			<div>
				{#if projectName}
					<div class="mb-3 flex items-center gap-2">
						{#if repositoryUrl}
							<GitHubIcon size={18} url={repositoryUrl} />
						{/if}
						<h3 class="text-lg font-semibold text-tx50">{projectName}</h3>
					</div>
					<p class="text-sm text-tx300">
						{projectSummary}
					</p>
				{/if}
			</div>

			<!-- Resources -->
			<div>
				<h3 class="mb-3 text-lg font-semibold text-tx50">Resources</h3>
				<ul class="space-y-2 text-sm text-tx300">
					{#if devContentUrl('doc') || contentTypes?.doc}
						<li>
							<a
								href={devContentUrl('doc') || `${resolve('doc')}/`}
								target="_blank"
								rel="external noopener noreferrer"
								class="transition-colors hover:text-tx50">Documentation</a
							>
						</li>
					{/if}
					{#if devContentUrl('tutorial') || contentTypes?.tutorial}
						<li>
							<a
								href={resolve('tutorial')}
								data-sveltekit-preload-data
								class="transition-colors hover:text-tx50">Tutorials</a
							>
						</li>
					{/if}
					{#if devContentUrl('example') || contentTypes?.example}
						<li>
							<a
								href={resolve('example')}
								data-sveltekit-preload-data
								class="transition-colors hover:text-tx50">Examples</a
							>
						</li>
					{/if}
					{#if devContentUrl('guide') || contentTypes?.guide}
						<li>
							<a
								href={resolve('guide')}
								data-sveltekit-preload-data
								class="transition-colors hover:text-tx50">Guides</a
							>
						</li>
					{/if}
					{#if devContentUrl('blog') || contentTypes?.blog}
						<li>
							<a
								href={resolve('blog')}
								data-sveltekit-preload-data
								class="transition-colors hover:text-tx50">Blog</a
							>
						</li>
					{/if}
				</ul>
			</div>
		</div>

		<!-- Bottom Bar -->
		<div class="mx-auto max-w-4xl border-t border-bg300 pt-6">
			<div class="flex flex-col items-center justify-between gap-4 md:flex-row">
				<!-- Copyright -->
				<div class="text-sm text-tx300">
					{#if projectName}
						© {currentYear} {projectName}. All rights reserved.
					{:else}
						© {currentYear} All rights reserved.
					{/if}
				</div>

				<!-- Powered by AfterPython -->
				<div class="flex items-center gap-2 text-sm text-tx300">
					<img src={asset('afterpython.svg')} alt="AfterPython" class="h-5 w-auto" />
					<span
						>Powered by <a
							href="https://afterpython.org"
							target="_blank"
							rel="noopener noreferrer"
							class="font-medium text-tx50 transition-colors hover:text-pm500">AfterPython</a
						></span
					>
				</div>
			</div>
		</div>
	</div>
</footer>
