%include('header.tpl',title='Pocetna stranica')
<form style="width:100%" action='{{form_akcija}}' method='POST'>
<div style="margin-left:100px;">
         <br>
         <h1>Uredi svoj profil:</h1>
         <div >
           <br>
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
           <div>
             <br>
             <label for="reg_lozinka">Lozinka:<span class="fb-required">*</span></label>
             <input type="password" placeholder="Unesite lozinku" name="reg_lozinka" maxlength="20" id="reg_lozinka" required="required">
           </div>
           <div>
             <br>
             <button type="submit" class="btn btn-success">Spremi promjene&nbsp;</button>
           </div>
</div>
</body>
</html>
