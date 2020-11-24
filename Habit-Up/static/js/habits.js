"use strict";

$.get("/OUR_ROUTE", (response) => {
  alert("HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII");
  $("h2").html(response);
});
