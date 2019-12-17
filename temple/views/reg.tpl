<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Bottle web project template">
    <meta name="author" content="datamate">
    <link rel="icon" type='image/x-icon' href="">
    <title>My UPI Project</title>
    <link rel="stylesheet" type="text/css" href="/static/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="/static/custom.css">
    <script type="text/javascript" src="/static/jquery.js"></script>
	<script type="text/javascript" src="/static/custom.js"></script>
    <script type="text/javascript" src="/static/bootstrap.min.js"></script>
</head>

<body>


	  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
	<div>
          <img id="logo" src=""></img><br>
    </div><br><br>
    <div class="container">
      <a class="navbar-brand" href="#">I have been there</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <a class="nav-link" href="/">Home
              <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="gradovi">Što želiš posjetit</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Upute</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="login">Prijavi se</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <div class="container">
    <div id="aplikacija">
       <form >
         <br>
         <h1>Registracija</h1>
         <div >
           <br>
           <div >
             <label for="txt_reg_ime" >Ime<span class="fb-required">*</span></label>
             <input type="text" placeholder="Unesite vaše ime" name="txt_reg_ime" id="txt_reg_ime" required="required" aria-required="true">
           </div>
           <div>
             <br>
             <label for="txt_reg_prezime" >Prezime<span class="fb-required">*</span></label>
             <input type="text" placeholder="Unesite vaše prezime" name="txt_reg_prezime" id="txt_reg_prezime" required="required" aria-required="true">
           </div>
           <div>
             <br>
             <label for="reg_datum">Datum rođenja</label>
             <input type="date" placeholder="Unesite vaš datum rođenja" class="datum" name="reg_datum" id="reg_datum">
           </div>
           <div><br>
             <label for="txt_reg_email" >Email<span class="fb-required">*</span></label>
             <input type="email" placeholder="Unesite vašu email adresu" name="txt_reg_email" id="txt_reg_email" required="required" aria-required="true">
           </div>
           <div><br>

             <label for="txt_reg_user" class="fb-text-label">Korisničko ime:<span class="fb-required">*</span>
             </label>
             <input type="text" placeholder="Unesite korisničko ime" class="reguser" name="txt_reg_user" maxlength="25" id="txt_reg_user" required="required" aria-required="true">
           </div>

           <div>
             <br>
             <label for="reg_lozinka">Lozinka:<span class="fb-required">*</span></label>
             <input type="password" placeholder="Unesite lozinku" name="reg_lozinka" maxlength="20" id="reg_lozinka" required="required">
           </div>
           <div>
             <br>
             <button type="submit" name="btn2" id="btn2" href="dodaj_grad">Registriraj se&nbsp;</button>
           </div>

         </div>

       </form>
  </div>

  </body>
</html>
