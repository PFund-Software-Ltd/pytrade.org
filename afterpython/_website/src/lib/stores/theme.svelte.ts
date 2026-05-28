import { browser } from '$app/environment';

type Theme = 'light' | 'dark';

class ThemeStore {
	theme = $state<Theme>('light');

	constructor() {
		if (browser) {
			// Initialize from localStorage or system preference
			const stored = localStorage.getItem('theme') as Theme | null;
			const prefersDarkQuery: MediaQueryList = window.matchMedia('(prefers-color-scheme: dark)');
			const systemPrefersDark: boolean = prefersDarkQuery.matches;

			this.theme = stored || (systemPrefersDark ? 'dark' : 'light');
			this.applyTheme(this.theme);

			// Listen for system preference changes
			prefersDarkQuery.addEventListener('change', (e) => {
				if (!localStorage.getItem('theme')) {
					this.setTheme(e.matches ? 'dark' : 'light');
				}
			});
		}
	}

	setTheme(newTheme: Theme) {
		this.theme = newTheme;
		this.applyTheme(newTheme);
		if (browser) {
			localStorage.setItem('theme', newTheme);
		}
	}

	toggle() {
		this.setTheme(this.theme === 'light' ? 'dark' : 'light');
	}

	private applyTheme(theme: Theme) {
		if (browser) {
			if (theme === 'dark') {
				document.documentElement.classList.add('dark');
			} else {
				document.documentElement.classList.remove('dark');
			}
		}
	}
}

export const themeStore = new ThemeStore();
