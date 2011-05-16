    bars_regress_coef = 3.0 / 5;
    bars_coef = 1;
    bars_max_len = 800;

    function display_refresh(data)
    {
      var max_len = -1;
      var resized = 0;
      for (id in data)
        max_len = Math.max(data[id].score , max_len);

      while (max_len * bars_coef  > bars_max_len)
      {
        bars_coef *= bars_regress_coef;
        resized = 1;
      }

      for (id in data)
      {
        if (data[id].score != dojo.byId("row_score_"+id).innerHTML || resized)
        {
          dojo.byId("row_score_"+id).innerHTML = data[id].score;
          dojo.animateProperty({
                  node: dojo.byId("row_filler_"+id),
                  properties: { width : data[id].score * bars_coef }}).play();
        }
        if ( window.bonus_points == undefined ) 
          continue;
        var bonus_val;
        if ( data[id].correct >= bonus_points.length ) 
          bonus_val = 0;
        else
          bonus_val = bonus_points[data[id].correct];
        if (bonus_val != dojo.byId("row_bonus_"+id).innerHTML)
          dojo.byId("row_bonus_"+id).innerHTML = bonus_val;
          
        
      }

    }
    function display_init(data){
      var list = dojo.byId("list");
      for (id in data)
      {
        var li=dojo.create("li", { class: "row" ,id:"row_"+id },list);
        var name_div=dojo.create("div",{ class: "name" },li);
        dojo.create("p",{class:"p_name",
                        innerHTML: data[id].name},name_div);

        var color
        if (id % 2==0)
          color="green";
        else
          color="blue";
        var bar_div=dojo.create("div",{class: color},li);

        dojo.create("div",{class:"left_filler",
                           innerHTML:"&nbsp;"},bar_div);

        dojo.create("div",{class:"filler",
                           id: "row_filler_"+id,
                           innerHTML:"&nbsp;",},bar_div);
        dojo.create("div",{class:"right_filler",
                           innerHTML:"&nbsp;"},bar_div);
        dojo.create("p",{class:"score",id:"row_score_"+id},bar_div);
        if ( window.bonus_points != undefined )
        {
          dojo.create("p", {class:"score",innerHTML:"(+"},bar_div);
          dojo.create("p",{class:"score",id:"row_bonus_"+id,innerHTML: 0,style:"margin-left:0px;"},bar_div);
          dojo.create("p",{class:"score",innerHTML:")",style:"margin-left:0px;"},bar_div);
        }

      }
      display_refresh(data);
      
    }

    
    function refresh_init()
    {
      dojo.xhrGet({
            url: api_address,
            handleAs: "json",
            load: display_init,
            error: function (){ alert("QQ");} });
    }
    function refresh(){
      dojo.xhrGet({
            url: api_address,
            handleAs: "json",
            load: display_refresh});

    }

