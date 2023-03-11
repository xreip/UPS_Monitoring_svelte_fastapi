<script>
	import OnlineIcon from '~icons/material-symbols/bolt-rounded';
	import UnpluggedIcon from '~icons/mdi/connection';
	import BatteryWarningIcon from '~icons/material-symbols/battery-alert';
	import NoConnectionIcon from '~icons/carbon/connection-signal-off';
	import LoadIcon from '~icons/entypo/bar-graph';
	import BatteryIcon from '~icons/material-symbols/battery-20';
	import VoltIcon from '~icons/material-symbols/electric-bolt-rounded';

	export let ups;

	const upsTypes = {
		online: {
			icon: OnlineIcon,
			text: 'Online',
			theme: 'green'
		},
		onbatt: {
			icon: UnpluggedIcon,
			text: 'On battery',
			theme: 'orange'
		},
		lowbatt: {
			icon: BatteryWarningIcon,
			text: 'Low battery',
			theme: 'red'
		},
		disconnected: {
			icon: NoConnectionIcon,
			text: 'Disconnected',
			theme: 'blue'
		}
	};

	$: definedUps = upsTypes[ups.status];
	$: theme = definedUps.theme;
</script>

<div
	class="bg-gray_blue border-p_gray_350 flex min-h-[480px] flex-col items-center justify-center rounded-2xl border py-8 px-6 shadow-md"
>
	<div class="text-t_gray_light text-center text-xl font-bold">{ups.name}</div>
	<div class="text-t_gray_med text-center text-lg font-semibold">{ups.model}</div>
	<div class="flex flex-col items-center p-4">
		<!-- <svelte:component
			this={definedUps.icon}
			height="140"
			width="140"
			class="text-alert_{theme} drop-shadow-[0_0_5px_{color}]"
		/> -->
		{#if ups.status === 'online'}
			<OnlineIcon
				height="140"
				width="140"
				class="text-alert_green drop-shadow-[0_0_5px_#00FF8555]"
			/>
		{:else if ups.status === 'onbatt'}
			<UnpluggedIcon
				height="140"
				width="140"
				class="text-alert_orange drop-shadow-[0_0_8px_#FFA80055]"
			/>
		{:else if ups.status === 'lowbatt'}
			<BatteryWarningIcon
				height="140"
				width="140"
				class="text-alert_red drop-shadow-[0_0_8px_#FF000038]"
			/>
		{:else if ups.status === 'disconnected'}
			<NoConnectionIcon height="140" width="140" class="text-alert_blue" />
		{/if}
		<div
			class="text-3xl  font-bold capitalize"
			class:text-alert_red={theme === 'red'}
			class:drop-shadow-[0_0_8px_#FF000038]={theme === 'red'}
			class:text-alert_orange={theme === 'orange'}
			class:drop-shadow-[0_0_8px_#FFA80055]={theme === 'orange'}
			class:text-alert_green={theme === 'green'}
			class:drop-shadow-[0_0_5px_#00FF8555]={theme === 'green'}
			class:text-t_gray_med={theme === 'blue'}
		>
			{definedUps.text}
		</div>
	</div>
	<div
		class="text-t_gray_light my-1 flex w-full items-center justify-between gap-4 text-center text-lg font-bold"
	>
		<div class="text-t_gray_med flex items-center gap-4">
			<BatteryIcon height="30" width="30" class="hover:text-t_gray_light" /><span
				>Battery charge</span
			>
		</div>
		<span class={ups.batt_charge < 50 ? 'text-alert_red' : ''}>{ups.batt_charge} %</span>
	</div>
	<div
		class="text-t_gray_light my-1 flex w-full items-center justify-between gap-4 text-center text-lg font-bold"
	>
		<div class="text-t_gray_med flex items-center gap-4">
			<LoadIcon height="30" width="30" class="hover:text-t_gray_light" /><span>Load</span>
		</div>
		<span>{ups.load} %</span>
	</div>
	<div
		class="text-t_gray_light my-1 flex w-full items-center justify-between text-center text-lg font-bold"
	>
		<div class="text-t_gray_med flex items-center gap-4">
			<VoltIcon height="30" width="30" class="hover:text-t_gray_light" /><span>Voltage</span>
		</div>
		<span>{ups.voltage} V</span>
	</div>
</div>
