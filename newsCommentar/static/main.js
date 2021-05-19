document.addEventListener('DOMContentLoaded', function() {

    let btn = document.getElementById('btn')
    btn.addEventListener('click', event => {
        event.preventDefault()

        // get text from inpit
        let txt = document.querySelector('.newComment')
        let massage = txt.value
        add(massage)

        // clear text-filed
        txt.value = ''
    })
})


function add(text) {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    fetch('comment', {
        method: 'POST',
        body: JSON.stringify({
            text: text,
            csrfmiddlewaretoken: csrftoken
        }),
        headers: { "X-CSRFToken": csrftoken },
    })
    .then(response => response.json())
    .then(data => {
        
        showPost(data)})
}

function showPost(data)
{
    let commentDiv = document.createElement('div')
    let paragraph = document.createElement('p')
    let h3 = document.createElement('h3')
    
    commentDiv.className = 'comment'

    //add data to h3 paragraph 
    paragraph.innerHTML = data[0].post
    h3.innerHTML = `${data[0].user} schreibt:`

    // add paragraph and h3 to commentDiv
    commentDiv.appendChild(h3)
    commentDiv.appendChild(paragraph)

    // add commentDiv to Comments
    let allComments = document.querySelector('.allComments')
    allComments.prepend(commentDiv)


}