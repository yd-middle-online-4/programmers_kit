var Links = {
    setColor:function(color) {
        // var alist = document.querySelectorAll('a');
        // var i = 0;
        // while(i < alist.length) {
        //     alist[i].style.color = color;
        //     i++;
        // }
        $('a').css('color', color);
    }       
}
var Body = {
    setColor:function (color) {
        //document.querySelector('body').style.color = color;
        $('body').css('color', color);
    },
    setBackgroundColor:function (color) {
        $('body').css('backgroundColor', color);
    }
}
    
function nightDayHandler(self) {
    var target = document.querySelector('body');
        if (self.value === 'Night Mode') {
            Body.setBackgroundColor('black')
            Body.setColor('white')
            self.value = 'Day Mode';

            Links.setColor('powderblue')
        } else {
            Body.setBackgroundColor('white')
            Body.setColor('black')
            self.value = 'Night Mode'

            Links.setColor('blue')
        }
    }