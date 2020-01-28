%include('header.tpl',title='Pocetna stranica')
<form method='POST'>
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
                        <th scope="row"> <a href='/nova_poruka/{{item["korisnik_id"]}}' value='{{item["korisnik_id"]}}'>KONTAKTIRAJ</a></th>

                        
                        
                    </tr>
                %end
              %end
            </tbody>
        </table>
		</div>
</form>
%include('footer.tpl')
