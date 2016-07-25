$(document).ready(function(){
    $('#modal-submit').click(function() {
        var oFReader = new FileReader();
        oFReader.readAsDataURL(document.querySelector("#input_avatar").files[0]);

        oFReader.onload = function (oFREvent) {
            document.getElementById("avatar").src = oFREvent.target.result;
        };
    });
});
