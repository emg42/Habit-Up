$("#checked-habit").click(function () {});

// function toggle_check() {
//   if (check == "on") {
//     check.value = "off";
//   } else {
//     check.value = "on";
//   }
// }

// function save() {
//   var checkBox = $(this).siblings("div");
//   localStorage.setItem("checkBox", checkBox.checked);
// }

// $("input:checkbox").change(function () {
//   if ($(this).is(":checked")) {
//     alert("checked");
//     save();
//     $(this).siblings("div").wrap("<s>");
//   } else {
//     $(this).not(":checked");
//     alert("unchecked");

//     $(this).prev().unwrap();

//     // $(this).toggle_check();
//   }
// });

// $(document).ready(function () {
//   $(this).click(function () {
//     $("#checked-habit").prop("checked", true);
//   });
//   $(this).click(function () {
//     $("#checked-habit").prop("checked", false);
//   });
// });

let now = moment();

var midnight = "0:00:00";
// var now = null;
var isNow = "16:52:23";
function checkTime() {
  var now = moment().format("H:mm:ss");
  if (now === midnight) {
    $("input:checkbox").attr("checked", false);
  }
}

setInterval(checkTime(), 1000);
