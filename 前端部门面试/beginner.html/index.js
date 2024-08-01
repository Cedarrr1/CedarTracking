//get
/*const xhr = new XMLHttpRequest()
xhr.open('GET', 'http://39.108.37.159:304/test')
xhr.send()
xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        console.log(JSON.parse(xhr.responseText))
        
    }
}*/

//post
const xhr = new XMLHttpRequest()
xhr.open('POST', 'http://39.108.37.159:304/test')
xhr.setRequestHeader('Content-Type','application/x-www-form-urlencoded')
xhr.send('name=cedar&age=18')
xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        console.log(JSON.parse(xhr.responseText))

    }
}