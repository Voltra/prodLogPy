import $ from "jquery"
import {$json} from "@voltra/json"

(_ => {
	console.log("ready");
	const $form = $("#searchForm");
	$form.on("submit", e => {
		e.preventDefault();
		const url = "https://reqres.in/api/users";

		const $input = $form.children("input[name='query']");
		const $errorField = $("#errorField");

		if ($input.value === "") {
			console.log("error");
			$errorField.addClass("" +
				"error");
			$errorField.append("PINGAS");
			return false
		}

		$json.post(url, {
			email: "toto@titi.tata",
			password: $input.value
		}).then(jsonData => {
			console.log(jsonData);
			$form.closest("div").append(jsonData);
		}).catch(console.error);
		return false;
	});
})();