% include('header.tpl', title='Korisnicka stranica')
<style>
.dropbtn {
  background-color: transparent;
  color: #248f8f;
  padding: 10px;
  font-size: 16px;
  border: none;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  margin-right:650px;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  width: auto;
  float:left;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

.container2 {
  padding: 2px 16px;
  background-color:transparent;
}

.dropdown-content a:hover {background-color: white;}

.dropdown:hover .dropdown-content {display: block;}

.dropdown:hover .dropbtn {background-color: white;}
.post{
  display:block;
  position: relative;
  align:center;
  text-align:left;
  padding:10px 10px 10px 10px;
  background-color:white;
  border-radius: 7px;
  box-shadow:5px 5px 5px 5px #9B9493;
}
p{
  font-size:13px;

}
</style>

</body>
<body style="background-image: url('https://wallpaperaccess.com/full/146276.jpg');">
<div class="container" style="margin-top:30px; ">
	<form style="width:100%">
    <ul class="nav nav-tabs">
      <li class="nav-item">
        <a class="nav-link" href="odabiranje_drzave" style='color:#248f8f;'>Dodaj novi grad</a>
      </li>
      <li class="nav-item">
      <div class="dropdown">
        <button class="dropbtn" style="background-color:transparent;">Poruke</button>
      <div class="dropdown-content">
        %if poruke!=[]:
          %for p in poruke:
            <a href='/poruke/{{p['ID_sugovornika']}}'>{{p['USERNAME']}}</a>
          %end
        %else:
          <a href='#'>Nema poruka</a>
        %end
      </div>
      </div>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="postavke_profila" aria-disabled="true" style='color:#248f8f;'>Postavke</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="odjava" style='color:#248f8f;'>Odjava</a>
      </li>
    </ul>      
    <br>  
    <div class="card">
      <div class="container2">
        <h5>Ime:{{data.ime}}</h5>
        <h5>Prezime:  {{data.prezime}}</h5>
        <h5>Spol:  {{data.spol}}</h5>
			</div>
    </div><br>
    
    <div class="col-sm-8">
        <br><br><br><br><br>
          %if lista!=[]:
            %for item in lista:
            <div class="post">
              <h2 >{{item["grad_naziv"]}}
                <span  style="font-size:13px; text-align:right;float:right;">
                  <a href='/azuriranje_posta?postid={{item["id_baze"]}}'>  Uredi</a><br>
                </span>
                <span style="font-size:13px; text-align:right;float:right;">
                  <a href='/izbrisi_post?postid={{item["id_baze"]}}'>Briši</a><br>
                </span>
              </h2>
              <p>OPIS: {{item["opis"]}}</p>
              <p>ZNAMENITOSTI: {{item["znamenitosti"]}}</p>
              <p>PRIJEVOZ: {{item["prijevoz"]}}</p>
              <p>SMJEŠTAJ: {{item["smjestaj"]}}</p>
              <p>HRANA: {{item["hrana"]}}</p>
              <p>ZANIMLJIVOSTI: {{item["zanimljivosti"]}}</p>
              <br>
              </div>
              <br>
            %end
          %end


		</div>
  </form>
</div>

% include("footer.tpl")
