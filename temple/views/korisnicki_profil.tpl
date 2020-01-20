% include('header.tpl', title='Korisnicka stranica')
<div class="container" style="margin-top:30px">
	<form style="width:100%" action='{{form_akcija}}' method='POST'>
  <div class="row">
    <div class="col-sm-4">
      <h2>About Me</h2>
      <h5>Photo of me:</h5>
      <div class="fakeimg">Fake Image</div>

      <ul class="nav nav-pills flex-column">
        <li class="nav-item">
          <a class="nav-link active" href="#">Dodaj novi grad koji si posjetio</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pregledaj svoje gradove</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Poruke</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Postavke</a>
        </li>
      </ul>
      <hr class="d-sm-none">
    </div>
    <div class="col-sm-8">
      <br>
      <h5>Ime</h5>
			<h5>Prezime</h5>
      <h5>Spol</h5>
    </div>
		<div class="col-sm-10">
			<table class="table">
            <thead>
                <tr>
                <th scope="col">Svi gradovi koje sam posjetio</th>
                </tr>
            </thead>
            <tbody>

                %for item in data:
                    <tr>
                        <th scope="row"> {{item.naziv}} </th>
                    </tr>
                %end
            </tbody>
        </table>
		</div>
  </div>
</form>
</div>
% include('footer.tpl')
