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
          <img id="logo" src="/logo.jpg"></img><br>
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

  </body>
</html>
