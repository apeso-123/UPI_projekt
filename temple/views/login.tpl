% include('header.tpl', title='Login')
<div class="container">
	<div id="aplikacija">

        <form>
          <div class="loog">
            <label class="label" for="uname"><b>Korisničko ime:<span class="fb-required">*</span></b></label>
            <input type="text" placeholder="Unesite korisničko ime" name="uname" id="user" required="required" aria-required="true">
            <br>
            <label class="label" for="pass"><b>Lozinka:<span class="fb-required">*</span></b></label>
            <input type="password" placeholder="Unesite lozinku" name="pass" id="pass" required="required" aria-required="true">
            <br>
            <button class="log" id="logiraj_se" type="login">Login</button>
            <button class="reg" id="registiraj"><a href="reg">Registriraj se</a></button>
          </div>

        </form>
    </div>
  </div>
% include('footer.tpl')
