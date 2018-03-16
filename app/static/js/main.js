(function(){
    document.addEventListener('DOMContentLoaded', function() {
        console.log("ready");
        var form = document.querySelector("#searchForm");
        form.addEventListener("submit", function(e){
            e.preventDefault();
            var url = "https://reqres.in/api/users";

            var input = form.querySelector("input[name='query']");
            var errorField = document.querySelector("#errorField");

            if (input.value === "") {
                console.log("error");
                errorField.classList.add("error");
                errorField.append("PINGAS");
                return false
            }

            $json.post(url, {
                email: "toto@titi.tata",
                password: input.value
            }).then(function(jsonData){
                console.log(jsonData);
                form.closest("div").append(jsonData);
            }).catch(console.error);
            return false;
        })
    });
})();