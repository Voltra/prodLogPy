import $ from "jquery"
import {$json} from "@voltra/json"
import TableGenerator from "@js/TableGenerator"

(_ => {
	console.log("ready");

	const $form = $("#searchForm");

	/*Catching event when submit if fired*/
	$form.on("submit", e => {
		e.preventDefault();
		const url = "url to target";

		const $input = $form.children("input[name='query']");
		const $errorField = $("#errorField");

		if ($input.value === "") {
			console.log("error");
			$errorField.addClass("" +
				"error");
			$errorField.append("No search data being given");
			return false
		}

		const tabGen = new TableGenerator("#result");

		const url = _ => "/activites/codePostal?cp=%cp%".replace("%cp%", encodeURIComponent(_));
		$json.get(url($input.val()))
		.then(::tabGen.load)
		.catch(err => $.flash("failure", "There was an error while fetching remote data"));

	});
})();