% include('header.tpl', title='Login')
<style>
* {
  box-sizing: border-box;
}

.bg-img {
  /* The image used */
  background-image: url("https://cdn.lifehack.org/wp-content/uploads/2013/06/083-explore2-1440x900-A-1024x640.jpg");
  
  min-height: 600px;

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
}

/* Add styles to the form container */
.container1 {
  position: absolute;
  right:0 ;
  margin: 20px;
  max-width: 300px;
  padding: 16px;
  background-color: white;
}
</style>

	<div class="bg-img">

        <form style="width:100%" action='{{form_akcija}}' method='POST' class="container1">
          <div><br>
            %if zastavica==True:
              <p style="color:red;">Pogrešno uneseno korisničko ime ili lozinka!</p>
            %end
            <label class="label" for="user_name"><b>Korisničko ime:<span class="fb-required">*</span></b></label>
            <input type="text" placeholder="Unesite korisničko ime" name="user_name" id="user_name" required="required" aria-required="true">
            <br><br>
            <label class="label" for="password"><b>Lozinka:<span class="fb-required">*</span></b></label><br>
            <input type="password" placeholder="Unesite lozinku" name="password" id="password" required="required" aria-required="true">
            <br><br>
            <button class="btn btn-success" type="submit" style="width:120px;height:40px;">Login</button><br><br>
            <button class="btn btn" ><a href="reg">Registriraj se</a></button>
          </div>

        </form>
    </div>
% include('footer.tpl')
