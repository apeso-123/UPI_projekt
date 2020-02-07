%include('header.tpl',title='Pocetna stranica')
<style>
.forma{
  position:relative;
  align:left;
  
}
</style>
<div class="forma">
<form class="" action='{{form_akcija}}' method='POST'>
<fieldset>

<!-- Form Name -->
<legend>Odaberi grad</legend>

<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="novi"></label>
  <div class="col-md-4">
    <button id="novi" name="novi" style="background-color:transparent;"><a href='/dodaj_novi_grad'>Dodaj novi grad u listu</a></button>
  </div>
</div>

<!-- Select Basic -->
<div class="form-group">
  <label class="col-md-4 control-label" for="selectbasic">Odaberi grad koji si posjetio:</label>
  <div class="col-md-4">
    <select id="odabrani_grad" name="odabrani_grad" class="form-control">
    %if grad!=None:
    %for item in grad:
      <option value={{item.id}}>{{item.naziv}}</option>
    %end
    %end
    </select>
  </div>
</div>

<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="nastavi"></label>
  <div class="col-md-4">
    <button id="nastavi"  name="nastavi" class="btn btn-success" type='submit'>Dalje</button>
    <a href='/korisnicki_profil'>Odustani</a>

  </div>
</div>

</fieldset>
</form>
</div>

%include('footer.tpl')
