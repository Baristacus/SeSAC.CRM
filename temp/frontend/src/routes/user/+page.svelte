<script>
	import { onMount } from 'svelte';
	import { getUsers } from '$lib/user';

	let users = [];

	onMount(async () => {
		try {
			users = await getUsers(1);
			console.log(users);
		} catch (error) {
			console.error(error);
		}
	});
</script>

<main>
	<h1>User Page</h1>
</main>

<style></style>
