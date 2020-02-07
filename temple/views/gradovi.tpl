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
.tablica{
  position:relative;
  top:15px;
  background-color:white;
  left:10%;
  margin-right:400px;
}
</style>
</body>
<body class="bg-img">
<form method='POST'>
<div class="tablica">
<div class="col-sm-8">
			<table class="table">
            <thead>
                <tr>
                <th scope="col" style="color:#ff8080;">KORISNIK</th>
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
                      <th scope="row">{{item["korisnik_user_name"]}} </th>
                      <th scope="row">{{item["opis"]}} </th>
                      <th scope="row">{{item["znamenitosti"]}} </th>
                        <th scope="row">{{item["prijevoz"]}} </th>
                        <th scope="row">{{item["smjestaj"]}} </th>
                        <th scope="row">{{item["hrana"]}} </th>
                        <th scope="row">{{item["zanimljivosti"]}} </th>
                        <th scope="row"> <a href='/nova_poruka?korisnikid={{item["korisnik_id"]}}' value='{{item["korisnik_id"]}}'>KONTAKTIRAJ</a></th>                        
                        
                    </tr>
                %end
              %end
            </tbody>
        </table>
		</div>
  </div>
</form>
%include('footer.tpl')
