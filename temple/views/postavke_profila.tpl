%include('header.tpl',title='Pocetna stranica')
<style>
.container_postavke{
  box-shadow: 2px 2px 2px 5px transparent;
  margin-left:400px;
  margin-right:500px;
  background-color:white;
  border:2px solid black;
  padding:25px;
  }
.bg-img {
  /* The image used */
  background-image: url("https://images.pexels.com/photos/255379/pexels-photo-255379.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940");
  
  min-height: 600px;

  /* Center and scale the image nicely */
  background-position: center;
  
  position: relative;
}
</style>
</body>
<body class="bg-img"><br>
<form style="width:100%" action='{{form_akcija}}' method='POST'>
<div class="container_postavke">
         <br>
         <h3>Uredi svoj profil:</h3>
         <div >
           <br>
          <label for="txt_reg_ime" >Ime<span class="fb-required">*</span></label>
             <input type="text" placeholder="Unesite vaše ime" name="txt_reg_ime" id="txt_reg_ime" value="{{data.ime}}" required="required" aria-required="true">
            
           </div>
           <div>
             <br>
             <label for="txt_reg_prezime" >Prezime<span class="fb-required">*</span></label>
             <input type="text" placeholder="Unesite vaše prezime" name="txt_reg_prezime" id="txt_reg_prezime" value="{{data.prezime}}" required="required" aria-required="true">
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
            <a href='/korisnicki_profil'>Odustani</a>

           </div>
</div>
</body>
</html>
