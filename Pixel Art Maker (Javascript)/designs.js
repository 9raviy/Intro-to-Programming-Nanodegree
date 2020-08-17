// Select size inputs
const height = document.querySelector('#inputHeight');
const width = document.querySelector('#inputWidth');

// When size is submitted by the user, call makeGrid()
const form = document.getElementById('sizePicker');
form.addEventListener('submit', function (event) {
    event.preventDefault(); makeGrid(height, width);
});

// Function to make grid as per the input height and width of Grid
function makeGrid(height, width) {
    const table = document.querySelector('#pixelCanvas'); //Select the table
    table.innerHTML = "";
    for (var i = 1; i <= height.value; i++) {
        var row = table.insertRow();
        for (var j = 1; j <= width.value; j++) {
            var col = row.insertCell();
        }
    }
}

// Select the color input and add an EventListener to trigger color through click
const cell = document.querySelector('#pixelCanvas');
cell.addEventListener('click', function (evt) {
    if (evt.target.nodeName.toLowerCase() === 'td') {
        var color = document.getElementById('colorPicker').value;
        evt.target.style.backgroundColor = color;
    }
})





