%include('header.tpl',title='Ažuriranje posta')
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: 15px;
  margin-left:100px;
  float:left;  
  font-family: arial;
  padding-left: 10px;
  padding-right: 10px;
  padding-top:10px;
  padding-bottom:10px;
  
}

.title {
  color: grey;
  font-size: 14px;
}
.mail {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  width: 100%;
  font-size: 18px;
}
</style>

<h2 style="text-align:center">Autori:</h2>

<div class="card">
  <h1>Antonia Pešo</h1>
  <p class="title">PMFST,Informatika</p>
  <p class="mail">apeso@pmfst.hr</p>
</div>
<div class="card">
  <h1>Klara Miloš</h1>
  <p class="title">PMFST,Informatika</p>
  <p class="mail">kmilos@pmfst.hr</p>
</div>
<div class="card">
  <h1>Kristina Nikolov</h1>
  <p class="title">PMFST,Informatika</p>
  <p class="mail">knikolov@pmfst.hr</p>
</div>
%include('footer.tpl')
