//$(document).ready(function(){
//    $(".sidenav").sidenav();
//   $('.carousel.carousel-slider').carousel({
//    fullWidth: true
//  });
//  });

// Get reference of the submit button
document.addEventListener("readystatechange", (e)=> {
const updateForm = document.getElementById("updateForm")
const editProfile = document.getElementById("edit_profile")

var searchForm = document.getElementById("searchForm")

searchForm.addEventListener('submit', (e) => {
    e.preventDefault()
    document.getElementById("home").style.display = "none"
    document.getElementById("results").style.display = "" 
    // Get search word input field value after the form is submitted
    const search_word = document.getElementById("word").value

    // Pass value to fetch api a search to get results
    fetch("/search?product_name=" + search_word)
    .then(res => {
        // Check if response is successful
        if (res.ok){
            // Return Json data to the next promise(`then`)
            return res.json()
        }else{
            // Cancel promise if server returns an error.
            return Promise.reject({status: res.status, statusText: res.statusText})
        }
    })
    .then((json_data) => {
        // Get Json data from previous promise after server response is successful.
        for(let product of json_data){
            document.getElementById("product_name").innerHTML = product["product_name"]
            document.getElementById("product_description").innerHTML = product["product_description"]
            document.getElementById("product_price").innerHTML = product["product_price"]
            document.getElementById("product_photoURL").innerHTML = product["product_photoURL"].src
        }
    })
})

editProfile.addEventListener('click', (e) => {
    document.getElementById("profile").style.display = "none"
    document.getElementById("update").style.display = "" 
})




updateForm.addEventListener('submit', (e) => {
    e.preventDefault()
    const sellerName = document.getElementById("seller_name").value
    const email = document.getElementById("email").value
    const phone = document.getElementById("phone").value
    const password = document.getElementById("password").value
    const city = document.getElementById("city").value
    const photo = document.getElementById("photo").files[0];
     let formData = new FormData();
     formData.append("photo", photo);
     formData.append("seller_name", sellerName);
     formData.append("email", email);
     formData.append("phone", phone);
     formData.append("password", password);
     formData.append("city", city);
    
    const options = {
        method: "PUT",
        body: formData
    }

    // Get logged In user id
    const userId = document.getElementById("userId").value
    fetch('/users/' + userId, options)
    .then(res => {
        if (res.ok){
            return res.json()
        }else{
            return Promise.reject({status: res.status, statusText: res.statusText})
        }
    })
    .then(json_data => {
        console.log(json_data)
        document.getElementById('success').innerText = json_data["msg"]
        window.location.reload()
    })
})
})
