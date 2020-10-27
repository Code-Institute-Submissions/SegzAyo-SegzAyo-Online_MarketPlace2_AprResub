//$(document).ready(function(){
//    $(".sidenav").sidenav();
//   $('.carousel.carousel-slider').carousel({
//    fullWidth: true
//  });
//  });

// Get reference of the submit button
document.addEventListener("readystatechange", (e)=> {
    console.log("test")
const updateForm = document.getElementById("updateForm")
const editProfile = document.getElementById("edit_profile")

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
    
    const data = {
        seller_name: sellerName,
        email: email,
        phone: phone,
        password: password,
        city: city
    }
    
    const options = {
        method: "PUT",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
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

// Add event handler on form submit
document.getElementById("searchForm").addEventListener('submit', (e) => {
    e.preventDefault()
    document.getElementById("home").style.display = "none"
    document.getElementById("results").style.display = "" 
    // Get search word input field value after the form is submitted
    const search_word = document.getElementById("search_word").value
    console.log(search_word)

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
    .then(json_data => {
        // Get Json data from previous promise after server response is successful.
        console.log(json_data)
        //window.location.reload()
    })
})
})
