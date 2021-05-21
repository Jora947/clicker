function call_click() {
    const click_node = document.getElementById('click-image')
    click_animation(click_node, 50)

    fetch('api/call_click', {
        method: 'GET'
    }).then(response => {
        if (response.ok) return response.json()
        else return Promise.reject(response)
    }).then(data => {
        document.getElementById('counter').innerText = data
    }).catch(err => console.log(err))
}

function update_boost(boost_id) {
    const csrftoken = getCookie('csrftoken')

    fetch('api/update_boost/', {
        method: 'POST',
        headers: {
            "X-CSRFToken": csrftoken,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            boost_id: boost_id
        })
    }).then(response => {
        if (response.ok) return response.json()
        else return Promise.reject(response)
    }).then(data => {
        document.getElementById('counter').innerText = data.main_cycle.coins_count
        document.getElementById('click_power').innerText = data.main_cycle.click_power
        
        render_boost(data.boost)
    }).catch(err => console.log(err))
}

function render_boost(boost) {
    const button = document.getElementById(`boost_${boost.id}`)
    button.querySelector('#boost_level').innerText = boost.level
    button.querySelector('#boost_power').innerText = boost.power
    button.querySelector('#boost_price').innerText = boost.price
}

function click_animation(node, time_ms) {
    const css_time = `.0${time_ms}s`
    node.style.cssText = `transition: all ${css_time} linear; transform: scale(0.95);`
    setTimeout(function() {
        node.style.cssText = `transition: all ${css_time} linear; transform: scale(1);`
    }, time_ms)
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}