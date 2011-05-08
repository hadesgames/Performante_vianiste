
var time_left= new Date(0,0,0,1,2,3)
function timer_redisplay()
{
    dojo.byId("timer_hours").innerHTML = time_left.getHours();
    dojo.byId("timer_minutes").innerHTML = time_left.getMinutes();
    dojo.byId("timer_seconds").innerHTML = time_left.getSeconds();
}
function timer_tick()
{
    time_left.setSeconds( time_left.getSeconds() - 1);
    if (time_left <= new Date(0,0,0,0,0,0) )
    {
      timer_timer.stop()
      timer_span=dojo.byId("timer");
      timer_span.innerHTML="Concursul s-a terminat!";
      return ;
    }

    timer_redisplay();
}

function timer_init()
{ 
    dojo.require("dojox.timing");
    timer_timer = new dojox.timing.Timer(1000)
    timer_timer.onStart = timer_redisplay;
    timer_timer.onTick  = timer_tick;
    timer_timer.start()
}

