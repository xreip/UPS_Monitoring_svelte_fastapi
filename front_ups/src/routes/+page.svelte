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
	<section class="grid gap-4 md:grid-cols-2 2xl:grid-cols-4 3xl:grid-flow-col my-20 px-2">
		<!-- {#each upsnotlazy as ups}
			<UpsComp {ups} />
		{/each} -->

		{#await ups}
			<section class="flex items-center justify-center col-span-4 min-h-[50vh]">
				<p class="text-3xl text-t_gray_med font-bold">Loading data...</p>
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
