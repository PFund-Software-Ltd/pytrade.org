<script lang="ts">
	import { asset, resolve } from '$app/paths';

	type LogoProps = {
		class?: string;
		size?: 'xs' | 'sm' | 'md' | 'lg' | 'xl';
		text?: string;
		showText?: boolean;
		logo?: string | null;
		logoDark?: string | null;
	};

	let {
		class: className = '',
		size = 'md',
		text = '',
		showText = true,
		logo,
		logoDark
	}: LogoProps = $props();

	// Probed in order when no explicit `logo` is configured via metadata.
	const DEFAULT_FORMATS = ['/logo.svg', '/logo.png', '/logo.jpg', '/logo.jpeg'];

	function normalizePath(value: string | null | undefined): string | null {
		const trimmed = value?.trim();
		if (!trimmed) return null;
		return trimmed.startsWith('/') ? trimmed : `/${trimmed}`;
	}

	const explicitLight = $derived(normalizePath(logo));
	const darkPath = $derived(normalizePath(logoDark));

	let lightFallbackIndex = $state(0);
	let hasLight = $state(true);
	let hasDark = $state(true);

	const lightSrc = $derived.by(() => {
		if (!hasLight) return null;
		if (explicitLight) return asset(explicitLight);
		if (lightFallbackIndex >= DEFAULT_FORMATS.length) return null;
		return asset(DEFAULT_FORMATS[lightFallbackIndex]);
	});
	const darkSrc = $derived(darkPath && hasDark ? asset(darkPath) : null);

	const sizeClasses = {
		xs: 'h-6',
		sm: 'h-10',
		md: 'h-14',
		lg: 'h-18',
		xl: 'h-22'
	};

	// Font size classes for logo text - matching MyST's responsive sizing
	const textSizeClasses = {
		xs: 'text-sm sm:text-md tracking-tight',
		sm: 'text-md sm:text-lg tracking-tight',
		md: 'text-md sm:text-xl tracking-tight',
		lg: 'text-lg sm:text-2xl tracking-tight',
		xl: 'text-xl sm:text-3xl tracking-tight'
	};

	function handleLightError() {
		if (!explicitLight && lightFallbackIndex < DEFAULT_FORMATS.length - 1) {
			lightFallbackIndex += 1;
		} else {
			hasLight = false;
		}
	}

	function handleDarkError() {
		hasDark = false;
	}
</script>

{#if lightSrc || darkSrc || (showText && text)}
	<a href={resolve('/')} class="flex items-center gap-3 {className}">
		{#if lightSrc}
			<img
				src={lightSrc}
				alt="Logo"
				class="{sizeClasses[size]} w-auto {darkSrc ? 'dark:hidden' : ''}"
				onerror={handleLightError}
			/>
		{/if}
		{#if darkSrc}
			<img
				src={darkSrc}
				alt="Logo"
				class="{sizeClasses[size]} w-auto {lightSrc ? 'hidden dark:block' : ''}"
				onerror={handleDarkError}
			/>
		{/if}
		{#if showText && text}
			<span class={textSizeClasses[size]}>
				{text}
			</span>
		{/if}
	</a>
{/if}
