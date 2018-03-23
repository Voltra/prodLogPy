import $ from "@js/loadJquery"
import {$json} from "@voltra/json"
import TableGenerator from "@js/TableGenerator"

(_ => {
	$(document).ready(_ => {
		console.log("ready");
		const $form = $("#searchForm");

		/*Catching event when submit if fired*/
		$form.on("submit", e => {
			e.preventDefault();

			const $input = $form.children("input[name='search']");
			const $errorField = $("#errorField");

			if ($input.value === "") {
				console.log("error");
				$errorField.addClass("" +
					"error");
				$errorField.append("No search data being given");
				return false
			}

			const tabGen = new TableGenerator("#result");

			const url = _ => "/activites/codePostal/%zip%".replace("%zip%", encodeURIComponent(_));
			$json.get(url($input.val()))
			.then(::tabGen.load)
			.catch(err => {
				$.flash("failure", "There was an error while fetching remote data");
				console.error(err);
			});

		});
	});
})();