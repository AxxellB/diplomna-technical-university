    function searchAndSort() {
            const searchQuery = document.getElementById("searchQuery").value;
            let sortBy = document.querySelector("ul li.active a").innerText.toLowerCase();
            if(sortBy != "newest"){
                sortBy = "popular"
            }
            const url = `http://127.0.0.1:8000/?q=${searchQuery}&sort=${sortBy}`;
            console.log(url)
            window.location.href = url;
            }