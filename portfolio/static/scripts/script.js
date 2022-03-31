
var isOpen = false;


function showFilters() {
    var djangoData = $('#programminglanguages').data();

  var tag = document.createElement("div");
  tag.setAttribute("id","dynamic-filters");
  var tag1 = document.createElement("ul")
  tag1.setAttribute("id","filter-list");
  tag1.classList.add("list-group");
  var filter0 = document.createElement('li')
  filter0.classList.add("list-group-item");
   var text0 = document.createTextNode(" programminglanguages ");
   filter0.appendChild(text0);
    var filters0ul = document.createElement("ul");
     filters0ul.setAttribute("id","filter-list");
  filters0ul.classList.add("list-group");
 var meta_content = document.getElementById("programminglanguages").getAttribute('content');
    console.log(meta_content)



   var filter1 = document.createElement("li");
   filter1.classList.add("list-group-item");
   var text1 = document.createTextNode("programmingtechniques")
   var filter2 = document.createElement("li")
   filter2.classList.add("list-group-item");
   var text2 = document.createTextNode("competences")
   var filter3 =  document.createElement("li")
   filter3.classList.add("list-group-item");
   var text3 = document.createTextNode("oses")
      var filter4 =  document.createElement("li")
   filter4.classList.add("list-group-item");
   var text4 = document.createTextNode("frameworks")

   filter1.appendChild(text1)
    filter2.appendChild(text2)
     filter3.appendChild(text3)
     filter4.appendChild(text4)
   tag1.appendChild(filter0)
   tag1.appendChild(filters0ul)
   tag1.appendChild(filter1)
   tag1.appendChild(filter2)
   tag1.appendChild(filter3)
   tag1.appendChild(filter4)
   tag.appendChild(tag1)
   var element = document.getElementById("filters");
   element.appendChild(tag);
   console.log(djangoData)
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


