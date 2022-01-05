
function getSortedItems(n) {
  var table,
    rows,
    switching,
    i,
    x,
    y,
    shouldSwitch,
    dir,
    switchcount = 0;
  table = document.getElementById("myTable");
  switching = true;
  dir = "asc";
  while (switching) {
    switching = false;
    rows = table.getElementsByTagName("TR");
    for (i = 1; i < rows.length - 1; i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          shouldSwitch = true;
          document.getElementById("th2").innerHTML = "Description ▼";
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          shouldSwitch = true;
          document.getElementById("th2").innerHTML = "Description ▲";
          break;
        }
      }
    }
    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount++;
    } else {
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}

function getFilteredItems() {
    const searchInput = document.getElementById("search");
    const rows = document.querySelectorAll("tbody tr");
    searchInput.addEventListener("keyup",function(event){
        const q = event.target.value.toLowerCase();
        rows.forEach(row =>{
            if(q.startsWith("!")){
                const qWithoutFirst = q.slice(1)
                row.querySelector('td').textContent.toLowerCase().includes(qWithoutFirst)
                ? (row.style.display = "none")
                : (row.style.display = "table-row");

            } if(!q.startsWith("!")){
            row.querySelector('td').textContent.toLowerCase().includes(q)
                ? (row.style.display = "table-row")
                : (row.style.display = "none");

            } if(q.slice(0,12).toLowerCase().startsWith("description:")){
                const qWithoutFirstTwelve = q.slice(12)
                row.querySelector('td:nth-child(2)').textContent.toLowerCase().includes(qWithoutFirstTwelve)
                ? (row.style.display = "table-row")
                : (row.style.display = "none");

            } if(q.slice(0,13).toLowerCase().startsWith("!description:")){
                const qWithoutFirstThirteen = q.slice(13)
                row.querySelector('td:nth-child(2)').textContent.toLowerCase().includes(qWithoutFirstThirteen)
                ? (row.style.display = "none")
                : (row.style.display = "table-row");

            } if(q === "description:" || q === "!" || q === "!description:"){
                row.querySelector('td').textContent.toLowerCase()
                ? (row.style.display = "table-row")
                : (row.style.display = "table-row");
            }
        });
    });
}

getFilteredItems()


function toggleTheme() {
    console.log("toggle theme")
}

var counter = 9
var table = document.getElementById("myTable")
var search = document.getElementById("search")
var deButton = document.getElementById("decrease-font-button")
var inButton = document.getElementById("increase-font-button")
var themeButton = document.getElementById("theme-button")
function sizer(table){
    if(counter == 3){
    table.style.fontSize = '50%';
    search.style.fontSize = '50%';
    deButton.style.fontSize = '50%';
    inButton.style.fontSize = '50%';
    themeButton.style.fontSize = '50%';
    }
    else if(counter == 4){
    table.style.fontSize = '60%';
    search.style.fontSize = '60%';
    deButton.style.fontSize = '60%';
    inButton.style.fontSize = '60%';
    themeButton.style.fontSize = '60%';
    }
    else if(counter == 5){
    table.style.fontSize = '70%';
    search.style.fontSize = '70%';
    deButton.style.fontSize = '70%';
    inButton.style.fontSize = '70%';
    themeButton.style.fontSize = '70%';
    }
    else if(counter == 6){
    table.style.fontSize = '80%';
    search.style.fontSize = '80%';
    deButton.style.fontSize = '80%';
    inButton.style.fontSize = '80%';
    themeButton.style.fontSize = '80%';
    }
    else if(counter == 7){
    table.style.fontSize = '90%';
    search.style.fontSize = '90%';
    deButton.style.fontSize = '90%';
    inButton.style.fontSize = '90%';
    themeButton.style.fontSize = '90%';
    }
    else if(counter == 8){
    table.style.fontSize = '100%';
    search.style.fontSize = '100%';
    deButton.style.fontSize = '100%';
    inButton.style.fontSize = '100%';
    themeButton.style.fontSize = '100%';
}
    else if(counter == 9){
    table.style.fontSize = '110%';
    search.style.fontSize = '110%';
    deButton.style.fontSize = '110%';
    inButton.style.fontSize = '110%';
    themeButton.style.fontSize = '110%';
    }
    else if(counter == 10){
    table.style.fontSize = '120%';
    search.style.fontSize = '120%';
    deButton.style.fontSize = '120%';
    inButton.style.fontSize = '120%';
    themeButton.style.fontSize = '120%';
    }
    else if(counter == 11){
    table.style.fontSize = '130%';
    search.style.fontSize = '130%';
    deButton.style.fontSize = '130%';
    inButton.style.fontSize = '130%';
    themeButton.style.fontSize = '130%';
    }
    else if(counter == 12){
    table.style.fontSize = '140%';
    search.style.fontSize = '140%';
    deButton.style.fontSize = '140%';
    inButton.style.fontSize = '140%';
    themeButton.style.fontSize = '140%';
    }
    else if(counter == 13){
    table.style.fontSize = '150%';
    search.style.fontSize = '150%';
    deButton.style.fontSize = '150%';
    inButton.style.fontSize = '150%';
    themeButton.style.fontSize = '150%';
    }
    else if(counter == 14){
    table.style.fontSize = '160%';
    search.style.fontSize = '160%';
    deButton.style.fontSize = '160%';
    inButton.style.fontSize = '160%';
    themeButton.style.fontSize = '160%';
    }
    else if(counter == 15){
    table.style.fontSize = '170%';
    search.style.fontSize = '170%';
    deButton.style.fontSize = '170%';
    inButton.style.fontSize = '170%';
    themeButton.style.fontSize = '170%';
}
}

function increaseFont() {
    if (counter < 15) {
        counter++
        console.log(counter);
        sizer(table)
    } else {
        alert('Max size');
    }
}



function decreaseFont() {
        if (counter > 3) {
        counter--
        console.log(counter);
        sizer(table)
    } else {
        alert('Min size');
    }
}


