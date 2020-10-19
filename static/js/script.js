//$(document).ready(function(){
//    $(".sidenav").sidenav();
//   $('.carousel.carousel-slider').carousel({
//    fullWidth: true
//  });
//  });

// Get reference of the submit button
const updateForm = document.getElementById("updateForm")

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
    })
})



