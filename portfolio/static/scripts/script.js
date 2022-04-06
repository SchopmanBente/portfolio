
var isOpen = false;
var programminglanguagesIsOpen = false;


function showFilters() {


  var tag = document.createElement("div");
  tag.setAttribute("id","dynamic-filters");
  var tag1 = document.createElement("ul")
  tag1.setAttribute("id","filter-list");
  tag1.classList.add("list-group");
/*
    var filter0 = createFilterName("programminglanguages")
  var filter0 = document.createElement('li')
  filter0.classList.add("list-group-item");
   var text0 = document.createTextNode(" programminglanguages ");
   filter0.appendChild(text0);
*/
    var djangoData = $('#programminglanguages').data();
    alert(djangoData.values);
    var arr = Object.values(djangoData)[0];
    var filter0 = createFilterName("programminglanguages", djangoData, arr.length);

    //filter0.setAttribute("onclick", "toggleFiltersFromChoosenFilter('programminglanguages',   programminglanguagesIsOpen )")
    tag.appendChild(filter0)
    /*
    var filters0ul = document.createElement("ul");
     filters0ul.setAttribute("id","filter-list-programminglanguages");
  filters0ul.classList.add("list-group");
filter0.appendChild(filters0ul)


 var meta_content = document.getElementById("programminglanguages").getAttribute('content');
    console.log(meta_content)





    var filters1ul = document.createElement("ul");
     filters1ul.setAttribute("id","filter-list");
  filters1ul.classList.add("list-group");

     var meta_content1 = document.getElementById("programmingtechniques").getAttribute('content');
      console.log(meta_content1)



   var filter2 = document.createElement("li")
   filter2.classList.add("list-group-item");
   var text2 = document.createTextNode("competence")
    var meta_content2 = document.getElementById("competence").getAttribute('content');

   var filter3 =  document.createElement("li")
   filter3.classList.add("list-group-item");
   var text3 = document.createTextNode("oses")
    var meta_content3 = document.getElementById("oses").getAttribute('content');

      var filter4 =  document.createElement("li")
   filter4.classList.add("list-group-item");
   var text4 = document.createTextNode("frameworks")
 var meta_content4 = document.getElementById("frameworks").getAttribute('content');
*/
   /*filter1.appendChild(text1)
    filter2.appendChild(text2)
     filter3.appendChild(text3)
     filter4.appendChild(text4)
   tag1.appendChild(filter0)
   tag1.appendChild(filters0ul)
   /*tag1.appendChild(filter1)
   tag1.appendChild(filter2)
   tag1.appendChild(filter3)
   tag1.appendChild(filter4)
   tag.appendChild(tag1) */
   var element = document.getElementById("filters");
   element.appendChild(tag);
    var arr = Object.values(djangoData)[0]
   console.log(djangoData)
    console.log(Object.keys(djangoData));
    console.log(Object.values(djangoData));
    var languages = Object.values(djangoData)[0][0].fields["language"]
    console.log(languages);
    var len=  arr.length;
    console.log(len);
    isOpen = true;

}
function removeFilters() {
  const element = document.getElementById("dynamic-filters");
  element.remove();
  isOpen = false;
}

function createIconFilter(name, number_of_options){
    console.log(number_of_options);
    var span = document.createElement("span");
    span.classList.add("material-icons");
    filter_name = name
    span.setAttribute("onclick", "toggleFiltersFromChoosenFilter(filter_name ,   programminglanguagesIsOpen )");
var icon = document.createTextNode("filter_list");
    span.appendChild(icon);
    console.log(span);
    return span

}

function createFilterName(name, djangoData,number_of_options){
     var filter = document.createElement("li");
   filter.classList.add("list-group-item");
   var text = document.createTextNode(name)
    filter.appendChild(text);
    var span =  createIconFilter(name, djangoData)
    filter.appendChild(span)
     filter.classList.add("list-group-item");
    return filter
}



function toggleFiltersFromChoosenFilter(name,  number_of_options, filterIsOpen){
if (filterIsOpen) {
    hideFiltersFromChoosenFilter(name, number_of_options);
} else {
    showFiltersFromChoosenFilter(name,number_of_options);
}

}
function hideFiltersFromChoosenFilter(name){
    const element = document.getElementById(name);
    element.remove();
    isOpen = false;
    alert(name)
}

function showFiltersFromChoosenFilter(name,number_of_options){
    alert("Ik werk hoor! (0)")
    var ul = document.createElement("ul");
    ul.classList.add("list-group");
    id = '#'+name;
    data = get_meta_content(id)
    alert("Ik werk hoor! (1)")
    alert(ul)

    /*
    var languages = Object.values(djangoData)[0][0].fields["language"]
    console.log(languages);

    for (var i = 0; i < number_of_options; i++) {
        console.log(array[0][i])
    }
    */
}

function get_meta_content(id){
    var djangoData = $(id).data();
    var arr = Object.values(djangoData)[0]
    var dict = {};
    /*
    var meta_content = document.getElementById("#programminglanguages").getAttribute('content');
       console.log(meta_content)
    */
    for (var i = 0; i < arr.length; i++) {
        console.log((arr[i]));

        for (const [key, value] of Object.entries(arr[i])) {
            console.log(`${key}: ${value}`);
            var keyOfObject = key
            if(keyOfObject == "fields"){
                for (const [key, value] of Object.entries(keyOfObject)) {
                    console.log(`${key}: ${value}`);
                }

            }
        }
        dict[i] = Object.values(i)

    }
    console.log(dict);
    return dict;

}

var btn = document.getElementById('filter');

function toggle() {
  if (isOpen) {
    removeFilters();
  } else {
    showFilters();
  }
}
