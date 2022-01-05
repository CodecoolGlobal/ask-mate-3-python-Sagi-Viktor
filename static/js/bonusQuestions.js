
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
          document.getElementById("th1").innerHTML = "Title ▼";
          document.getElementById("th2").innerHTML = "Description ▼";
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          shouldSwitch = true;
          document.getElementById("th1").innerHTML = "Title ▲";
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

function increaseFont() {
    console.log("increaseFont")
}

function decreaseFont() {
    console.log("decreaseFont")
}


