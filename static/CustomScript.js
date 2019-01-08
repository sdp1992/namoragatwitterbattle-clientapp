
 var tweetCanvas = document.getElementById("chart_count");
 var tweetCanvasPositive = document.getElementById("chart_positive");
 var tweetCanvasNegative = document.getElementById("chart_negative");

    Chart.defaults.global.defaultFontFamily = "Georgia";
    Chart.defaults.global.defaultFontSize = 18;
    Chart.defaults.global.pointRadius = 1;
    Chart.defaults.global.pointHoverRadius = 2;
    //Chart.defaults.global.animation = 'linear';

    var chartOptions = {
        maintainAspectRatio: false,
        responsive: true,
        legend: {
            display: true,
            position: 'left',
            labels: {
                        boxWidth: 100,
                        fontColor: 'black'
            }
        },
        layout: {
            padding: {
                left: 20,
                right: 20,
                top: 50,
                bottom: 50
            }
        },
        scales: {
            xAxes: [{

                gridLines: {
                    display:false
                }

            }],
            yAxes: [{
                gridLines: {
                    display:true
                },
                ticks: {
                    min: 0,
                    stepSize: 5
                }
            }]
        }
    };

    var lineChart = new Chart(tweetCanvas, {
        type: 'line',
        data: {
            labels: [],
            datasets: [
            {
                    label: "Narendra Modi",
                    data: [],
                    lineTension: 1,
                    fill: false,
                    borderColor: 'rgb(224, 135, 80)',
                    backgroundColor: 'transparent',
                    pointBorderColor: 'rgb(224, 135, 80)',
                    pointBackgroundColor: 'black',
                    pointHitRadius: 5,
                    pointBorderWidth: 1
            },
            {
                    label: "Rahul Gandhi",
                    data: [],
                    lineTension: 1,
                    fill: false,
                    borderColor: 'rgb(67, 153, 219)',
                    backgroundColor: 'transparent',
                    pointBorderColor: 'rgb(67, 153, 219)',
                    pointBackgroundColor: 'black',
                    pointHitRadius: 5,
                    pointBorderWidth: 0
            }
            ]
        },

        options: chartOptions
    });

    var lineChartPositive = new Chart(tweetCanvasPositive, {
        type: 'line',
        data: {
            labels: [],
            datasets: [
            {
                    label: "Narendra Modi",
                    data: [],
                    lineTension: 0.3,
                    fill: false,
                    borderColor: 'rgb(224, 135, 80)',
                    backgroundColor: 'transparent',
                    pointBorderColor: 'rgb(224, 135, 80)',
                    pointBackgroundColor: 'black',
                    pointHitRadius: 30,
                    pointBorderWidth: 1
            },
            {
                    label: "Rahul Gandhi",
                    data: [],
                    lineTension: 0.3,
                    fill: false,
                    borderColor: 'rgb(67, 153, 219)',
                    backgroundColor: 'transparent',
                    pointBorderColor: 'rgb(67, 153, 219)',
                    pointBackgroundColor: 'black',
                    pointHitRadius: 30,
                    pointBorderWidth: 1
            }
            ]
        },

        options: chartOptions
    });

    var lineChartNegative = new Chart(tweetCanvasNegative, {
        type: 'line',
        data: {
            labels: [],
            datasets: [
            {
                    label: "Narendra Modi",
                    data: [],
                    lineTension: 0.3,
                    fill: false,
                    borderColor: 'rgb(224, 135, 80)',
                    backgroundColor: 'transparent',
                    pointBorderColor: 'rgb(224, 135, 80)',
                    pointBackgroundColor: 'black',
                    pointHitRadius: 30,
                    pointBorderWidth: 1
            },
            {
                    label: "Rahul Gandhi",
                    data: [],
                    lineTension: 0.3,
                    fill: false,
                    borderColor: 'rgb(67, 153, 219)',
                    backgroundColor: 'transparent',
                    pointBorderColor: 'rgb(67, 153, 219)',
                    pointBackgroundColor: 'black',
                    pointHitRadius: 30,
                    pointBorderWidth: 1
            }
            ]
        },

        options: chartOptions
    });

    var src_Labels_1 = [];
    var src_NamoData = [];
    var src_RagaData = [];

    var src_Labels_2 = [];
    var src_NamoData_positive = [];
    var src_RagaData_positive = [];

    var src_NamoData_negative = [];
    var src_RagaData_negative = [];

    setInterval(function(){
          $.getJSON('/refreshData', {
            }, function(data) {

               src_Labels_1 = data.sLabel1;
               src_Labels_2 = data.sLabel2;

               src_NamoData = data.sNamoData;
               src_RagaData = data.sRagaData;

               src_NamoData_positive = data.sNamoPositive;
               src_RagaData_positive = data.sRagaPositive;

               src_NamoData_negative = data.sNamoNegative;
               src_RagaData_negative = data.sRagaNegative;

           });

           lineChart.data.labels = src_Labels_1;
           lineChart.data.datasets[0].data = src_NamoData;
           lineChart.data.datasets[1].data = src_RagaData;
           lineChart.update();

           lineChartPositive.data.labels = src_Labels_2;
           lineChartPositive.data.datasets[0].data = src_NamoData_positive;
           lineChartPositive.data.datasets[1].data = src_RagaData_positive;
           lineChartPositive.update();

           lineChartNegative.data.labels = src_Labels_2;
           lineChartNegative.data.datasets[0].data = src_NamoData_negative;
           lineChartNegative.data.datasets[1].data = src_RagaData_negative;
           lineChartNegative.update();

      },1000);