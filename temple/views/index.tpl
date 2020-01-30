%include('header.tpl',title='Pocetna stranica')
<style>
.container2 {
  position: relative;
  font-family: Stencil Std, fantasy;
  font-size: 110px;
}

.content1 {
  position: absolute;
  bottom: 100px;
  right: 130px;
  
  color: white;
  padding-left: 40px;
  padding-right: 40px;
  padding-top:40px;
  padding-bottom:40px;
}
.search1 {
  position:middle;
  margin-left:100px;
  width: 100%;
  font-size: 18px;
  padding: 11px;
  
}
</style>
<form action='{{form_akcija}}' method='POST'>
<br>
    <div class="search1">
      <input type="text" name='search' id='search' placeholder="Search.." name="search">
      <button type="submit">Search</button><br>
      <p>*Ako želite pretraživati po državi,morate unijeti naziv države na engleskom jeziku!</p></div><br>
  <!-- Page Content -->
%for item in data:

  <div class="container2">
  <a href='/gradovi/{{item.id}}'><img src="{{item.link_slike}}" alt="Slika" style="width:800px;margin-left:100px;"></a>
  <div class="content1">
    <h1 id="odabrana_slika" name="odabrana_slika" ><a href='/gradovi/{{item.id}}'>{{item.naziv}}</a></h1>
  </div>
  </div>

<br><br>
%end
</form>
</body>
</html>
