% include('header.tpl', title='Korisnicka stranica')
<style>
.dropbtn {
  background-color: white;
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

.dropdown-content a:hover {background-color: white;}

.dropdown:hover .dropdown-content {display: block;}

.dropdown:hover .dropbtn {background-color: white;}
</style>


<div class="container" style="margin-top:30px">
	<form style="width:100%">
  <ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link" href="odabiranje_drzave" style='color:#248f8f;'>Dodaj novi grad</a>
  </li>
  <li class="nav-item">
  <div class="dropdown">
  <button class="dropbtn">Poruke</button>
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
    <div class="row">
    <div class="col-sm-4">
      
      
      <hr class="d-sm-none">
    </div><br><br>
    <div class="col-sm-0">
      <br>
      <h5>Ime:  {{data.ime}}</h5>
			
			<h5>Prezime:  {{data.prezime}}</h5>
			
      <h5>Spol:  {{data.spol}}</h5>
			<br><br>
    </div>
   <div class="col-sm-8">
			<table class="table">
            <thead>
                <tr>
                <th></th>
                <th scope="col" style="color:#ff8080;">GRAD</th>
                <th scope="col" style="color:#ff8080;">OPIS</th>
                <th scope="col" style="color:#ff8080;">ZNAMENITOSTI</th>
                <th scope="col" style="color:#ff8080;">PRIJEVOZ</th>
                <th scope="col" style="color:#ff8080;">SMJEŠTAJ</th>
                <th scope="col" style="color:#ff8080;">HRANA</th>
                <th scope="col" style="color:#ff8080;">ZANIMLJIVOSTI</th>
                </tr>
            </thead>
            <tbody>

              %if lista!= []:
                %for item in lista:
                    <tr>
                        <th scope="row">{{item["id_baze"]}} </th>
                        <td>{{item["grad_naziv"]}} </td>
                        <td>{{item["opis"]}} </td>
                        <td>{{item["znamenitosti"]}} </td>
                        <td>{{item["prijevoz"]}} </td>
                        <td>{{item["smjestaj"]}} </td>
                        <td>{{item["hrana"]}} </td>
                        <td>{{item["zanimljivosti"]}} </td>
                        <td> 
                            <a href='/azuriranje_posta?postid={{item["id_baze"]}}'>Ažuriraj
                                <i class="fas fa-edit"></i>
                            </a>
                        </td>
                        <td> 
                            <a href='/izbrisi_post?postid={{item["id_baze"]}}'>Briši
                                <i class="fas fa-trash-alt"></i
                            </a>
                        </td>
                        
                    </tr>
                %end
              %end
            </tbody>
        </table>
        <br><br><br><br><br><br>
		</div>
		
  </div>
  </form>
</div>

% include('footer.tpl')
