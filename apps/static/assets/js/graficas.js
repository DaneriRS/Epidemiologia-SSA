
// Data retrieved from https://netmarketshare.com/
// Build the chart
Highcharts.chart('insti', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: null,
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: false
            },
            showInLegend: true
        }
    },
    series: [{
        name: 'Porcentaje',
        colorByPoint: true,
        data: [{
            name: 'SSA',
            y: 74.77,
            sliced: true,
            selected: true
        },  {
            name: 'ISSSTE',
            y: 12.82
        },  {
            name: 'IMSS',
            y: 4.63
        }, {
            name: 'SEMAR',
            y: 2.44
        }, {
            name: 'SEDENA',
            y: 2.02
        }, {
            name: 'Other',
            y: 1.28
        }]
    }]
});

// Age categories
var categories = [
    '0-9', '10-19', '20-29', '25-29', '30-39','40-49',
    '50-59', '60-69', '70-79', '80+'
];

Highcharts.chart('edad', {
    chart: {
        type: 'bar'
    },
    title: {
        text: null,
    },
    accessibility: {
        point: {
            valueDescriptionFormat: '{index}. Age {xDescription}, {value}%.'
        }
    },
    xAxis: [{
        categories: categories,
        reversed: false,
        labels: {
            step: 1
        },
        accessibility: {
            description: 'Age (hombre)'
        }
    }, { // mirror axis on right side
        opposite: true,
        reversed: false,
        categories: categories,
        linkedTo: 0,
        labels: {
            step: 1
        },
        accessibility: {
            description: 'Age (mujer)'
        }
    }],
    

    plotOptions: {
        series: {
            stacking: 'normal',
            borderRadius: '50%'
        }
    },

    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + ', Edad ' + this.point.category + '</b><br/>' +
                'Porcentaje: ' + Highcharts.numberFormat(Math.abs(this.point.y), 1) + '%';
        }
    },

    series: [{
        name: 'Hombre',
        data: [
            -8.98, -7.52, -6.65, -5.72, -4.85,
            -3.71, -2.76, -2.07, -1.70, -1.47,
        ]
    }, {
        name: 'Mujer',
        data: [
            8.84, 7.42, 6.57, 5.68, 4.83,
            3.74, 2.80, 2.14, 1.79, 1.59,
        ]
    }]
});

Highcharts.chart('juris', {
    colorAxis: {
        minColor: '#FFFFFF',
        maxColor: Highcharts.getOptions().colors[0]
    },
    series: [{
        type: 'treemap',
        layoutAlgorithm: 'squarified',
        clip: false,
        data: [{
            name: 'JS - Morelia',
            value: 6,
            colorValue: 1
        }, {
            name: 'JS - Zamora',
            value: 6,
            colorValue: 2
        }, {
            name: 'JS - Zitácuaro',
            value: 4,
            colorValue: 3
        }, {
            name: 'JS - Pátzcuaro',
            value: 3,
            colorValue: 4
        }, {
            name: 'JS - Uruapan',
            value: 2,
            colorValue: 5
        }, {
            name: 'JS - Piedad',
            value: 2,
            colorValue: 6
        }, {
            name: 'JS - Apatzingan',
            value: 1,
            colorValue: 7
        }, {
            name: 'JS - Lázaro Cárdenas',
            value: 2,
            colorValue: 6
        }]
    }],
    title: {
        text: 'Highcharts Treemap'
    }
});
