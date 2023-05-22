// Data retrieved from https://netmarketshare.com/

// Age categories
var gruposEdad = [
    '0-09 Años', '10-19 Años', '20-29 Años', '25-29 Años', '30-39 Años','40-49 Años',
    '50-59 Años', '60-69 Años', '70-79 Años', '80+ Años',
];
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
                enabled: true,
                format: '<b>{point.percentage:.1f} %</b>'
            },
            showInLegend: true
        }
    },
    series: [{
        name: 'Positivos',
        colorByPoint: true,
        data: [{
            name: 'SSA',
            y: 74.77,
            sliced: true,
            selected: true
        },  {
            name: 'IMSS',
            y: 4.63
        },  {
            name: 'ISSSTE',
            y: 12.82
        },  {
            name: 'IMSS-BIENESTAR',
            y: 4.63
        }, {
            name: 'PRIVADA',
            y: 1.28
        }, {
            name: 'SEMAR',
            y: 2.44
        }, {
            name: 'SEDENA',
            y: 2.02
        }]
    }]
});



Highcharts.chart('edad', {
  chart: {
    type: 'bar'
  },
  title: {
    text: null,
  },
  accessibility: {
    point: {
      valueDescriptionFormat: '{index}. Edad {xDescription}, {value}%.'
    }
  },
  xAxis: [{
    categories: gruposEdad,
    labels: {
      step: 1
    },
    accessibility: {
      description: 'Edad (hombre)'
    },
    title: {
      text: 'Grupo de edad'
    },
  }, { // mirror axis on right side
    opposite: true,
    reversed: false,
    labels: {
      step: 1
    },
    accessibility: {
      description: 'Edad (mujer)'
    }
  }],
  yAxis: {
    title: {
      text: 'Confirmados'
    },
    labels: {
      formatter: function() {
        return Math.abs(this.value) + '%';
      }
    },
    accessibility: {
      description: 'Confirmados',
      rangeDescription: 'Range: 0 to 5%'
    }
  },

  plotOptions: {
    series: {
      stacking: 'normal',
      borderRadius: '50%'
    }
  },

  tooltip: {
    formatter: function() {
      return '<b>' + this.series.name + ', : ' + '#' + '</b><br/>' +
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
        text: null
    }
});


Highcharts.chart('defInsti', {
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
                enabled: true,
                format: '<b>{point.percentage:.1f} %</b>',
            },
            showInLegend: true
        }
    },
    series: [{
        name: 'Defunciones',
        colorByPoint: true,
        data: [{
            name: 'SSA',
            y: 74.77,
            sliced: true,
            selected: true
        },  {
            name: 'IMSS',
            y: 4.63
        },  {
            name: 'ISSSTE',
            y: 12.82
        },  {
            name: 'IMSS-BIENESTAR',
            y: 6.63
        }, {
            name: 'PRIVADA',
            y: 0.28
        }, {
            name: 'SEMAR',
            y: 1.44
        }, {
            name: 'SEDENA',
            y: 0.82
        }]
    }]
});



Highcharts.chart('defEdad', {
  chart: {
    type: 'bar'
  },
  title: {
    text: null,
  },
  accessibility: {
    point: {
      valueDescriptionFormat: '{index}. Edad {xDescription}, {value}%.'
    }
  },
  xAxis: [{
    categories: gruposEdad,
    labels: {
      step: 1
    },
    accessibility: {
      description: 'Edad (hombre)'
    },
    title: {
      text: 'Grupo de edad'
    },
  }, { // mirror axis on right side
    opposite: true,
    reversed: false,
    labels: {
      step: 1
    },
    accessibility: {
      description: 'Edad (mujer)'
    }
  }],
  yAxis: {
    title: {
      text: 'Confirmados'
    },
    labels: {
      formatter: function() {
        return Math.abs(this.value) + '%';
      }
    },
    accessibility: {
      description: 'Confirmados',
      rangeDescription: 'Range: 0 to 5%'
    }
  },

  plotOptions: {
    series: {
      stacking: 'normal',
      borderRadius: '50%'
    }
  },

  tooltip: {
    formatter: function() {
      return '<b>' + this.series.name + ', : ' + '#' + '</b><br/>' +
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
