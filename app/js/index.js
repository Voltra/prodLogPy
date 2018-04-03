import $ from "@js/loadJquery"
import {$json} from "@voltra/json"
import TableGenerator from "@js/TableGenerator"
import generateSpinnerlord from "@js/generateSpinnerlord"
import spinnerLordRemover from "spinner-lord"
import {json} from "@js/urls"

(_ => {
	// window.$ = $;
	// window.$json = $json;

	$.when(
		$.getJSON(json("form.json"))
	).done(form => {
		$(document).ready(_ => {
			console.log("ready");
			const tabGen = new TableGenerator("#result");
			const $form = $(form.form);
			const $input = $form.children(form.field);
			const $select = $form.children(form.select.selector);

			form.select.options
			.map(({key, value}) => $("<option>", {value: key, text: value}))
			.forEach($option => $option.appendTo($select));

			const validRoutes = form.select.options.map(({key}) => key);

			/*Catching event when submit if fired*/
			$form.on("submit", e => {
				e.preventDefault();

				const value = $input.val();
				const route = $select.val();

				if (/^\s*$/.test(value)) {
					const error = "No search data has been given";
					console.error(error);
					$.flash(error, "failure");
					return false
				}

				if(!validRoutes.includes(route)){
					const error = "Invalid criteria, nice try ;) !";
					console.error(error);
					$.flash(error, "failure");
					return false;
				}



				const url = (route, value) => form.url.regex
				.replace(form.url.replaceValue, encodeURIComponent(value))
				.replace(form.url.replaceRoute, /*encodeURIComponent(*/route/*)*/);

				generateSpinnerlord($).prependTo(document.body);
				const removeSpinnerlord = spinnerLordRemover.bind(null, $);
				$json.get(url(route, value))
				.then(::tabGen.load)
				.then(removeSpinnerlord)
				.catch(err => {
					$.flash("There was an error while fetching remote data", "failure");
					console.error(err);
					removeSpinnerlord();
				});
			});
		});
	}).catch(console.error);
})();