function updateBalance() {
    $.ajax({
        url: "/updatebalance",
        type: "POST",
        success: function (response) {
            $("#balanceComponent").html(response);
        },
        error: function (xhr) { }
    });
}

function updateWorkersOnline() {
    $.ajax({
        url: "/updateworkersonline",
        type: "POST",
        success: function (response) {
            $("#workersOnlineComponent").html(response);
        },
        error: function (xhr) { }
    });
}

function updateWorkersState() {
    $.ajax({
        url: "/updateworkersstate",
        type: "POST",
        success: function (response) {
            $("#workersStateComponent").html(response);
        },
        error: function (xhr) { }
    });
}

// ---------------------------------------------------------------------------------------------

$("document").ready(function () {
    updateBalance();
    updateWorkersOnline();
    updateWorkersState();
});

var interval = window.setInterval(function () {
    updateBalance();
    updateWorkersOnline();
    updateWorkersState();
}, 1000);
