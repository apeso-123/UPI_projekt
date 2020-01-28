%include('header.tpl',title='Pocetna stranica')
<form class="form-horizontal" action='{{form_akcija}}' method='POST'>
<div class="container" style="margin-top:30px; margin-left:midlle;">
<fieldset>

<!-- Form Name -->


<!-- Select Basic -->
  <p id="grad_vrijednost" name="grad_vrijednost" value="{{grad}}"></p>
<div class="container">
  <img src="{{link_slike}}" alt="Notebook" style="width:600px;">

</div>

<!-- Textarea -->
<div class="form-group">
  <label class="col-md-4 control-label" for="opis">Napišite kakav je dojam na Vas ostavio taj grad:</label>
  <div class="col-md-4">                     
    <textarea class="form-control" id="opis" name="opis" required="required"></textarea>
  </div>
</div>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="znamenitosti">Koje ste znamenitosti posjetili?</label>  
  <div class="col-md-4">
  <input id="znamenitosti" name="znamenitosti" type="text" required="required" placeholder=""  class="form-control input-md">  
  </div>
</div>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="smjestaj">U kojem ste smještaju boravili?</label>  
  <div class="col-md-4">
  <input id="smjestaj" name="smjestaj" type="text" placeholder="" required="required" class="form-control input-md">
  </div>
</div>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="prijevoz">Kojim prijevozom ste se najviše služili?</label>  
  <div class="col-md-4">
  <input id="prijevoz" name="prijevoz" type="text" placeholder="" required="required" class="form-control input-md">
  </div>
</div>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="hrana">Koja mjesta za jesti biste preporučili?</label>  
  <div class="col-md-4">
  <input id="hrana" name="hrana" type="text" placeholder="" required="required" class="form-control input-md">
  </div>
</div>

<!-- Textarea -->
<div class="form-group">
  <label class="col-md-4 control-label" for="zanimljivosti">Zanimljivosti koje ste vidjeli ili nešto što Vas je dojmilo?</label>
  <div class="col-md-4">                     
    <textarea class="form-control" id="zanimljivosti" required="required" name="zanimljivosti"></textarea>
  </div>
</div>

<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="singlebutton"></label>
  <div class="col-md-4">
    <button id="singlebutton" name="singlebutton" type="submit" class="btn btn-success">Dodaj</button>
  </div>
</div>

</fieldset>
</div>
</form>

%include('footer.tpl')
