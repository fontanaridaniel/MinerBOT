function updateMonthWarningsComparison() {
    $.ajax({
        url: "/updatemonthearningscomparison",
        type: "POST",
        success: function (response) {
            $("#monthWarningsComparison").html(response);
        },
        error: function (xhr) { }
    });
}

// var workDoneChartCtx = document.getElementById('workDoneChart').getContext('2d');
// var workDoneChart = new Chart(workDoneChartCtx, {
//     type: "pie",
//     data: {
//         labels: [],
//         datasets: [{
//             label: '',
//             data: [],
//             backgroundColor: ''
//         }]
//     },
//     options: {
//         responsive: true,
//         maintainAspectRatio: false,
//         legend: {
//             display: false,
//         },
//         animation: {
//             duration: 0
//         },
//     }
// });

function updateWorkDoneChart(create = false) {
    $.ajax({
        type: 'POST',
        url: '/updateworkdonechart',
        dataType: "json",
        success: function (result) {
            if (create)
                workDoneChart.data = result;
            else {
                workDoneChart.data.datasets.data = result["datasets"]["data"];
            }
            workDoneChart.update();
        }
    });
}


function updateWorkersEarnings() {
    $.ajax({
        url: "/updateworkersearnings",
        type: "POST",
        success: function (response) {
            $("#workersEarnings").html(response);
        },
        error: function (xhr) { }
    });
}

// ---------------------------------------------------------------------------------------------

$("document").ready(function () {
    updateMonthWarningsComparison();
    // updateWorkDoneChart(create = true);
    updateWorkersEarnings();
});

var interval = window.setInterval(function () {
    updateMonthWarningsComparison();
    // updateWorkDoneChart();
    updateWorkersEarnings();
}, 1000);
