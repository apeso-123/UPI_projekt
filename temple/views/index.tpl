%include('header.tpl',title='Pocetna stranica')
<form >
<br>
  <!-- Page Content -->
%for item in data:
<div class="container">
  <a href='/gradovi/{{item.id}}'><img src="{{item.link_slike}}" alt="Slika" style="width:600px; margin-left:100px;"></a>
  <div class="content">
    <h1 id="odabrana_slika" name="odabrana_slika" ><a href='/gradovi/{{item.id}}'>{{item.naziv}}</a></h1>
  </div>
</div>
<br><br>
%end
</form>
</body>
</html>
