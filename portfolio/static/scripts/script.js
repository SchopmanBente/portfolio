
var isOpen = false;
var programminglanguagesIsOpen = false;
var selectedProgrammingLanguages = {};

function showFilters() {
 var tag = document.createElement("div");
  tag.setAttribute("id","dynamic-filters");
  var form = createForm("form_all_filters", helloWorld())

  var tag1 = document.createElement("ul");
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
    tag1.appendChild(filter0);
    var submit = getSubmitButton();
    form.appendChild(tag1);
    //form.appendChild(submit);
    tag.appendChild(form);
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
   element.appendChild(form);
    isOpen = true;

}
function removeFilters() {
  const element = document.getElementById("filter-list");
  element.remove();
  isOpen = false;
}
function helloWorld(){
    alert("hello World!")
}
function createForm(id, action){
     var form = document.createElement("form");
     form.setAttribute("type","submit");
     form.setAttribute("id", id);
     form.setAttribute("action",action)
     return form
}
function getCheckedCheckBoxes(){
    console.log("function getCheckedCheckBoxes()");
}
function getSubmitButton(data){
    var button = document.createElement("input")
    button.setAttribute("type","submit")
    return button
}
function createSelectedFilter(data, name, number_of_options){
    var ul = document.createElement("ul");
    ul.classList.add("list-group");
    filter_list_id = "filter_list_" + name;
    ul.setAttribute("id",filter_list_id);
    ul.setAttribute("onclick", getCheckedCheckBoxes())
    for(var key in data) {
        var value = data[key];
        var pk = value["pk"];
        var language = value["fields"]["language"];
        console.log(pk);
        console.log(language)
        var li = document.createElement("li")
        li.classList.add("list-group-item");
        li.setAttribute("id",pk);
        var checkbox = document.createElement("input")
        checkbox.setAttribute("type","checkbox")
        checkbox.setAttribute("id", pk)
        checkbox.setAttribute("name", language)
        var label = document.createElement("label")
        label.setAttribute("for", language)
        var text = document.createTextNode(language);
        label.appendChild(text)
        li.appendChild(checkbox)
        li.appendChild(label)
        console.log(li);
        ul.appendChild(li)
        console.log(key);
        console.log(value);



    }

    return ul
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
    alert("Ik werk hoor! (0)");

    id = '#'+name;
    data = get_meta_content(id);
    filters = createSelectedFilter(data,name, number_of_options);
    element = document.getElementById("filter_list_programminglanguages")
    if (typeof(element) != 'undefined' && element != null){
        const element = document.getElementById("filter_list_programminglanguages");
        element.remove();
        programminglanguagesIsOpen = false;
        return "";
    } else {

        html_filters = document.getElementById("form_all_filters").append(filters);
        return html_filters;

    }


}

function get_meta_content(id){
    var djangoData = $(id).data();
    var arr = Object.values(djangoData)[0]
    var dict = {};

    for (var i = 0; i < arr.length; i++) {

        for (const [key, value] of Object.entries(arr[i])) {
            var keyOfObject = key
            if(keyOfObject == "fields"){
                var fields = value
            }
            if (keyOfObject == "pk") {
                var pk = value
            }
        }
        dict[i] = {pk, fields};

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