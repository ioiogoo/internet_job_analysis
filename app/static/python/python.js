// 生成全国地图分布图
function LoadMap(data, geoCoordMap) {
    var map_chart_wrap = document.getElementById("map_chart_wrap");
    var map_chart = echarts.init(map_chart_wrap);
    option = null;
    // 这个函数可以不要
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
        tooltip: {
            trigger: 'item',
            formatter: function (params) {
                return params.name + ' : ' + params.value[2];
            }
        },
    // 下面是映射关系
        visualMap: {
            // 自定义分段
            type: 'piecewise',
            pieces: [
            {min: 1, max: 10},
            {min: 10, max: 100},
            {min: 100, max: 1000},
            // {value: 1, label: '1', color: '#98EFAA'},
            ],
            inRange: {
                    symbolSize: [6, 20],
                    color: ['#8517A6', '#64117E', '#4B0D5E']
                    // color: ['purple']
                },
            outOfRange: {
                symbolSize: [5, 30],
                color: '#f3efff'
            }
        },
    // 设置地理位置坐标系
        geo: {
            map: 'china',
            label: {
                emphasis: {
                    show: true
                }
            },
            itemStyle: {
                normal: {
                    // areaColor: '#f3e1e1',
                    areaColor: '#F3F3F3',
                    borderColor: '#111'
                },
                emphasis: {
                    areaColor: '#a7bcd6'
                }
            }
        },
        series: [
            {
                name: 'city_China',
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
            },
            {
            name: 'Top 5',
            type: 'effectScatter',
            coordinateSystem: 'geo',
            data: convertData(data.sort(function (a, b) {
                return b.value - a.value;
            }).slice(0, 6)),
            showEffectOn: 'render',
            rippleEffect: {
                brushType: 'stroke'
            },
            hoverAnimation: true,
            label: {
                normal: {
                    formatter: '{b}',
                    position: 'right',
                    show: true
                }
            },
            itemStyle: {
                normal: {
                    color: '#f4e925',
                    shadowBlur: 10,
                    shadowColor: '#333'
                }
            },
            zlevel: 1,
        },
        ]
    };
    // 生成图表
    if (option && typeof option === "object") {
        map_chart.setOption(option, true);
    };
    // 定义点击事件
    map_chart.on('click', function (params) {
        if (params.componentType == 'series') {
            window.open('/city/' + params.name);
        }
        // window.open('/city/' + params.name);
    });
}

// 生成柱状图 第一个参数y轴，第二个参数x轴， 第三个参数绑定元素
function LoadImage_barChart(y, x ,bindto, onclickname){
    var data_list = ['招聘岗位数量'].concat(y)
    var chart = c3.generate({
        bindto:bindto,
        data : {
            columns:[
            data_list,
            ],

            type: 'bar',

            labels:{
                format:{
                    招聘岗位数量:d3.format('')
                }
            },
            onclick: function(d,i){
                console.log(d)
                var cityIndex = d.x;
                var city = x[cityIndex];
                window.open('/' + onclickname+ '/' + city)
            }
        },

        legend: {
        show : false,
        position: 'right',
                },
        bar: {
        width: {
            ratio: 0.5
        }
        },

        axis:{
            x:{
                type:'category',
                categories :x
            }
        }
    })
}


// 生成饼形图,第一个参数是json数据{'name':'calue', ...}，第二个参数绑定元素，第三个参数是点击后参数变化
function LoadImage_pieChart(json, bindto, onclickname){
    var chart = c3.generate({
        bindto: bindto,
        data :{
            json:json,
            type: 'pie',
            onclick : function(d,i) {
                var keyword = d.id;
                window.open('/' + onclickname + '/' + keyword)
            }
        }
    })
}
