<script lang="ts">
	import { asset, resolve } from '$app/paths';
	import type { AssetPath } from '$app/types';

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
	const DEFAULT_FORMATS = ['logo.svg', 'logo.png', 'logo.jpg', 'logo.jpeg'];

	// `asset()` expects a path relative to `static/` (no leading slash);
	// logo paths come from metadata at runtime, hence the `AssetPath` cast.
	function normalizePath(value: string | null | undefined): AssetPath | null {
		const trimmed = value?.trim().replace(/^\/+/, '');
		if (!trimmed) return null;
		return trimmed as AssetPath;
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
		return asset(DEFAULT_FORMATS[lightFallbackIndex] as AssetPath);
	});
	const darkSrc = $derived(darkPath && hasDark ? asset(darkPath) : null);

	const sizeClasses = {
		xs: 'h-6',
		sm: 'h-10',
		md: 'h-14',
		lg: 'h-18',
		xl: 'h-22'
	};

	// Same heights in px, set as the <img> height attribute: a fallback if CSS is late, so the logo
	// can't flash at its natural size (the default logo.svg is 1024×1024). No width attribute, so any
	// logo keeps its own aspect ratio; the classes above override this once CSS loads.
	const sizePx = {
		xs: 24,
		sm: 40,
		md: 56,
		lg: 72,
		xl: 88
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
				height={sizePx[size]}
				class="{sizeClasses[size]} w-auto {darkSrc ? 'dark:hidden' : ''}"
				onerror={handleLightError}
			/>
		{/if}
		{#if darkSrc}
			<img
				src={darkSrc}
				alt="Logo"
				height={sizePx[size]}
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
