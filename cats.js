
function makeCatRequest(){
  var catName = document.getElementById("cat-name").value;
  }

	var query = "https://cat-fact.herokuapp.com"+ catNames;
  query = query.replace(/ /g, "%20");

	catRequest = new XMLHttpRequest();
	catRequest.open('GET', query, true);
	catRequest.onload = processCatRequest;
	catRequest.send();
}


function processCatRequest(){
  if(catRequest.readyState != 4){
    return;
  }
