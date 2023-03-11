export const ssr = false;
import {redirect} from "@sveltejs/kit"

export const load = () => {
	let user = true
	console.log("Ran layout auth check")
	if (!user) {
		console.log("Access Denied")
		throw redirect(303, "/login")
	}
}