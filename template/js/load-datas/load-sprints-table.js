$(document).ready(function() {
    sprintsTableJSON = sprintsTableJSON
    console.log(sprintsTableJSON[Object.keys(sprintsTableJSON)[0]].sprint_name)
    console.log(Object.keys(sprintsTableJSON).length)

    for(var i = 0; i < Object.keys(sprintsTableJSON).length; i++)
    {
        console.log(sprintsTableJSON[Object.keys(sprintsTableJSON)[i]].sprint_name)
        document.getElementById('table-of-sprints-name').insertAdjacentHTML('beforeend', '<ul id="elements'+ i + '" class="list-style-none">')
        document.getElementById('elements' + i).insertAdjacentHTML('beforeend', '<li><a href="javascript:void(0)"><i class="fa fa-check text-success"></i> ' + sprintsTableJSON[Object.keys(sprintsTableJSON)[i]].sprint_name + '</a></li>')
        document.getElementById('table-of-sprints-name').insertAdjacentHTML('beforeend', '</ul>')
    }

})
