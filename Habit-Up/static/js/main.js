// $("#habit-checkbox").change(function(evt) {
//   this.prop("checked", true);
//   alert("checked is true");
//   }
// });

$("input:checkbox").change(function () {
  if ($(this).is(":checked")) {
    alert("checked");
  }

  $("#habit-desc").wrap("<strike>");
});

// $("#input:checkbox").toggle(
//   function () {
//     if ($(this).is(":checked")) {
//       $("#habit-desc").hide(400);
//       $("#check-off-form").append(
//         `<s><div id="habit-striked">{{ habit.habit_name }}</div></s>`
//       );
//     }
//   },

//   function () {
//     if (!$(this).is(":checked")) {
//       $("#habit-desc").show(400);
//       $("#habit-striked").hide(400);
//     }
//   }
// );
