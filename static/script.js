document.addEventListener("DOMContentLoaded", function () {

    console.log("Portfolio website loaded successfully!");

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function () {

            console.log("Contact form submitted.");

        });

    }

});