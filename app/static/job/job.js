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
