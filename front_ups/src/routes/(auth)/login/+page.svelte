<script>
	// Svelte
	import { fly, fade } from 'svelte/transition';
	import { goto } from '$app/navigation';
	import { user } from '../../stores';

	let codes = ['', '', '', '', '', ''];
	let refs = [];
	let inputError = '';

	$: codeString = codes.join('');

	function handleInput(event, index) {
		codes[index] = event.target.value;

		if (index < refs.length - 1 && event.target.value.length === 1) {
			refs[index + 1].focus();
		}
	}

	async function handleSubmit(e) {
		inputError = '';
		if (codeString.length === 6) {
			console.log(codeString);
			// getting the action url

			try {
				const ACTION_URL = e.target.action;

				const data = {
					code: codeString
				};
				const res = await fetch(ACTION_URL, {
					method: 'POST',
					body: JSON.stringify(data),
					headers: {
						'content-type': 'application/json'
					}
				});
				if (!res.ok) {
					throw new Error(`Fetch error: ${res}`);
				}
				$user = true;
				goto('/');
			} catch (error) {
				console.log(error);
				inputError = 'Bad OTP code';
				codes = ['', '', '', '', '', ''];
			}
		} else {
			inputError = 'Code must be 6 characters long';
		}
	}
</script>

<section class="container mx-auto my-6 flex min-h-[50vh] flex-col items-center justify-center p-4">
	<h2 class="text-t_gray_med mt-2 p-2 text-center text-5xl font-bold">Login</h2>
	<h3 class="text-p_gray_350 mb-2 text-center text-xl font-semibold">Enter your OTP code</h3>
	<form
		action="http://127.0.0.1:8000/otp"
		on:submit|preventDefault={handleSubmit}
		class="bg-gray_blue border-p_gray_350  relative flex min-h-[200px] flex-col items-center justify-evenly rounded-2xl border py-10 px-6 drop-shadow-[0_0px_10px_rgba(0,0,4,0.35)]"
	>
		<div class="flex min-w-[20rem] items-center justify-center gap-4 px-4 pb-4">
			{#each [...Array(6).keys()] as index}
				<input
					type="text"
					maxlength="1"
					bind:this={refs[index]}
					on:input={(event) => handleInput(event, index)}
					value={codes[index]}
					class="border-p_gray_600 bg-p_gray_350 text-p_gray_800 
                focus-visible:outline-primary  h-[2.5rem] max-w-[2.5rem] rounded-md border text-center 
                text-2xl font-bold focus:outline-none"
				/>
			{/each}
		</div>
		<button
			type="submit"
			class="border-b-p_gray_350 bg-p_gray_500
        hover:border-p_gray_500 hover:bg-p_gray_700 mt-4 rounded-xl 
        border-b-4 py-2 px-8 font-bold text-white shadow 
        active:translate-y-1 active:scale-[98%]
        ">Login</button
		>
		{#if inputError}
			<p
				in:fly={{ y: 20, duration: 200 }}
				out:fade={{ duration: 100 }}
				class="text-alert_red absolute bottom-3 text-sm"
			>
				{inputError}
			</p>
		{/if}
	</form>
</section>
