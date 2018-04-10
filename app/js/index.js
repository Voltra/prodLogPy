import $ from "@js/loadJquery"
import {$json} from "@voltra/json"
import TableGenerator from "@js/TableGenerator"
import generateSpinnerlord from "@js/generateSpinnerlord"
import spinnerLordRemover from "spinner-lord"
import {json} from "@js/urls"

(_ => {
	window.$ = $;
	window.$json = $json;

	Promise.all([
		$json.get(json("form.json"))
	]).then(([form]) => {
		$(document).ready(_ => {


			$('#hidder').on('click', function () {
				$('#geo').slideToggle();
        	});

			console.log("ready");
			const tabGen = new TableGenerator("#result");
			const $form = $(form.form);
			const $input = $form.children(form.field);
			const $select = $form.children(form.select.selector);

			/*Charging the various options into the selector*/
			form.select.options
			.map(({key, value}) => $("<option>", {value: key, text: value}))
			.forEach($option => $option.appendTo($select));

			const validRoutes = form.select.options.map(({key}) => key);

			/*Catching event when submit if fired*/
			$form.on("submit", e => {
				e.preventDefault();

				const value = $input.val();
				const route = $select.val();

				/*Test if the value searched is not empty*/
				if (/^\s*$/.test(value)) {
					const error = "No search data has been given";
					console.error(error);
					$.flash(error, "failure");
					return false
				}

				/*Test if the asked route is actually one of ours own routes, and not a false one*/
				if(!validRoutes.includes(route)){
					const error = "Invalid criteria, nice try ;) !";
					console.error(error);
					$.flash(error, "failure");
					return false;
				}


				/*Creating the route url*/
				const url = (route, value) => form.url.regex
				.replace(form.url.replaceValue, encodeURIComponent(value))
				.replace(form.url.replaceRoute, /*encodeURIComponent(*/route/*)*/);

				/*The actual part that loading the data*/
				generateSpinnerlord($).prependTo(document.body);
				const removeSpinnerlord = spinnerLordRemover.bind(null, $);
				$json.get(url(route, value))
				.then(data => {
					if(data === []) {
						$.flash("There was no value for this research", "failure");
						return data;
					}
					initMap();
				  return Promise.resolve(data.map(item => {
				  	const  title =  item["Nom Equipement"];
					const {Latitude, Longitude} = item;
					addMarker({lat: parseFloat(Latitude), lng: parseFloat(Longitude)}, title, map);
					delete item["Latitude"];
					delete item["Longitude"];
					return item;
				  }));
				}).then(::tabGen.load)
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