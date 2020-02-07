%include('header.tpl',title='Poruke')
<style>
.poravnanje{
  margin: 0 auto;
  max-width: 800px;
  padding: 0 20px;
}
.container1 {
  border: 2px solid #dedede;
  background-color: #f1f1f1;
  border-radius: 5px;
  border-color: pink;
  padding: 10px;
  margin: 10px 0;
}

.darker {
  border-color: #pink;
  background-color: #ddd;
}

.container1::after {
  content: "";
  clear: both;
  display: table;
}

.container1 h7 {
  float: left;
  max-width: 60px;
  width: 100%;
  margin-right: 20px;
  border-radius: 50%;
}

.container1 h7.right {
  float: right;
  margin-left: 20px;
  margin-right:0;
}

.time-right {
  float: right;
  color: #aaa;
}

.time-left {
  float: left;
  color: #999;
}
.botun{
  background-color:#666666;
  border-radius:15px;
  max-width: 100px;
  padding: 0 20px;

}
.forma{
  border-radius:12px;
  border-color:#666666;
  width: 100%;
  height:100px;
}
</style>
</body>
<body style="background-image: url('https://wallpaperaccess.com/full/146276.jpg');">
<form action='{{form_akcija}}' method='POST'>

  <div class="poravnanje"><br>
  <h5>{{username}}</h5><br>
  %for item in data:
    %if logirani!=item.id_posiljatelj:
      <div class="container1">
        <p style="float:left;">{{item.tekst}}</p>
        <span class="time-right">{{item.datum}}</span>
      </div>
    %else:
     <div class="container1 darker">
       <p style="float:right;" >{{item.tekst}}</p><br>
       <span class="time-left">{{item.datum}}</span>
     </div>
    %end
  %end
  

<div class="form-group">
  <div>                     
    <textarea class="forma" id="tekst_poruke" name="tekst_poruke"></textarea>
  </div>
</div>

<!-- Button -->
<div>
  <label class="col-md-4 control-label" for="singlebutton"></label>
  <div class="col-md-6">
    <button id="singlebutton" name="singlebutton" type="submit" class="botun" >Pošalji</button>
    <a href='/korisnicki_profil'>Natrag na svoj profil</a><br><br>

  </div>
</div>
</form>
</body>
</html>
