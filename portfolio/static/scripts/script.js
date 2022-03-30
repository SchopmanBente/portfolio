
var isOpen = false;

function showFilters() {
/*
  document.getElementById("filters").innerHTML +=  "<div class='filters'>" +=
  "<p> {% trans programminglanguages %}</p>" +=
  "</div>"; */

  var tag = document.createElement("div");
  tag.setAttribute("id","dynamic-filters");
  var filter0 = document.createElement('p')
   var text0 = document.createTextNode(" programminglanguages ");
   var filter1 = document.createElement("p")
   var text1 = document.createTextNode("programmingtechniques")
   var filter2 = document.createElement("p")
   var text2 = document.createTextNode("competence")
   var filter3 =  document.createElement("p")
   var text3 = document.createTextNode("oses")
   filter0.appendChild(text0);
   filter1.appendChild(text1)
    filter2.appendChild(text2)
     filter3.appendChild(text3)
   tag.appendChild(filter0)
   tag.appendChild(filter1)
   tag.appendChild(filter2)
   tag.appendChild(filter3)
   var element = document.getElementById("filters");
   element.appendChild(tag);
    isOpen = true;

}
function removeFilters() {
  const element = document.getElementById("dynamic-filters");
  element.remove();
  isOpen = false;
}


var btn = document.getElementById('filter');

function toggle() {
  if (isOpen) {
    removeFilters();
  } else {
    showFilters();
  }
}

