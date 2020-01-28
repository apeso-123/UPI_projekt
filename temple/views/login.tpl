% include('header.tpl', title='Login')
<div class="container">
	<div id="aplikacija">

        <form style="width:100%" action='{{form_akcija}}' method='POST'>
          <div class="loog"><br>
            %if zastavica==True:
              <p style="color:red;">Pogrešno uneseno korisničko ime ili lozinka!</p>
            %end
            <label class="label" for="user_name"><b>Korisničko ime:<span class="fb-required">*</span></b></label>
            <input type="text" placeholder="Unesite korisničko ime" name="user_name" id="user_name" required="required" aria-required="true">
            <br><br>
            <label class="label" for="password"><b>Lozinka:<span class="fb-required">*</span></b></label>
            <input type="password" placeholder="Unesite lozinku" name="password" id="password" required="required" aria-required="true">
            <br><br>
            <button class="btn btn-success" type="submit">Login</button><br><br>
            <button class="btn btn-success" ><a href="reg">Registriraj se</a></button>
          </div>

        </form>
    </div>
  </div>
% include('footer.tpl')
