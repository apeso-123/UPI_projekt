%include('header.tpl',title='Pocetna stranica')
<br><br><br><br>
<form style="width:100%" action='{{form_akcija}}' method='POST'>
  <div class="col_sm-8">
      <fieldset>
        <div class="form-group">
          <label class="col-md-4 control-label" for="selectbasic">Odaberi državu u kojoj se taj grad nalazi:</label>
          <div class="col-md-4">
            <select id="selectbasic" name="selectbasic" class="form-control">
              %if data != None:
                	%for item in data:
                    <option value={{item.id}}>{{item.naziv}}</option>
                  %end
              %end
            </select><br>
            <div class="col-md-8">
              <button id="singlebutton" name="singlebutton" type="submit" class="btn btn-success">Dalje</button>
            </div>
          </div>
        </div>
      </fieldset>


  </div>
</form
</body>
</html>
