/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			screens: {
				'2xl': '1350px'
			},
			colors: {
				primary: '#00ACCF',
				alert_red: '#E02631',
				alert_orange: '#FFA800',
				alert_green: '#00FF85',
				alert_blue: '#4A6B72',
				dark_bg: '#232323',
				gray_blue: '#2C3033',
				t_gray_light: '#A5A5A5',
				t_gray_med: '#606060',
				p_gray_100: 'hsl(190, 0%, 7%)',
				p_gray_150: 'hsl(190, 0%, 13%)',
				p_gray_200: 'hsl(190, 0%, 16%)',
				p_gray_300: 'hsl(190, 0%, 19%)',
				p_gray_350: 'hsl(190, 0%, 27%)',
				p_gray_400: 'hsl(190, 0%, 38%)',
				p_gray_500: 'hsl(190, 5%, 50%)',
				p_gray_600: 'hsl(196, 19%, 65%)',
				p_gray_700: 'hsl(196, 25%, 80%)',
				p_gray_800: 'hsl(190, 39%, 93%)'
			}
		}
	},
	plugins: []
};
