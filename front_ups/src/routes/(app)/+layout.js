export const ssr = false;
import {redirect} from "@sveltejs/kit"
import { user } from "../stores";

export const load = () => {
	console.log("Ran layout auth check")
    let userValue;
    user.subscribe(value => {
        userValue = value;
    })
	if (!userValue) {
		console.log("Access Denied")
		throw redirect(303, "/login")
	}
}