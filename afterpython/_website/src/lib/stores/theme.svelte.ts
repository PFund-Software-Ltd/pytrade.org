import { browser } from '$app/env';

type Theme = 'light' | 'dark';
export type ThemeMode = Theme | 'system';

const MODES: ThemeMode[] = ['system', 'light', 'dark'];

class ThemeStore {
	/** What the user picked; 'system' follows the OS */
	mode = $state<ThemeMode>('system');
	/** OS preference, kept live */
	#systemTheme = $state<Theme>('light');
	/** Theme actually applied */
	theme = $derived<Theme>(this.mode === 'system' ? this.#systemTheme : this.mode);

	constructor() {
		if (browser) {
			const stored = localStorage.getItem('theme');
			if (stored === 'light' || stored === 'dark') this.mode = stored;

			const prefersDarkQuery = window.matchMedia('(prefers-color-scheme: dark)');
			this.#systemTheme = prefersDarkQuery.matches ? 'dark' : 'light';
			prefersDarkQuery.addEventListener('change', (e) => {
				this.#systemTheme = e.matches ? 'dark' : 'light';
				this.#apply();
			});
			this.#apply();
		}
	}

	setMode(mode: ThemeMode) {
		this.mode = mode;
		if (browser) {
			if (mode === 'system') localStorage.removeItem('theme');
			else localStorage.setItem('theme', mode);
			this.#apply();
		}
	}

	/** Cycle: system → light → dark → system */
	toggle() {
		this.setMode(MODES[(MODES.indexOf(this.mode) + 1) % MODES.length]);
	}

	#apply() {
		document.documentElement.classList.toggle('dark', this.theme === 'dark');
	}
}

export const themeStore = new ThemeStore();
