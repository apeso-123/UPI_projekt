%include('header.tpl',title='Nova Poruka')
<style>
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

/* Modal Content */
.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

/* The Close Button */
.close {
  color: #aaaaaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}
.bg-img {
  /* The image used */
  background-image: url("https://images.pexels.com/photos/255379/pexels-photo-255379.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940");
  
  min-height: 600px;

  /* Center and scale the image nicely */
  background-position: center;
  
  position: relative;
}

</style>
</body>
<body class="bg-img">
<form class="form-horizontal" action='{{form_akcija}}' method='POST' style='margin-left:250px;'>
<br>
  <h3>Nova poruka</h3>
  <input type="hidden" class="form-control" id="broj" name='broj' value='{{primatelj}}'>  
  <textarea class="form-control" id="textarea1" name="textarea1" style="width:350px;height:150px;"></textarea><br>
  <button id="singlebutton" name="singlebutton" type="submit" class="btn btn-primary">Pošalji</button>
    <a href='/'>Odustani</a>
    <!-- The Modal -->
  <div id="myModal" class="modal">

  <!-- Modal content -->
    <div class="modal-content">
      <span class="close">&times;</span>
      <p>Poruka poslana!</p>
    </div>
  </div>
</form>
<script>
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("singlebutton");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
</script>

</body>
</html>
