%include('header.tpl',title='Ažuriranje posta')

<form class="form-horizontal" action='{{form_akcija}}' method='POST'>
<div class="container" style="margin-top:30px; margin-left:midlle;">
<fieldset>
<input type="hidden" class="form-control" id="postid" name='postid' value='{{data.id_baze if data != None else ""}}'>
<input type="hidden" class="form-control" id="gradid" name='gradid' value='{{data.grad_id if data != None else ""}}'>

<!-- Textarea -->
<div class="form-group">
  <label class="col-md-4 control-label" for="opis">Napišite kakav je dojam na Vas ostavio taj grad:</label>
  <div class="col-md-4">                     
    l<textarea cass="form-control" id="opis" name="opis" required="required">{{data.opis}}</textarea>
  </div>
</div>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="znamenitosti">Koje ste znamenitosti posjetili?</label>  
  <div class="col-md-4">
  <input id="znamenitosti" name="znamenitosti" type="text" required="required" value="{{data.znamenitosti}}"  class="form-control input-md">  
  </div>
</div>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="smjestaj">U kojem ste smještaju boravili?</label>  
  <div class="col-md-4">
  <input id="smjestaj" name="smjestaj" type="text" value="{{data.smjestaj}}" required="required" class="form-control input-md">
  </div>
</div>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="prijevoz">Kojim prijevozom ste se najviše služili?</label>  
  <div class="col-md-4">
  <input id="prijevoz" name="prijevoz" type="text" value="{{data.prijevoz}}" required="required" class="form-control input-md">
  </div>
</div>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="hrana">Koja mjesta za jesti biste preporučili?</label>  
  <div class="col-md-4">
  <input id="hrana" name="hrana" type="text" value="{{data.hrana}}" required="required" class="form-control input-md">
  </div>
</div>

<!-- Textarea -->
<div class="form-group">
  <label class="col-md-4 control-label" for="zanimljivosti">Zanimljivosti koje ste vidjeli ili nešto što Vas je dojmilo?</label>
  <div class="col-md-4">                     
    <textarea class="form-control" id="zanimljivosti" required="required" name="zanimljivosti">{{data.zanimljivosti}}</textarea>
  </div>
</div>

<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="singlebutton"></label>
  <div class="col-md-4">
    <button id="singlebutton" name="singlebutton" type="submit" class="btn btn-success">Spremi</button>
    <a href='/korisnicki_profil'>Odustani</a>

  </div>
</div>

</fieldset>
</div>
</form>

%include('footer.tpl')
