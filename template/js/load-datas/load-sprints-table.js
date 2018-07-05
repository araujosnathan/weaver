$(document).ready(function() {
    let keys = Object.keys(sprintsTableJSON).sort()
    for(var i = 0; i < keys.length; i++)
    {
        document.getElementById('table-of-sprints-name').insertAdjacentHTML('beforeend', '<ul id="elements'+ i + '" class="list-style-none">')
        document.getElementById('elements' + i).insertAdjacentHTML('beforeend', '<li><a id="' + keys[i] + '" href="javascript:void(0)"><i class="fa fa-check text-success"></i> ' + sprintsTableJSON[keys[i]].sprint_name + '</a></li>')
        document.getElementById('table-of-sprints-name').insertAdjacentHTML('beforeend', '</ul>')
    }

})
