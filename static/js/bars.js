    function display_refresh(data)
    {
      for (id in data)
      {
        if (data[id].score != dojo.byId("row_score_"+id).innerHTML)
        {
          dojo.byId("row_score_"+id).innerHTML = data[id].score;
          dojo.animateProperty({
                  node: dojo.byId("row_filler_"+id),
                  properties: { width : data[id].score }}).play();
        }
      }

    }
    function display_init(data){
 //     alert(data);
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
                           innerHTML:"&nbsp;",
                           style:"width: "+data[id].score+"px;"},bar_div);
        dojo.create("div",{class:"right_filler",
                           innerHTML:"&nbsp;"},bar_div);
        dojo.create("p",{class:"score",id:"row_score_"+id,innerHTML: data[id].score},bar_div);

      }
      
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

