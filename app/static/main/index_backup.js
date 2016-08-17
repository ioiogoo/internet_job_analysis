function LoadImage(){
var chart = c3.generate({
    bindto : '#job_category',
    data: {
        columns: [
            ['data1', 30, 200, 100, 400, 150],
        ],
        names :{
          'data1': '职业'
        },
        type: 'bar',
        onclick: function (d, i) { window.open('') },
        labels : {
        format : {
        data1 : d3.format(''),
                  }
                  }
    },
    axis: {
      x :{
        type : 'category',
        categories : ['python', 'c', 'java', 'c++', ',net']
      }
    },
    // size: {
    //     height: 240,
    //     width: 480
    // }
});
}
