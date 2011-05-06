
var time_left= new Date(0,0,0,1,2,3)
function timer_redisplay()
{
    node = dojo.byId("timer");

    node.innerHTML=dojo.date.locale.format(time_left,{ selector: "date",
                                                       datePattern: "H:m:s"});
}
function timer_tick()
{
    time_left.setSeconds( time_left.getSeconds() - 1);
    timer_redisplay();
}

function timer_init()
{ 
    dojo.require("dojo.date.locale");
    dojo.require("dojox.timing");
    var t = new dojox.timing.Timer(1000)
    t.onStart = timer_redisplay;
    t.onTick  = timer_tick;
    t.start()
}

