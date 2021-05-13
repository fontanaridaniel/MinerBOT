Chart.defaults.LineWithLine = Chart.defaults.line;
Chart.controllers.LineWithLine = Chart.controllers.line.extend({
    draw: function (ease) {
        Chart.controllers.line.prototype.draw.call(this, ease);
        if (this.chart.tooltip._active && this.chart.tooltip._active.length) {
            var activePoint = this.chart.tooltip._active[0],
                ctx = this.chart.ctx,
                x = activePoint.tooltipPosition().x,
                topY = this.chart.legend.bottom,
                bottomY = this.chart.chartArea.bottom;

            ctx.save();
            ctx.beginPath();
            ctx.moveTo(x, topY);
            ctx.lineTo(x, bottomY);
            ctx.lineWidth = 1;
            ctx.strokeStyle = '#FF0000';
            ctx.stroke();
            ctx.restore();
        }
    }
});

var options = {
    responsive: true,
    maintainAspectRatio: false,
    tooltips: {
        enabled: true,
        intersect: false,
        mode: 'index',
        position: 'average',
        bodySpacing: 6,
    },
    elements: {
        point: {
            radius: 0
        }
    },
    animation: {
        duration: 0
    },
    scales: {
        yAxes: [{
            ticks: {
                suggestedMax: 40,
                suggestedMin: 0
            }
        }],
        xAxes: [{
            ticks: {
                display: false
            }
        }]
    },
};


options.title = { display: true, text: 'HASHRATE [ MH/s ]' };
var hashRatechartCtx = document.getElementById('hashRateChart').getContext('2d');
var hashRateChart = new Chart(hashRatechartCtx, {
    type: "LineWithLine",
    data: {
        labels: [],
        datasets: []
    },
    options: options
});
function updateHashRateChart(create = false) {
    $.ajax({
        type: 'POST',
        url: '/updatehashratechart',
        dataType: "json",
        success: function (result) {

            if (create) hashRateChart.data = result;
            else {
                hashRateChart.data.labels = result.labels;
                hashRateChart.data.datasets.forEach(function (element, index) {
                    element.data = result.datasets[index].data;
                });
            }
            hashRateChart.update();
        }
    });
}

options.title = { display: true, text: 'SHARES ACCEPTED' };
var sharesChartCtx = document.getElementById('sharesChart').getContext('2d');
var sharesChart = new Chart(sharesChartCtx, {
    type: "LineWithLine",
    data: {
        labels: [],
        datasets: []
    },
    options: options
});
function updateSharesChart(create = false) {
    $.ajax({
        type: 'POST',
        url: '/updateshareschart',
        dataType: "json",
        success: function (result) {

            if (create) sharesChart.data = result;
            else {
                sharesChart.data.labels = result.labels;
                sharesChart.data.datasets.forEach(function (element, index) {
                    element.data = result.datasets[index].data;
                });
            }
            sharesChart.update();
        }
    });
}

options.title = { display: true, text: 'POWER [ W ]' };
var powerChartCtx = document.getElementById('powerChart').getContext('2d');
var powerChart = new Chart(powerChartCtx, {
    type: "LineWithLine",
    data: {
        labels: [],
        datasets: []
    },
    options: options
});
function updatePowerChart(create = false) {
    $.ajax({
        type: 'POST',
        url: '/updatepowerchart',
        dataType: "json",
        success: function (result) {

            if (create) powerChart.data = result;
            else {
                powerChart.data.labels = result.labels;
                powerChart.data.datasets.forEach(function (element, index) {
                    element.data = result.datasets[index].data;
                });
            }
            powerChart.update();
        }
    });
}


options.title = { display: true, text: 'TEMPERATURE [ °C ]' };
var temperatureChartCtx = document.getElementById('temperatureChart').getContext('2d');
var temperatureChart = new Chart(temperatureChartCtx, {
    type: "LineWithLine",
    data: {
        labels: [],
        datasets: []
    },
    options: options
});
function updateTemperatureChart(create = false) {
    $.ajax({
        type: 'POST',
        url: '/updatetemperaturechart',
        dataType: "json",
        success: function (result) {

            if (create) temperatureChart.data = result;
            else {
                temperatureChart.data.labels = result.labels;
                temperatureChart.data.datasets.forEach(function (element, index) {
                    element.data = result.datasets[index].data;
                });
            }
            temperatureChart.update();
        }
    });
}

// ---------------------------------------------------------------------------------------------

$(document).ready(function () {
    updateHashRateChart(create = true);
    updateSharesChart(create = true);
    updatePowerChart(create = true);
    updateTemperatureChart(create = true);
})
var intervalId = window.setInterval(function () {
    updateHashRateChart();
    updateSharesChart();
    updatePowerChart();
    updateTemperatureChart();
}, 1000);