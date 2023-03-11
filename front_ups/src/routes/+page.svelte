<script>
	import UpsComp from './UpsComp.svelte';

	export let data;
	const { ups } = data.lazy;
	// const { upsnotlazy } = data;
</script>

<svelte:head>
	<title>Home - UPS monitor</title>
	<meta name="Home" content="Home monitoring screen" />
</svelte:head>

<main class="container mx-auto">
	<section class="3xl:grid-flow-col my-20 grid gap-4 px-2 md:grid-cols-2 2xl:grid-cols-4">
		<!-- {#each upsnotlazy as ups}
			<UpsComp {ups} />
		{/each} -->

		{#await ups}
			<section class="col-span-4 flex min-h-[50vh] items-center justify-center">
				<p class="text-t_gray_med text-3xl font-bold">Loading data...</p>
			</section>
		{:then dataups}
			{#each dataups as ups}
				<UpsComp {ups} />
			{/each}
		{:catch error}
			<p>error : {error}</p>
		{/await}
	</section>
</main>
