%include('header.tpl',title='Pocetna stranica')
<form class="form-horizontal" action='{{form_akcija}}' method='POST'>
<fieldset>

<!-- Form Name -->
<br><br><br>
<legend>Dodavanje novog grada</legend>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="textinput">Unesi naziv grada:</label>  
  <div class="col-md-4">
  <input id="textinput" name="textinput" type="text" placeholder="" class="form-control input-md" required="">
    
  </div>
</div>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="textinput">Dodaj link na sliku tog grada:</label>  
  <div class="col-md-4">
  <input id="textinput" name="textinput" type="text" placeholder="" class="form-control input-md" required="">
    
  </div>
</div>

<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="singlebutton"></label>
  <div class="col-md-4">
    <button id="singlebutton" type='submit' name="singlebutton" class="btn btn-success">Dalje</button>
  </div>
</div>

</fieldset>
</form>



%include('footer.tpl')
