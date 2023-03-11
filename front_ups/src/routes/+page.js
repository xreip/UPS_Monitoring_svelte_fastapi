export const load = async ({ fetch }) => {
	const upsRes = await fetch('http://127.0.0.1:8000/ups');
	const upsData = await upsRes.json();
	return { upsData };
};
