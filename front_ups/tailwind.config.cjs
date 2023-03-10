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
				primary_b: '#26D7BA',
				secondary: '#73E7A0',
				yellow_third: '#F9F871',
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
