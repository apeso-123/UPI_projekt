% include('header.tpl', title='Korisnicka stranica')

<div class="container" style="margin-top:30px">
	<form style="width:100%">
  <div class="row">
    <div class="col-sm-4">
      <h2>Tu bi tribala slika doc:</h2>
      <br><br><br>

      <ul class="nav nav-pills flex-column">
        <li class="nav-item">
          <a class="nav-link" href="odabiranje_drzave">Dodaj novi grad</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Poruke</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Postavke</a>
        </li>
      </ul>
      <hr class="d-sm-none">
    </div><br><br>
    <div class="col-sm-8">
      <br>
      <h5>Ime:  {{data.ime}}</h5>
			
			<h5>Prezime:  {{data.prezime}}</h5>
			
      <h5>Spol:  {{data.spol}}</h5>
			
    </div>
   <br><br><br>
   <div class="col-sm-8">
			<table class="table">
            <thead>
                <tr>
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
                        <th scope="row">{{item["grad_naziv"]}} </th>
                        <th scope="row">{{item["opis"]}} </th>
                        <th scope="row">{{item["znamenitosti"]}} </th>
                        <th scope="row">{{item["prijevoz"]}} </th>
                        <th scope="row">{{item["smjestaj"]}} </th>
                        <th scope="row">{{item["hrana"]}} </th>
                        <th scope="row">{{item["zanimljivosti"]}} </th>
                        
                        
                    </tr>
                %end
              %end
            </tbody>
        </table>
		</div>
		
  </div>
  </form>
</div>

% include('footer.tpl')
