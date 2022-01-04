// you receive an array of objects which you must sort in the by the key "sortField" in the "sortDirection"
function getSortedItems(items, sortField, sortDirection) {
    console.log(items)
    console.log(sortField)
    console.log(sortDirection)

    // === SAMPLE CODE ===
    // if you have not changed the original html uncomment the code below to have an idea of the
    // effect this function has on the table
    //
    if (sortDirection === "asc") {
        const firstItem = items.shift()
        if (firstItem) {
            items.push(firstItem)
        }
    } else {
        const lastItem = items.pop()
        if (lastItem) {
            items.push(lastItem)
        }
    }

    return items
}

// you receive an array of objects which you must filter by all it's keys to have a value matching "filterValue"
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
            } if(q === "!"){
                row.querySelector('td').textContent.toLowerCase()
                ? (row.style.display = "table-row")
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
            } if(q === "description:"){
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
