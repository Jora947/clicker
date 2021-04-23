function call_click() {
    fetch('api/call_click', {
        method: 'GET'
    }).then(response => {
        if (response.ok) return response.json()
        else return Promise.reject(response)
    }).then(data => {
        document.getElementById('counter').innerText = data
    }).catch(err => console.log(err))
}