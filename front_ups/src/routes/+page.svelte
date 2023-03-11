<script>
	import ky from 'ky';
	import UpsComp from './UpsComp.svelte';

	async function getDataKy() {
		const response = await ky.get('http://127.0.0.1:8000/ups').json();
		return response;
	}
	let myapidata = getDataKy();

	export let data;
	const { upsData } = data;
</script>

<svelte:head>
	<title>Home - UPS monitor</title>
	<meta name="Home" content="Home monitoring screen" />
</svelte:head>

<main class="container mx-auto">
	<section class="grid gap-4 md:grid-cols-2 2xl:grid-cols-4 3xl:grid-flow-col my-20 px-2">
		{#each upsData as ups}
			<UpsComp {ups} />
		{/each}

		{#await myapidata}
			<p>...waiting</p>
		{:then dataups}
			{#each dataups as ups}
				<UpsComp {ups} />
			{/each}
		{:catch error}
			<p>error : {error}</p>
		{/await}
	</section>
</main>
