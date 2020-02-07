%include('header.tpl',title='Pocetna stranica')
<style>

.bg-img {
  /* The image used */
  background-image: url("https://images.pexels.com/photos/255379/pexels-photo-255379.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940");
  
  min-height: 600px;

  /* Center and scale the image nicely */
  background-position: center;
  
  position: relative;
}
.card1 {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: 15px;
  float:left;
  text-align: center;
  padding-left: 10px;
  padding-right: 10px;
  padding-top:10px;
  padding-bottom:10px;
  background-color:white;

}
.search1 {
  position:middle;

  margin-left:100px;
  width: 100%;
  font-size: 14px;  
  
}
.box1 {
  border: 2px solid transparent;
  padding-top:5px;
  padding-right:40px;
  padding-bottom:7px;
  border-radius: 7px;
  /*box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);*/
  

  /*border-color:rgba(0, 0, 0, 0.2);*/
  
}
</style>
</body>
<body class="bg-img">
<form action='{{form_akcija}}' method='POST'>
<br>
    <div class="search1">
      <input type="text" name='search' id='search' class="box1" placeholder="Search.." name="search">
      <button type="submit" class="btn btn-light">Pretraži</button><br>
      <p style="font-size:10px;">*Ako želite pretraživati po državi,morate unijeti naziv države na engleskom jeziku!</p></div><br>
  <!-- Page Content -->
%for item in data:
  <div class="card1">
    <a href='/gradovi/{{item.id}}'><img src="{{item.link_slike}}" alt="Denim Jeans" style="width:100%"></a>
    <h1 style='font-family:"Brush Script MT", cursive	; font-style: italic;' ><a href='/gradovi/{{item.id}}'>{{item.naziv}}</a></h1><br>
  </div>
%end
</form>

</body>
</html>
