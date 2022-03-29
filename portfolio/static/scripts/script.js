function showFilters() {
  document.getElementById("filter").innerHTML +=  "<h3>This is the text which has been inserted by JS</h3>";

}

function addRow() {
  const div = document.createElement('div');

  div.className = 'row';

  div.innerHTML = `"<nav role='filter'>Test </nav>'" `;

  document.getElementById('content').appendChild(div);
}

function removeRow(input) {
  document.getElementById('content').removeChild(input.parentNode);
}
function basicPopup(url) {
    popupWindow = window.open(url,'popUpWindow','height=500,width=500,left=100,top=100,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no, status=yes');
}