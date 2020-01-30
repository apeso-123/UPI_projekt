%include('header.tpl',title='Nova Poruka')

<form class="form-horizontal" action='{{form_akcija}}' method='POST' style='margin-left:250px;'>
<fieldset>
<br>
<!-- Form Name -->
<h3>Nova poruka</h3>

<input type="hidden" class="form-control" id="broj" name='broj' value='{{primatelj}}'>

<!-- Textarea -->

<div class="form-group">
  <div class="col-md-4">                     
    <textarea class="form-control" id="textarea1" name="textarea1"></textarea>
  </div>
</div>

<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="singlebutton"></label>
  <div class="col-md-4">
    <button id="singlebutton" name="singlebutton" type="submit" class="btn btn-primary">Pošalji</button>
    <a href='/'>Odustani</a>
  </div>
  
</div>

</fieldset>
</form>
 

</body>
</html>
