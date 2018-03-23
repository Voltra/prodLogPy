import $ from "jquery"
import {$json} from "@voltra/json"

(_ => {
	console.log("ready");
	const form = document.querySelector("#searchForm");
	form.addEventListener("submit", e => {
		e.preventDefault();
		const url = "https://reqres.in/api/users";

		const input = form.querySelector("input[name='query']");
		const errorField = document.querySelector("#errorField");

		if (input.value === "") {
			console.log("error");
			errorField.classList.add("error");
			errorField.append("PINGAS");
			return false
		}

		$json.post(url, {
			email: "toto@titi.tata",
			password: input.value
		}).then(jsonData => {
			console.log(jsonData);
			form.closest("div").append(jsonData);
		}).catch(console.error);
		return false;
	});
})();