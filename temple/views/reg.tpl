% include('header.tpl',title='Registracija')
  <div class="container">
    <div id="aplikacija">
       <form style="width:100%" action='{{form_akcija}}' method='POST'>
         <br>
         <h1>Registracija</h1>
         <div >
           <br>
           <div >
             <label for="txt_reg_ime" >Ime<span class="fb-required">*</span></label>
             <input type="text" placeholder="Unesite vaše ime" name="txt_reg_ime" id="txt_reg_ime"  required="required" aria-required="true">
           </div>
           <div>
             <br>
             <label for="txt_reg_prezime" >Prezime<span class="fb-required">*</span></label>
             <input type="text" placeholder="Unesite vaše prezime" name="txt_reg_prezime" id="txt_reg_prezime"  required="required" aria-required="true">
           </div>
           <div>
             <label for="reg_spol">Odaberite kojeg ste spola:<span class="fb-required">*</span></label><br>
             <input type="radio" name="reg_spol" value='Z'> Ž<br>
             <input type="radio" name="reg_spol" value='M'> M<br>
           </div>

           <div><br>
             <label for="txt_reg_user" class="fb-text-label">Korisničko ime:<span class="fb-required">*</span>
             </label>
             <input type="text" placeholder="Unesite korisničko ime"  class="reguser" name="txt_reg_user" maxlength="25" id="txt_reg_user" required="required" aria-required="true">
           </div>

           <div>
             <br>
             <label for="reg_lozinka">Lozinka:<span class="fb-required">*</span></label>
             <input type="password" placeholder="Unesite lozinku" name="reg_lozinka" maxlength="20" id="reg_lozinka" required="required">
           </div>
           <div>
             <br>
             <button type="submit">Registriraj se&nbsp;</button>
           </div>

         </div>

       </form>
  </div>
% include('footer.tpl')
