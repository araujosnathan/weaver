$(document).ready(function() {
    let keys = Object.keys(sprintsTableJSON).sort()
    for(var i = 0; i < keys.length; i++)
    {
        document.getElementById('sprint-notifications').insertAdjacentHTML('beforeend', '<a id="element' + i + '" href="#">')
        document.getElementById('element' + i).insertAdjacentHTML('beforeend','<div id="img:' + keys[i] + '" class="btn btn-success btn-circle m-r-10"><i class="fa fa-link"></i></div>')
        document.getElementById('element' + i).insertAdjacentHTML('beforeend','<div id="name:' + keys[i] + '" class="mail-contnet"><h5>' + sprintsTableJSON[keys[i]].sprint_name + '</h5>')
        document.getElementById('element' + i).insertAdjacentHTML('beforeend','</div>')
        document.getElementById('sprint-notifications').insertAdjacentHTML('beforeend','</a>')
    }

})
