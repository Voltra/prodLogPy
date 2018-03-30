export default function ($) {
    const $div = $("<div></div>", {
        id: "spinner-lord",
        class: "voltra"
    });

    for(let i in [0,0])
        $("<span>").appendTo($div);

    return $div;
}