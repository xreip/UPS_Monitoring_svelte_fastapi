export const ssr = false;
import {redirect} from "@sveltejs/kit"
import { user } from "../stores";
import {onDestroy} from 'svelte';

export const load = () => {
	console.log("Ran layout auth check")
    let userValue;
    const unsubscribe = user.subscribe(value => {
        userValue = value;
    })
	if (!userValue) {
		console.log("Access Denied")
		throw redirect(303, "/login")
	}
    onDestroy(unsubscribe)
}