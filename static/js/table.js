    function display_refresh(data)
    {
      for (team_id in data)
        for (problem_id in data[team_id].score_list)
        {
          wrong = data[team_id].score_list[problem_id].wrong_tries;
          correct = data[team_id].score_list[problem_id].solved;
          if (wrong == 0 && correct == 0)
            continue;

          cell = dojo.byId("cell_"+team_id+"_"+problem_id);

          if ( correct)
            cell.className =  "cell_score correct";
          else
            cell.className = "cell_score wrong";
          cell.innerHTML = correct + wrong;

        }
    }
    function display_init(data){
      // this function creates  the table
      table = dojo.byId("score_table");
      // table headers: 
      if (data.length == 0) 
        return ;
      row = dojo.create("tr",{},table);
      dojo.create("th",{},row);
     
      for (i in data[0].score_list)
        dojo.create("th",{
                          class: "score_table_header",
                          innerHTML: (parseInt(i) + 1)},row);

      for (team_id in data)
      {
        row=dojo.create("tr",{id: "row_"+team_id},table);

        dojo.create("td",{
                          class:"cell_name",
                          innerHTML:data[team_id].name
                        },row);

        for (problem_id in data[team_id].score_list)
        {
          if (team_id % 2)
            color = "white";
          else
            color = "blue";
          cell=dojo.create("td",{ 
                                  id : "cell_"+team_id+"_"+problem_id,
                                  class : "cell_score " + color,
                                },row);
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
