var map_chart_wrap = document.getElementById("map_chart_wrap");
var map_chart = echarts.init(map_chart_wrap);
option = null;

var convertData = function (data) {
    var res = [];
    for (var i = 0; i < data.length; i++) {
        var geoCoord = geoCoordMap[data[i].name];
        if (geoCoord) {
            res.push({
                name: data[i].name,
                value: geoCoord.concat(data[i].value)
            });
        }
    }
    return res;
};

option = {
    backgroundColor: '#fff',
    title: {
        text: '全国Python岗位需求量',
        subtext: 'data from Lagou',
        x:'center',
        textStyle: {
            color: '#000'
        }
    },
    tooltip: {
        trigger: 'item',
        formatter: function (params) {
            return params.name + ' : ' + params.value[2];
        }
    },

    visualMap: {
        type: 'piecewise',
        pieces: [
        {value: 1, label: '1', color: '#98EFAA'},
        {min: 1, max: 10},
        {min: 11, max: 110},
        {value: 213, label: '213'},
        {value: 469, label: '469'},
        {min: 110},
        ],
        inRange: {
                symbolSize: [5, 30],
                // color: ['#E0022B', '#E09107', '#A3E00B']
                color: ['#f6efa6', '#d88273', '#bf444c']
            },
        outOfRange: {
            symbolSize: [10, 30],
            color: '#f3efff'
        }
    },

    geo: {
        map: 'china',
        label: {
            emphasis: {
                show: true
            }
        },
        itemStyle: {
            normal: {
                areaColor: '#f3e1e1',
                borderColor: '#111'
            },
            emphasis: {
                areaColor: '#bbb'
            }
        }
    },
    series: [
        {
            name: 'Python',
            type: 'scatter',
            coordinateSystem: 'geo',
            data: convertData(data),
            label: {
                normal: {
                    show: false
                },
                emphasis: {
                    show: false
                }
            },
            itemStyle: {
                emphasis: {
                    borderColor: '#fff',
                    borderWidth: 1
                }
            }
        }
    ]
};
if (option && typeof option === "object") {
    map_chart.setOption(option, true);
};

map_chart.on('click', function (params) {
    // 控制台打印数据的名称
    console.log(params.name);
});
