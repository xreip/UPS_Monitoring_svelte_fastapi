<script>
	import OnlineIcon from '~icons/material-symbols/bolt-rounded';
	import UnpluggedIcon from '~icons/mdi/connection';
	import BatteryWarningIcon from '~icons/material-symbols/battery-alert';
	import NoConnectionIcon from '~icons/carbon/connection-signal-off';
	import LoadIcon from '~icons/entypo/bar-graph';
	import BatteryIcon from '~icons/material-symbols/battery-20';
	import VoltIcon from '~icons/material-symbols/electric-bolt-rounded';
	import Icon from '@iconify/svelte';
	let nut_status = 'up';
	let data = [
		{
			name: 'UPS Dell Phase 1',
			model: 'Dell 1920W Power',
			status: 'online',
			batt_charge: 100,
			load: 45,
			voltage: 26.3
		},
		{
			name: 'UPS Dell Phase 2',
			model: 'Dell 1920W Power',
			status: 'onbatt',
			batt_charge: 64,
			load: 12,
			voltage: 25.6
		},
		{
			name: 'UPS Eaton Main Server',
			model: 'Eaton 800W v2.0',
			status: 'lowbatt',
			batt_charge: 24,
			load: 25,
			voltage: 24.9
		},
		{
			name: 'UPS Dell SimFarm',
			model: 'Dell Tower 2000W Power',
			status: 'disconnected',
			batt_charge: 0,
			load: 0,
			voltage: 0
		}
	];
</script>

<svelte:head>
	<title>Home - UPS monitor</title>
	<meta name="Home" content="Home monitoring screen" />
</svelte:head>

<header class="my-6 container mx-auto">
	<div class="flex items-center justify-between">
		<Icon icon="carbon:logo-svelte" height="80" class="text-t_gray_light" />
		<p class="text-xl font-bold text-t_gray_light ">UPS status panel</p>
	</div>
</header>
<main class="container mx-auto">
	<section class="grid gap-4 md:grid-cols-2 2xl:grid-cols-4 3xl:grid-flow-col my-20 px-2">
		{#each data as ups}
			<div
				class="bg-gray_blue rounded-2xl py-8 px-6 border border-p_gray_350 shadow-md min-h-[480px] flex flex-col justify-center items-center"
			>
				<div class="text-t_gray_light font-bold text-xl text-center">{ups.name}</div>
				<div class="text-t_gray_med font-semibold text-lg text-center">{ups.model}</div>
				<div class="flex flex-col items-center p-4">
					{#if ups.status === 'online'}
						<OnlineIcon
							height="140"
							width="140"
							class="text-alert_green drop-shadow-[0_0_5px_#00FF8555]"
						/>
						<div
							class="text-3xl text-alert_green drop-shadow-[0_0_5px_#00FF8555] font-bold capitalize"
						>
							{ups.status}
						</div>
					{/if}
					{#if ups.status === 'onbatt'}
						<UnpluggedIcon
							height="140"
							width="140"
							class="text-alert_orange drop-shadow-[0_0_8px_#FFA80055]"
						/>
						<div
							class="text-3xl text-alert_orange drop-shadow-[0_0_5px_#FFA80038] font-bold capitalize"
						>
							{ups.status}
						</div>
					{/if}
					{#if ups.status === 'lowbatt'}
						<BatteryWarningIcon
							height="140"
							width="140"
							class="text-alert_red drop-shadow-[0_0_8px_#FF000038]"
						/>
						<div
							class="text-3xl text-alert_red drop-shadow-[0_0_5px_#FF000038] font-bold capitalize"
						>
							{ups.status}
						</div>
					{/if}
					{#if ups.status === 'disconnected'}
						<NoConnectionIcon height="140" width="140" class="text-alert_blue" />
						<div class="text-3xl text-p_gray_400 font-bold capitalize">
							{ups.status}
						</div>
					{/if}
				</div>
				<div
					class="text-center text-t_gray_light font-bold text-lg my-1 flex items-center gap-4 justify-between w-full"
				>
					<div class="text-t_gray_med flex items-center gap-4">
						<BatteryIcon height="30" width="30" /><span>Battery charge</span>
					</div>
					<span class={ups.batt_charge < 50 ? 'text-alert_red' : ''}>{ups.batt_charge} %</span>
				</div>
				<div
					class="text-center text-t_gray_light font-bold text-lg my-1 flex items-center gap-4 justify-between w-full"
				>
					<div class="text-t_gray_med flex items-center gap-4">
						<LoadIcon height="30" width="30" /><span>Load</span>
					</div>
					<span>{ups.load} %</span>
				</div>
				<div
					class="text-center text-t_gray_light font-bold text-lg my-1 flex items-center justify-between w-full"
				>
					<div class="text-t_gray_med flex items-center gap-4">
						<VoltIcon height="30" width="30" /><span>Voltage</span>
					</div>
					<span>{ups.voltage} V</span>
				</div>
			</div>
		{/each}
	</section>
</main>
<footer>
	<p class="text-t_gray_med text-center py-4 pt-12">
		<span />nut monitoring is <span class="text-alert_green">{nut_status}</span>
	</p>
</footer>
